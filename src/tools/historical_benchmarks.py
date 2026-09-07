"""Tool: ground opportunity fit in real historical award data instead of vibes.

data/nonprofit_award_benchmarks_fy2021.csv is derived from USASpending.gov's public
bulk-download API (FY2021 prime-award transactions, filtered to recipients flagged
"NONPROFIT WITH 501C3 IRS STATUS", grouped by CFDA program). See data/extract_benchmarks.sql
for the exact query that produced it and how to regenerate it against a fresh pull.
"""
from __future__ import annotations

import csv
import os

from strands import tool

_DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "nonprofit_award_benchmarks_fy2021.csv",
)

_ROWS: list[dict] | None = None


def _load() -> list[dict]:
    global _ROWS
    if _ROWS is None:
        with open(_DATA_PATH, newline="") as f:
            _ROWS = list(csv.DictReader(f, strict=True))
    return _ROWS


@tool
def historical_award_context(cfda_number: str = "", keyword: str = "") -> list[dict]:
    """Look up real FY2021 federal award history for 501(c)(3) nonprofits under a CFDA program.

    Use this BEFORE recommending an opportunity, to check whether nonprofits actually win this
    program, at what typical dollar amount, and how competitive/geographically spread it is.

    Args:
        cfda_number: exact CFDA/Assistance Listing number (e.g. "93.600"). Preferred if known.
        keyword: fallback free-text match against the program title if cfda_number is unknown.

    Returns:
        Matching benchmark rows: award_count, avg/min/max award amount, states_represented,
        awarding_agency_name. Empty list means no FY2021 nonprofit award history was found for
        this program in the sample -- treat that as a signal to verify eligibility manually,
        not as proof the program doesn't fund nonprofits.
    """
    rows = _load()
    cfda_number = cfda_number.strip()
    keyword = keyword.strip().lower()

    matches = []
    for row in rows:
        if cfda_number and row["cfda_number"] == cfda_number:
            matches.append(row)
        elif keyword and keyword in row["cfda_title"].lower():
            matches.append(row)
    return matches
