"""Tool: help an org clear the compliance floor, not just name it.

Born from the sharpest form of Vu Le's critique across three independent taste-council passes:
naming a barrier (SAM.gov registration, a negotiated indirect cost rate) isn't the same as
helping an org clear it. This tool returns the real, current, publicly-documented steps for
both processes -- stable federal procedure, not per-program data this codebase has verified,
so it's safe to state as fact rather than as an estimate the way estimate_compliance_burden's
overhead-rate assumption is.

This does not close Vu Le's deeper "reach" critique -- whether a real org has actually used
this guidance -- which requires real-world deployment and usage, not more local code. It closes
the narrower, real gap of a tool that could name a wall but not describe a way over it.
"""
from __future__ import annotations

from strands import tool

SAM_GOV_STEPS = [
    "Confirm the org has an EIN (Employer Identification Number) from the IRS. Most established "
    "nonprofits already have one; if not, apply free at irs.gov -- takes minutes online.",
    "Create a free Login.gov account (SAM.gov requires this for identity verification) at "
    "login.gov, using the email of whoever will manage the registration long-term, not a "
    "personal email that might change.",
    "Go to sam.gov, sign in with Login.gov, and select 'Get Started' then 'Register Entity' "
    "(new registration) -- not 'Search Records', which only looks up existing entities.",
    "Enter the org's legal business name (exactly as filed with the IRS), physical address, "
    "and EIN. SAM.gov cross-validates this against IRS records; a mismatch (e.g. a DBA name "
    "instead of the legal name) is the most common reason registrations stall.",
    "Complete the Core Data, Assertions, and Points of Contact sections: business types "
    "(select nonprofit/501(c)(3)), NAICS codes for the org's activities, and at least one "
    "named point of contact.",
    "Provide banking information for Electronic Funds Transfer (EFT) -- required before "
    "registration can be marked active, since this is how any federal award actually gets paid.",
    "Submit for validation. SAM.gov issues a Unique Entity ID (UEI) automatically once the "
    "registration is submitted (UEI replaced the old DUNS number in April 2022); full "
    "validation against IRS records commonly takes 1-2 weeks but can run longer if any field "
    "doesn't match exactly.",
    "Registration must be renewed annually (SAM.gov will email a reminder) -- an expired "
    "registration blocks new applications the same way a missing one does.",
]

NICRA_STEPS = [
    "Know the no-negotiation fallback: under 2 CFR 200.414(f), any org that has never had a "
    "negotiated indirect cost rate can claim a flat 10% de minimis rate on Modified Total "
    "Direct Costs with no negotiation required -- this is available immediately, always, and "
    "is what estimate_compliance_burden assumes when has_indirect_cost_rate_agreement is False.",
    "To negotiate a real rate instead: identify the org's cognizant agency (the federal agency "
    "providing the largest share of the org's direct federal funding, or assigned by HHS's "
    "Division of Cost Allocation for most nonprofits without an obvious cognizant agency).",
    "Prepare an indirect cost rate proposal per 2 CFR 200 Appendix IV (for nonprofits): a cost "
    "allocation plan splitting direct vs. indirect costs, built from at least one year of "
    "actual audited or reviewed financial statements.",
    "Submit the proposal to the cognizant agency for review and negotiation. A first-time "
    "negotiation commonly takes several months, not weeks -- this is why estimate_compliance_burden "
    "treats 'no NICRA' as the realistic default for an org's near-term award, not a same-cycle fix.",
    "Once negotiated, the rate applies to ALL federal awards the org receives, not just one "
    "grant -- a one-time investment, not a per-application cost.",
]


@tool
def compliance_guide(topic: str) -> dict:
    """Return the real, step-by-step process to clear a named compliance floor item.

    Call this when an opportunity is otherwise strong but the org's SAM.gov registration or
    indirect cost rate agreement status is "no" or "unknown", so the brief can tell the org how
    to clear the blocker, not just that it exists.

    Args:
        topic: "sam_gov" or "nicra".

    Returns:
        A dict with "steps" (ordered list of real, stable federal-process steps) and
        "typical_timeline" (a plain-language estimate, clearly a rule of thumb).
    """
    topic = topic.strip().lower()
    if topic == "sam_gov":
        return {
            "steps": SAM_GOV_STEPS,
            "typical_timeline": "1-2 weeks for a clean application; longer if the legal name, "
            "address, or EIN don't exactly match IRS records on the first submission.",
        }
    if topic == "nicra":
        return {
            "steps": NICRA_STEPS,
            "typical_timeline": "Immediate for the 10% de minimis fallback (no negotiation "
            "needed); several months for a first-time negotiated rate.",
        }
    return {
        "steps": [],
        "typical_timeline": "",
        "error": f"Unknown topic {topic!r}; expected 'sam_gov' or 'nicra'.",
    }
