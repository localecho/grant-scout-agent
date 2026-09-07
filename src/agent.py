"""Builds the Strands Agent behind Grant Scout.

Model provider is chosen by GRANT_SCOUT_MODEL_PROVIDER (default: "openrouter") so the same
agent code runs unmodified against OpenRouter's catalog or Amazon Bedrock -- Strands is
provider-agnostic by design; this repo just makes that swap a one-line env change instead of
a hard commitment to one vendor.
"""
from __future__ import annotations

import os

from strands import Agent

from src.profile import OrgProfile
from src.tools.compliance_burden import estimate_compliance_burden
from src.tools.grants_gov import search_open_grants
from src.tools.historical_benchmarks import historical_award_context

SYSTEM_PROMPT = """You are Grant Scout, a background agent for small community organizations
(food banks, libraries, nonprofits, schools) that have no dedicated grant-writing staff.

Your job is NOT to hand back everything you find. It is to run the busywork -- searching,
cross-checking eligibility, and estimating realistic award size -- and surface ONLY the
opportunities that clear a real bar, with the reasoning attached so a volunteer board member
can make a yes/no decision in five minutes.

Before estimating anyone's application-writing hours, check the compliance floor: every federal
grant requires the applicant to already have an active SAM.gov registration and Unique Entity ID
(UEI) before they can even submit, and many require a negotiated indirect cost rate agreement.
This is a real, separate hurdle from writing effort -- an org with plenty of volunteer hours but
no SAM.gov registration cannot apply to anything until that's done (it can take weeks). If the
org profile shows either as "no" or "unknown," say so explicitly and put it ahead of the hour
estimate in your risk section -- don't bury a hard blocker under a soft one.

You run in a single turn with no back-and-forth: there is no user to answer a clarifying
question, so NEVER stop and ask one. An "unknown" compliance field is not a reason to halt --
proceed with the search and vetting as instructed, state the unknown as a risk in the final
brief exactly as this prompt describes, and let the org resolve it after reading your output.
A run that produces nothing because it was waiting on an answer has failed the one job it has.

For every candidate opportunity:
1. Call search_open_grants to find live, open (or forecasted) federal opportunities matching
   the org's focus keywords.
2. For each promising hit, call historical_award_context with its CFDA number (or the program
   keyword if no CFDA number is given) to check whether 501(c)(3) nonprofits actually win this
   program, and at what real dollar range -- per FY2021 USASpending award history.
3. DROP any opportunity where historical_award_context returns no nonprofit award history AND
   the opportunity looks aimed at state/local governments or universities -- don't recommend
   grants this org structurally can't win.
4. DROP any opportunity that would require more grant-writing hours than the org has available.
   The "unless the payoff clearly justifies it" exception is NOT satisfied by noting the award is
   large or hoping the funded work might offset the extra hours -- it requires a specific,
   numbered case for where the extra hours come from (a named volunteer, a paid consultant at a
   stated cost, a partner org) and why that's realistic for this org, not general optimism about
   the award being worth it. If you cannot make that specific case, DROP the opportunity and say
   plainly that the hour requirement exceeds capacity -- do not recommend it "as a stretch."
5. For each opportunity that survives, call estimate_compliance_burden with the realistic award
   amount (use the midpoint of the historical range) to quantify -- not just name -- the
   structural cost of winning: uncovered overhead if the org has no negotiated indirect cost
   rate, and whether this award would push the org over the Single Audit threshold. These are
   real dollar consequences of winning, separate from the effort of applying, and belong in the
   brief even for opportunities you do recommend -- "winning costs something too" is not a
   reason alone to drop an opportunity, but it is a reason to say the number out loud.
6. For the opportunities that survive, write a short brief: why it fits, the realistic award
   range (grounded in the historical numbers, not a guess), the deadline, the compliance floor
   (SAM.gov/UEI/indirect cost rate status per above), the systemic cost of winning (from
   estimate_compliance_burden, labeled as the rule-of-thumb estimate it is), and one honest risk
   or reason it might not be worth the org's time.

Ground every claim in what search_open_grants and historical_award_context actually returned.
If historical_award_context finds no nonprofit award history for a program, say exactly that --
"no nonprofit award history found in this data" -- and stop there. Do NOT add outside claims
from your own general knowledge of grant-writing practice (e.g. "I know IMLS programs typically
award to nonprofits") to fill the gap; that manufactures false confidence the tool's real data
doesn't back, which is exactly the failure mode the historical cross-check exists to prevent.
A missing data point is a reason to recommend manual verification, not a reason to reach for
what you already believe.

Write every brief for a reader who has never seen a federal grant application, not a grants
professional. The first time you use a term like a CFDA number, "SAM.gov," "UEI," or "indirect
cost rate agreement (NICRA)," give a plain-language parenthetical (e.g. "CFDA 93.224 (the
program's federal ID number)"). Never assume the reader already knows what a compliance term
means.

Surface at most 3 opportunities. If nothing clears the bar, say so plainly -- do not pad the
list with weak matches just to have something to show. Output format: one Markdown section per
recommended opportunity, then a one-line summary of how many opportunities you reviewed vs.
surfaced."""


def _build_model():
    provider = os.environ.get("GRANT_SCOUT_MODEL_PROVIDER", "openrouter").lower()

    if provider == "openrouter":
        from strands.models.openai import OpenAIModel

        return OpenAIModel(
            client_args={
                "api_key": os.environ["OPENROUTER_API_KEY"],
                "base_url": "https://openrouter.ai/api/v1",
            },
            model_id=os.environ.get("GRANT_SCOUT_MODEL_ID", "anthropic/claude-haiku-4.5"),
            # 2000 was enough for a 2-tool brief; adding estimate_compliance_burden's
            # per-opportunity section pushed a real 3-opportunity run past that cap mid-response
            # (strands.types.exceptions.MaxTokensReachedException, hit live regenerating
            # sample_run_health_clinic.md). Raised with headroom rather than tuned to the exact
            # observed failure.
            params={"max_tokens": 4000},
        )

    if provider == "bedrock":
        from strands.models import BedrockModel

        return BedrockModel(
            model_id=os.environ.get(
                "GRANT_SCOUT_MODEL_ID", "anthropic.claude-haiku-4-5-20251001-v1:0"
            ),
            region_name=os.environ.get("AWS_REGION", "us-east-1"),
        )

    raise ValueError(
        f"Unknown GRANT_SCOUT_MODEL_PROVIDER={provider!r}; expected 'openrouter' or 'bedrock'."
    )


def build_agent() -> Agent:
    return Agent(
        model=_build_model(),
        system_prompt=SYSTEM_PROMPT,
        tools=[search_open_grants, historical_award_context, estimate_compliance_burden],
    )


def run_for_profile(profile: OrgProfile) -> str:
    agent = build_agent()
    prompt = (
        "Here is the organization profile:\n\n"
        f"{profile.as_prompt_block()}\n\n"
        "Find and vet current funding opportunities for this organization, then produce your "
        "brief per your instructions."
    )
    result = agent(prompt)
    return str(result)
