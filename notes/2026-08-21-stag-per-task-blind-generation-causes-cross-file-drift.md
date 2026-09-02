---
id: 2026-08-21-stag-per-task-blind-generation-causes-cross-file-drift
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [meta_agent, stag-build, code-generation, drift, manual-repair]
sources:
  - ref: "Turn 159's real bug-verification table and turn 300's explicit 'the exact same six patterns keep breaking' list (migration numbering, parallel folders, router wiring, column-name drift e.g. scheduled_drop_date/drop_at, enum drift e.g. PENDING_REMOVAL/PENDING_CANCEL, duplicate .env.example) match the note's six categories almost verbatim; turn 296 independently confirms the PENDING_CANCEL enum bug in the live code"
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [159, 300]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, each pattern was independently verified against the real generated code across tasks 2 through 7 of the same build
- verified: 2026-08-21
- REVIEW: high-impact

# meta_agent.py's task-by-task file generation, with no visibility into earlier tasks' output, produced the same six categories of cross-file drift on every task

## Body
Building the "Step 0 shared infrastructure" scaffold for the Small Business Tools platform (a FastAPI + Next.js + Supabase monorepo) with an early version of meta_agent.py, every one of the 13-14 build tasks generated its files with no awareness of what earlier tasks had already written, and the same six failure categories recurred on nearly every task, requiring manual (uncompensated) repair each time: (1) migration files invented their own numbering scheme instead of matching the project's established `YYYYMMDDHHMMSS_description.sql` convention, sometimes sorting to run before the schema they depended on; (2) tasks built parallel folder structures (e.g. `api/routes/` and `api/deps/`) duplicating existing ones (`routers/`, `core/`); (3) new routers were written but never wired into `main.py`, so the endpoints didn't exist at runtime; (4) column names drifted between a migration and the code reading it within the same task (e.g. migration `scheduled_drop_date` vs. code `drop_at`); (5) enum/status-string values drifted the same way within a single task (e.g. code referencing `PENDING_CANCEL` when the enum only defined `PENDING_REMOVAL`); (6) a fresh `.env.example` got written at the wrong location or with different key names each task, silently overwriting the comprehensive one from task 1. None of these were random — they recurred in the same shape every time because each task's generation call had zero context about the project's evolving conventions.

## Links
- causes, 2026-08-21-stag-into-context-start-at-flags-added-for-repair-builds.md, the flags added to point a run at an existing project and feed it real anchor context.
- causes, 2026-08-21-stag-convention-scanner-and-post-task-validator-added.md, the automated mitigation built for this exact failure class.
