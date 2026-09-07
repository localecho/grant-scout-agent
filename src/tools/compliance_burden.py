"""Tool: quantify the structural post-award cost of winning a grant, not just the odds of it.

Born from a taste-council critique (Vu Le, the adversarial seat, in
data/reports/moot_verdict_grant-scout-submission_2026-09-07_v1.txt and again independently in
_v4.txt): a search-and-vet tool that stops at "can this org win it" launders a real systemic
cost into invisibility. Two of those costs are well-documented federal policy, not speculation,
and can be computed exactly rather than gestured at:

1. Indirect cost recovery cap. Under 2 CFR 200.414(f) (the "Uniform Guidance"), any nonprofit
   without a negotiated indirect cost rate agreement (NICRA) may claim a flat 10% de minimis
   rate against Modified Total Direct Costs. Real nonprofit overhead is commonly cited in the
   15-30% range (GuideStar/Candid's "overhead myth" research is the standard citation here);
   this tool uses a conservative 20% assumption, clearly labeled as an assumption, not a
   per-program fact this codebase has verified data for.

2. Single Audit threshold. Under 2 CFR 200 Subpart F, an org that expends $750,000+ in federal
   awards in a fiscal year must undergo a Single Audit -- a real, recurring compliance cost
   (commonly cited in the low-to-mid five figures annually for a small nonprofit's first audit,
   again labeled as a rule-of-thumb, not data this tool has verified).

This does NOT claim to solve the systemic critique -- a flashlight that quantifies the maze's
walls is still a flashlight, not a door. It closes the specific gap of asserting a structural
cost exists without ever putting a number on it.
"""
from __future__ import annotations

from strands import tool

DE_MINIMIS_INDIRECT_RATE = 0.10
ASSUMED_REAL_OVERHEAD_RATE = 0.20
SINGLE_AUDIT_THRESHOLD_USD = 750_000
ASSUMED_FIRST_YEAR_SINGLE_AUDIT_COST_USD = (12_000, 25_000)


@tool
def estimate_compliance_burden(
    award_amount_usd: float,
    has_indirect_cost_rate_agreement: bool | None,
    estimated_current_annual_federal_funding_usd: float = 0.0,
) -> dict:
    """Estimate the real post-award structural costs of winning a specific federal award.

    Call this for any opportunity that survives to the brief stage, using the realistic award
    amount from historical_award_context (use the midpoint of the range if a range was given).

    Args:
        award_amount_usd: the realistic award amount being considered.
        has_indirect_cost_rate_agreement: from the org profile. None = unknown (treated as "no"
            for this estimate, since an org that doesn't know almost certainly doesn't have one).
        estimated_current_annual_federal_funding_usd: the org's current total federal funding
            from all sources, for the Single Audit threshold check.

    Returns:
        A dict with uncovered_overhead_estimate_usd (0 if the org has a negotiated rate),
        crosses_single_audit_threshold (bool), and the assumptions used, so the agent can
        cite them as estimates rather than verified facts.
    """
    has_rate = bool(has_indirect_cost_rate_agreement)
    uncovered_overhead_estimate_usd = 0.0
    if not has_rate:
        shortfall_rate = ASSUMED_REAL_OVERHEAD_RATE - DE_MINIMIS_INDIRECT_RATE
        uncovered_overhead_estimate_usd = round(award_amount_usd * shortfall_rate, 2)

    total_federal_with_this_award = (
        estimated_current_annual_federal_funding_usd + award_amount_usd
    )
    crosses_single_audit_threshold = total_federal_with_this_award >= SINGLE_AUDIT_THRESHOLD_USD

    return {
        "uncovered_overhead_estimate_usd": uncovered_overhead_estimate_usd,
        "overhead_assumption": (
            "0% (org has a negotiated indirect cost rate agreement)"
            if has_rate
            else f"assumes {ASSUMED_REAL_OVERHEAD_RATE:.0%} real overhead vs. the "
            f"{DE_MINIMIS_INDIRECT_RATE:.0%} de minimis rate an org without a NICRA can claim "
            f"under 2 CFR 200.414(f) -- a rule-of-thumb gap, not data this tool has verified "
            f"for this specific program"
        ),
        "crosses_single_audit_threshold": crosses_single_audit_threshold,
        "single_audit_note": (
            f"total federal funding would reach ${total_federal_with_this_award:,.0f}/year, "
            f"at or above the ${SINGLE_AUDIT_THRESHOLD_USD:,} threshold that triggers a Single "
            f"Audit under 2 CFR 200 Subpart F -- commonly a "
            f"${ASSUMED_FIRST_YEAR_SINGLE_AUDIT_COST_USD[0]:,}-"
            f"${ASSUMED_FIRST_YEAR_SINGLE_AUDIT_COST_USD[1]:,}/year recurring cost for a small "
            f"org's first audit (rule of thumb, not verified per-org data)"
            if crosses_single_audit_threshold
            else f"total federal funding (${total_federal_with_this_award:,.0f}/year) stays "
            f"under the ${SINGLE_AUDIT_THRESHOLD_USD:,} Single Audit threshold"
        ),
    }
