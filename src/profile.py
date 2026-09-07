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

    @classmethod
    def from_yaml(cls, path: str) -> "OrgProfile":
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)

    def as_prompt_block(self) -> str:
        return (
            f"Org name: {self.name}\n"
            f"Org type: {self.org_type}\n"
            f"Mission: {self.mission}\n"
            f"Annual budget: ${self.annual_budget_usd:,}\n"
            f"States served: {', '.join(self.states)}\n"
            f"Focus keywords: {', '.join(self.focus_keywords)}\n"
            f"Grant-writing capacity: ~{self.max_grant_writing_hours_available} volunteer/staff hours available\n"
            f"Notes: {self.notes}"
        )
