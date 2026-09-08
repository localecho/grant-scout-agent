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

Strands Agents SDK, four tools, one system prompt that encodes the *judgment* (drop plausible-
sounding matches that fail the historical-award cross-check; quantify what winning actually
costs; weigh effort against payoff; cap output at 3; say "nothing cleared the bar" rather than
pad the list). Model provider is
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

Grant program titles are misleading by design, and "no verified award history" isn't a blanket
drop rule — the system prompt only auto-drops a zero-history program when it *also* reads as
aimed at governments or universities. When that second condition is ambiguous, the agent
surfaces the program anyway with the gap stated as an explicit, unresolved risk rather than
either silently dropping it or silently trusting the title — `sample_run_library.md` shows this
for the IMLS library programs ("these programs *may* fund nonprofits, but I cannot confirm that
with the available data... recommend you manually verify"). A taste-council review then caught a
sharper failure mode in an earlier version of that same run: the agent had papered over a
real data gap with its own outside "I know from grant-writing practice..." claim instead of just
naming the gap — a groundedness violation, fixed by an explicit instruction to never substitute
outside knowledge for what the tools actually returned.

The harder challenge came from a different critique entirely: a program can have excellent,
well-documented nonprofit award history and still be a bad recommendation, because *winning* it
imposes real federal compliance costs — an indirect-cost-rate gap, or crossing the $750K Single
Audit threshold — that a six-volunteer-hour board can't absorb. `search_open_grants` and
`historical_award_context` together can't see that; a third tool, `estimate_compliance_burden`,
computes it from the real award size and the org's compliance-floor status. It's now load-bearing
in the recommend/drop decision, not just a caveat: `sample_run_library.md` and
`sample_run_afterschool.md` both show the Community Services Block Grant (CFDA 93.570) — a
program with strong nonprofit history — dropped specifically because winning it would trigger a
Single Audit the org can't afford.

A nonprofit-sector critic on our own review panel pushed further: naming a blocker (SAM.gov,
no indirect cost rate) isn't the same as helping an org clear it. A fourth tool,
`compliance_guide`, answers that directly — it returns the real, stable, publicly-documented
federal process for both (EIN → Login.gov → sam.gov registration → EFT banking → validation for
SAM.gov; the 10% de minimis fallback vs. a negotiated rate for NICRA), and the agent includes it
verbatim in the brief instead of just naming the wall. `sample_run_food_bank.md` shows this live:
the org gets an 8-step SAM.gov registration walkthrough, not just "you need to register."

## Accomplishments we're proud of

Run against four differently-shaped orgs (food pantry, library, health clinic, afterschool
program), the current agent converges on the same disciplined shape every time: flag the
compliance floor before searching, ground every claim in what the tools actually returned (never
padded with outside assumptions), give the org a real path to clear any blocker it names, and
surface exactly the one opportunity that clears every bar — fit, real award history, capacity,
*and* affordable compliance cost — rather than a list. That's not one demo tuned to look good;
it's the same prompt and the same four tools producing consistent, defensible judgment across
four real, live runs.

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
