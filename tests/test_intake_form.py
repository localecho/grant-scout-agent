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
    )
    yaml_path = tmp_path / "profile.yaml"
    yaml_path.write_text(profile_to_yaml(profile))

    round_tripped = OrgProfile.from_yaml(str(yaml_path))
    assert round_tripped == profile


def test_render_form_includes_every_field_and_escapes_error():
    body = render_form(error="<script>bad</script>")
    for name in ("name", "mission", "org_type", "annual_budget_usd", "states"):
        assert f'name="{name}"' in body
    assert "<script>bad</script>" not in body
    assert "&lt;script&gt;" in body
