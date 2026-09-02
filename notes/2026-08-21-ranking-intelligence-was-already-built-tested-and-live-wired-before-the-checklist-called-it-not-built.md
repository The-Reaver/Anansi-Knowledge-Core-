---
id: 2026-08-21-ranking-intelligence-was-already-built-tested-and-live-wired-before-the-checklist-called-it-not-built
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [ranking-intelligence, geo, checklist-drift, gitignore, sales-tooling]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn establishing that factor_audit.py and its test suite were already built, tested, and live-wired a day before the checklist called ranking intelligence not-built."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Ranking Intelligence + AI Search Edge (Sonar/CCC)\""
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
- confidence: high — files read directly, test suite executed live during this sweep (15/15 passed), router wiring confirmed by grep, commit dates cross-checked
- verified: 2026-08-21

# Ranking Intelligence (factor_audit.py) was fully built, tested, and wired into a live router before the 2026-08-03 checklist said it "awaits build"

## Body
The 2026-08-03 master checklist stated: "docs/RANKING_FACTORS_CATALOG.md seeded, SPEC_RANKING_INTELLIGENCE
awaits build." This was already false on the day it was written. `reports/RANKING_INTELLIGENCE_BUILD_REPORT.md`
(tracked in git, committed in `1991e9b` on 2026-08-02 — one day before the checklist) declares "all
deliverables built and green," with `projects/geo_platform/backend/app/services/ranking/factor_audit.py`
(`audit_ranking` + `scorecard_markdown`, 19 weighted factors across 5 families) built and
`projects/geo_platform/tests/test_factor_audit.py` at 15/15 passing. Re-running that test file live
today (`venv/Scripts/python.exe projects/geo_platform/tests/test_factor_audit.py`) still gives 15/15
passed, so the build is not bit-rotted. Beyond "built": it is live-wired, not just offline code —
`projects/geo_platform/backend/app/routers/client.py` imports `build_ranking_panel`/`render_ranking_section`
from `dashboard_panels.py` (which itself calls `audit_ranking`/`scorecard_markdown`) and exposes it at
`GET /{site_id}/dashboard/ranking`, and `client.router` is included in `main.py`. The likely mechanic
for how this was missed: `projects/` is gitignored (`.gitignore:12`), so the code itself is invisible
to `git log`, but the build report proving it exists WAS tracked and committed a day before the
checklist — so the miss was not "no evidence available," it was a tracked report not being consulted
(or a stale docs/PROJECT_DASHBOARD.md status being copied forward instead; see companion note on that
dashboard's staleness). No commits or file changes touch this workstream's paths between 2026-08-03
and today (2026-08-21) — the 18-day-stale checklist is stale in date only; the substance was already
wrong at inception.

## Links
- specs/SPEC_RANKING_INTELLIGENCE.md
- reports/RANKING_INTELLIGENCE_BUILD_REPORT.md
- docs/RANKING_FACTORS_CATALOG.md
- projects/geo_platform/backend/app/services/ranking/factor_audit.py (gitignored, disk-only)
- projects/geo_platform/backend/app/routers/client.py
