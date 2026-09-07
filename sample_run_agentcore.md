# Sample run: AgentCore Runtime entrypoint, invoked over HTTP

Proves `deploy/agentcore_app.py` is real, working AgentCore-compatible code, not just an
aspiration in a README. Captured 2026-09-07 running the local AgentCore dev server
(`python deploy/agentcore_app.py`) and hitting it exactly as Bedrock AgentCore Runtime would.

```
$ curl -s http://localhost:8080/ping
{"status":"Healthy","time_of_last_update":1788821866}

$ curl -s -X POST http://localhost:8080/invocations \
    -H "Content-Type: application/json" \
    -d '{"profile_path": "profiles/example_food_bank.yaml"}'
```

Response (truncated to the summary; full brief reviewed 60+ opportunities via live grants.gov
calls and the real FY2021 benchmark table):

```json
{
  "org": "Riverside Community Food Pantry",
  "brief": "... Final tally: 1 recommended | 59 reviewed and eliminated ..."
}
```

This run is a good example of the agent's honesty bar in practice: even the one opportunity
that cleared the historical-award and topical-fit checks (AmeriCorps Seniors RSVP) was flagged
as exceeding the org's stated 6-hour volunteer capacity, with an explicit "if you must do it
solo in 6 hours, this is not viable" -- the agent declined to oversell its one finding rather
than pad a thin result.

**Not deployed to AWS for this submission** (no AWS credentials configured for this build) --
see README's Known limitations. `agentcore launch` is the remaining step for an operator with
Bedrock AgentCore access.
