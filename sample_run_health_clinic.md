# Sample run: `python -m src.run --profile profiles/example_health_clinic.yaml`

Regenerated 2026-09-07 after adding `estimate_compliance_burden` — a new tool that quantifies
the structural post-award cost of winning (uncovered overhead under 2 CFR 200.414's 10% de
minimis indirect cost rate, and the 2 CFR 200 Subpart F Single Audit threshold) — in response
to Vu Le's critique across two independent taste-council passes
(`data/reports/moot_verdict_grant-scout-submission_2026-09-07_v1.txt` and `_v4.txt`): a
search-and-vet tool that stops at "can you win it" launders a real systemic cost into
invisibility. This replaces an earlier version made before that tool existed (and one
mid-transition run that hit a real `MaxTokensReachedException` — see `src/agent.py`'s
`max_tokens` comment — from adding a third tool's output to the same token budget). 14 tool
calls: 3 `search_open_grants`, 8 `historical_award_context`, 3 `estimate_compliance_burden`.
Trimmed only to remove Strands' tool-call progress lines.

---

Running Grant Scout for: Cedar Valley Community Health Clinic

I'll search for federal funding opportunities matched to Cedar Valley's mission, then vet each one for real eligibility and workload fit.

Good match. Now let me check historical award context for the most promising candidates for a small rural health clinic like Cedar Valley. I'll focus on HRSA programs (which typically support health centers) and CDC programs aimed at health systems or nonprofits, avoiding NIH research centers and academic-heavy grants.

Solid leads. Now let me check a few more HRSA programs and a CDC program that looked relevant:

Excellent. I now have three programs with real FY2021 nonprofit award history. Before recommending them, I need to alert Cedar Valley to a **critical blocker**: they do not have a SAM.gov registration and Unique Entity ID (UEI). This is a hard prerequisite for all federal grants—applications cannot be submitted without it. Now let me estimate compliance costs for the most promising opportunities using realistic historical award amounts:

Now I have enough data to write the briefs. Let me surface the three opportunities with real nonprofit award history and feasible compliance burden for Cedar Valley's small clinic.

---

## **CRITICAL COMPLIANCE FLOOR: SAM.gov Registration Required**

**Before pursuing any federal grant, Cedar Valley must:**
1. **Obtain a Unique Entity ID (UEI)** from SAM.gov and complete full registration. This is a hard prerequisite—no application can be submitted without it. Registration can take 2–4 weeks.
2. **Obtain a negotiated indirect cost rate agreement (NICRA).** Currently, Cedar Valley has no NICRA and cannot claim more than 10% of modified total direct costs as overhead. Every award won will incur an estimated **uncovered overhead cost** (the gap between real overhead and what federal rules allow the clinic to claim). This is a real dollar consequence, not a procedural inconvenience—see estimates below.

Both must be completed before submitting any application.

---

## **1. Rural Health Network Development Program (CFDA 93.912)**

**Why it fits:**
This HRSA program directly supports small health care providers, including look-alike FQHCs, to build networks and improve quality. Cedar Valley's rural West Virginia location and underinsured patient population align exactly with the program's intent.

**Realistic award range:**
FY2021 nonprofit awardees received **$49,500–$922,000** (average $250,000). Cedar Valley should budget planning for a mid-range award of approximately **$200,000–$300,000**.

**Deadline:**
Open 08/13/2026 (no posted close date; typically HRSA programs stay open 60–90 days).

**Compliance requirements:**
- ✓ SAM.gov UEI: **Required** (hard blocker—see above).
- ✓ Indirect cost rate agreement: Not mandatory, but Cedar Valley will absorb an estimated **~$25,000 in uncovered overhead** per year if it wins a $250K award and remains on the 10% de minimis rate without a NICRA.

**Estimated post-award structural cost:**
~$25,000/year in uncovered overhead (the difference between 20% real overhead and the 10% rate allowed without a NICRA). Cedar Valley stays under the $750K Single Audit threshold even if it wins, so no external audit burden.

**One honest risk:**
This is a planning/network-building grant, not operational funding for direct patient care. Cedar Valley will need to frame the proposal around building regional partnerships (e.g., connecting with other rural providers, data sharing, quality improvement consortiums) rather than requesting funds to expand its own clinic operations. If the clinic's main gap is operational funding, this may not solve it.

---

## **2. Technical and Non-Financial Assistance to Health Centers (CFDA 93.129)**

**Why it fits:**
HRSA's health center technical assistance program supports capacity-building for FQHC look-alikes and designated FQHCs. Cedar Valley is explicitly eligible. This program funds training, quality improvement infrastructure, health IT, and workforce development—all leverage for a small clinic to professionalize its operations.

**Realistic award range:**
FY2021 nonprofit awardees received **$137,500–$4,896,000** (average $718,000). The wide range reflects varying project scope. Cedar Valley should anticipate **$300,000–$800,000** for a focused project (e.g., EHR implementation, care coordination training, slide-scale payment system enhancement).

**Deadline:**
Open 08/03/2026 (no posted close date).

**Compliance requirements:**
- ✓ SAM.gov UEI: **Required** (hard blocker—see above).
- ✓ Indirect cost rate agreement: Not mandatory, but Cedar Valley will absorb an estimated **~$72,000 in uncovered overhead** per year if it wins a mid-range $718K award.

**Estimated post-award structural cost:**
~$72,000/year in uncovered overhead. Cedar Valley *just barely stays under* the $750K Single Audit threshold at the high end of the range; if it wins a $750K+ award, it will trigger mandatory annual independent audits (added cost ~$8,000–$15,000/year depending on scope). This is manageable but worth flagging now.

**One honest risk:**
The high end of the historical award range ($4.9M) typically goes to large networks or regional consortiums, not standalone clinics. Cedar Valley should aim for a focused, well-scoped project (single high-impact initiative) rather than broad capacity-building, and research prior successful proposals in its size class to set realistic expectations. Application competitiveness will depend on clarity of project design and track record of execution—a clinic with limited prior grant history may score lower than an established health center network.

---

## **3. Assistance Programs for Chronic Disease Prevention and Control (CFDA 93.945)**

**Why it fits:**
CDC's chronic disease prevention program funds implementation and evaluation of clinical interventions in health systems. Cedar Valley's chronic disease management mission (see profile: "chronic-disease management") aligns with this. The program prioritizes rural and underserved populations, which Cedar Valley serves.

**Realistic award range:**
FY2021 nonprofit awardees received **$54,000–$1,460,000** (average $336,000). Cedar Valley should plan for **$200,000–$500,000** for a discrete disease-focus project (e.g., diabetes management pathway, hypertension screening, asthma action planning).

**Deadline:**
Open 07/28/2026 (no posted close date; typically 60–90 days).

**Compliance requirements:**
- ✓ SAM.gov UEI: **Required** (hard blocker—see above).
- ✓ Indirect cost rate agreement: Not mandatory. Cedar Valley will absorb an estimated **~$34,000 in uncovered overhead** per year if it wins a mid-range $336K award.

**Estimated post-award structural cost:**
~$34,000/year in uncovered overhead. Cedar Valley stays well under the $750K Single Audit threshold, so no audit requirement triggered.

**One honest risk:**
This is primarily an evaluation/research program. The CDC typically funds projects that generate proof-of-concept data, publish findings, and are designed to be scaled or disseminated—not primarily to support clinic operations. Cedar Valley's application will succeed only if it frames the project as an intervention pilot *with built-in measurement and evaluation* (e.g., "we will screen 200 uninsured patients for hypertension, implement a cost-free home monitoring protocol, and measure adherence and outcomes quarterly"). Pure operational funding requests typically score poorly in this program.

---

## Summary

**3 opportunities reviewed; 3 recommended.**
All three have documented FY2021 nonprofit award history and realistic payoff for Cedar Valley's profile. **However, the clinic cannot submit any application until it completes SAM.gov UEI registration.** Once registered, Cedar Valley should prioritize 93.912 (Rural Health Network Development) as the lowest-lift entry point (~15 hours, $200K–$300K), then pursue 93.129 (Technical Assistance) if it has a concrete 1–2 year capacity-building project in mind (moderate lift, $300K–$800K). CDC 93.945 (Chronic Disease) is viable but requires framing as a research/evaluation project, not operations—recommend only if Cedar Valley has staff capacity to design and monitor a rigorous pilot.
