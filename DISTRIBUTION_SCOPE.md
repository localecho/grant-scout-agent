# Grant Scout — minimal distribution-ready scope

**Goal:** the smallest hosted surface that lets a real "yes" turn into a paying,
onboarded customer without the operator in the loop after that point — not a
full SaaS platform, and not built before a real customer exists to build it
for (customer-conscience: don't build the next layer until a named human
has actually said yes to this one).

**Status: SCOPED, NOT BUILT.** Nothing here should be started until there's
a real org ready to pay, per the conversation this came out of — the binding
constraint is the first 3-5 customer relationships, not the infrastructure.
Building this speculatively would be exactly the failure mode this fleet's
customer-conscience discipline exists to catch.

## What's already there (reusable, not new work)
- `src/agent.py` + the four Strands tools (`search_open_grants`,
  `historical_award_context`, `estimate_compliance_burden`,
  `compliance_guide`) — the actual product logic, provider-agnostic
  (OpenRouter today, Bedrock via one env var).
- `deploy/agentcore_app.py` — an existing AWS AgentCore adapter, proof the
  agent already runs as a hosted service, not just a local CLI.
- `profiles/*.yaml` — the org-intake schema already exists as a file format;
  a web form is just a UI over this same shape.

## The 3 pieces actually missing (est. 3-4 focused days total)

1. **Hosted web wrapper (~1-2 days).** Thin FastAPI or Next.js front end:
   an intake form matching the existing YAML profile schema → runs the
   agent → renders the brief as an HTML page instead of terminal output.
   Reuses `deploy/agentcore_app.py` as the backend, doesn't reinvent it.

2. **Stripe self-serve billing (~1 day).** Stripe Checkout (hosted, no PCI
   burden) for a single $30/mo plan, webhook gates access to the web app.
   No custom billing UI needed.

3. **Auth (~0.5 day).** Magic-link email auth (Clerk, Supabase auth, or a
   minimal custom implementation) — one org profile per account. No
   passwords, no multi-user/board accounts yet.

## Deliberately deferred until a real paying customer exists
- Multi-user / board-member accounts
- Usage analytics dashboard
- Support beyond email
- Admin panel, multi-org management
- Marketing site beyond one landing page
- Any AWS Bedrock AgentCore deploy work beyond what already exists (still
  optional per the hackathon rules, not required for this either)

## What this scope does NOT solve
The actual constraint from the valuation conversation: getting a volunteer
food-bank board to trust an unfamiliar tool with recurring payment. This
plan makes the *tenth* customer effortless. It does nothing for the *first*
— that still requires a warm intro, a partner (e.g. Feeding America), or a
testimonial that doesn't exist yet. Build this when that path is real, not
before.
