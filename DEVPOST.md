# Devpost submission draft — Agents for Humans Hackathon

Track: **Good Neighbor Agents**

Status: DRAFT. Fill in `<REPO_URL>` and `<LIVE_DEMO_URL>` (optional) before pasting into the
Devpost form. Video link added once recorded per `VIDEO_SCRIPT.md`.

---

## Project name

**Grant Scout**

## Elevator pitch (one line)

A background agent that quietly hunts and vets federal grants for small nonprofits, and only
interrupts a volunteer board when it finds one worth their limited hours.

## What it does

Small community organizations — food banks, libraries, after-school programs — lose real money
not because writing grant applications is hard, but because *finding the few they can actually
win* is a slow, manual slog through thousands of listings most of them are ineligible for.

Grant Scout takes a one-time org profile (mission, budget, states, focus area, available
volunteer hours) and runs the busywork end to end:

1. Searches grants.gov's live public API for open/forecasted opportunities matching the org.
2. Cross-checks each promising hit against real historical award data (derived from
   USASpending.gov) to see whether nonprofits like this org actually win that program, and at
   what real dollar amount — not a guess.
3. Weighs the application effort against the payoff, against the org's stated volunteer
   capacity.
4. Surfaces at most 3 opportunities with an honest brief (fit, real $ range, deadline, one
   risk) — or says plainly that nothing cleared the bar. It does not pad the list.

See `sample_run_food_bank.md` in the repo for a full, real (not scripted) run — and
`sample_run_library.md`, `sample_run_health_clinic.md`, `sample_run_afterschool.md` for three
more, against three differently-shaped orgs, so the judgment isn't resting on one anecdote.

## Who it's for

Any small 501(c)(3) or community organization without a grant-writing department — food banks,
food pantries, libraries, small local nonprofits, community health orgs, school programs run by
volunteer boards. This is the exact "Good Neighbor" audience: groups serving people, not
individuals with a personal-assistant budget.

## Why it matters

There are ~4M unique federal grant awards on record and 80K+ live opportunity listings at any
time (grants.gov), but a volunteer board with 6 hours a month to spend on grant-seeking cannot
manually triage that. The result is real money left unclaimed by exactly the organizations that
need it most, not because they're ineligible but because nobody had time to look. An agent that
runs this search-and-vet loop in the background and only surfaces genuine, winnable matches
turns "we should apply for grants sometime" into an actual, actionable short list every cycle.

## How we built it

Strands Agents SDK, two tools, one system prompt that encodes the *judgment* (drop plausible-
sounding matches that fail the historical-award cross-check; weigh effort against payoff; cap
output at 3; say "nothing cleared the bar" rather than pad the list). Model provider is
OpenRouter by default (Strands' OpenAI-compatible provider pointed at OpenRouter's endpoint),
with a first-class, code-identical Amazon Bedrock path available via one environment variable —
demonstrating Strands' provider-agnostic design rather than avoiding AWS's own model stack.

Real data end to end: `search_open_grants` calls grants.gov's live public search API (no key
required); `historical_award_context` reads a table derived from a real USASpending.gov bulk
award-data pull (FY2021 prime-award transactions filtered to 501(c)(3) recipients), with the
exact extraction SQL committed alongside it for reproducibility.

The same agent also runs behind a real Amazon Bedrock AgentCore Runtime entrypoint
(`deploy/agentcore_app.py`) — verified locally end-to-end via the AgentCore dev server and a
live HTTP `/invocations` call, not just a claim in a README.

## Challenges we ran into

Grant program titles are misleading by design (a program literally titled "Cold Chain Grants
for Emergency Food Assistance" turned out, per the historical data, to have no verified
nonprofit award history — likely aimed at states or commercial distributors). The zero-history
signal isn't a blanket drop rule, though: the system prompt only auto-drops it when the program
*also* reads as aimed at governments or universities. Cold Chain Grants was ambiguous on that
second condition, so the agent surfaced it as opportunity #3 with the eligibility gap stated as
an explicit, unresolved risk ("I cannot recommend this without you first verifying eligibility")
rather than either silently dropping it or silently trusting the title. Getting the system prompt
to hold that distinction — flag genuine ambiguity, drop clear non-fits, recommend clear fits —
took real iteration, and running it against three more org profiles (library, health clinic,
afterschool program) surfaced the full range: one run recommended two opportunities outright,
one declined all three of its top candidates and said so, and one explicitly talked itself out of
recommending a well-funded, on-topic program (AmeriCorps) once the award size and compliance
burden didn't match the org's five volunteer hours.

## Accomplishments we're proud of

The agent treats "no verified award history" as a real risk to disclose, not a fact to hide or a
fact to auto-reject on. Across four org profiles it produced three different outcomes — two
opportunities surfaced, zero surfaced, and a well-funded program talked out of the shortlist —
using the same system prompt and the same two tools every time. That range, not any single
transcript, is the evidence that the judgment generalizes rather than being tuned to one demo.

## What we learned

Cross-checking one live data source against a second, independent real data source is a cheap,
high-leverage pattern for keeping an agent honest about eligibility claims that titles and
keywords alone will get wrong.

## What's next

Two concrete gaps, both named plainly rather than glossed over. First: deploy the existing,
tested AgentCore entrypoint to live AWS infrastructure (`agentcore launch`), then a scheduled
version that runs weekly per org and only emails a human when a new opportunity clears the bar —
taken from a locally-verified AgentCore endpoint to an always-on one. Second: the CLI + YAML
interface assumed technical comfort the target audience often doesn't have; `src/intake_form.py`
(a real, tested HTML form, zero new dependencies) already closes the *editing* half of that gap —
what's left is hosting it so an org reaches it without anyone running Python locally, which is
the same AWS-deployment step as above.

## Built with

Strands Agents SDK, Python, OpenRouter, Amazon Bedrock (alternate provider path), grants.gov
public API, USASpending.gov public bulk data.

## Links

- Repo: `<REPO_URL>` (MIT license, visible in About)
- Live demo: `<LIVE_DEMO_URL>` (optional)
- Demo video: `<VIDEO_URL>`
