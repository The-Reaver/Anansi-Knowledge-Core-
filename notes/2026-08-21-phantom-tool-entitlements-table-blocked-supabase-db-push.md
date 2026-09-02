---
id: 2026-08-21-phantom-tool-entitlements-table-blocked-supabase-db-push
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, supabase, migrations, phantom-table, entitlements]
sources:
  - ref: "Archive turn 266: 'No migration ever creates tool_entitlements ... 000600_tool_entitlements_rls.sql ... its own header says depends on 0006...which creates public.tool_entitlements — but that create migration was never written (000500 mistakenly alters entitlements instead). On a fresh supabase db push, Phase 2 dies here with relation public.tool_entitlements does not exist'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [266, 266]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A tool-toggle service and its RLS migration both referenced a `tool_entitlements` table that no migration ever actually created, breaking `supabase db push` on a fresh database
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — confirmed by reading tool_toggle_service.py, the migration chain, and the schema.sql definitions directly
- verified: 2026-08-21
## Body
In the `project_brief_step0_resolved` backend, `tool_toggle_service.py` set `ENTITLEMENTS_TABLE = "tool_entitlements"` and filtered/inserted on a `tool_slug` column, and a later migration (`20250101000600_tool_entitlements_rls.sql`) ran `alter table public.tool_entitlements ...` whose own header claimed a prior migration (`000500`) created that table — but `000500` actually altered the pre-existing `entitlements` table instead, so `tool_entitlements` was never created by any migration. On a fresh `supabase db push`, this made the `000600` migration fail with `relation "public.tool_entitlements" does not exist`, blocking Phase 2 of the deploy entirely. Every call through the frontend's `/api/tools/*` endpoints — the exact toggle path the app relies on — was silently failing at the DB layer for the same reason, independent of the migration-chain failure. The general lesson: a table referenced by application code or by an `alter`/`create policy`/`create index` statement in one migration must actually be created by some migration in the chain, or both the schema and the migration application will fail in ways that surface far from the actual root cause.
## Links
- related, 2026-08-21-entitlements-canonicalized-on-tool-id-over-tool-slug.md, the decision made to resolve this bug
- related, 2026-08-21-three-way-tool-catalog-slug-drift-enum-is-canonical.md, the related but distinct catalog-slug drift found in the same subsystem
