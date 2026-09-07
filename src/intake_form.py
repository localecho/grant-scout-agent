"""A no-YAML, no-editor intake path for the exact audience Grant Scout is built for.

The CLI's `--profile some.yaml` flow assumes someone comfortable hand-editing YAML. The
"who it's for" pitch (a volunteer board with no grant-writing department) is often also a board
with no one comfortable doing that. This module serves a plain HTML form -- fill in the blanks,
submit, get back a saved profile YAML and the exact next command to run. Zero new dependencies:
stdlib `http.server` only, matching the "two tools, not ten" restraint the rest of the build
already commits to.

This closes the *editing* gap, not the *hosting* gap -- someone still has to run
`python -m src.intake_form` once (e.g. the org's one tech-comfortable volunteer, or whoever set
up the CLI in the first place) and hand the org the URL it prints. Removing that last step too
means hosting this somewhere the org can reach without anyone running Python locally, which is
the same AWS-deployment gap named in README's Known limitations -- not solved by this file.
"""
from __future__ import annotations

import html
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import yaml

from src.profile import OrgProfile

FIELD_LABELS = {
    "name": "Organization name",
    "mission": "Mission (one or two sentences)",
    "org_type": 'Organization type (e.g. "501(c)(3) nonprofit, food bank")',
    "annual_budget_usd": "Annual budget in dollars (numbers only, e.g. 420000)",
    "states": "States served (comma-separated postal codes, e.g. OH, KY)",
    "focus_keywords": "Focus keywords (comma-separated, e.g. food assistance, nutrition)",
    "max_grant_writing_hours_available": "Volunteer/staff hours available for grant writing per cycle",
    "notes": "Anything else the agent should know (optional)",
}

TRISTATE_FIELDS = {
    "sam_gov_registered": "Registered on SAM.gov with a Unique Entity ID (UEI)?",
    "has_indirect_cost_rate_agreement": "Have a negotiated indirect cost rate agreement?",
}


def _tristate_select(field_name: str, label: str) -> str:
    return f"""
    <label>{html.escape(label)}
      <select name="{field_name}">
        <option value="unknown" selected>Not sure</option>
        <option value="yes">Yes</option>
        <option value="no">No</option>
      </select>
    </label>"""


def render_form(error: str | None = None) -> str:
    text_fields = "\n".join(
        f'<label>{html.escape(label)}<input name="{name}" required></label>'
        if name not in ("mission", "notes")
        else f'<label>{html.escape(label)}<textarea name="{name}"'
        f'{" required" if name == "mission" else ""}></textarea></label>'
        for name, label in FIELD_LABELS.items()
    )
    tristate_fields = "\n".join(
        _tristate_select(name, label) for name, label in TRISTATE_FIELDS.items()
    )
    error_html = f'<p class="error">{html.escape(error)}</p>' if error else ""
    return f"""<!doctype html>
<html><head><title>Grant Scout - Tell us about your organization</title>
<style>
body {{ font-family: sans-serif; max-width: 640px; margin: 2rem auto; padding: 0 1rem; }}
label {{ display: block; margin-bottom: 1rem; }}
input, select, textarea {{ display: block; width: 100%; padding: 0.4rem; margin-top: 0.25rem; }}
.error {{ color: #a00; font-weight: bold; }}
button {{ padding: 0.6rem 1.2rem; }}
</style></head>
<body>
<h1>Grant Scout: tell us about your organization</h1>
<p>No YAML, no code. Fill this in once; Grant Scout uses it every time it searches for grants
on your behalf.</p>
{error_html}
<form method="POST">
{text_fields}
{tristate_fields}
<button type="submit">Save profile</button>
</form>
</body></html>"""


def _tristate_to_bool(value: str | None) -> bool | None:
    if value == "yes":
        return True
    if value == "no":
        return False
    return None


