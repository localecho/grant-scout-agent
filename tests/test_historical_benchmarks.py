"""Unit tests for the historical_award_context tool -- no network, no model calls.

These exercise the real derived FY2021 benchmark data shipped in data/, so a failure here
means the data file moved or the parsing logic broke, not that an LLM answered wrong.
"""
from src.tools.historical_benchmarks import historical_award_context


def test_known_cfda_returns_real_head_start_row():
    rows = historical_award_context(cfda_number="93.600")
    assert len(rows) == 1
    row = rows[0]
    assert row["cfda_title"] == "HEAD START"
    assert int(row["award_count"]) > 1000
    assert int(row["avg_award_amount"]) > 0


def test_keyword_fallback_matches_title_case_insensitively():
    rows = historical_award_context(keyword="head start")
    assert any(r["cfda_number"] == "93.600" for r in rows)


def test_unknown_program_returns_empty_not_an_error():
    rows = historical_award_context(cfda_number="00.000", keyword="")
    assert rows == []


def test_empty_query_matches_nothing_by_design():
    rows = historical_award_context(cfda_number="", keyword="")
    assert rows == []
