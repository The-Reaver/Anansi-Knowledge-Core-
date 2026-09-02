---
id: 2026-08-21-jobs-table-column-drift-two-competing-migrations
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, supabase, migrations, jobs-table, column-drift]
sources:
  - ref: "Archive turns 360-371: supabase db push fails with 'column run_at does not exist' because schema.sql created jobs with job_type/run_after while the 001000 migration's create-table-if-not-exists silently no-op'd; the agent then reads jobs_repo.py, poller.py, and admin_service.py and finds they disagree too (type/completed_at vs finished_at vs job_type)"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [360, 371]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A `jobs` table was created twice with disagreeing columns because a later `create table if not exists` migration silently no-op'd against an earlier table of the same name
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the exact error (`column "run_at" does not exist`) was reproduced live during `supabase db push`, and the fix was verified against a real query of the applied schema afterward
- verified: 2026-08-21
## Body
In `project_brief_step0_resolved`, the base schema migration (`20250101000000_schema.sql`) already created a `public.jobs` table using columns `job_type` and `run_after`, but a later migration (`20250101001000_create_jobs_table.sql`) used `create table if not exists jobs` expecting columns `run_at`, `type`, `result`, `claimed_at`, and `completed_at` — because the table already existed, that later `create table if not exists` was a silent no-op, leaving the old column names in place, and its subsequent `create index ... on public.jobs (run_at)` then failed with `column "run_at" does not exist`, killing `db push` partway through the chain. The authoritative column set was determined by reading the code that actually queries the table (`jobs_repo.py`'s read/write path), not either migration in isolation — even the application code itself disagreed in places (`poller.py` used `finished_at` as a kwarg name where the repo expected `completed_at`, and `admin_service.py` selected `job_type` where the real column was `type`). The migration was rewritten to reconcile the existing table to the code's real expectations via guarded column renames and `add column if not exists`, rather than assuming either migration's original definition was correct.
## Links
- related, 2026-08-21-migrations-must-be-idempotent-verify-actual-schema-in-sql-editor.md, the general lesson this incident produced
