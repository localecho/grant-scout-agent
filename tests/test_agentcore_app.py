"""Unit tests for the AgentCore entrypoint's payload handling -- mocks run_for_profile so
this doesn't make a real model/network call. The handler was also verified live against a
real local AgentCore dev server (see sample_run_agentcore.md); this test guards the payload
contract so a refactor can't silently break it.
"""
from unittest.mock import patch

from deploy.agentcore_app import invoke


@patch("deploy.agentcore_app.run_for_profile", return_value="mocked brief text")
def test_invoke_with_inline_profile(mock_run):
    result = invoke(
        {
            "profile": {
                "name": "Test Org",
                "mission": "Test mission",
                "org_type": "501(c)(3) nonprofit",
                "annual_budget_usd": 100000,
                "states": ["OH"],
            }
        }
    )
    assert result["org"] == "Test Org"
    assert result["brief"] == "mocked brief text"
    mock_run.assert_called_once()


@patch("deploy.agentcore_app.run_for_profile", return_value="mocked brief text")
def test_invoke_with_profile_path(mock_run):
    result = invoke({"profile_path": "profiles/example_food_bank.yaml"})
    assert result["org"] == "Riverside Community Food Pantry"
    assert result["brief"] == "mocked brief text"


def test_invoke_with_neither_key_returns_error():
    result = invoke({"something_else": True})
    assert "error" in result
