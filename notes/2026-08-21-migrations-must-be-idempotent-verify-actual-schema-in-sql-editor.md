---
id: 2026-08-21-migrations-must-be-idempotent-verify-actual-schema-in-sql-editor
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, supabase, migrations, idempotency, verification]
sources:
  - ref: "Archive turns 383-395: `supabase db push` reports 'Remote database is up to date' even though the jobs-table fix never actually applied; the agent has the operator run a direct SQL query in Supabase's SQL Editor against information_schema.columns and supabase_migrations.schema_migrations, and the returned CSV at turn 395 confirms the real, reconciled schema"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [383, 395]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# `supabase db push` records each applied migration individually, so a partially-applied migration can leave the schema stuck between two states, only detectable by querying the real schema
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the CLI-vs-live-schema discrepancy and its resolution via a direct SQL query are directly traceable to the incident described in the archive. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly observed: a failed migration got recorded as applied via CLI "up to date," and only a live query of information_schema and supabase_migrations.schema_migrations revealed the true (fixed) state
- verified: 2026-08-21
## Body
`supabase db push` applies migrations one at a time and records each as it goes; a migration that errors mid-statement (as happened with an index creation on a column that didn't exist yet in this session) is not recorded, so a re-run resumes at that failure point. But the CLI can also report "up to date" for a migration whose fix was in fact applied and recorded, without the operator or agent being able to trust that assumption from the CLI output alone — the only way to be certain was to run a direct SQL query against `information_schema.columns` and `supabase_migrations.schema_migrations` in the Supabase SQL Editor and compare the actual column list to what the code expects. Because of this, migrations intended to reconcile an existing table's shape should be written idempotently (`create table if not exists`, guarded `alter table ... rename column` wrapped in existence checks, `drop policy if exists` before `create policy`), and after any `db push`, the real schema and seed data should be verified with a live query rather than assumed correct from CLI output.
REVIEW: high-impact
## Links
- related, 2026-08-21-jobs-table-column-drift-two-competing-migrations.md, the specific incident that motivated this finding
