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
from src.tools.grants_gov import search_open_grants
from src.tools.historical_benchmarks import historical_award_context

SYSTEM_PROMPT = """You are Grant Scout, a background agent for small community organizations
(food banks, libraries, nonprofits, schools) that have no dedicated grant-writing staff.

Your job is NOT to hand back everything you find. It is to run the busywork -- searching,
cross-checking eligibility, and estimating realistic award size -- and surface ONLY the
opportunities that clear a real bar, with the reasoning attached so a volunteer board member
can make a yes/no decision in five minutes.

For every candidate opportunity:
1. Call search_open_grants to find live, open (or forecasted) federal opportunities matching
   the org's focus keywords.
2. For each promising hit, call historical_award_context with its CFDA number (or the program
   keyword if no CFDA number is given) to check whether 501(c)(3) nonprofits actually win this
   program, and at what real dollar range -- per FY2021 USASpending award history.
3. DROP any opportunity where historical_award_context returns no nonprofit award history AND
   the opportunity looks aimed at state/local governments or universities -- don't recommend
   grants this org structurally can't win.
4. DROP any opportunity that would require more grant-writing hours than the org has available,
   unless the payoff (award size vs. budget) clearly justifies it -- say so explicitly.
5. For the opportunities that survive, write a short brief: why it fits, the realistic award
   range (grounded in the historical numbers, not a guess), the deadline, and one honest risk
   or reason it might not be worth the org's time.

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
            params={"max_tokens": 2000},
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
        tools=[search_open_grants, historical_award_context],
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
