# Sample run: `python -m src.run --profile profiles/example_health_clinic.yaml`

Regenerated 2026-09-07 after adding the compliance-floor instruction to `SYSTEM_PROMPT`
(`src/agent.py`) and the `sam_gov_registered` / `has_indirect_cost_rate_agreement` fields to
`OrgProfile` — a fix made in response to a taste-council review
(`data/reports/moot_verdict_grant-scout-submission_2026-09-07_v1.txt`) flagging that hour
estimates alone miss the real first hurdle: an org can have plenty of volunteer capacity and
still be blocked for weeks by a missing SAM.gov registration. This replaces an earlier run made
before that fix — kept only this version so the repo doesn't carry stale evidence of a
now-fixed gap. 14 tool calls: 5 `search_open_grants`, 9 `historical_award_context`. Trimmed
only to remove Strands' tool-call progress lines.

---

Running Grant Scout for: Cedar Valley Community Health Clinic

## Summary

**Reviewed: 47 opportunities | Surfaced: 1**

---

## **STOP: Compliance Blocker Alert**

Before examining specific opportunities, Cedar Valley Community Health Clinic faces a **hard requirement that must be resolved first**:

- **SAM.gov Registration & Unique Entity ID (UEI): NO** ✗
- **Indirect Cost Rate Agreement: NO** ✗

**Every federal grant requires an active SAM.gov registration and UEI before submission.** This is not a soft preference—it's a system-level blocker. The clinic cannot submit a federal application without it.

- **Timeline to resolve:** SAM.gov registration typically takes 3–5 business days once initiated, but full validation can take 2–3 weeks. The clinic should **prioritize this immediately** and register at sam.gov.
- **Indirect cost rate agreement:** Many HRSA and HHS programs require a negotiated indirect cost rate (NICRA) negotiated through HHS Shared Services Centers or the clinic's cognizant federal agency. This is separate from SAM registration and takes additional time (typically 4–8 weeks if pursuing for the first time).

**Recommendation:** Do not proceed with grant applications until SAM.gov registration is complete. An indirect cost rate agreement can often be negotiated in parallel with an application, but SAM registration is non-negotiable.

---

## Opportunity 1: **Fiscal Year 2027 Service Area Competition (HRSA-27-006/008/009 — Health Center Program)**

**Program:** HRSA-27-006 / HRSA-27-008 / HRSA-27-009
**CFDA:** 93.224 (Health Center Program)
**Sponsoring Agency:** Health Resources and Services Administration (HRSA)
**Status:** Open 07/31/2026 – TBD (no close date posted; typical HRSA cycles close in fall)

### Why This Fits
Cedar Valley is a "look-alike" seeking to provide primary care to uninsured/underinsured residents in a rural mill town. The HRSA Health Center Program (SAC) is the **primary federal operating grant program** for health centers that serve as Federally Qualified Health Centers (FQHCs) or meet FQHC parity standards. A look-alike clinic with demonstrated capacity and patient need in a health professional shortage area is exactly the intended audience for this program.

### Realistic Award Range
FY2021 data shows 254 nonprofit health centers were funded under CFDA 93.224 with an **average award of $3.18M, min $7.8K, max $46.9M** across 32 states. Cedar Valley's $1.45M budget suggests it would likely fall in the **$400K–$1.5M range** for a look-alike clinic serving a defined rural/mill-town population—well below the mean (which includes large urban systems), but substantial enough to meaningfully expand services.

### Deadline & Key Dates
- **Application open:** 07/31/2026
- **Expected close:** Late fall 2026 (likely October–November; check grants.gov 30 days before anticipated close)

### Compliance Notes
- **SAM.gov/UEI:** Required (currently **NOT** complete — do not apply until resolved).
- **NICRA (indirect cost rate):** Required or allowed. Many HRSA programs allow you to negotiate a rate *during* the grant period if you don't have one pre-award, but having one pre-submission strengthens the application. Cedar Valley should contact its HHS cognizant agency (likely the Philadelphia HRSA regional office for WV) to discuss negotiating an NICRA in parallel with application prep.

### Estimated Grant-Writing Effort
**~25–35 hours.** This is a full-cycle federal application (SF-424, HRSA needs/capacity narrative, budget justification, compliance documents, program-specific forms). Cedar Valley has ~15 volunteer/staff hours available. This exceeds capacity **unless the clinic brings in a consultant or partner grant writer at no cost.**

### Why It Might Not Be Worth It (Risk)
1. **Compliance blocker:** SAM registration and NICRA negotiation are non-negotiable prerequisites and will delay submission by 3–8 weeks.
2. **Grant-writing capacity shortfall:** 25–35 hours far exceeds the 15 hours available. The clinic would need external pro-bono writing help (consider reaching out to Primary Care Association (PCA) chapters in WV—listed in search result HRSA-27-014—which provide technical assistance to health centers).
3. **Competitive:** Even though 254 awards were made in FY2021 nationwide, a look-alike clinic competing with FQHC-designated centers and larger networks may have lower odds. Ask HRSA regional staff about funding patterns for look-alikes vs. FQHCs in WV specifically.

---

## Opportunities Dropped (Analysis)

**Rural Health Network Development Program (HRSA-27-051, CFDA 93.912):** While this program *did* fund nonprofits in FY2021 (23 awards, avg $250K), it focuses on *network development and care coordination*, not individual clinic operations. Cedar Valley's profile suggests it needs **operating support**, not network facilitation. A networked clinic could reapply to this after establishing an FQHC designation, but this is not the right fit for standalone clinic funding.

**Appalachian Region Healthcare Support Program (HRSA-27-053, CFDA 93.619):** Zero FY2021 nonprofit award history returned. Program rules may restrict awards to state/local governments or research institutions. Dropped pending manual verification of eligibility.

**Rural Communities Opioid Response Programs (HRSA-27-040/043, CFDA 93.690):** No FY2021 nonprofit award history. These programs may be restricted to non-health-center providers or academic institutions. Not recommended without further eligibility verification.

**Chronic Care Telehealth Centers of Excellence (HRSA-27-055, CFDA 93.467):** No FY2021 nonprofit award history. Likely restricted to research institutions or academic medical centers. Dropped.

**NIH research programs (RFAs for chronic disease research, pain management, etc.):** Require principal investigator credentials, research protocols, and IRB approval—structurally mismatched for a clinical service organization with no research infrastructure. Dropped.

---

## Next Steps

1. **Register on SAM.gov immediately.** Assign this to the 0.25 FTE grants coordinator. Target: complete by end of month.
2. **Contact WV HRSA Regional Office** (Philadelphia Regional Office covers WV) to discuss NICRA negotiation and ask about FY2027 Health Center Program eligibility for look-alikes in rural mill towns.
3. **Contact WV Primary Care Association** (if one exists; check HRSA regional resources) for pro-bono grant-writing support or referral to consultants who specialize in FQHC/look-alike applications.
4. **Monitor grants.gov for final SAC close date** (expected late fall 2026) and prepare a Letter of Intent or pre-application inquiry to HRSA if that option becomes available.
