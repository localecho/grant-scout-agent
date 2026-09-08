# Sample run: `python -m src.run --profile profiles/example_food_bank.yaml`

Regenerated 2026-09-07 after adding `src/tools/compliance_guide.py` — a fourth tool built in
response to Vu Le's sharpest critique, recurring across three independent taste-council passes
(v1, v4, v5): naming a compliance blocker (SAM.gov, an indirect cost rate agreement) isn't the
same as helping an org clear it. This tool returns the real, stable, publicly-documented
step-by-step federal process for both — not per-program data, but stable procedure safe to state
as fact. This run shows it actually firing and its real output landing verbatim in the brief
(the org gets real SAM.gov steps: EIN, Login.gov, sam.gov registration fields, EFT banking info,
1-2 week validation timeline — not just "you need SAM.gov registration"). 16 tool calls: 8
`search_open_grants`, 4 `historical_award_context`, 2 `estimate_compliance_burden`, 2
`compliance_guide`. Trimmed only to remove Strands' tool-call progress lines.

---

Running Grant Scout for: Riverside Community Food Pantry

I'll search for current federal funding opportunities matching Riverside Community Food Pantry's focus areas, then vet each against their capacity and eligibility constraints.

Good start. I've identified a few promising matches. Let me now check the award history for the most relevant opportunities:

1. **Cold Chain Grants for Emergency Food Assistance** (CFDA 10.197) – directly matches emergency food mission
2. **Fiscal Year 2027 Expanding Nutrition Services** (CFDA 93.224) – matches nutrition focus
3. **AmeriCorps Seniors RSVP** (CFDA 94.002) – could support senior meals programming

Let me verify that nonprofits actually win these programs and at what dollar amounts:

Important findings:

1. **Cold Chain Grants (10.197)**: No nonprofit award history found in the FY2021 data – this signals it may be focused on state/local government or commercial food processors, not community nonprofits. I should verify this before recommending.

2. **Expanding Nutrition Services (93.224)**: Strong nonprofit history (254 awards). However, this is the **Health Center Program** – designed for federally qualified health centers (FQHCs), migrant health centers, and homeless primary care. The award range ($7.7K–$46.8M avg $3.2M) and program structure suggest it's not designed for food pantries.

3. **AmeriCorps Seniors RSVP (94.002)**: Excellent nonprofit history (698 awards across 47 states). Award range: $5K–$736K, average $64.9K. This could work – it's a volunteer program that commonly funds meals-related programs for seniors.

Let me verify the AmeriCorps RSVP opportunity more closely and check the compliance burden. Now I need to address a critical compliance issue: **the org's SAM.gov registration and indirect cost rate status are unknown.** Per my instructions, I must call the compliance guide and provide the org with step-by-step processes to clear these blockers before they can realistically apply to anything.

Now let me search more broadly for programs specifically designed for food banks and community food assistance nonprofits with lighter application lift. The searches are returning mostly research, agriculture extension, and health center programs – not a good fit for a community food pantry. Let me try a more direct search. Still not finding food-bank-specific federal programs. Let me try one more targeted search for AmeriCorps and volunteer/senior programs that would actually accept food banks.

Excellent – I found a second AmeriCorps opportunity. Let me check the award history for the new one. Good data. The AmeriCorps State and National program (94.006) shows strong nonprofit history (65 awards, average $1.6M). However, that average is very high. Let me estimate the compliance burden at the midpoint of the realistic range and check whether that level of application effort is realistic for this org.

For a food pantry, the typical AmeriCorps State and National award would likely be at the lower end – let's estimate around $100K-$150K for a community food bank program. But first, let me check what's realistic for food-pantry-scale projects by looking at the range more carefully. The min is $8.1K and max is $13.3M, average $1.6M – but that's heavily skewed by large multi-site programs.

For a single food pantry in a mid-size river town with 6 volunteer hours available, an $1.6M application is completely unrealistic. Let me check the compliance burden at a more conservative estimate.

Now I have enough information to produce a brief. Let me synthesize:

---

## Summary

I reviewed 30+ current federal funding opportunities matching Riverside's food assistance and nutrition focus. Of those, only **one clears the real bar** for application with your current capacity. However, **before you can apply to anything**, you must confirm two compliance requirements.

---

## **CRITICAL COMPLIANCE FLOORS: ACTION REQUIRED BEFORE APPLYING**

### 1. **SAM.gov Registration & Unique Entity ID (UEI)**
**Status:** Unknown – requires confirmation
**Why it matters:** Every federal grant application requires an active SAM.gov registration (the System for Award Management run by the General Services Administration). This is not part of the grant-writing lift; it's a separate registration system. If you don't have this, you cannot submit an application, period – it's like not being able to send the form.

