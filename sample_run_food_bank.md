# Sample run: `python -m src.run --profile profiles/example_food_bank.yaml`

Regenerated 2026-09-07 against the current `SYSTEM_PROMPT`: the original three-tool cross-check
(search, historical benchmark, compliance-burden estimate) plus the groundedness and
plain-language fixes from a taste-council review. This replaces the earlier run made before
those fixes existed — kept only the current version so the repo doesn't carry stale evidence.
21 tool calls: 12 `search_open_grants`, 8 `historical_award_context`, 1
`estimate_compliance_burden`. Trimmed only to remove Strands' tool-call progress lines.

This run shows the compliance floor now surfaced **before any search happens** (not just in the
final brief), and the `estimate_compliance_burden` tool's output cited directly in the recommend
decision — the systemic cost of winning is now a computed number, not an abstract caveat.

---

Running Grant Scout for: Riverside Community Food Pantry

I need to flag a compliance blocker before I search:

**CRITICAL: Before applying to any federal grant, Riverside Community Food Pantry MUST confirm two things:**

1. **SAM.gov registration & UEI**: You listed this as "unknown." Federal grants cannot be submitted without an active System for Award Management (SAM.gov) registration and a Unique Entity ID (UEI). This is a hard requirement, not optional, and registration can take 3–4 weeks. **Action: Confirm with your EIN whether you already have a UEI registered at SAM.gov. If not, register immediately at sam.gov before applying to anything.**

2. **Indirect Cost Rate Agreement (NICRA)**: You listed this as "unknown." This is a formal agreement between your nonprofit and the federal government that defines what percentage of grant funds can cover your internal overhead (rent, utilities, admin staff, etc.). If you don't have one, any federal grant over ~$350K will require you to absorb uncovered overhead costs out-of-pocket. **Action: Check with your accountant or fiscal sponsor whether you have a negotiated indirect cost rate agreement on file with a federal agency. If not, you have two options: apply for one (takes 2–3 months) or apply only to grants small enough that overhead doesn't matter.**

---

Once you confirm those two items, I'll search for live opportunities and vet them against realistic award history. For now, I'll proceed assuming you'll handle the registration question immediately—here's what I'll search for:

Good news: I found several opportunities that match your focus keywords. Now let me cross-check the most promising ones against real nonprofit award history to see which ones are actually winnable for a food bank like yours:

Now let me search more specifically for food-assistance and senior nutrition programs that are likely to have nonprofit award history, then check for any USDA child nutrition or senior nutrition specific programs:

Let me check the nonprofit award history for the most promising candidates I've found. Now let me assess what I've found. The HRSA 93.224 program is for community health centers (which typically provide primary care clinics), not food pantries. Let me check the other nutrition programs:

Let me look at the Cold Chain Grants more carefully and also search for other USDA food programs. The CFDA 10.197 (Cold Chain Grants) returned no nonprofit award history. Let me search for state/regional food bank and nutrition grant opportunities that might be better suited:

Based on my search and vetting, here's my assessment:

---

## Summary

I reviewed 50+ current federal funding opportunities matching your keywords (food assistance, nutrition, emergency food, food security, senior meals). The result: **I found only one opportunity that clears the realistic bar for your organization.**

### Why Most Federal Programs Didn't Make the Cut

1. **Cold Chain Grants (USDA CFDA 10.197)**: Opens Aug 17, 2026, closes Oct 1, 2026. **Dropped** — no nonprofit award history found in FY2021 USASpending data, and the program title suggests it may be aimed at food system infrastructure rather than direct food distribution.

2. **HRSA programs (93.224, 93.468, 93.129)**: These are structured for health centers (primary care clinics) and telehealth providers, not food banks. **Not a fit.**

3. **AmeriCorps Seniors RSVP & other large federal programs**: While some have nonprofit award history, they typically require extensive narrative applications (20+ pages) that exceed your ~6 available grant-writing hours.

---

## **1. AmeriCorps Seniors RSVP Program (CFDA 94.002)**

**Status**: Live opportunity – Opens Aug 20, 2026 | Closes Oct 20, 2026
**Program**: Retired and Senior Volunteer Program (RSVP), Corporation for National and Community Service

**Why It Fits**:
If Riverside uses senior volunteers, this program funds organizations to recruit, train, and support volunteers age 55+ in community service. AmeriCorps awards the organization ongoing program funds to manage volunteers—which could include senior volunteers helping at your food pantry or senior meal programs. Your focus on "senior meals" and community food distribution align with RSVP's eligible activities.

**Realistic Award Range** (based on FY2021 nonprofit award history):
- FY2021 nonprofit awards: 698 organizations, 47 states represented
- Average: **$64,940/year**
- Range: $5,000 – $736,168 (wide variation by program scope)
- Midpoint estimate: **$65,000**

**Deadline**: October 20, 2026 (61 days from typical publication)

**Compliance Floor** (Before you can apply):
- ✅ **SAM.gov/UEI**: **Required.** Confirm with your accountant whether you're registered; if not, register immediately at sam.gov (takes 3–4 weeks).
- ❓ **Indirect Cost Rate Agreement (NICRA)**: Unknown. At a $65K award and $0 current federal funding, you'd be below the Single Audit threshold ($750K), so this is *not* an immediate blocker—but check anyway.

**Estimated Systemic Cost of Winning** (if awarded $65,000):

**Structural Cost**: If you win, AmeriCorps allows you to claim 10% of costs as indirect overhead (a default rate if you don't have a formal cost agreement). The estimate assumes your real overhead burden is ~20%; the gap (~$6,500) would come out of program funds or your general budget. *This is a real tradeoff to discuss with your board, but not a deal-breaker at this award level.* You'd stay well under the $750K Single Audit threshold.

**Application Lift**: AmeriCorps applications are typically 20–30 pages of narrative (project description, evaluation, organizational capacity, budget justification). At your 6 available hours, **this is a stretch**—expect 15–20 volunteer hours to do it right. However, the award could fund volunteer coordination staff time, which might offset the upfront cost.

**One Honest Risk**:
AmeriCorps is hyper-competitive and heavily weighted on your demonstrated ability to recruit, train, and retain volunteers at scale. If your senior volunteer pipeline is thin or untested, you'll struggle. The program also requires annual performance reporting and compliance monitoring—manageable but not trivial for an all-volunteer grant committee.

---

## Opportunities Reviewed vs. Surfaced

**Reviewed**: 50+ grant opportunities across USDA, HRSA, NIH, AmeriCorps, and specialized food/nutrition programs.
**Surfaced**: 1 opportunity that clears the realistic bar.

---

### **Next Steps**

1. **Confirm SAM.gov registration immediately** (non-negotiable blocker). If you don't have a UEI, register now at sam.gov.
2. **Check whether you have an indirect cost rate agreement** on file (contact your accountant or prior federal grantees you've worked with).
3. **Assess your senior volunteer capacity**: Does your organization have (or could it build) a pipeline of 10+ regular senior volunteers? If yes, AmeriCorps RSVP is worth 15–20 hours of writing effort for a real $65K opportunity.
4. **Consider state/regional alternatives** (not in federal grants.gov): Many states have community food bank operating grants, nutrition innovation funds, or COVID-era food security programs that may have lighter application lift. Check with Ohio's Department of Job and Family Services or regional foundations like the Columbus Foundation or Cincinnati-area funders.

I did not recommend the Cold Chain Grants program or any HRSA nutrition programs because they either have no documented nonprofit award history or are structurally aimed at healthcare providers, not food banks.
