# Grant Scout

A background agent that finds and vets federal funding opportunities for small community
organizations — food banks, libraries, after-school programs, community health nonprofits —
that don't have a grant-writing department. Built with the [Strands Agents
SDK](https://strandsagents.com) for AWS's **Agents for Humans Hackathon** (Good Neighbor track).

## The problem

Small nonprofits lose real money to a search problem, not a writing problem: grants.gov lists
tens of thousands of live opportunities, most of which a given org is structurally ineligible
for (aimed at state governments, universities, or Fortune 500 contractors), and figuring out
*which few* are real, winnable, and worth a volunteer board's limited hours takes hours of
manual triage per grant cycle. That triage is exactly the kind of repetitive, judgment-heavy
background task an agent should absorb — and only interrupt a human for the handful of
opportunities that actually clear the bar.

## What it does

Give it a one-time org profile (mission, budget, states served, focus keywords, how many
volunteer hours are realistically available for grant writing). It then:

1. **Searches** grants.gov's live public API for currently open or forecasted opportunities
   matching the org's focus area.
2. **Cross-checks each candidate against real award history** — a table derived from
   USASpending.gov's public bulk grant-award data — to see whether 501(c)(3) nonprofits
   actually win that program, and at what real dollar range. A program that *sounds* like a
   fit by title alone (e.g. a "nutrition" program that's actually federal health-center
   funding) gets dropped here instead of wasting a volunteer's afternoon.
3. **Weighs application cost against payoff** against the org's stated volunteer-hour budget.
4. **Surfaces at most 3 opportunities** — each with the real historical award range, the
   deadline, and one honest risk — or says plainly that nothing cleared the bar this cycle.

See real runs (live grants.gov data, no mocked output) against four differently-shaped orgs —
[`sample_run_food_bank.md`](sample_run_food_bank.md),
[`sample_run_library.md`](sample_run_library.md),
[`sample_run_health_clinic.md`](sample_run_health_clinic.md),
[`sample_run_afterschool.md`](sample_run_afterschool.md) — chosen to cover the full range of
outcomes (opportunities surfaced, zero surfaced, a well-funded program talked out of the
shortlist), not just one clean anecdote.

## Why this is a non-trivial Strands build

The interesting part isn't "call an LLM with a search tool." It's that the agent is instructed
to actively **reject** plausible-looking matches using a second, independent real-data source —
see [`ARCHITECTURE.md`](ARCHITECTURE.md) for the tool-calling flow and why the two-tool
cross-check is the load-bearing design decision here, not an afterthought.

## Quickstart

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in OPENROUTER_API_KEY (openrouter.ai/keys)
python -m src.run --profile profiles/example_food_bank.yaml
```

Run the test suite (no network or API key required — the agent's tools are unit-tested
independently of any model call):

```bash
python -m pytest -v
```

`tests/test_judgment_invariants.py` is a small automated eval harness, not just tool-plumbing
tests: it checks real properties of the committed sample-run transcripts (never surfaces more
than 3 opportunities, at least one profile gets zero surfaced, every verdict is grounded in a
real dollar figure or an explicit no-award-history finding) so a prompt regression breaking the
agent's judgment gets caught mechanically, not by re-reading four transcripts by eye.

## Model provider

Strands is provider-agnostic; this repo defaults to **OpenRouter** (one key, fast iteration
across models) and includes a first-class **Amazon Bedrock** path with the identical agent
code — flip `GRANT_SCOUT_MODEL_PROVIDER=bedrock` in `.env` (requires AWS credentials
configured normally). See `src/agent.py`.

## Running on Amazon Bedrock AgentCore

`deploy/agentcore_app.py` wraps the same `Agent` from `src/agent.py` in a
[`BedrockAgentCoreApp`](https://strandsagents.com/docs/user-guide/deploy/deploy_to_bedrock_agentcore/) —
no separate agent logic, just the deployment adapter. Verified working locally end-to-end
(see [`sample_run_agentcore.md`](sample_run_agentcore.md) for a real HTTP request/response):

```bash
python deploy/agentcore_app.py                          # starts the local AgentCore dev server
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"profile_path": "profiles/example_food_bank.yaml"}'
```

Deploying to real AWS infrastructure (`agentcore configure` + `agentcore launch`) requires an
AWS account with Bedrock AgentCore access, which wasn't set up for this submission — see Known
limitations.

## No-YAML intake for non-technical org staff

The CLI's `--profile some.yaml` flow assumes comfort hand-editing YAML — not a safe assumption
for the volunteer boards this is built for. `src/intake_form.py` serves a plain HTML form
(stdlib `http.server` only, no new dependency) that takes the same fields as a profile YAML and
saves a normal profile file — no special-casing, reads through the same `OrgProfile.from_yaml`
path as one written by hand:

```bash
python -m src.intake_form   # prints a local URL; open it in a browser, fill in the blanks
```

See [`sample_run_intake_form.md`](sample_run_intake_form.md) for a real, unmocked run (server
started, real HTTP requests, a real saved YAML, and a plain-language validation error instead of
a stack trace on bad input).

## Known limitations

- **Not deployed to live AWS infrastructure.** The AgentCore entrypoint above is real,
  tested code, but this submission runs it locally rather than on Bedrock AgentCore Runtime
  (no AWS account was configured for this build). `agentcore launch` is the remaining step.
- **Benchmark data is FY2021.** `historical_award_context` reads a static extract; it doesn't
  re-pull from USASpending live. A program with no FY2021 nonprofit history isn't necessarily
  unwinnable today — the agent is instructed to treat that as a real risk signal to disclose,
  not silent proof of ineligibility (see the sample run's Cold Chain Grants call). Regenerate
  the table for a newer year with `data/extract_benchmarks.sql`.
- **`search_open_grants` caps at 25 results per call** (grants.gov's per-request max) with no
  pagination across calls. Fine for a single org's focused keyword search; would need paging
  to exhaustively enumerate a broad category.
- **The shipped interface still needs one technically-comfortable person, just fewer of them.**
  `src/intake_form.py` (below) closes the *editing* gap — filling in a browser form instead of
  hand-writing YAML — but someone still has to run `python -m src.intake_form` once and hand the
  org a URL. Closing that last *hosting* gap means an always-on deployment (AgentCore, Lambda, or
  similar), which this submission has not done — see the AgentCore section above.

## Bring your own org

Copy `profiles/example_food_bank.yaml`, edit the fields, and point `--profile` at your new
file. No code changes required.

## Project layout

```
src/
  agent.py                    Strands Agent + system prompt + model provider switch
  profile.py                  Org profile loader
  run.py                      CLI entrypoint
  tools/
    grants_gov.py             Live grants.gov search tool
    historical_benchmarks.py  Real FY2021 USASpending nonprofit-award lookup tool
data/
  nonprofit_award_benchmarks_fy2021.csv   Derived real award-history table (see extract_benchmarks.sql)
profiles/
  example_food_bank.yaml      Sample org profile used in the demo
  example_library.yaml        Rural public library profile (see sample_run_library.md)
  example_health_clinic.yaml  FQHC-lookalike health clinic profile (see sample_run_health_clinic.md)
  example_afterschool.yaml    Afterschool youth program profile (see sample_run_afterschool.md)
tests/                        Unit tests (mocked network, no model calls)
deploy/
  agentcore_app.py            Bedrock AgentCore Runtime entrypoint (same Agent, HTTP adapter)
```

## License

MIT — see [`LICENSE`](LICENSE).

## Built for

AWS **Agents for Humans Hackathon** (Devpost), Good Neighbor track. See
[`DEVPOST.md`](DEVPOST.md) for the submission write-up.
