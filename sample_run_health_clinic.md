# Sample run: `python -m src.run --profile profiles/example_health_clinic.yaml`

Regenerated 2026-09-07 after adding `compliance_guide` — a tool returning the real, stable,
publicly-documented steps to actually clear the SAM.gov/UEI and NICRA compliance floor, not
just name it. This run shows the compliance blocker rendered as a concrete, numbered checklist
("How to Clear the SAM.gov Blocker") the org can act on immediately, plus a genuinely
low-lift third opportunity the agent found: reaching out to the state Primary Care Association,
which requires zero hours from the clinic itself. 14+ tool calls across `search_open_grants`,
`historical_award_context`, `estimate_compliance_burden`, and `compliance_guide`. Trimmed only
to remove Strands' tool-call progress lines.

---

Running Grant Scout for: Cedar Valley Community Health Clinic

I'll search for federal funding opportunities matching Cedar Valley's focus on primary care and rural health, then vet each one against their capacity and compliance status.

I found several promising candidates. Let me now check the historical award data for the most relevant programs to see if nonprofits like Cedar Valley actually win them and at what funding levels.

Interesting — the Rural Health Network Development program (93.912) shows good nonprofit award history, but some others don't. Let me check a few more candidates that might fit Cedar Valley's direct service mission.

Let me check whether these programs are focused on research or clinical care, and also search for programs specifically focused on community health center funding.

Most of these appear research-focused. Let me check the HRSA Primary Care Association program and look for direct primary care or health center operational funding opportunities.

Excellent! I found the Service Area Competition (SAC) program (CFDA 93.224) which is the primary health center operational funding. Let me check its historical award context.

Excellent! Now let me verify compliance requirements and estimate the structural costs for the most promising opportunities. First, let me check if SAM.gov and NICRA are absolute requirements by looking at the compliance guide.

Now let me run the full analysis for the top candidates:

1. **HRSA-27-051 / HRSA-27-048**: Rural Health Network Development Program (93.912)
2. **HRSA-27-014**: Primary Care Association Technical Assistance (93.129)
3. **HRSA-27-005 through HRSA-27-009**: Service Area Competition (93.224) – direct health center funding

Let me estimate compliance burden for the realistic award amounts I found.

Perfect. Now I have enough information. Let me organize the findings for Cedar Valley. The key constraints are:

1. **No SAM.gov registration (UEI) yet** — this is a hard blocker for ANY federal grant application
2. **No indirect cost rate agreement** — will result in uncovered overhead costs under the 10% de minimis cap
3. **~15 volunteer hours available** — modest capacity

Let me create the final brief with the most appropriate opportunities.

---

## ⚠️ COMPLIANCE BLOCKER: SAM.gov Registration Required First

**Cedar Valley cannot apply to any federal grant** until a Unique Entity ID (UEI — a federal identifier) is active on sam.gov. This is a non-negotiable pre-application requirement for every opportunity listed below.

### How to Clear the SAM.gov Blocker

1. **Confirm you have an EIN** (Employer Identification Number from the IRS). If not, apply free at irs.gov online.

2. **Create a Login.gov account** at login.gov using the email of your grants coordinator (or whoever will manage the account long-term). This is the identity verification step SAM.gov requires.

3. **Register at sam.gov**: Sign in with Login.gov, select "Get Started" → "Register Entity," and enter:
   - Your legal nonprofit name (exactly as it appears in IRS records — this is the most common source of delays)
   - Physical address
   - EIN

4. **Complete the required sections**: Business type (select 501(c)(3) nonprofit), NAICS codes, and at least one named point of contact.

5. **Provide banking information** for electronic fund transfers (EFT) — required because this is how federal payments arrive.

