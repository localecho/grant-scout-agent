"""Org profile: the small amount of context a community org gives the agent once."""
from __future__ import annotations

from dataclasses import dataclass, field

import yaml


@dataclass
class OrgProfile:
    name: str
    mission: str
    org_type: str  # e.g. "501(c)(3) nonprofit", "public library", "food bank"
    annual_budget_usd: int
    states: list[str]
    focus_keywords: list[str] = field(default_factory=list)
    max_grant_writing_hours_available: int = 10
    notes: str = ""
    # None = unknown/unstated. Federal grants gate on SAM.gov registration + a Unique Entity ID
    # (UEI) before an application can even be submitted, and many require an indirect cost rate
    # agreement -- a real compliance floor that hour-estimates alone don't capture. Per Diane
    # Leonard's review (data/reports/moot_verdict_grant-scout-submission_2026-09-07_v1.txt):
    # hour-estimates without this gate miss the actual first hurdle most six-volunteer-hour
    # orgs fail before the writing hours even start.
    sam_gov_registered: bool | None = None
    has_indirect_cost_rate_agreement: bool | None = None

    @classmethod
    def from_yaml(cls, path: str) -> "OrgProfile":
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        try:
            return cls(**data)
        except TypeError as exc:
            raise ValueError(
                f"{path} is missing or misnames a required field ({exc}). "
                f"Required fields: name, mission, org_type, annual_budget_usd, states."
            ) from exc

    def _compliance_status(self, value: bool | None) -> str:
        return "unknown -- ask the org to confirm" if value is None else ("yes" if value else "no")

    def as_prompt_block(self) -> str:
        return (
            f"Org name: {self.name}\n"
            f"Org type: {self.org_type}\n"
            f"Mission: {self.mission}\n"
            f"Annual budget: ${self.annual_budget_usd:,}\n"
            f"States served: {', '.join(self.states)}\n"
            f"Focus keywords: {', '.join(self.focus_keywords)}\n"
            f"Grant-writing capacity: ~{self.max_grant_writing_hours_available} volunteer/staff hours available\n"
            f"SAM.gov registered (has a Unique Entity ID): {self._compliance_status(self.sam_gov_registered)}\n"
            f"Has an indirect cost rate agreement: {self._compliance_status(self.has_indirect_cost_rate_agreement)}\n"
            f"Notes: {self.notes}"
        )
