---
id: 2026-08-21-spec-lead-scoring-was-already-built-when-the-checklist-called-it-not-built
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [hbot, geo, sales, lead-scoring, checklist-drift, gitignore]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn establishing that lead_scorer.py and its test suite already existed and passed before the checklist called SPEC_LEAD_SCORING not-yet-built."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"HBOT go-to-market\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [226, 229]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — files read directly, test suite executed live during this sweep (16/16 passed), build report and commit dates cross-checked
- verified: 2026-08-21

# SPEC_LEAD_SCORING's deliverables exist, pass 16/16 tests, and predate the 2026-08-03 checklist that called the spec "not yet built"

## Body
The 2026-08-03 master checklist stated "SPEC_LEAD_SCORING not yet built" for the HBOT go-to-market
workstream. This sweep found `projects/geo_platform/backend/app/services/sales/lead_scorer.py` and
`projects/geo_platform/tests/test_lead_scorer.py` already exist and are substantive: `score_lead` and
`rank_leads` are implemented per spec (hospital hard-filter, fit/opportunity/priority formulas,
Excel-style rounding, documented off-label term lists), and running the standalone test file live
during this sweep produced 16/16 passed (the in-repo `reports/LEAD_SCORING_BUILD_REPORT.md` records
15/15 as of its writing — one test was added since). A `POST /sales/rank-leads` read-only endpoint is
also wired per the report. More surprising than the build existing: the build report is dated
2026-07-26 and both `docs/HBOT_LEAD_RANKING.md` and `specs/SPEC_LEAD_SCORING.md` were committed
2026-07-27 — all before the 2026-08-03 checklist date. So the checklist's "not yet built" claim was
already stale on the day it was written, not just stale now. The likely mechanic: `projects/` is
gitignored in this repo (`.gitignore:12:projects/`), so `git log` shows nothing for these files even
though they exist on disk and were built — a checklist author relying on git history alone for this
path would miss real, already-complete work. The spec's own handoff gate is still FAIL (393 pre-existing
problems fleet-wide, per the build report), so this is not a "fully done, ship it" status — but the
core deliverable the checklist flagged as missing is not missing.

## Links
(none — points to specs/SPEC_LEAD_SCORING.md, reports/LEAD_SCORING_BUILD_REPORT.md, and
projects/geo_platform/backend/app/services/sales/lead_scorer.py directly, all in-repo)
