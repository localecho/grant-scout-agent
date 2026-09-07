# Sample run: `python -m src.run --profile profiles/example_health_clinic.yaml`

Captured 2026-09-07 against live grants.gov data and the real FY2021 USASpending benchmark
table shipped in `data/`. Not edited for content — trimmed only to remove the tool-call
progress lines Strands streams to stdout (`Tool #1: search_open_grants`, etc.). 18 tool calls
total: 9 `search_open_grants`, 9 `historical_award_context`.

This run shows the agent surfacing real awards while flagging a **structural eligibility
question the org profile itself couldn't answer** (FQHC-lookalike status) — rather than
either hiding that ambiguity or refusing to engage with it.

---

Running Grant Scout for: Cedar Valley Community Health Clinic

I'll search for federal funding opportunities matching Cedar Valley Community Health Clinic's focus, then vet each candidate against real award history and the org's capacity constraints.

Good initial yield. Now let me filter to the most promising candidates for a FQHC-lookalike clinic in rural WV and check real award history:

**Strong candidates to vet:**
1. HRSA-27-051: Rural Health Network Development Program (93.912)
2. HRSA-27-045: Rural Health Value Program (93.692)
3. HRSA-27-053: Appalachian Region Healthcare Support Program (93.619)
4. HRSA-27-040/043: Rural Communities Opioid Response Program (93.690)

**Lower priority (research-focused, unlikely fit):**
- Most NIH programs (require research infrastructure, not service delivery)
- Title X (family planning; not primary focus)
- THCGME (graduate medical education; not a clinic service model)

Let me check award history on the HRSA programs:

Interesting: only 93.912 (Rural Health Network Development) shows strong nonprofit award history. The others (93.692, 93.619, 93.690) show no FY2021 nonprofit award records in the sample. Let me dig deeper on those three to understand their real eligibility:

No award history in the FY2021 sample for those three. Given that these are newer or more specialized HRSA programs, and without nonprofit precedent, **I should not recommend them without flagging they may be state/local-focused or require manual eligibility review by the org.**

Let me check whether 93.912 award history actually includes similar clinic models and verify the fit, then widen the search to catch any additional primary-care or clinic-focused programs I may have missed:

Good—I found multiple SAC (Service Area Competition) listings (93.224) which are the core HRSA community health center funding. Let me check 93.224 award history:

Excellent—93.224 is *the* signature HRSA community health center funding with massive nonprofit uptake (254 awards in FY2021 alone), averaging ~$3.2M. However, **this is for FQHCs, not lookalikes.** Cedar Valley is currently a "lookalike" not yet formally designated. I need to confirm whether lookalikes are eligible. The SAC listing dates are future-dated (07/31/2026), so the org needs to check eligibility with HRSA directly.

Let me also look for any infrastructure or planning grants aimed at pre-FQHC organizations, then check the "Rural Health Network Development Planning Program" (93.912, Planning track) and confirm award history:

The planning track doesn't show in the FY2021 sample, but the regular 93.912 did. Let me now synthesize what I know:

---

## **ANALYSIS SUMMARY:**

Reviewed 40+ opportunities across three search queries. After filtering for a rural, uninsured-focused primary-care FQHC-lookalike in WV, I found:

### **Opportunities Cleared:**

1. **HRSA-27-051 & HRSA-27-048: Rural Health Network Development Program & Planning Program (CFDA 93.912)**
   - **Why it fits:** Direct match for rural health clinic collaboration; 23 nonprofits awarded in FY2021 ($250k avg).
   - **Real award range:** $49.5k–$923k (FY2021 history). Most awards likely $100k–$350k range.
   - **Deadline:** 08/13/2026 (forecasted; no close date yet).
   - **Effort:** Moderate (5–10 hours for network planning/partnership concept). Viable for 15-hour capacity.
   - **Risk:** Requires multi-partner network structure. If Cedar Valley is the *only* applicant (not leading a network), this may not fit. Also, lookalike status—not yet FQHC—should be verified with HRSA to confirm eligibility.
   - **SAM/DUNS:** Yes, will need SAM.gov registration and UEI (org notes this is a gap).

