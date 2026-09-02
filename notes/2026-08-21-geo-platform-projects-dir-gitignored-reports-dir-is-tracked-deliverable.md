---
id: 2026-08-21-geo-platform-projects-dir-gitignored-reports-dir-is-tracked-deliverable
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, repo-structure, git, gitignore, geo-platform]
sources:
  - ref: "Turns 78-81 show the agent running git status/diff and concluding 'projects/ is gitignored... the report in reports/ is the tracked deliverable', restated in the final report at turn 86."
    reliability: high
    origin: "STAG session, 2026-07-22, \"GEO days 3-5 audit engine\" (backfilled from historical transcript d4e8f900, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-22-backfill-d4e8f900.jsonl
  turns: [78, 86]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: medium, the agent asserts this directly after checking git status/diff, but the raw command output was stripped from this transcript so it isn't independently re-verifiable from this source alone
- verified: 2026-08-21

# In the stag repo, projects/geo_platform application code is gitignored and untracked; reports/ is the tracked deliverable directory

## Body
While preparing to commit the days 3-5 audit-engine work, the agent checked git status and found that `projects/` is gitignored in the stag repo, meaning the GEO platform's actual application code (rubric.py, audit_engine.py, the test fixtures, the new test file) is untracked by git — matching the same setup already observed during the earlier D1 build. Only `reports/` is the tracked deliverable directory; that's why the agent's committed output for this session was `reports/GEO_D3_BUILD_REPORT.md` rather than the code itself. Anyone picking up GEO platform work from git history alone will not see the actual `projects/geo_platform` source in commits — it has to be located on disk directly. This is a structural fact about how the repo is currently configured, not a judgment on whether it's the right setup.

## Links
- related-to, 2026-08-21-geo-d3-audit-engine-real-implementation-replaces-always-95-stub.md, the build session where this repo-structure fact was surfaced.
