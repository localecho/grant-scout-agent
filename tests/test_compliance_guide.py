from src.tools.compliance_guide import compliance_guide


def test_sam_gov_returns_ordered_real_steps():
    result = compliance_guide("sam_gov")
    assert len(result["steps"]) >= 5
    assert any("EIN" in step for step in result["steps"])
    assert any("Login.gov" in step for step in result["steps"])
    assert any("Unique Entity ID" in step or "UEI" in step for step in result["steps"])
    assert result["typical_timeline"]


def test_nicra_returns_ordered_real_steps():
    result = compliance_guide("nicra")
    assert len(result["steps"]) >= 3
    assert any("10%" in step or "de minimis" in step for step in result["steps"])
    assert any("cognizant agency" in step for step in result["steps"])
    assert result["typical_timeline"]


def test_topic_is_case_and_whitespace_insensitive():
    assert compliance_guide("  SAM_GOV  ")["steps"] == compliance_guide("sam_gov")["steps"]


def test_unknown_topic_returns_error_not_a_crash():
    result = compliance_guide("something_else")
    assert result["steps"] == []
    assert "error" in result
