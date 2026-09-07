# Sample run: `python -m src.run --profile profiles/example_afterschool.yaml`

Regenerated 2026-09-07 against the current `SYSTEM_PROMPT` (compliance floor + groundedness +
plain-language + `estimate_compliance_burden`). This replaces an earlier run made before those
fixes existed — kept only the current version so the repo doesn't carry stale evidence. 39 tool
calls: 21 `search_open_grants`, 12 `historical_award_context`, 3 `estimate_compliance_burden`.
Trimmed only to remove Strands' tool-call progress lines. The longest and most exploratory of
the four runs, since "afterschool program" has no single clean federal CFDA match.

This run shows `estimate_compliance_burden` doing real work in the drop decision twice over:
both AmeriCorps State & National and the Community Services Block Grant have strong nonprofit
award history, but both get dropped once the compliance-burden check shows the award size would
force a Single Audit and administrative burden this two-person org can't absorb — the same
pattern shown for the library profile, on a completely different set of programs.

---

Running Grant Scout for: Northside Kids Afterschool Alliance

I'll search for federal funding opportunities that match Northside Kids Afterschool Alliance's mission and capacity, then vet each one against actual award history and compliance requirements.

Let me start by searching for opportunities in their focus areas:

Most of these results are research-focused, tribal/state-level, or unrelated to afterschool programs. Let me search more specifically for programs that fund K-8 youth services and afterschool activities, then try more direct searches for programs that support community organizations running youth/afterschool services.

These results are still not closely matching. I see the Cold Chain Grants program which might be tangentially relevant. Let me try a more focused search on Department of Education programs and USDA nutrition programs, and check for any USDA child nutrition or senior nutrition specific programs.

The Cold Chain Grants program appears in multiple searches. Let me check its historical award data, and also search directly for programs supporting community nonprofits with youth/education missions. I found one promising lead: Community Economic Development Projects (CFDA 93.570). Let me check its historical record and look for more youth/tutoring focused programs.

Good! Community Economic Development Projects shows nonprofit award history. Let me continue searching for more youth-focused and education programs, particularly looking for Title I programs and other ED-funded initiatives. Excellent! I found AmeriCorps State and National Grants (94.006). Let me check its historical award data along with a few more specific searches.

Good! AmeriCorps shows solid nonprofit award history. Now let me estimate the compliance burden for the two most promising opportunities (Community Economic Development Projects and AmeriCorps), and also look for any smaller, more accessible opportunities.

Now let me check the AmeriCorps compliance estimate and search for any additional opportunities specifically for K-8 afterschool programs. Let me do one more targeted search specifically for foundation/federal programs serving urban low-income youth and schools, and also check the Lewis-Houghton Civics program.

I see Head Start and Early Head Start programs mentioned. These are for younger children (under 5), not K-8. Let me check the Drug-Free Communities program since it appeared twice and could potentially work for youth prevention programming.

Excellent! Drug-Free Communities shows solid nonprofit award history with smaller grants (~$102K average). Now let me estimate compliance for that program and check if there are any other accessible programs.

Based on my thorough search, I have found three opportunities that show clear nonprofit award history, realistic award sizes, and reasonable application loads for this organization. Let me now compile my final brief.

---

## Summary

I searched 50+ federal grant opportunities across the org's focus areas (afterschool programming, youth tutoring, out-of-school time enrichment, and child nutrition). Most were either research-focused, tribal/state-level, or university-focused and returned no nonprofit award history.

**I am recommending ONE opportunity**, which is the only one that clearly fits Northside Kids' profile on both mission and capacity grounds. The other two candidates that showed nonprofit award history are problematic for different reasons (see below).

---

## Recommended Opportunity

### **Drug-Free Communities Support Program Grants (CFDA 93.276)**

**Why it fits:**
This CDC/HHS program funds community coalitions to prevent youth substance abuse through local partnerships and programming. While Northside Kids would need to position the grant around a youth prevention angle (beyond tutoring), the program explicitly funds nonprofits running youth programs in low-income neighborhoods, and Ohio is well-represented in historical awards. The award scale is **realistic for a small org**: FY2021 data shows 781 nonprofits won an average of **$102,151** (range: $0–$365,819).

**Realistic award range:**
$80,000–$150,000 based on historical data (midpoint: ~$102K).

**Deadline:**
Open date 07/28/2026; close date not listed in the current posting, typically 60–90 days from open.

**Compliance floor (must confirm before applying):**
- **SAM.gov registration & UEI: *Status unknown* — this is a hard blocker.** The org profile says "unknown." This must be confirmed and obtained if missing; registration can take 2–4 weeks and is required before submission.
- **Indirect cost rate agreement: *Status unknown* — treat as missing.** If the org wins this award without a negotiated rate (NICRA), it can only claim 10% of modified total direct costs as overhead, but real overhead is typically 15–20%.

**Estimated post-award structural cost (if the org has no NICRA):**
~$10,200 uncovered overhead annually (the gap between the 10% de minimis cap and real ~20% overhead). **Does not trigger Single Audit threshold** ($102K total federal funding stays below $750K).

**Key risk:**
This program is designed around **drug-free community coalitions**, not general afterschool enrichment. Northside Kids would need to reframe its tutoring and meals work as part of a youth substance-abuse prevention strategy—which is achievable but requires a conceptual fit beyond the org's stated core mission. If the org is willing and able to make that case, the award size and compliance load are both very manageable.

---

## Why the other two candidates were dropped:

**1. AmeriCorps State & National Grants (CFDA 94.006)**
✓ 65 nonprofits won in FY2021; average award **$1.64M** (range: $8,100–$13.3M).
✗ **Award size is too large for this org's capacity**: A $1.6M+ annual award would dramatically exceed Northside Kids' current $180K budget and would require substantial administrative infrastructure, partnership management, and compliance overhead. Winning this grant would likely force a major organizational restructuring and would create significant Single Audit compliance costs ($12K–$25K+ annually, as a new threshold trigger). The 5-hour volunteer grant-writing capacity is nowhere near sufficient to manage a proposal of this scale. **Not recommended unless the org has a clear path to scale up its operations.**

**2. Community Services Block Grant Discretionary Awards (CFDA 93.570)**
✓ 33 nonprofits won in FY2021; average award **$761,540** (range: $197K–$1.18M).
✗ **Same issue**: Awards at this scale would trigger the Single Audit threshold ($750K) and create $12K–$25K annual compliance costs. While smaller than AmeriCorps, still a structural mismatch for an org running on 2 staff, a $180K budget, and 5 volunteer grant-writing hours.

---

**Final count: Reviewed 50+ opportunities; 1 strongly recommended; 2 promising but structurally misaligned with org capacity.**

**Next step for the board:**
Confirm SAM.gov/UEI status immediately (this is a blocker). If confirmed, evaluate whether reframing the program around youth substance-abuse prevention (in addition to academic support and meals) is authentic to the mission or a stretch. If the fit feels real, the Drug-Free Communities grant is a realistic opportunity at the right scale.
