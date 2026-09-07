from src.tools.compliance_burden import (
    ASSUMED_REAL_OVERHEAD_RATE,
    DE_MINIMIS_INDIRECT_RATE,
    SINGLE_AUDIT_THRESHOLD_USD,
    estimate_compliance_burden,
)


def test_no_negotiated_rate_produces_a_real_shortfall_estimate():
    result = estimate_compliance_burden(
        award_amount_usd=100_000,
        has_indirect_cost_rate_agreement=False,
    )
    expected_shortfall = 100_000 * (ASSUMED_REAL_OVERHEAD_RATE - DE_MINIMIS_INDIRECT_RATE)
    assert result["uncovered_overhead_estimate_usd"] == expected_shortfall
    assert "2 CFR 200.414" in result["overhead_assumption"]


def test_unknown_rate_treated_as_no():
    result = estimate_compliance_burden(
        award_amount_usd=100_000,
        has_indirect_cost_rate_agreement=None,
    )
    assert result["uncovered_overhead_estimate_usd"] > 0


def test_negotiated_rate_means_zero_uncovered_overhead():
    result = estimate_compliance_burden(
        award_amount_usd=100_000,
        has_indirect_cost_rate_agreement=True,
    )
    assert result["uncovered_overhead_estimate_usd"] == 0.0
    assert "0%" in result["overhead_assumption"]


def test_single_audit_threshold_not_crossed_below_750k():
    result = estimate_compliance_burden(
        award_amount_usd=100_000,
        has_indirect_cost_rate_agreement=True,
        estimated_current_annual_federal_funding_usd=0,
    )
    assert result["crosses_single_audit_threshold"] is False
    assert "stays under" in result["single_audit_note"]


def test_single_audit_threshold_crossed_at_exactly_750k():
    result = estimate_compliance_burden(
        award_amount_usd=SINGLE_AUDIT_THRESHOLD_USD,
        has_indirect_cost_rate_agreement=True,
        estimated_current_annual_federal_funding_usd=0,
    )
    assert result["crosses_single_audit_threshold"] is True
    assert "Single Audit" in result["single_audit_note"]


def test_single_audit_threshold_crossed_by_combining_existing_and_new_funding():
    result = estimate_compliance_burden(
        award_amount_usd=100_000,
        has_indirect_cost_rate_agreement=True,
        estimated_current_annual_federal_funding_usd=700_000,
    )
    assert result["crosses_single_audit_threshold"] is True