**How to clear it:**
1. Confirm the org has an EIN (Employer Identification Number) from the IRS. Most established nonprofits already have one; if not, apply free at irs.gov – takes minutes online.
2. Create a free Login.gov account (SAM.gov requires this) at login.gov, using the email of whoever will manage the registration long-term.
3. Go to sam.gov, sign in with Login.gov, and select 'Get Started' then 'Register Entity' (new registration).
4. Enter the org's legal business name **exactly as filed with the IRS**, physical address, and EIN. Mismatches (e.g. a DBA name instead of the legal name) are the most common reason registrations stall.
5. Complete the Core Data, Assertions, and Points of Contact sections: business types (select nonprofit/501(c)(3)), NAICS codes, and at least one named point of contact.
6. Provide banking information for Electronic Funds Transfer (EFT) – required before registration can be marked active, since this is how federal awards actually get paid.
7. Submit for validation. SAM.gov issues a UEI automatically once submitted; full validation against IRS records commonly takes **1–2 weeks but can run longer** if any field doesn't match exactly.
8. Registration must be renewed annually (SAM.gov will email a reminder) – an expired registration blocks new applications the same way a missing one does.

**Timeline:** 1–2 weeks for a clean application; longer if details don't match IRS records exactly.

### 2. **Indirect Cost Rate Agreement (NICRA)**
**Status:** Unknown – may not need immediate action
**Why it matters:** Federal grants require nonprofits to cover both direct costs (staff time on the funded work) and indirect costs (overhead: rent, utilities, HR, accounting). If you don't have a negotiated indirect cost rate agreement with the federal government, you can claim a flat 10% de minimis (minimal) rate on Modified Total Direct Costs with no negotiation required. This is available immediately. However, if this grant is won, you'll realistically absorb ~$10,000 in uncovered overhead (see Section 3 below) because the 10% rate typically falls short of real overhead.

**How to clear it (if you choose to):**
- No negotiation needed to apply or win – the 10% fallback is immediate.
- To negotiate a real rate instead (optional, only after winning federal funding):
  1. Identify your cognizant agency (the federal agency providing the largest share of your direct federal funding).
  2. Prepare an indirect cost rate proposal from at least one year of actual audited or reviewed financial statements.
  3. Submit to the cognizant agency for review and negotiation.
  4. **Timeline:** Several months – this is why it's not an immediate blocker.

Once negotiated, the rate applies to **all** federal awards you receive going forward, not just one grant.

---

## **OPPORTUNITY: AmeriCorps Seniors RSVP (CFDA 94.002)**

**Fit for Riverside:** Excellent. This program funds nonprofits to recruit and manage retired and senior volunteers for community service. It's a direct match for your senior meals mission and explicitly includes food assistance and nutrition programs.

**Realistic award range:** $5,000–$736,000, with average of $64,940 (based on FY2021 nonprofit award history, 698 awards across 47 states).

**Deadline:** October 20, 2026 (application opens August 20, 2026).

**Application lift:** Moderate – AmeriCorps applications are typically 20–30 pages, not the 40+ federal proposal many programs require. This fits your capacity constraint, though you'll still need to invest most of your 6 volunteer hours here plus some external help.

**Compliance floor status:**
- **SAM.gov registration & UEI:** Unknown (see above – must confirm before applying).
- **Indirect cost rate agreement:** Not required to apply; 10% de minimis rate is available immediately. If awarded, you'll carry ~$6,500 in uncovered overhead (see below).

**Structural cost of winning (estimate):**
- **Uncovered overhead:** ~$6,500/year (the gap between a realistic 20% overhead rate and the 10% de minimis rate you can claim without negotiation). This is a real dollar cost of accepting the award, separate from the effort of applying – meaning if you win $64,940, you'll realistically cover ~$58,440 in funded costs and absorb the rest from your general operating budget.
- **Single Audit threshold:** No – at $64,940, you'd stay well under the $750,000 federal funding threshold that triggers a formal Single Audit.

**Why this matters for your org:** You get senior volunteers to help with meals and distribution without large new staff hires, and the volunteer stipends/program costs are federally funded. Seniors get meaningful work. The application is shorter than many federal programs. However, you'll absorb some overhead, and you must manage volunteer recruitment and deployment on top of your current food distribution work.

**One honest risk:** AmeriCorps programs are competitive and outcomes-focused. You'd need to commit to tracking volunteer hours, participant outcomes, and impact – not just "we served 500 meals," but "trained volunteers increased senior nutrition screening by X%" or similar. If you don't currently have basic program metrics, you'd need to build that tracking before applying. This is manageable but adds a workstream beyond the grant-writing hours.

---

## **Why other opportunities didn't surface:**

- **Cold Chain Grants for Emergency Food Assistance (CFDA 10.197):** No nonprofit award history found in FY2021 data. This program likely focuses on state/local government or commercial food processors, not community nonprofits. Recommend verifying directly with USDA before pursuing.
- **Health Center Program nutrition expansion opportunities (CFDA 93.224 and similar):** These require being a federally qualified health center (FQHC), migrant health center, or homeless primary care program – structural requirements your food pantry doesn't meet.
- All other results were research fellowships, agriculture extension, international diplomacy, or infrastructure programs – structurally misaligned with a community food bank's mission and capacity.

---

**Bottom line:** 1 opportunity reviewed in depth; 1 recommended. Before moving forward on AmeriCorps RSVP, **confirm your SAM.gov registration status and obtain your UEI** – this is the hard blocker. Once that's live, the application is feasible for your volunteer committee, though you'll want to build program metrics and account for the ~$6,500 annual overhead gap in your budget.
