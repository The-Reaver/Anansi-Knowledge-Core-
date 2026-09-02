---
id: 2026-08-21-postgres-pgvector-provisioning-built-and-live-rls-not-confirmed
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [postgres, pgvector, supabase, knowledge-core, rls, security, checklist-staleness]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn establishing that the pgvector store named as untouched backlog is actually live and populated, with no RLS statements found in the table SQL."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Older backlog (SafeGuard Identity booking, AI clinical scribe research, Fleet Dashboard release-to-Orlok, external fix-corpus scoping, Postgres/pgvector provisioning, Lords of Cian Archive + NYC Marketplace Lovable builds)\""
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
- confidence: high on the build/live-data claim (code and dev-log read directly); medium on the RLS gap (absence of evidence in the code and dev log, not a positive confirmation that RLS is off)
- verified: 2026-08-21
- REVIEW: high-impact

# The "Postgres and pgvector provisioning decision," named as untouched backlog on 2026-08-03, is now real, tested, production code with real note data in it -- and the operator's own ratified RLS requirement for that table has no confirmed evidence of being met

## Body

reports/STAG_MASTER_CHECKLIST_2026-08-03.md lists "The Postgres and pgvector provisioning decision" under "Older backlog, not touched this session." research/knowledge-home/notes/2026-08-08-cheap-cloud-supabase-decision.md (ratified 2026-08-09) confirms that as of 2026-08-08 the choice (Supabase pgvector, table `kc_note_vectors` at vector(768)) was "a decision, not a live system: nothing has been stood up yet," and explicitly conditions any write on the table having "row-level security enabled and a policy restricting access to the service role only."

By 2026-08-16 it was stood up for real. research/knowledge-home/notes/2026-08-16-knowledge-core-vector-store-never-persisted-note-content-only-embeddings.md documents building `PgNoteStore` (`kc_notes` table) alongside the existing `PgVectorStore` (`kc_note_vectors`), wired through a new `graph_store_from_env()` factory, "proven with a real write-in-one-process, read-in-a-fresh-process round trip against the live Supabase Postgres." The code exists on disk today at projects/geo_platform/knowledge_core/graph/store/{pg_vector_store.py, pg_note_store.py, graph_store.py, factory.py} with a real integration test (tests/test_kc_foundation_pg_note_store_integration.py). projects/geo_platform/GEO_DEVELOPMENT_LOG.md's 2026-08-17 entry confirms this isn't a sandbox toy: querying the live Supabase project's real schema via the Railway service-role key found exactly four tables already provisioned -- `kc_notes`, `kc_note_vectors`, `capability_ledger`, `ledger_reuse_events` -- and an earlier entry (~line 956) describes cleaning up 189 real notes down to 90 uniques directly in `kc_notes`/`kc_note_vectors` on the live database. So the "provisioning decision" claim is stale by more than a decision -- it is stale by a fully built, live, populated data store.

What was not found: any RLS enablement or policy SQL for either `kc_notes` or `kc_note_vectors` anywhere in the four store files, the migration/schema SQL embedded in those files (`CREATE_TABLE_SQL` in both pg_note_store.py and pg_vector_store.py creates plain tables with no `ENABLE ROW LEVEL SECURITY` or `CREATE POLICY` statements), or in GEO_DEVELOPMENT_LOG.md's extensive 2026-08-17 RLS work (which rebuilds RLS policies and `EXPECTED_TABLES`/policy-name assertions for the 16-table GEO Suite schema -- `clients_select`, `clients_update`, etc. -- but does not mention `kc_notes` or `kc_note_vectors` by name in that pass). This is an absence-of-evidence finding, not a positive confirmation the tables are unprotected -- RLS could have been applied by hand in the Supabase dashboard, outside any file this sweep can see. But the 2026-08-08 decision note's own explicit precondition ("must have row-level security enabled... before any note is written to it") appears to have been bypassed in practice: notes were already being written, cleaned up, and re-verified against this live table by 2026-08-16, without any file-level trace of the RLS step the ratified decision required first.

## Links
- corrects: the 2026-08-03 master-checklist claim for workstream "Older backlog" (Postgres/pgvector provisioning item)
- see also: research/knowledge-home/notes/2026-08-08-cheap-cloud-supabase-decision.md (the RLS precondition), research/knowledge-home/notes/2026-08-16-knowledge-core-vector-store-never-persisted-note-content-only-embeddings.md (the build), projects/geo_platform/knowledge_core/graph/store/pg_vector_store.py, projects/geo_platform/knowledge_core/graph/store/pg_note_store.py
