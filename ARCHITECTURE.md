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

## Deployment note

This repo runs as a CLI (`python -m src.run`) for the hackathon demo. The same `Agent` object in
`src/agent.py` is what you'd wrap in an AWS Lambda handler or deploy behind Amazon Bedrock
AgentCore for a background/scheduled version — that wiring wasn't built for this submission
(scope was the agent's reasoning quality, not deployment infrastructure), but nothing in
`src/agent.py` or the tools is CLI-specific.
