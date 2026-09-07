from src.profile import OrgProfile


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