def parse_form(fields: dict[str, str]) -> OrgProfile:
    """Build an OrgProfile from raw (already-decoded) form fields. Raises ValueError with a
    plain-language message on bad input -- no stack traces shown to a non-technical submitter."""
    missing = [
        name
        for name in ("name", "mission", "org_type", "annual_budget_usd", "states")
        if not fields.get(name, "").strip()
    ]
    if missing:
        raise ValueError(
            "Please fill in: " + ", ".join(FIELD_LABELS.get(f, f) for f in missing)
        )

    try:
        budget = int(fields["annual_budget_usd"].replace(",", "").replace("$", "").strip())
    except ValueError:
        raise ValueError('Annual budget must be a plain number, e.g. "420000" (no letters).')

    try:
        hours = int(fields.get("max_grant_writing_hours_available", "10").strip() or "10")
    except ValueError:
        raise ValueError('Volunteer hours must be a plain number, e.g. "6".')

    return OrgProfile(
        name=fields["name"].strip(),
        mission=fields["mission"].strip(),
        org_type=fields["org_type"].strip(),
        annual_budget_usd=budget,
        states=[s.strip().upper() for s in fields["states"].split(",") if s.strip()],
        focus_keywords=[k.strip() for k in fields.get("focus_keywords", "").split(",") if k.strip()],
        max_grant_writing_hours_available=hours,
        notes=fields.get("notes", "").strip(),
        sam_gov_registered=_tristate_to_bool(fields.get("sam_gov_registered")),
        has_indirect_cost_rate_agreement=_tristate_to_bool(fields.get("has_indirect_cost_rate_agreement")),
    )


def profile_to_yaml(profile: OrgProfile) -> str:
    """Serialize back to the exact YAML shape OrgProfile.from_yaml expects, so a profile saved
    here round-trips through the normal CLI path with no special-casing."""
    data = {
        "name": profile.name,
        "mission": profile.mission,
        "org_type": profile.org_type,
        "annual_budget_usd": profile.annual_budget_usd,
        "states": profile.states,
        "focus_keywords": profile.focus_keywords,
        "max_grant_writing_hours_available": profile.max_grant_writing_hours_available,
        "notes": profile.notes,
        "sam_gov_registered": profile.sam_gov_registered,
        "has_indirect_cost_rate_agreement": profile.has_indirect_cost_rate_agreement,
    }
    return yaml.safe_dump(data, sort_keys=False)


def _slugify(name: str) -> str:
    return "".join(c.lower() if c.isalnum() else "_" for c in name).strip("_") or "org"


class IntakeHandler(BaseHTTPRequestHandler):
    profiles_dir = "profiles"

    def log_message(self, *args):  # quiet the default stderr access log
        pass

    def do_GET(self):
        self._respond(200, render_form())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8")
        fields = {k: v[0] for k, v in parse_qs(raw).items()}
        try:
            profile = parse_form(fields)
        except ValueError as exc:
            self._respond(400, render_form(error=str(exc)))
            return

        os.makedirs(self.profiles_dir, exist_ok=True)
        out_path = os.path.join(self.profiles_dir, f"{_slugify(profile.name)}.yaml")
        with open(out_path, "w") as f:
            f.write(profile_to_yaml(profile))

        self._respond(
            200,
            f"""<!doctype html><html><head><title>Saved</title></head><body
            style="font-family: sans-serif; max-width: 640px; margin: 2rem auto;">
            <h1>Saved</h1>
            <p>Profile for <strong>{html.escape(profile.name)}</strong> saved to
            <code>{html.escape(out_path)}</code>.</p>
            <p>To run Grant Scout for this organization, run:</p>
            <pre>python -m src.run --profile {html.escape(out_path)}</pre>
            </body></html>""",
        )

    def _respond(self, status: int, body: str) -> None:
        encoded = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


def main() -> None:
    port = int(os.environ.get("GRANT_SCOUT_INTAKE_PORT", "8765"))
    server = HTTPServer(("127.0.0.1", port), IntakeHandler)
    print(f"Grant Scout intake form running at http://127.0.0.1:{port} -- open it in a browser.")
    server.serve_forever()


if __name__ == "__main__":
    main()
