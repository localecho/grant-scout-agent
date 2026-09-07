# Sample run: `python -m src.intake_form`

Proves `src/intake_form.py` is real, working code — not an aspiration in a README — closing the
gap a taste-council review flagged: the CLI + hand-edited YAML flow assumes exactly the kind of
technical comfort the "who it's for" pitch (a volunteer board with no grant-writing department)
often doesn't have. Captured 2026-09-07 running the real stdlib HTTP server and hitting it with
real HTTP requests (no mocking).

```
$ python -m src.intake_form
Grant Scout intake form running at http://127.0.0.1:<port> -- open it in a browser.

$ curl -s http://127.0.0.1:<port>/ | head -15
<!doctype html>
<html><head><title>Grant Scout - Tell us about your organization</title>
...
<h1>Grant Scout: tell us about your organization</h1>
<p>No YAML, no code. Fill this in once; Grant Scout uses it every time it searches for grants
on your behalf.</p>
<form method="POST">
...
```

A real form submission — no YAML file touched by hand:

```
$ curl -s -X POST http://127.0.0.1:<port>/ \
    --data-urlencode "name=Fairview Township Public Library" \
    --data-urlencode "mission=Provide free library access to a rural township." \
    --data-urlencode "org_type=501(c)(3) nonprofit, independent public library" \
    --data-urlencode "annual_budget_usd=310,000" \
    --data-urlencode "states=ky" \
    --data-urlencode "focus_keywords=digital literacy, rural library" \
    --data-urlencode "max_grant_writing_hours_available=8" \
    --data-urlencode "notes=One part-time grants volunteer." \
    --data-urlencode "sam_gov_registered=no" \
    --data-urlencode "has_indirect_cost_rate_agreement=unknown"

<h1>Saved</h1>
<p>Profile for <strong>Fairview Township Public Library</strong> saved to
<code>profiles/fairview_township_public_library.yaml</code>.</p>
<p>To run Grant Scout for this organization, run:</p>
<pre>python -m src.run --profile profiles/fairview_township_public_library.yaml</pre>
```

The saved file is a normal profile YAML — no special-casing, reads through the exact same
`OrgProfile.from_yaml` path as a hand-written one:

```yaml
name: Fairview Township Public Library
mission: Provide free library access to a rural township.
org_type: 501(c)(3) nonprofit, independent public library
annual_budget_usd: 310000
states:
- KY
focus_keywords:
- digital literacy
- rural library
max_grant_writing_hours_available: 8
notes: One part-time grants volunteer.
sam_gov_registered: false
has_indirect_cost_rate_agreement: null
```

Bad input gets a plain-language re-render of the form, not a stack trace — the audience this is
for should never see a Python traceback:

```
$ curl -s -X POST http://127.0.0.1:<port>/ --data-urlencode "mission=x" -w "\nHTTP_STATUS:%{http_code}\n"
... (form re-rendered with "Please fill in: Organization name, ...") ...
HTTP_STATUS:400
```

## What this does and doesn't close

**Closes:** the *editing* gap — filling in blanks in a browser instead of hand-editing YAML in a
text editor. Covered by `tests/test_intake_form.py` (form parsing, tri-state compliance fields,
plain-language validation errors, and a round-trip through the real `OrgProfile.from_yaml`).

**Does not close:** the *hosting* gap. Someone still has to run `python -m src.intake_form` once
and hand the org a URL — that's the same "not deployed to live AWS infrastructure" limitation
already named in `README.md`. A hosted version (AgentCore, Lambda, or any always-on host) is the
remaining step to make this reachable without anyone running Python locally.
