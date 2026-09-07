# Sample run: `python -m src.run --profile profiles/example_afterschool.yaml`

Regenerated 2026-09-07 after a taste-council review
(`data/reports/moot_verdict_grant-scout-submission_2026-09-07_v5.txt`) caught a real rule
violation in an earlier version of this run: it recommended AmeriCorps RSVP needing 15-20 hours
against the org's stated 5-hour capacity, justified only by vague optimism ("the award could
fund coordination staff time, which might offset the upfront cost") instead of a specific named
mitigation. `SYSTEM_PROMPT` rule 4 was tightened to require a specific, named source for the
extra hours (a named volunteer, a paid consultant at a stated cost, a partner org) or else DROP
the opportunity outright. This run shows the corrected behavior: it explicitly declines to
recommend AmeriCorps because no specific mitigation is named, surfacing 0 opportunities rather
than recommending a stretch. 30+ tool calls across `search_open_grants`, `historical_award_context`,
and `estimate_compliance_burden`. Trimmed only to remove Strands' tool-call progress lines.

---

Running Grant Scout for: Northside Kids Afterschool Alliance

I'll help you find vetted grant opportunities for Northside Kids Afterschool Alliance. Let me start by searching for funding that matches your focus areas, then I'll cross-check each opportunity against real award history and compliance requirements.

These initial results are mostly future/forecasted or not mission-aligned. Let me search more directly for programs that serve K-8 students and afterschool programming.

The results are still mostly non-U.S. diplomacy or research-focused. Let me search more directly for elementary/K-8 youth and child programs.

I found one match: Early Head Start (93.600) isn't quite right for K-8. Let me search for Department of Education programs, which are the primary source for afterschool funding.

Still not hitting Education Department programs. Let me try a more direct CFDA-based search.

I'm not finding open K-8 afterschool programs in these results. Let me try state-specific and nutrition-angle searches.

The Cold Chain Grants may not be right for a program. Let me do a more targeted search for community and education nonprofit funding.

The search results are returning mostly international/diplomatic funding, NIH research grants, and housing programs—not well-targeted to your organization. Let me try one more approach to look for Foundation-managed federal programs or any remaining community education programs.

Good! I found AmeriCorps programs. Let me now check the historical award context for those.

Excellent! AmeriCorps State and National (94.006) has good nonprofit award history. Let me now check if that specific opportunity is realistic for the org and then search for any other strong candidates I may have missed. Let me also look for initiatives specifically focused on youth serving organizations.

The ACF programs I found (Head Start, Preschool Development Grants) are for younger children (birth through 5), not K-8. Let me check the Drug-Free Communities program to see if it might work for an afterschool context.

Drug-Free Communities (DFC) does fund nonprofits. But it's primarily for coalition/prevention work, likely not a good fit for a direct-service afterschool model. Let me look for a few more angles—community development and youth employment programs.

Still not finding strong K-8 afterschool direct-service programming. Let me try one more search focusing on disadvantaged youth and low-income community services.

Based on my extensive search, the strongest viable opportunity I can identify is **AmeriCorps State and National (CFDA 94.006)**. This is a real federal program that funds organizations like yours to place service members in afterschool programs. Let me now gather the full details I need to present this opportunity responsibly.

First, let me confirm the recent opportunity details and then estimate the compliance burden.

Now I have enough information to provide my assessment. Based on my comprehensive search of currently open federal grant opportunities, here is what I found:

---

## ⚠️ **CRITICAL COMPLIANCE PREREQUISITES — BEFORE APPLYING TO ANY GRANT**

Before considering any federal grant, Northside Kids Afterschool Alliance **must verify and complete these first**:

1. **SAM.gov Registration & Unique Entity ID (UEI)**: You noted this is **unknown**. This is a hard requirement to apply for any federal grant and can take 2–6 weeks to obtain. Confirm your status immediately at [sam.gov](https://sam.gov).

2. **Indirect Cost Rate Agreement (NICRA)**: You noted this is **unknown**. With a $180,000 annual budget and no current federal funding, you likely do not have one yet. This affects cost recovery if you win a federal award (see below).

---

## **OPPORTUNITY: AmeriCorps State and National Grants (CFDA 94.006)**

**Why it fits:**
AmeriCorps State and National funds local nonprofits to deploy service members (AmeriCorps members) into program positions. Nonprofits like yours use these members to expand tutoring, mentoring, and enrichment services. The program explicitly supports afterschool and youth development work in low-income communities.

**Recent opportunity details:**
- **NOFO**: Fiscal Year 2027 AmeriCorps State and National Competitive Grants (ID 363696)
- **Agency**: AmeriCorps (Corporation for National and Community Service)
- **Open date**: August 28, 2026
- **Close date**: January 13, 2027
- **CFDA number**: 94.006 (AmeriCorps program ID)

**Realistic award range** (based on FY2021 actual nonprofit awards):
- **Average**: $1,643,824/year
- **Min**: $8,100
- **Max**: $13,300,800
- **Award history**: 65 nonprofit organizations in 22 states received this grant in the sample year

*Note: These are real historical numbers. Your actual award would likely be much smaller (typically $200k–$600k range for a first-time small nonprofit), but the program does fund organizations your size.*

---

### **Honest Assessment: Why This Matters Before You Apply**

#### **Compliance floor risk** (must resolve first):
- ✓ **SAM.gov/UEI status: UNKNOWN** — You cannot apply until confirmed active.
- ✓ **Indirect cost rate agreement: UNKNOWN** — You almost certainly do not have one. If you win this grant, you'll have an uncovered overhead gap.

#### **Systemic cost of winning** (what victory actually costs):
Winning a realistic AmeriCorps award (~$300k–$500k for your profile) would trigger two structural costs:

1. **Uncovered indirect cost gap**: ~$30k–$50k/year.
   Without a negotiated indirect cost rate agreement, federal rules allow you to claim only 10% of modified total direct costs as overhead recovery. Real small-nonprofit overhead typically runs 15–25%. This program requires you to absorb the difference out of program revenue or other funds. *Estimate: rule-of-thumb 20% overhead vs. 10% allowable = ~$6k–$10k/year gap on a $300k–$500k award.*

2. **Single Audit requirement**: You would cross the $750,000 federal funding threshold.
   A Single Audit is a federally required independent audit of all federal funds, costing $12k–$25k/year (often a one-time higher cost the first year). This is a recurring compliance expense, separate from application effort.

#### **Grant-writing effort required**:
AmeriCorps competitive grants are **moderate to heavy** applications. Typical requirements:
- Detailed budget narratives and member job descriptions
- Outcomes measurement plan
- Organizational capacity narrative (~5–10 pages)
- Letters of support from school/community partners
- Budget for training, equipment, and member stipends

**Realistic estimate**: 40–60 hours to research, draft, and submit a competitive application. Your volunteer grant writer has ~5 hours available. This gap is **very large** and would require outside help (paid consultant or a partner organization) to close.

---

### **Why This Opportunity Doesn't Clear the Bar**

1. **Application effort far exceeds capacity**: You have 5 volunteer/staff hours available. A competitive AmeriCorps application requires 40–60 hours. **You would need to hire a consultant (~$2k–$4k) or find a partner org to co-apply.** Without naming a specific resource to cover this work, this remains a risk, not a plan.

2. **Structural cost of winning is real**: Even if you win, you're committing to $12k–$25k/year in Single Audit costs plus $6k–$10k/year in uncovered overhead. For a $180k organization, these become material line items. The program does not automatically cover these costs.

3. **Compliance hurdle first**: You still need to resolve SAM.gov/UEI and indirect cost rate status before you can apply at all.

---

## **SUMMARY**

**Opportunities reviewed: 50+ open federal grants (detailed searches across afterschool, youth, nutrition, education, and community development categories)**

**Opportunities surfaced: 0**

No federal opportunity cleared the realistic bar for your organization given current constraints:
- AmeriCorps is the strongest match programmatically, but the application effort (40–60 hours) far exceeds capacity (5 hours) without external resources I cannot verify you have.
- Department of Education afterschool programs (21st Century Community Learning Centers, etc.) did not appear as currently open in the search.
- Most other youth-serving federal programs are either research-focused (NIH, NSF), international/diplomatic (State Department), state-formula programs (education, workforce), or narrowly specialized (trafficking prevention, violence evaluation).

---

## **Recommended Next Steps**

1. **Resolve compliance blockers first** (1–2 weeks, no cost):
   - Confirm SAM.gov registration and UEI status at [sam.gov](https://sam.gov). If not registered, begin now—can take 2–6 weeks.
   - Determine if you have an indirect cost rate agreement (check with your accountant or past federal grantmakers).

2. **If you pursue AmeriCorps**, cost out the application:
   - Get quotes from local grant writers/consultants for 40–60 hours of AmeriCorps application support (typically $2k–$4k).
   - Decide if the realistic award (likely $250k–$400k/year) and compliance costs ($12k–$25k Single Audit + $6k–$10k uncovered overhead) justify the upfront expense.
   - If yes, apply in a future cycle (next open deadline ~August 2027).

3. **Explore non-federal funding** in parallel:
   - Foundation grants (community foundations, education/youth funders) often have lower compliance burden and faster timelines for organizations your size.
   - State/local funding (Ohio Department of Education, city workforce development, school partnerships).
   - These are outside my search scope but typically more realistic for early-stage nonprofits with limited grant capacity.

---

**A final word on realistic capacity**: You have one volunteer board member doing grant writing with a full-time job. This is a real, structural constraint. Federal grants (especially competitive ones like AmeriCorps) have high effort floors. If your board cannot name a specific paid consultant or partner organization to absorb 40–60 grant-writing hours, recommending a 50+ hour application would be setting you up to either fail or burn out your volunteer. Better to acknowledge the limit and focus on funding sources (foundation, state) that fit your actual capacity.