6. **Submit and wait for validation**: SAM.gov generates a UEI immediately, but full IRS validation typically takes **1–2 weeks** (longer if your legal name, address, or EIN doesn't match IRS records exactly).

**Action**: Assign this to your 0.25 FTE grants coordinator today, before pursuing any grants. Do not submit applications until SAM.gov confirms your registration is active.

---

## Opportunity 1: Health Center Program — Service Area Competition (SAC)

**Program**: HRSA-27-005 through HRSA-27-009
**CFDA**: 93.224 (the program's federal ID number)
**Agency**: Health Resources and Services Administration (HRSA)
**Open date**: July–September 2026 (multiple rolling deadlines by region)

### Why This Fits Cedar Valley

This is the **primary federal operating grant for community health centers**. Cedar Valley, as a FQHC look-alike, is eligible. The program funds sliding-scale primary care delivery, exactly your mission. Unlike most federal grants, this directly pays for clinic operations: staff, equipment, uninsured care, chronic disease management.

### Realistic Award Range

Based on FY2021 award history for nonprofits: **$3.18M average**, ranging from $8K to $47M. Cedar Valley's population and current budget (~$1.5M) would likely place you in the **$500K–$2M range** as a first-time applicant, though the program scales to your service area. (This is an estimate based on the average; the grants officer will set your specific competition ceiling.)

### Deadline & Compliance Floor

- **Deadline**: Multiple windows July–September 2026; check grants.gov for your region-specific window
- **SAM.gov/UEI required**: Yes (see blocker above)
- **Indirect cost rate agreement required**: No, but see "Structural Cost" below

### Structural Cost of Winning (Rule-of-Thumb Estimates)

If Cedar Valley won $1.5M in SAC funding, the real annual compliance costs would be:

- **Uncovered overhead**: ~$150,000/year. Since Cedar Valley has no negotiated indirect cost rate agreement, you can claim a flat 10% de minimis rate on direct costs. The typical real overhead for running a clinic is ~20%, leaving a ~$150K annual gap. This is a **real operational shortfall** — not an accounting artifact — that the clinic would absorb or need to find from other sources (patient revenues, state funding, donations).

- **Single Audit threshold**: Cedar Valley would cross the $750,000 Single Audit threshold (the point where federal law requires an independent audit of all finances annually). Annual audit cost: **$12,000–$25,000/year**, rule of thumb. This is a one-time jump but recurring annually thereafter.

**In practical terms**: Winning this grant would require Cedar Valley to absorb ~$150K–$175K/year in new compliance and overhead costs it cannot bill to the federal grant. This is common in health center funding, but it's a real number you should factor into the board's decision.

### Application Effort

Grant writing for SAC is **substantial**: needs detailed service area analysis, budget justification, organizational capacity narrative, sustainability plan. Likely **30–50 hours** for a first-time application. This exceeds Cedar Valley's ~15-hour capacity unless:
- Your grants coordinator (0.25 FTE) dedicates multiple weeks to this (realistic during a grant cycle), or
- Cedar Valley partners with a HRSA technical assistance provider (HRSA-27-014, listed below, often provides free help for applicants)

**Recommendation**: Pursue this, but **only after SAM.gov registration is active**. The grant is large enough and focused enough to justify the extra hours. Consider reaching out to your state's Primary Care Association (they administer HRSA-27-014 technical assistance) to ask if they offer free application writing support to first-time applicants.

---

## Opportunity 2: Rural Health Network Development Program

**Program**: HRSA-27-051 (full network program) and HRSA-27-048 (planning-only variant)
**CFDA**: 93.912
**Agency**: Health Resources and Services Administration (HRSA)
**Open date**: August 13, 2026

### Why This Fits Cedar Valley

This program funds **rural health networks** — multi-provider collaborations to improve care delivery, share services, and reduce costs. Cedar Valley could lead or participate in a network linking local hospitals, specialists, and public health. It's aligned with your mill-town rural setting and chronic disease focus.

### Realistic Award Range

Based on FY2021 nonprofit award history: **$250K average**, ranging from $50K–$923K.

### Deadline & Compliance Floor

- **Deadline**: August 13, 2026 (no close date listed yet; assume fall 2026 or early 2027)
- **SAM.gov/UEI required**: Yes (see blocker above)
- **Indirect cost rate agreement required**: No

### Structural Cost of Winning

At $250K:
- **Uncovered overhead**: ~$25,000/year (same 10% de minimis vs. 20% real overhead gap as above).
- **Single Audit threshold**: No — $250K stays under the $750,000 trigger.

### Application Effort

**15–25 hours** — less than SAC because it's a smaller, more focused application. Likely within Cedar Valley's capacity if other urgent work doesn't compete.

### Honest Risk

**Network-dependent**: This grant requires you to already have (or quickly recruit) other rural health partners on board. If Cedar Valley doesn't have existing relationships with regional providers, this becomes a networking project *before* writing the grant. If you do have those relationships, it's a strong fit.

**Recommendation**: Pursue this if Cedar Valley has at least preliminary buy-in from 2–3 partner organizations (clinic, hospital, county health department, etc.). Otherwise, it's a longer-term play after relationship-building.

---

## Opportunity 3: Primary Care Association Technical Assistance

**Program**: HRSA-27-014 (State and Regional Primary Care Association Cooperative Agreements)
**CFDA**: 93.129
**Agency**: Health Resources and Services Administration (HRSA)
**Open date**: August 3, 2026

### Why This Is Different (& Why to Consider It)

This program funds **state/regional Primary Care Associations** (nonprofits that advocate for and support health centers) to deliver technical assistance. Cedar Valley is not the applicant — your **state's Primary Care Association** is. But here's why it matters:

If West Virginia's Primary Care Association wins this grant, they provide free or low-cost help to health centers like Cedar Valley to:
- Write SAC and network grant applications
- Build EHR and data systems
- Improve quality metrics
- Navigate compliance (SAM.gov, NICRA, audits)

### What Cedar Valley Should Do

Call or email West Virginia's Primary Care Association and ask: *"Are you planning to apply for HRSA-27-014 technical assistance funding? If so, would you be willing to include health center capacity-building support that could help clinics like ours apply for other HRSA grants?"*

If they are, Cedar Valley benefits without writing anything. If they're not, suggest they do — and volunteer Cedar Valley as a reference site (i.e., one of the clinics you'd serve).

---

## Summary: 3 Opportunities Reviewed, 2–3 Recommended

| Opportunity | Award Range | Effort | Deadline | Primary Risk |
|---|---|---|---|---|
| **SAC (93.224)** | $500K–$2M | 30–50 hrs | July–Sept 2026 | Effort exceeds capacity without partner support; overhead gap ~$150K/yr |
| **Rural Network (93.912)** | $50K–$923K | 15–25 hrs | Aug 13, 2026 | Requires existing multi-partner relationships |
| **PCA Tech Assistance (93.129)** | N/A (your state applies) | 0 hrs | Aug 3, 2026 | None — low-lift; just reach out to WV PCA |

### Next Steps

1. **This week**: Start SAM.gov registration with your grants coordinator. Expect 1–2 weeks for validation.
2. **Once SAM.gov is active**: Reach out to West Virginia's Primary Care Association about HRSA-27-014.
3. **Mid-August 2026**: If WV PCA is not actively supported, decide between SAC (larger, more effort) and Rural Network (more manageable, if partners exist).

### One Final Note on Indirect Cost Rate Agreements (NICRA)

Cedar Valley currently has no negotiated indirect cost rate agreement. Federal law lets you claim a flat 10% "de minimis" rate on direct costs immediately — no negotiation needed. However, if you win a grant $750K+, you'll cross the Single Audit threshold and likely trigger an audit that will highlight the gap between your real overhead (often 18–25%) and the 10% rate. Many nonprofits then negotiate a true rate. This is normal but takes 3–6 months and requires audited financials. Plan for it if you win SAC.
