# Architecture

Grant Scout is a single Strands `Agent` with two tools and a system prompt that tells it what
"good enough to surface" means. There's no orchestration framework beyond Strands itself — the
judgment (search → cross-check → drop weak matches → write a brief) lives in the prompt and is
executed via the agent's normal tool-calling loop.

```mermaid
flowchart TD
    subgraph Input
        P[Org profile YAML<br/>mission, budget, states, keywords, volunteer hours]
    end

    subgraph Agent["Strands Agent (src/agent.py)"]
        SP[System prompt:<br/>search → vet → drop weak matches → brief top 3 max]
    end

    subgraph Tools
        T1[search_open_grants<br/>grants.gov public API<br/>live, open/forecasted opportunities]
        T2[historical_award_context<br/>FY2021 USASpending extract<br/>real nonprofit award $ + counts]
    end

    subgraph Model["Model provider (swappable via env var)"]
        OR[OpenRouter<br/>OpenAI-compat endpoint<br/>default]
        BR[Amazon Bedrock<br/>optional, same agent code]
    end

    subgraph Output
        O[Markdown brief:<br/>at most 3 opportunities,<br/>each with fit + $ range + honest risk<br/>OR "nothing cleared the bar"]
    end

    P --> Agent
    Agent <--> T1
    Agent <--> T2
    Agent <--> Model
    Agent --> O
```

## Why this shape

- **Two tools, not ten.** The judging criteria reward "genuine effort and a working, non-trivial
  implementation," not tool-count. The non-trivial part here is the *cross-check*: an opportunity
  that sounds like a fit by title alone gets rejected if `historical_award_context` shows no real
  nonprofit award history for that program. That's the difference between a keyword-matcher and
  an agent that actually vets.
- **Real data, not fixtures.** `search_open_grants` hits grants.gov live. `historical_award_context`
  reads a table derived from a real USASpending.gov bulk pull (`data/extract_benchmarks.sql`
  documents the exact query) — not synthetic or invented numbers.
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
estimate in your risk section -- don't bury a hard blocker under a soft one.

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
   range (grounded in the historical numbers, not a guess), the deadline, the compliance floor
   (SAM.gov/UEI/indirect cost rate status per above), and one honest risk or reason it might not
   be worth the org's time.

Surface at most 3 opportunities. If nothing clears the bar, say so plainly -- do not pad the
list with weak matches just to have something to show. Output format: one Markdown section per
recommended opportunity, then a one-line summary of how many opportunities you reviewed vs.
surfaced.
```

Note step 3 is a **drop rule with a condition, not a blanket ban** on zero-history programs — a
program with no FY2021 nonprofit history but an ambiguous (not obviously state/university-aimed)
title survives to the brief stage flagged as an open risk, rather than being silently dropped or
silently trusted. See `sample_run_food_bank.md`'s Cold Chain Grants call for exactly this case,
and the corrected framing of it in `DEVPOST.md`'s Challenges section.

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
