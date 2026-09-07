# Sample run: `python -m src.run --profile profiles/example_library.yaml`

Captured 2026-09-07 against live grants.gov data and the real FY2021 USASpending benchmark
table shipped in `data/`. Not edited for content — trimmed only to remove the tool-call
progress lines Strands streams to stdout (`Tool #1: search_open_grants`, etc.). 16 tool calls
total: 9 `search_open_grants`, 7 `historical_award_context`.

This is the **zero-opportunities case** — the agent's cross-check found no verifiable nonprofit
award history for any of the programs that fit this org's mission, and it refused to guess.

---

Running Grant Scout for: Fairview Township Public Library

I'll search for open federal opportunities that match this rural public library's mission and constraints, then vet each candidate against real nonprofit award history.

Good starting set. The most promising candidates for this rural public library are:
1. **National Leadership Grants for Libraries (CFDA 45.312)** – IMLS, general library tech/literacy
2. **Lewis-Houghton Civics and Democracy Initiative (CFDA 42.015)** – Library of Congress, civics/literacy
3. **Tribal Broadband Connectivity Program (CFDA 11.029)** – may not be eligible, but worth checking

Let me vet these against real nonprofit award history:

No FY2021 nonprofit award history in the sample for any of these three. That's a red flag, but doesn't automatically disqualify them — IMLS programs and Library of Congress grants are legitimate library funding sources. Let me try broader searches to see if there's any nonprofit award history under these agency programs:

The historical award database isn't returning matches for these programs in the FY2021 sample. Let me try a few more targeted searches to find programs with actual proven nonprofit award history in rural/library contexts:

Good — I see a couple of new IMLS programs (Native American Library Services) and the PART Energy Program (USDA rural broadband). Let me check those for historical nonprofit awards:

The FY2021 USASpending historical data isn't returning nonprofit awards for library-specific programs. This is likely because the sample data is limited or these programs didn't award in FY2021 with nonprofit recipients. However, I know from grant writing practice that IMLS programs (especially National Leadership Grants and Native American Library Services grants) are standard library funding sources that DO award to public library nonprofits — just not necessarily captured in this historical sample.

Let me try one more broad search to see if there are any other opportunities I'm missing, and then I'll make my recommendations based on what I know about these legitimate library programs:

## Summary & Recommendation

I reviewed **15 unique opportunities** across multiple searches. Here's what I found:

**The hard truth:** The FY2021 USASpending historical data has no nonprofit award records for the library-focused programs that would be the most natural fit for Fairview Township Public Library (IMLS grants, Library of Congress programs, broadband access programs). This creates a verification gap.

**However, I cannot recommend any opportunities I cannot ground in historical evidence.** The board needs to know what's realistic before committing 8 volunteer hours.

### Why Nothing Survives the Vetting:

1. **National Leadership Grants for Libraries (CFDA 45.312)** – Open 9/1/26, close 11/13/26. This is legitimately designed for exactly this org's mission. *But:* No FY2021 nonprofit award data in the system. Without historical context on award size, frequency, or competitiveness, I cannot estimate realistic odds or award range. The program website would need manual review.

2. **Lewis-Houghton Civics and Democracy Initiative (CFDA 42.015)** – Library of Congress, open 8/7/26, close 9/18/26. Good fit for digital literacy/education. *But:* Same issue — no historical nonprofit awards in the sample.

3. **Tribal Broadband Connectivity Program (CFDA 11.029)** – Likely tribal-only eligibility; Fairview Township is not a tribal entity. **Dropped.**

4. All other USDA rural grants (PART Energy, etc.) are infrastructure/utility-focused, not library services.

### Bottom Line

**0 opportunities recommended.** The grants that fit this library's mission (IMLS, Library of Congress) lack verifiable FY2021 nonprofit award history in the available data, and I won't recommend spending 8 hours on a blind shot.

**Next step:** Your board should:
- Contact **IMLS directly** (imls@imls.gov) to ask past award sizes and nonprofit success rates for National Leadership Grants libraries in rural KY.
- Check the **Library of Congress grants website** directly for Lewis-Houghton eligibility and past awards.
- Once you have that context, these could be worth pursuing — but verify before writing.
