import pytest

from src.intake_form import parse_form, profile_to_yaml, render_form
from src.profile import OrgProfile


def test_parse_form_builds_correct_profile():
    fields = {
        "name": "Riverside Community Food Pantry",
        "mission": "Distribute emergency food.",
        "org_type": "501(c)(3) nonprofit, food bank",
        "annual_budget_usd": "420,000",
        "states": "oh, KY",
        "focus_keywords": "food assistance, nutrition",
        "max_grant_writing_hours_available": "6",
        "notes": "All-volunteer committee.",
        "sam_gov_registered": "yes",
        "has_indirect_cost_rate_agreement": "no",
    }
    profile = parse_form(fields)
    assert profile.name == "Riverside Community Food Pantry"
    assert profile.annual_budget_usd == 420000
    assert profile.states == ["OH", "KY"]
    assert profile.focus_keywords == ["food assistance", "nutrition"]
    assert profile.max_grant_writing_hours_available == 6
    assert profile.sam_gov_registered is True
    assert profile.has_indirect_cost_rate_agreement is False


def test_parse_form_captures_existing_federal_funding_for_single_audit_check():
    """Regression test: estimated_current_annual_federal_funding_usd used to be defined on
    OrgProfile but never collected by this form, so it silently defaulted to 0.0 for every
    real submitter -- meaning the "load-bearing" Single Audit threshold check could only ever
    fire off the size of a single new award, never off an org's real existing federal funding.
    Found by an adversarial review 2026-09-09; this test pins the fix."""
    fields = {
        "name": "Cedar Valley Community Health Clinic",
        "mission": "Provide sliding-scale primary care.",
        "org_type": "501(c)(3) nonprofit, FQHC look-alike",
        "annual_budget_usd": "1450000",
        "states": "WV",
        "estimated_current_annual_federal_funding_usd": "550,000",
    }
    profile = parse_form(fields)
    assert profile.estimated_current_annual_federal_funding_usd == 550000.0


def test_parse_form_defaults_federal_funding_to_zero_when_left_blank():
    fields = {
        "name": "Test Org",
        "mission": "Test mission.",
        "org_type": "501(c)(3)",
        "annual_budget_usd": "100000",
        "states": "OH",
    }
    profile = parse_form(fields)
    assert profile.estimated_current_annual_federal_funding_usd == 0.0


def test_parse_form_rejects_non_numeric_federal_funding_with_plain_language_error():
    fields = {
        "name": "Test Org",
        "mission": "Test mission.",
        "org_type": "501(c)(3)",
        "annual_budget_usd": "100000",
        "states": "OH",
        "estimated_current_annual_federal_funding_usd": "a lot",
    }
    with pytest.raises(ValueError, match="plain number"):
        parse_form(fields)


def test_parse_form_tristate_defaults_to_none_when_unset_or_unknown():
    fields = {
        "name": "Test Org",
        "mission": "Test mission.",
        "org_type": "501(c)(3)",
        "annual_budget_usd": "100000",
        "states": "OH",
    }
    profile = parse_form(fields)
    assert profile.sam_gov_registered is None
    assert profile.has_indirect_cost_rate_agreement is None

    fields["sam_gov_registered"] = "unknown"
    profile = parse_form(fields)
    assert profile.sam_gov_registered is None


def test_parse_form_rejects_missing_required_fields_with_plain_language_error():
    with pytest.raises(ValueError, match="Organization name"):
        parse_form({"mission": "x", "org_type": "x", "annual_budget_usd": "1", "states": "OH"})


def test_parse_form_rejects_non_numeric_budget_with_plain_language_error():
    fields = {
        "name": "Test Org",
        "mission": "Test",
        "org_type": "501(c)(3)",
        "annual_budget_usd": "a lot",
        "states": "OH",
    }
    with pytest.raises(ValueError, match="plain number"):
        parse_form(fields)


def test_profile_to_yaml_round_trips_through_org_profile_from_yaml(tmp_path):
    profile = OrgProfile(
        name="Test Org",
        mission="Test mission.",
        org_type="501(c)(3)",
        annual_budget_usd=100000,
        states=["OH"],
        focus_keywords=["food"],
        max_grant_writing_hours_available=8,
        notes="notes here",
        sam_gov_registered=True,
        has_indirect_cost_rate_agreement=None,
        estimated_current_annual_federal_funding_usd=250000.0,
    )
    yaml_path = tmp_path / "profile.yaml"
    yaml_path.write_text(profile_to_yaml(profile))

    round_tripped = OrgProfile.from_yaml(str(yaml_path))
    assert round_tripped == profile
    assert round_tripped.estimated_current_annual_federal_funding_usd == 250000.0


def test_render_form_includes_every_field_and_escapes_error():
    body = render_form(error="<script>bad</script>")
    for name in (
        "name", "mission", "org_type", "annual_budget_usd", "states",
        "estimated_current_annual_federal_funding_usd",
    ):
        assert f'name="{name}"' in body
    assert "<script>bad</script>" not in body
    assert "&lt;script&gt;" in body
