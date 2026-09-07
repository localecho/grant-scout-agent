import pytest

from src.profile import OrgProfile


def test_missing_required_field_raises_clear_error(tmp_path):
    bad_profile = tmp_path / "bad.yaml"
    bad_profile.write_text("name: Incomplete Org\nmission: Missing other fields\n")

    with pytest.raises(ValueError, match="Required fields"):
        OrgProfile.from_yaml(str(bad_profile))


def test_loads_example_profile():
    profile = OrgProfile.from_yaml("profiles/example_food_bank.yaml")
    assert profile.name == "Riverside Community Food Pantry"
    assert "OH" in profile.states
    assert profile.annual_budget_usd == 420000


def test_prompt_block_includes_all_fields():
    profile = OrgProfile.from_yaml("profiles/example_food_bank.yaml")
    block = profile.as_prompt_block()
    assert profile.name in block
    assert profile.mission in block
    assert "$420,000" in block


def test_compliance_status_unstated_by_default():
    profile = OrgProfile.from_yaml("profiles/example_food_bank.yaml")
    assert profile.sam_gov_registered is None
    assert profile.has_indirect_cost_rate_agreement is None
    block = profile.as_prompt_block()
    assert "SAM.gov registered" in block
    assert "unknown -- ask the org to confirm" in block


def test_compliance_status_reports_stated_yes_and_no():
    profile = OrgProfile(
        name="Test Org",
        mission="Test",
        org_type="501(c)(3)",
        annual_budget_usd=100000,
        states=["OH"],
        sam_gov_registered=True,
        has_indirect_cost_rate_agreement=False,
    )
    block = profile.as_prompt_block()
    assert "SAM.gov registered (has a Unique Entity ID): yes" in block
    assert "Has an indirect cost rate agreement: no" in block
