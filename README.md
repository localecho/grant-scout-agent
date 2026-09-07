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

See a real run (live grants.gov data, no mocked output) in
[`sample_run_food_bank.md`](sample_run_food_bank.md).

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

## Model provider

Strands is provider-agnostic; this repo defaults to **OpenRouter** (one key, fast iteration
across models) and includes a first-class **Amazon Bedrock** path with the identical agent
code — flip `GRANT_SCOUT_MODEL_PROVIDER=bedrock` in `.env` (requires AWS credentials
configured normally). See `src/agent.py`.

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
tests/                        Unit tests (mocked network, no model calls)
```

## License

MIT — see [`LICENSE`](LICENSE).

## Built for

AWS **Agents for Humans Hackathon** (Devpost), Good Neighbor track. See
[`DEVPOST.md`](DEVPOST.md) for the submission write-up.
