"""Amazon Bedrock AgentCore Runtime entrypoint for Grant Scout.

Wraps the same Agent built in src/agent.py -- no separate agent logic lives here. This is
the deployment adapter, not a second implementation.

Local test:
    python deploy/agentcore_app.py
    curl -X POST http://localhost:8080/invocations \
      -H "Content-Type: application/json" \
      -d '{"profile": {"name": "Test Org", "mission": "...", "org_type": "...",
                        "annual_budget_usd": 100000, "states": ["OH"]}}'
    # or, to reuse a profile already on disk:
    curl -X POST http://localhost:8080/invocations \
      -H "Content-Type: application/json" \
      -d '{"profile_path": "profiles/example_food_bank.yaml"}'

AWS deploy (requires an AWS account with Bedrock AgentCore access and OPENROUTER_API_KEY /
GRANT_SCOUT_MODEL_PROVIDER set as environment on the runtime -- not configured for this
submission, see README's Known limitations):
    agentcore configure --entrypoint deploy/agentcore_app.py
    agentcore launch
"""
from __future__ import annotations

import sys
from pathlib import Path

from bedrock_agentcore.runtime import BedrockAgentCoreApp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.agent import run_for_profile
from src.profile import OrgProfile

app = BedrockAgentCoreApp()


@app.entrypoint
def invoke(payload: dict) -> dict:
    """AgentCore Runtime entrypoint.

    Accepts either:
      {"profile": {...inline OrgProfile fields...}}
      {"profile_path": "profiles/example_food_bank.yaml"}
    """
    if "profile" in payload:
        profile = OrgProfile(**payload["profile"])
    elif "profile_path" in payload:
        profile = OrgProfile.from_yaml(payload["profile_path"])
    else:
        return {
            "error": "payload must include either 'profile' (inline org fields) "
            "or 'profile_path' (path to an org profile YAML file)."
        }

    brief = run_for_profile(profile)
    return {"org": profile.name, "brief": brief}


if __name__ == "__main__":
    app.run()
