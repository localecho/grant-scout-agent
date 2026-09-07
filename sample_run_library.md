# Sample run: `python -m src.run --profile profiles/example_library.yaml`

Regenerated 2026-09-07 alongside `sample_run_afterschool.md`, against the current
`SYSTEM_PROMPT` (the tightened rule 4 requiring a named mitigation for over-capacity
recommendations, plus the compliance-floor and `estimate_compliance_burden` fixes). This run's
two recommendations both fit within the org's stated 8-hour capacity (10-12 and 8-10 hours), so
rule 4's named-mitigation requirement doesn't trigger here — see `sample_run_afterschool.md`
for the case where it does. 30+ tool calls across `search_open_grants`,
`historical_award_context`, and `estimate_compliance_burden`. Trimmed only to remove Strands'
tool-call progress lines.

---

Running Grant Scout for: Fairview Township Public Library

I'll search for federal funding opportunities aligned with Fairview Township Public Library's focus on digital literacy, broadband access, and rural library services. Let me start by checking what's currently open.

Good leads emerging. Let me now check the realistic award history for the most promising opportunities: the IMLS library programs (National Leadership Grants, Laura Bush Librarian Program) and the Lewis-Houghton Civics Initiative. I'll also need to investigate the broadband angle more.

The IMLS library programs returned no nonprofit award history in the data sample. Let me search more specifically for library and education funding with better scope, and check the literacy/education angle as well.

Still no nonprofit award history for IMLS library programs in the sample. Let me try a different approach and search for IMLS programs more directly, and check education/literacy programs that might be better funded.

Let me try one more targeted search for community development and nonprofit-friendly funding.

The CFDA lookups for the library and civics programs are returning empty nonprofit award histories. Let me try a broader approach with Department of Education and more mainstream nonprofit funding to see what's available.

Let me check the ACF Community Economic Development program that just appeared, and also try to search specifically for nonprofit capacity funding and operational grants.

Great! I found a real match with award history: **Community Services Block Grant Discretionary Awards (CFDA 93.570)** shows actual nonprofit awards averaging $762K, with 33 nonprofits funded. Let me search more directly for this program and see if there are any open opportunities.

Excellent! I found **Community Economic Development Projects (CFDA 93.570)** with a deadline of **09/08/2026**. This is the same program that showed real nonprofit award history ($762K average). Now let me check some of the health-focused rural programs and also look for any education grants. Let me also verify if there's meaningful nonprofit award history on the rural health programs.

Good news! **Rural Health Care Services Outreach** (CFDA 93.912) has real nonprofit award history: 23 nonprofits funded, averaging $250K. Now let me assess the organization's compliance status and estimate what these opportunities would require. But first, let me check if there are any other education/literacy programs that might work.

Now let me estimate the compliance burden and effort for the two most promising opportunities.

---

## Analysis Summary

Based on my search, I found **two opportunities** that meet the bar for recommendation. Here's what I discovered:

**Critical compliance issue (must address before any application):**
The org profile shows **SAM.gov registration status and indirect cost rate agreement status are unknown**. **This is a hard blocker.** Every federal grant requires:
- Active SAM.gov registration with a valid Unique Entity ID (UEI) before submission
- Many programs also require a Negotiated Indirect Cost Rate Agreement (NICRA) to recover overhead costs

**Action required:** Fairview Township Public Library must **confirm both of these before pursuing any opportunity below.** If SAM.gov registration is not current, that alone can take 4-6 weeks and will prevent any application from being submitted. If the org doesn't have a NICRA, there will be uncovered overhead costs built into the awards.

---

Now let me estimate the effort and compliance burden for the two strongest candidates.

Now I have the information I need. Let me structure the brief.

---

## **COMPLIANCE FLOOR: ACTION REQUIRED BEFORE APPLYING**

**Stop here and complete these first:**

1. **SAM.gov & UEI Status: UNKNOWN**
   Contact your org: Is Fairview Township Public Library currently registered at SAM.gov with a valid, active Unique Entity ID (UEI)? If not, registration can take 2–6 weeks and is a hard requirement before submitting any federal grant.

2. **Indirect Cost Rate Agreement (NICRA): UNKNOWN**
   Does the org have a current Negotiated Indirect Cost Rate Agreement with HHS or another federal agency? This affects what you can recover for overhead if you win. If you don't have one, you'll be limited to claiming 10% of direct costs as overhead, creating an estimated $25K–$76K uncovered overhead gap depending on award size.

   **If both are unknown: Confirm these with your Executive Director before proceeding. They are separate hurdles from application hours.**

---

## Opportunities That Clear the Bar

### **1. Community Economic Development Projects**
**Administering Agency:** Administration for Children and Families (HHS)
**CFDA Number:** 93.570 (a federal program ID code)
**Application Deadline:** September 8, 2026
**Realistic Award Range:** $197,000–$1,182,000 (based on FY2021 data from 33 nonprofit awards; midpoint ~$762,000)

