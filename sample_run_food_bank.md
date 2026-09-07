# Sample run: `python -m src.run --profile profiles/example_food_bank.yaml`

Regenerated 2026-09-07 against the current `SYSTEM_PROMPT`. Two earlier regenerations of this
exact profile stalled mid-run asking the operator a clarifying question about compliance status
instead of producing a brief — a real bug for a single-shot CLI tool with no back-and-forth.
Fixed with an explicit instruction never to stop and ask, since there's no one to answer. This
run also shows the strengthened rule 4 (Vu Le / Hamel Husain's catch, in
`data/reports/moot_verdict_grant-scout-submission_2026-09-07_v5.txt`) working: rather than
recommending AmeriCorps on vague optimism, the brief says plainly to bring in "a paid consultant
or skilled volunteer" if the real hour count exceeds capacity, or "pass on this cycle." 19 tool
calls: 12 `search_open_grants`, 6 `historical_award_context`, 1 `estimate_compliance_burden`.
Trimmed only to remove Strands' tool-call progress lines.

---

Running Grant Scout for: Riverside Community Food Pantry

I'll search for current funding opportunities for Riverside Community Food Pantry, focusing on food assistance and food security programs they might qualify for.

Good starting point. I found one clear match: "Cold Chain Grants for Emergency Food Assistance" (CFDA 10.197). Let me also check the two HRSA nutrition programs that appeared. Now I'll check the historical award data for these candidates.

The Cold Chain Grants show no nonprofit award history in FY2021 data. The CFDA 93.224 (Health Center Program) is aimed at health centers, not food banks, based on the title. CFDA 93.129 shows some history but the title says "Technical and Non-Financial Assistance to Health Centers" — also not a fit for a food bank.

Let me do a more targeted search for food pantry and food bank specific programs, and also check USDA nutrition and emergency assistance programs more directly. I'm seeing mostly research, health center, and training programs. Let me search more specifically for grants that go directly to nonprofits for food distribution and community services.

Good! I found AmeriCorps Seniors RSVP and the Diaper Distribution program. Let me check the historical award data for these, as well as search for any other direct-to-nonprofit food or community assistance programs.

Excellent! AmeriCorps Seniors RSVP has strong nonprofit award history. The Diaper Distribution program has no historical award data, so I'll note that as a gap. Let me do one more targeted search for food-focused grants that nonprofits might access. The food-related searches are returning mostly research, education, and agriculture training programs. Let me check the AmeriCorps State and National program that appeared earlier and do one more check on whether there are specific emergency food programs at the federal level that go to nonprofits.

Based on my comprehensive search, I've found very limited federal grant opportunities that are a good fit for a small community food bank. The major federal food assistance programs (SNAP, WIC, USDA direct meal programs) are typically administered through states and don't accept individual nonprofit applications.

The best candidates are:

1. **AmeriCorps Seniors RSVP** (94.002) — proven nonprofit track record
2. **AmeriCorps State and National** (94.006) — also proven nonprofit track record but likely requires more complex application
3. **Cold Chain Grants for Emergency Food Assistance** (10.197) — promising title but no nonprofit award history found

Let me assess the workload and feasibility for each:

**AmeriCorps Seniors RSVP**: The search showed it's open (AC-08-20-2026, closes 10/20/2026) with strong nonprofit history (698 awards, avg ~$65K). This would require a grant application, but it's feasible for a small food bank with 6 volunteer hours if the app is straightforward. Let me check the compliance burden.

**AmeriCorps State and National**: Much larger awards (avg $1.6M) but would likely require a more complex application - probably too much lift for ~6 hours.

Let me now do the compliance burden analysis for the most promising candidate. Good information. Now let me verify one more time by searching specifically for any other low-lift grant opportunities targeted at food banks or small nonprofits in Ohio or nationally. These results are mostly international affairs, defense, research, or housing programs—not relevant to food banks.

Based on my comprehensive search and vetting, I have only **one** opportunity that clears the bar for Riverside Community Food Pantry. Here is my brief:

---

## AmeriCorps Seniors RSVP Competition (FY 2027)

**Opportunity Match:**
This program directly funds nonprofits to recruit, place, and support senior volunteers in community service roles. A food bank can use RSVP volunteers for food sorting, distribution coordination, delivery, and client outreach—core operations that align with your mission and could extend your staff capacity without payroll expense.

**Award Range (FY2021 Historical Data):**
$5,000 to $736,000 per award; average $64,940. Realistic midpoint for a small food bank startup or small-to-mid sized program: **$45,000–$70,000**.

**Deadline:**
Applications close **October 20, 2026** (opens August 20, 2026). ~7 weeks to apply—feasible given your 6-hour volunteer writing capacity if the NOFO (Notice of Funding Opportunity) asks for a straightforward application rather than a 40-page proposal.

**Compliance Floor — Required Before You Apply:**
- **SAM.gov registration & Unique Entity ID (UEI):** Status unknown per your profile. This is a **hard blocker**—you cannot apply until this is active. If you don't have it, apply now at sam.gov; processing can take 2–4 weeks. Confirm status with your board immediately.
- **Indirect cost rate agreement (NICRA):** Status unknown. You do not need one to apply, but if you win, you may want one to simplify accounting. Many small nonprofits operate under the 10% de minimis rate (a simplified default).

**Structural Cost of Winning (Rule-of-Thumb Estimate):**
Assuming a $65,000 award and no negotiated indirect cost rate agreement: your organization would likely carry **~$6,500/year in uncovered overhead** (the difference between the 20% real overhead rate most nonprofits absorb and the 10% de minimis simplified rate you can claim). This is not a deal-breaker—it's normal for federal grants—but it's real money that offsets part of the grant. You would **not** cross the $750,000 Single Audit threshold with a $65K award.

**Why This Fits:**
- Proven track record: 698 nonprofits won RSVP awards in FY2021 across 47 states. Community-based organizations like yours are exactly who this program targets.
- Light application lift compared to most federal grants (relative to a 40-page RFP).
- Directly addresses your capacity constraint: senior volunteers extend your food distribution and outreach without new staff payroll.
- Geographic spread is broad; Ohio nonprofits won awards in this program.

**One Honest Risk:**
The application workload and complexity will become clear only when you download the full NOFO on grants.gov. Some RSVP applications are relatively light; others require detailed logic models, sustainability plans, and volunteer recruitment strategies. If the NOFO reveals a 15–20+ page application with heavy program design sections, this will likely exceed your 6-hour capacity unless you can bring in a paid consultant or skilled volunteer who specializes in grant writing. Before deciding to pursue this, download the NOFO, read the application instructions, and estimate hours. If it's >6 hours and you don't have a specific resource to cover those extra hours, pass on this cycle and revisit when you can build more capacity.

---

**Summary:** Reviewed 75+ current federal grant opportunities across food assistance, nutrition, community services, and small grants; surfaced **1 recommendation**.
