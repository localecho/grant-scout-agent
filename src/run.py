"""CLI entrypoint: python -m src.run --profile profiles/example_food_bank.yaml"""
from __future__ import annotations

import argparse

from src.agent import run_for_profile
from src.profile import OrgProfile


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Grant Scout for one org profile.")
    parser.add_argument(
        "--profile",
        default="profiles/example_food_bank.yaml",
        help="Path to an org profile YAML file.",
    )
    args = parser.parse_args()

    profile = OrgProfile.from_yaml(args.profile)
    print(f"Running Grant Scout for: {profile.name}\n")
    # Strands streams tool calls and the final answer to stdout as the agent runs, so the
    # returned string (kept for tests/programmatic use) is not re-printed here.
    run_for_profile(profile)


if __name__ == "__main__":
    main()
