---
id: 2026-08-21-ccc-sonar-all-nine-modules-had-partial-builds-before-checklist-implied-only-specs-existed
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [ai-search-edge, sonar, ccc, checklist-drift, gitignore, geo]
sources:
  - ref: "Turns 218-229: assistant launches an 18-workstream background re-verification sweep of the 2026-08-03 master checklist (turn 218) and consolidates the sub-agents' findings, including the Ranking Intelligence + AI Search Edge (Sonar/CCC) workstream, for the operator (turn 229)."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Ranking Intelligence + AI Search Edge (Sonar/CCC)\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# All nine AI Search Edge / Citation Command Center modules (M1-M9) already had PARTIAL code+test builds before the checklist implied only the master spec existed
- id: 2026-08-21-ccc-sonar-all-nine-modules-had-partial-builds-before-checklist-implied-only-specs-existed
- type: finding
- status: ratified
- class: confirmed
- source: STAG master-checklist refresh sweep, 2026-08-21, workstream "Ranking Intelligence + AI Search Edge (Sonar/CCC)"
- confidence: high — build reports read directly (all tracked in git), commit dates cross-checked, router wiring checked by grep
- verified: 2026-08-21
- tags: ai-search-edge, sonar, ccc, checklist-drift, gitignore, geo

## Body
The 2026-08-03 checklist described the AI Search Edge / Citation Command Center as: "specs/SPEC_CCC_MASTER.md
is the authoritative spec... Build order: Ranking Intelligence first, then Sonar layers on top" — with
`docs/PROJECT_DASHBOARD.md` (which the checklist appears to draw from) stating "Next action for CCC:
Anirak (or ORLOK) drafts SPEC_CCC_1_gap_detection.md first." The clear implication is that as of
2026-08-03, no CCC module build had started. That is false: `reports/CCC_M1_INGESTION_BUILD_REPORT.md`
through `CCC_M9_ADMIN_BUILD_REPORT.md` (8 of 9 modules; M7 lives under
`reports/M7_AGENT_GATES_BUILD_REPORT.md`) are all tracked in git, committed by 2026-07-28 (`aea3a6b`,
`442fbd4`, `5ce4585`) — days before the checklist. Each is explicitly status **PARTIAL** (e.g. M2 Sonar:
"D1-D4 offline measurement layer built; full DoD still open"; M3 Citation Influence: "offline CII/FDS/
schema intelligence landed; Track A weights still UNVALIDATED"). Matching code exists on disk at
`projects/geo_platform/backend/app/services/ranking/{citation_influence,schema_intelligence,
entity_clustering,content_brief}.py` and `projects/geo_platform/backend/app/services/sonar/{accuracy_audit,
alert_gates,citation_classifier,gap_analysis,multi_model,sonar_weights,visibility_metrics}.py`
(gitignored, so invisible to `git log`, but present and dated by their build reports to 2026-07-28).
Unlike Ranking Intelligence (see companion note), none of this Sonar/CCC code is wired into any FastAPI
router in `projects/geo_platform/backend/app/routers/` or included in `main.py` — grepping the router
directory for `ranking|sonar|citation_influence|factor_audit` only matches `client.py` and
`sales_preview.py`, and both only reference the Ranking Intelligence panel, never Sonar/CCC. So "PARTIAL"
in the build reports is accurate in the sense that mattered most (offline logic + tests exist, but no
live surface) — the checklist's error is not that it overstated remaining work, it's that it implied the
work queue was still at "spec drafting," when in fact a full round of implementation had already
happened and stalled at the offline-only stage. No commits touch these paths between 2026-08-03 and
today, and `SPEC_CCC_1_gap_detection.md` (the file the dashboard names as "next") was never created —
the fleet built the nine `SPEC_CCC_M<n>_*.md` files instead, under different naming.

## Links
- specs/SPEC_CCC_MASTER.md
- reports/CCC_M1_INGESTION_BUILD_REPORT.md through reports/CCC_M9_ADMIN_BUILD_REPORT.md
- reports/M7_AGENT_GATES_BUILD_REPORT.md
- docs/AI_SEARCH_EDGE_GAME_PLAN.md
- docs/ANIRAK_ROADMAP.md (M11 section, describes the CCC build queue)
