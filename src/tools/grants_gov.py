"""Tool: search live, open federal funding opportunities via grants.gov's public search API.

No API key required. Docs: https://grants.gov/api
"""
from __future__ import annotations

import requests
from strands import tool

GRANTS_GOV_SEARCH_URL = "https://api.grants.gov/v1/api/search2"


@tool
def search_open_grants(keyword: str, rows: int = 10) -> list[dict]:
    """Search grants.gov for currently open or forecasted federal funding opportunities.

    Args:
        keyword: free-text search term (e.g. "food security", "youth mentoring", "library broadband").
        rows: how many results to return (max 25).

    Returns:
        A list of opportunity dicts with id, number, title, agency, openDate, closeDate, cfdaList.
    """
    rows = max(1, min(rows, 25))
    payload = {
        "rows": rows,
        "keyword": keyword,
        "oppStatuses": "forecasted|posted",
    }
    try:
        resp = requests.post(GRANTS_GOV_SEARCH_URL, json=payload, timeout=20)
        resp.raise_for_status()
        body = resp.json()
    except requests.RequestException as exc:
        # Surface a structured signal the agent can reason about and report to the user,
        # instead of crashing the whole run on a transient grants.gov outage.
        return [{"error": f"grants.gov search failed: {exc}"}]
    hits = body.get("data", {}).get("oppHits", [])
    return [
        {
            "id": h.get("id"),
            "number": h.get("number"),
            "title": h.get("title"),
            "agency": h.get("agency"),
            "open_date": h.get("openDate"),
            "close_date": h.get("closeDate"),
            "cfda_numbers": h.get("cfdaList", []),
            "url": f"https://www.grants.gov/search-results-detail/{h.get('id')}",
        }
        for h in hits
    ]