2. **HRSA-27-006, 07, 08, 09: Service Area Competition (SAC) for Health Centers (CFDA 93.224)**
   - **Why it fits:** *The* core HRSA funding stream for community health centers; 254 nonprofits awarded in FY2021.
   - **Real award range:** Avg $3.18M; min $7.7k, max $46.8M. Cedar Valley's $1.45M budget would likely qualify for $200k–$600k depending on service population and unmet need.
   - **Deadline:** 07/31/2026 – 09/01/2026 (forecasted, state-dependent).
   - **Effort:** HIGH (20–40 hours for full SAC application—RFP, budget narrative, clinical protocols, board governance docs, etc.). **Exceeds org's 15-hour capacity unless external consultant hired.**
   - **Risk:** **CRITICAL ELIGIBILITY QUESTION:** SAC typically funds FQHCs, not lookalikes. Cedar Valley *must* confirm with HRSA whether it can apply for SAC in "lookalike" status or if it needs to complete FQHC designation first. If ineligible, this is a dead-end; if eligible, it's the biggest prize but requires consultant support.
   - **SAM/DUNS:** Yes, required.

### **Opportunities NOT Recommended:**

- **HRSA-27-053 (Appalachian Region Healthcare Support)**, **93.690 (Rural Communities Opioid Response)**, **93.692 (Rural Health Value):** No FY2021 nonprofit award history in sample; likely state/local/regional entity-focused or newly piloted. Without proof of nonprofit eligibility, too risky to recommend.
- **CDC/NIH programs (93.945, 93.940, 93.307, 93.279, etc.):** All require research infrastructure, clinical trials, or academic partnerships. Cedar Valley is a service clinic, not a research institution. Misaligned.
- **Title X (93.217), Infertility Training (93.260):** Specialty focus not aligned with primary mission.

---

## **BRIEF RECOMMENDATIONS:**

### **1. Rural Health Network Development Program (HRSA-27-051 & 48)**
**CFDA 93.912 | Opens 08/13/2026**

Cedar Valley should apply **if it can partner with other local health providers** (other clinics, ambulances, mental-health agencies, etc.). This program funds multi-partner networks to improve rural access; a clinic alone may struggle to meet competitive bar.

- **Realistic award:** $150k–$400k over multiple years
- **Effort:** 6–10 grant-writing hours (moderate)
- **Key action:** Identify 2–3 local partners and clarify shared goals (e.g., chronic disease care coordination, referral pathways). Draft simple MOU.
- **Blocker:** Needs UEI/SAM.gov registration; no indirect cost rate yet (org will need to allow rate to be negotiated or use 10% de minimis if under $25M total federal awards).
- **Why it matters:** Clear nonprofit precedent; manageable effort-to-award ratio; aligns with mission.

---

### **2. Health Center Program Service Area Competition (HRSA-27-006 et al.)**
**CFDA 93.224 | Opens 07/31/2026 – 09/01/2026 (state-dependent)**

This is the gold-standard funding for clinics like Cedar Valley, but **ONLY IF the org is FQHC-eligible or FQHC-designated.** The org must contact HRSA's Bureau of Primary Health Care immediately to confirm whether "lookalike" clinics can compete in the SAC. If yes, this is priority #1. If no, skip unless/until FQHC designation is complete.

- **Realistic award:** $300k–$800k annually (depending on uninsured population served; Cedar Valley's ~$1.45M budget suggests mid-range placement)
- **Effort:** 25–40 hours (full proposal, financials, board/governance docs, clinical protocols). **Exceeds internal capacity.** Recommend hiring a freelance grant writer (cost: $2k–$5k) or partner with a grant-writing nonprofit.
- **Why it matters:** Only source of operational funding at this scale; directly supports uninsured primary care.
- **Timeline risk:** SAC opens late July 2026; requires fast turnaround. Org should begin FQHC-eligibility inquiry *now* to use transition time.

---

### **3. — ALTERNATIVE FOR CAPACITY CONSTRAINT —**
If the org cannot afford external grant-writing support for SAC (option 2) and lacks network partners for 93.912, **focus on 93.912 (Network Development) as the higher-probability, internal-capacity option.** It's smaller but achievable with volunteer effort and has real nonprofit precedent.

---

## **IMMEDIATE TO-DO LIST:**

1. **Contact HRSA Bureau of Primary Health Care** (1-888-ASK-HRSA or grants.hrsa.gov) to clarify SAC eligibility for non-designated lookalike clinics. If eligible, SAC becomes priority #1.
2. **Register for SAM.gov UEI** if not done. This is a prerequisite for any federal grant.
3. **Identify potential network partners** (hospital, other clinics, behavioral health) for 93.912 application.
4. **Budget decision:** If SAC is eligible and high-priority, allocate $3k–$5k for external grant-writing support. ROI: $300k+ over years >> cost.

---

## **SUMMARY:**

Reviewed 40+ opportunities. **Surfaced 2 viable fits** (93.912 achievable internally; 93.224 transformational but requires FQHC confirmation + external writing support). Dropped ~35 due to research-focus, specialty scope, or no nonprofit award precedent. The org's main constraint is capacity and FQHC status clarity—both addressable with planning.
