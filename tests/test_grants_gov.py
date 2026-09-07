"""Unit test for the grants.gov tool's response parsing, with the network call mocked.

A live-network test would be flaky in CI; the parsing logic is what this repo owns.
"""
from unittest.mock import MagicMock, patch

from src.tools.grants_gov import search_open_grants

FAKE_RESPONSE = {
    "data": {
        "oppHits": [
            {
                "id": "123",
                "number": "USDA-TEST-0001",
                "title": "Emergency Food Assistance Program",
                "agency": "Department of Agriculture",
                "openDate": "01/01/2026",
                "closeDate": "12/31/2026",
                "cfdaList": ["10.568"],
            }
        ]
    }
}


@patch("src.tools.grants_gov.requests.post")
def test_search_open_grants_parses_hits(mock_post):
    mock_resp = MagicMock()
    mock_resp.json.return_value = FAKE_RESPONSE
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp

    results = search_open_grants(keyword="food assistance", rows=5)

    assert len(results) == 1
    assert results[0]["title"] == "Emergency Food Assistance Program"
    assert results[0]["cfda_numbers"] == ["10.568"]
    assert results[0]["url"].endswith("/123")


@patch("src.tools.grants_gov.requests.post")
def test_rows_is_clamped_to_25(mock_post):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"data": {"oppHits": []}}
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp

    search_open_grants(keyword="x", rows=999)

    sent_payload = mock_post.call_args.kwargs["json"]
    assert sent_payload["rows"] == 25
