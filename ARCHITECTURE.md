# Architecture

Grant Scout is a single Strands `Agent` with four tools and a system prompt that tells it what
"good enough to surface" means. There's no orchestration framework beyond Strands itself — the
judgment (search → cross-check → cost-check → drop weak matches → write a brief) lives in the
prompt and is executed via the agent's normal tool-calling loop.

```mermaid
flowchart TD
    subgraph Input
        P[Org profile YAML<br/>mission, budget, states, keywords, volunteer hours,<br/>compliance status]
    end

    subgraph Agent["Strands Agent (src/agent.py)"]
        SP[System prompt:<br/>compliance floor → search → vet → cost-check → brief top 3 max]
    end

    subgraph Tools
        T1[search_open_grants<br/>grants.gov public API<br/>live, open/forecasted opportunities]
        T2[historical_award_context<br/>FY2021 USASpending extract<br/>real nonprofit award $ + counts]
        T3[estimate_compliance_burden<br/>2 CFR 200 math<br/>uncovered overhead + Single Audit check]
        T4[compliance_guide<br/>real SAM.gov/NICRA process<br/>step-by-step, not just "you need this"]
    end

    subgraph Model["Model provider (swappable via env var)"]
        OR[OpenRouter<br/>OpenAI-compat endpoint<br/>default]
        BR[Amazon Bedrock<br/>optional, same agent code]
    end

    subgraph Output
        O[Markdown brief:<br/>at most 3 opportunities,<br/>each with fit + $ range + compliance cost + honest risk<br/>OR "nothing cleared the bar"]
    end

    P --> Agent
    Agent <--> T1
    Agent <--> T2
    Agent <--> T3
    Agent <--> T4
    Agent <--> Model
    Agent --> O
```

## Why this shape

- **Four tools, not ten.** The judging criteria reward "genuine effort and a working,
  non-trivial implementation," not tool-count. The non-trivial part is the layered vetting: an
  opportunity that sounds like a fit by title alone gets rejected if `historical_award_context`
  shows no real nonprofit award history, a program with excellent award history can still get
  dropped if `estimate_compliance_burden` shows winning it would cost more than the org can
  absorb, and a blocker the agent names (SAM.gov, no indirect cost rate) comes with the real,
  step-by-step process to clear it via `compliance_guide` — a wall, a vet, and a way over the
  wall, not just a keyword-matcher.
- **Real data, not fixtures.** `search_open_grants` hits grants.gov live. `historical_award_context`
  reads a table derived from a real USASpending.gov bulk pull (`data/extract_benchmarks.sql`
  documents the exact query) — not synthetic or invented numbers. `estimate_compliance_burden`
  computes from real federal regulation (2 CFR 200.414(f)'s 10% de minimis rate, 2 CFR 200 Subpart
  F's $750K Single Audit threshold), with its overhead-rate assumption clearly labeled as an
  assumption, not data this tool has verified per-program.
- **Provider-agnostic on purpose.** `src/agent.py::_build_model` switches on
  `GRANT_SCOUT_MODEL_PROVIDER`. The default is OpenRouter (fast iteration, one key, hundreds of
  models); `bedrock` is a first-class alternate path with the same agent code, so this is a
  demonstration of Strands' provider-agnosticism rather than a workaround.
- **The agent is told to say no.** The system prompt caps output at 3 opportunities and
  explicitly instructs it to report "nothing cleared the bar" rather than pad the list — this is
  the "only surfaces when there's a real decision" theme from the brief, enforced in the prompt,
  not just claimed in the README.

## The system prompt (the actual load-bearing artifact)

This README and this doc both say "the judgment lives in the prompt, not the orchestration." Here
it is verbatim, straight from `src/agent.py::SYSTEM_PROMPT` — not a paraphrase:

```text
You are Grant Scout, a background agent for small community organizations
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
estimate in your risk section -- don't bury a hard blocker under a soft one. Naming a blocker is
not enough: if sam_gov_registered or has_indirect_cost_rate_agreement is "no" or "unknown," call
compliance_guide with the relevant topic ("sam_gov" and/or "nicra") and include its real,
step-by-step process in the brief, not just the fact that a blocker exists. An org that can't
act on your warning hasn't been helped by it.

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
surfaced.
```

Note step 3 is a **drop rule with a condition, not a blanket ban** on zero-history programs — a
program with no FY2021 nonprofit history but an ambiguous (not obviously state/university-aimed)
title survives to the brief stage flagged as an open risk, rather than being silently dropped or
silently trusted; see `sample_run_library.md`'s treatment of the IMLS library programs for a
current example ("these programs *may* fund nonprofits, but I cannot confirm that with the
available data... recommend you manually verify"). Step 6's compliance-burden check adds a
second, independent reason to drop an otherwise-strong opportunity: `sample_run_library.md` and
`sample_run_afterschool.md` both show the Community Services Block Grant (CFDA 93.570) — a
program with real, strong nonprofit award history — dropped anyway because winning it would
cross the $750K Single Audit threshold and impose real compliance costs the org can't absorb.

## Evaluation across profiles, not one anecdote

One clean sample run is a vibe check, not evidence the judgment generalizes. `profiles/` now
ships four differently-shaped orgs — food pantry, public library, community health clinic,
afterschool program — each run live against grants.gov + the real benchmark table with zero
edits beyond stripping Strands' tool-call progress lines:

- `sample_run_food_bank.md`
- `sample_run_library.md`
- `sample_run_health_clinic.md`
- `sample_run_afterschool.md`

## Deployment note

Two entrypoints wrap the same `Agent` object from `src/agent.py` — nothing agent-specific lives
in either adapter:

- `src/run.py` — CLI, used for the hackathon demo video.
- `deploy/agentcore_app.py` — a real `BedrockAgentCoreApp` HTTP entrypoint, verified working
  locally end-to-end against the AgentCore Runtime dev server (see `sample_run_agentcore.md`).
  Not deployed to live AWS infrastructure for this submission (no AWS account configured for
  this build) — `agentcore launch` is the remaining step for an operator with Bedrock
  AgentCore access.
- `src/intake_form.py` — a stdlib-only HTML form, so the org profile can be filled in by
  someone who has never seen YAML (see `sample_run_intake_form.md`). Still runs locally; hosting
  it is the same remaining AWS step as the AgentCore entrypoint above.
