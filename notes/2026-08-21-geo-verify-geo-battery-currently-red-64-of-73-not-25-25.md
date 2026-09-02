---
id: 2026-08-21-geo-verify-geo-battery-currently-red-64-of-73-not-25-25
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — added a caveat that the 64/73 count is a snapshot needing reconfirmation from the live GEO Suite session. Operator retains veto per Mandate 1."
project: geo
tags: [geo-suite, geo-platform, verify-py, testing, checklist-drift, compliance]
sources:
  - ref: "Archive turns 226-229: STAG master-checklist refresh sweep, 2026-08-21, workstream 'GEO Suite' — live run of `./venv/Scripts/python.exe verify.py --geo`, full output captured"
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"GEO Suite\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [226, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high — command run live this sweep (`./venv/Scripts/python.exe verify.py --geo`), full output captured
- verified: 2026-08-21
- REVIEW: high-impact

# The 2026-08-03 checklist's "verify.py --geo passes 25/25" is stale on both the count and the color: today's live run is RED, 64/73, on 73 files

## Body
The 2026-08-03 master checklist claimed "Built and verified, verify.py --geo passes 25/25." Running the
same command live today (`./venv/Scripts/python.exe verify.py --geo` from repo root, the correct runner
per `research/knowledge-home/notes/2026-08-08-root-verify-py-is-the-battery-runner-not-anything-inside-projects-geo-platform.md`)
gives **64/73 green, RED, 9 of 73 test files failed** — a different test count (73, not 25 — the suite has
grown substantially) and a different color (red, not green). This root venv (`C:\Users\abadm\stag\venv`) is
also independently confirmed stale as of 2026-07-30 in `projects/geo_platform/STATUS.md`, which self-reported
45/45 at that time — so the checklist's "25/25" number does not match either the 2026-07-30 in-repo status
doc or today's live run; three different counts across three points in time (25, 45, 73), none of which
currently agree.

Breakdown of today's 9 failures:
- 7 are environment drift, not code bugs: `ModuleNotFoundError: No module named 'twilio'` (test_admin_dashboard,
  test_admin_metrics, test_auth_and_schema, test_client_dashboard, test_client_metrics, test_dashboard_panels,
  test_sales_preview) and `No module named 'asyncpg'` (test_scheduler_poller). Both packages are declared in
  `projects/geo_platform/backend/pyproject.toml` but are absent from the root venv (`pip show` confirms not
  found) — the venv used to run the battery has drifted out of sync with the backend's declared dependencies.
- 1 is a real assertion failure with compliance weight: `test_compliance_checker.py` is 23/24, failing
  `test_accessibility_findings_have_no_fabricated_legal_basis`. This is not a fabrication bug — it is a stale
  test. `backend/app/services/compliance/regulatory_citations.py` has a real, currently **uncommitted** local
  change (see companion note on the geo_platform repo split) that wires four real, well-sourced ADA/WCAG
  citations (42 U.S.C. §12182, Robles v. Domino's Pizza 9th Cir., DOJ's 2022 guidance, DOJ's 2024 Title II
  final rule, each with a source URL and a scope caveat that the 2024 rule binds public entities not private
  clients) into `wcag-*` findings. The test still asserts the *old* policy (wcag findings must carry `[]`),
  so real, deliberate, sourced work is what's currently failing the battery — but because it is uncommitted
  and the test wasn't updated alongside it, `verify.py --geo` reports red for a reason a status reader would
  reasonably read as "regression" rather than "in-progress legal work not yet reconciled with its own test."

Net: the checklist's headline number is unusable as a current status signal — it predates a large expansion
of the test suite, and today's actual run is red for a mix of a fixable venv gap and a real but currently
uncommitted change to compliance-critical (legal citation) code that needs its test updated to match before
this can honestly be called "verified" again.

Caveat added at promotion (2026-08-26): the 64/73 count is a 2026-08-21 snapshot. Reverification on
2026-08-25 confirmed the root venv still lacks `twilio` and `asyncpg` and that
`regulatory_citations.py` still carries the same uncommitted WCAG-citation content, but the full
`verify.py --geo` battery was deliberately not re-run from this stag-side session — GEO Suite has its
own continuously-active dedicated session elsewhere, and this count should not be chased or guessed
from here. Any consumer of this note should get a fresh `verify.py --geo` run from the actual GEO
Suite session before treating 64/73 as current.

## Links
- related-to, research/knowledge-home/notes/2026-08-08-root-verify-py-is-the-battery-runner-not-anything-inside-projects-geo-platform.md, confirms verify.py at repo root (not inside projects/geo_platform) is the correct runner used here.
