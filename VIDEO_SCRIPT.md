# Demo video script (target: 3–4 minutes, max 5)

Format: screen recording + voiceover, per the rules (no camera required). Record terminal at a
large font size; the sample run in `sample_run_food_bank.md` is the safe fallback if a live
grants.gov call is slow/rate-limited during recording — but try live first, it's more
convincing.

## 0:00–0:30 — The problem (cold open, no slides needed)

Voiceover, over a shot of grants.gov's search page with a huge result count visible:

> "There are over 80,000 live federal grant opportunities right now. A small food pantry with
> an all-volunteer board might have six hours a month to spend finding one they can actually
> win. That search-and-filter problem — not the writing — is where they lose real money."

## 0:30–1:00 — Who it's for

> "Grant Scout is a background agent for organizations like that: food banks, libraries,
> small nonprofits — the Good Neighbor track's audience. You give it your org's profile once —
> mission, budget, states, focus area, and how many volunteer hours you actually have — and it
> does the busywork."

Cut to: `profiles/example_food_bank.yaml` on screen, scroll through it briefly.

## 1:00–1:20 — Architecture, 20 seconds, one diagram

Cut to: `ARCHITECTURE.md`'s mermaid diagram (rendered — GitHub renders it natively).

> "It's one Strands agent with two tools. One searches grants.gov live. The other checks a
> real program's award history against actual USASpending federal award data — so a grant that
> *sounds* like a fit gets rejected if nonprofits never actually win it."

## 1:20–3:00 — Live run (the core of the video)

Terminal, full screen:

```
python -m src.run --profile profiles/example_food_bank.yaml
```

Let it run. Narrate over the tool calls as they stream:

> "Watch it search, then cross-check. Here — Cold Chain Grants for Emergency Food Assistance,
> sounds perfect. It checks the historical data... no 501(c)(3) award history at all. It flags
> that as a real risk instead of recommending it anyway."

Let the final brief render on screen (3 opportunities max, one "did not recommend" section).
Pause on the AmeriCorps RSVP recommendation — real dollar range, real deadline, honest risk.

> "Three opportunities out of forty-plus reviewed, each with a real award-size range and an
> honest risk — not forty links dumped on a volunteer board with no context."

## 3:00–3:30 — Provider-agnostic, briefly

Cut to: `src/agent.py`, the `_build_model` function.

> "It defaults to OpenRouter for fast iteration, but it's the exact same agent code on Amazon
> Bedrock — one environment variable. Strands made that a non-event."

## 3:30–3:50 — Tests / reproducibility

Terminal:

```
python -m pytest -v
```

Show green.

> "The tools are unit-tested independently of any model call, so anyone can verify the search
> parsing and the award-history lookup without needing an API key."

## 3:50–4:10 — Why it matters / close

> "This turns 'we should look into grants sometime' into an actual short list, every cycle,
> without asking a volunteer board to become grant-search experts. Thanks for watching."

## Recording checklist

- [ ] Terminal font size ≥ 18pt, high-contrast theme
- [ ] `.env` has a real (rate-limited-safe) OPENROUTER_API_KEY, not committed to the repo
- [ ] Do a dry run first — grants.gov result counts and content will differ from
      `sample_run_food_bank.md` since it's a live search
- [ ] Export at 1080p, keep under 5:00 hard cap
- [ ] Upload to YouTube (unlisted is fine) and paste the link into `DEVPOST.md`