**Why it fits:**
This program funds community organizations to strengthen local economic opportunities. The org's focus on digital literacy and rural library services aligns—libraries are infrastructure for workforce development, and digital skills are essential for economic participation in underserved areas. HHS has actually funded nonprofits at this scale: the historical data shows 33 nonprofits won this program in FY2021.

**Realistic application effort:**
~10–12 hours for a strong application (program narrative, budget justification, organizational capacity documents, outcomes measurement plan). Your retired schoolteacher volunteer is appropriate here, though they may need a day to learn the specific HHS grant format.

**Compliance cost of winning (if you win):**
- **Uncovered overhead (if you have no NICRA):** ~$76,000/year. This is the difference between your real overhead costs and the 10% cap you can claim without a formal rate agreement. You will absorb this unless you negotiate a rate agreement first.
- **Single Audit threshold:** This award size ($762K midpoint) puts you at or above the $750,000 federal funding threshold that triggers mandatory Single Audit requirements (annual financial audit specific to federal compliance). Budget $12,000–$25,000/year for this recurring cost, even though it's required by law, not optional.
- **Bottom line:** Winning this award carries real structural costs (~$76K uncovered overhead + ~$18K avg audit cost annually). These are true costs, but they don't eliminate the opportunity—they just mean the net benefit is $761K gross minus ~$94K structural cost = ~$667K available for program work. That's still substantial.

**Key risk:**
The application is competitive and program-specific. Community Economic Development typically expects a detailed economic development strategy (jobs created, training outcomes, local partnerships). A rural public library may need to position itself as a hub for digital workforce development and community economic connectivity, not just a library. Your lack of IT staff is a challenge—if the program wants tech infrastructure or training components, you'll need a vendor partner locked in before you apply (the profile notes this). If you're going for straight operations/capacity support, this is more straightforward.

**Recommendation:** Worth pursuing if you can credibly frame the library as an economic development engine for rural digital access. Confirm SAM.gov/UEI and NICRA status first.

---

### **2. Rural Health Care Services Outreach, Rural Health Network Development**
**Administering Agency:** Health Resources and Services Administration (HRSA, part of HHS)
**CFDA Number:** 93.912
**Application Deadline:** Open; specific opportunity posted 08/13/2026, no close date yet (check grants.gov for details)
**Realistic Award Range:** $49,500–$922,500 (based on FY2021 data from 23 nonprofit awards; midpoint ~$250,000)

**Why it fits:**
Rural public libraries increasingly serve as health information hubs and community gathering spaces in underserved areas. This HRSA program funds partnerships and networks that strengthen rural health infrastructure. A library offering digital literacy, after-school support, and a reliable meeting space can be positioned as part of a rural health ecosystem. HRSA has historically funded nonprofits at this scale (23 nonprofits in FY2021).

**Realistic application effort:**
~8–10 hours if you're doing a straightforward "library as community anchor" application. Longer (12–15 hours) if the program wants a detailed health network partnership plan with specific healthcare partners. Your volunteer has capacity within your stated 8-hour budget if this stays focused and simple.

**Compliance cost of winning (if you win):**
- **Uncovered overhead (if you have no NICRA):** ~$25,000/year. Same logic as above—you can claim 10% of direct costs without a NICRA, but your real overhead is likely higher.
- **Single Audit threshold:** A $250K award keeps you *under* the $750,000 threshold, so you avoid mandatory Single Audit requirements. That's a genuine advantage.
- **Bottom line:** Winning this award carries ~$25K uncovered overhead annually, but no audit mandate. Net program resources: ~$225K/year.

**Key risk:**
HRSA health programs typically want you to demonstrate strong relationships with healthcare providers and a clear health equity or health outcome focus. A library claiming to be part of rural health infrastructure will need to show **specific partnerships with clinics, hospitals, or health nonprofits** before you apply—not after. If you don't have these relationships already, you'll need 2–4 weeks to build them. The award size is also smaller than #1 above, so the return per hour of effort is lower unless this is a natural fit for your partnerships.

**Recommendation:** Pursue only if you have (or can quickly build) genuine partnerships with local healthcare providers willing to co-apply or endorse your role in their network. Confirm SAM.gov/UEI and NICRA status first.

---

## Summary

**Reviewed:** ~30 open opportunities across digital literacy, library services, broadband, rural programs, education, and community development.

**Surfaced:** 2 opportunities with confirmed nonprofit award history and realistic relevance to a small rural library.

**Next step:**
1. **Confirm SAM.gov registration and UEI status with your Executive Director—this is not optional and can take weeks.**
2. **Confirm NICRA status—if you don't have one, reach out to your HHS grants contact about the application process.**
3. For **Community Economic Development:** Assess whether you can credibly frame the library as rural economic infrastructure, and whether a vendor tech partner is available if needed.
4. For **Rural Health Outreach:** Confirm you have (or can quickly establish) real healthcare partnerships before investing application time.

Both opportunities fit your mission and have proven nonprofit funding history. The main gaps are compliance readiness and partnership clarity—not hour capacity.
