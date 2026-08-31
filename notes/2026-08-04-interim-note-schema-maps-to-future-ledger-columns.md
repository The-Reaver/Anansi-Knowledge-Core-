---
id: 2026-08-04-interim-note-schema-maps-to-future-ledger-columns
type: decision
status: ratified
source: "this chat, 2026-08-04, Abad asked for the nine clarifying questions from the Brain Trust's Mandate 10 ruling to be answered and filed as a standing reference (source status: active); mined from candidates/2026-08-25/2026-08-04-blackfire-brain-trust-nine-questions-resolved.md"
project: fleet
tags: [knowledge-core, schema, ledger, migration, atomic-notes]
supersedes: []
superseded_by: null
---

# The markdown note schema (id/type/source/tags/Body/Links) is deliberately designed to map onto the future ledger's database columns

## Body

The interim markdown format used for atomic notes is not an arbitrary choice — it was chosen because it maps cleanly onto the capability ledger's real columns once deployed: `type` maps to `artifact_type`, `source` maps to `source_type` and `source_ref`, the Body maps to `lesson_summary`, and Links map to the reuse relationships. Notes written under this format now are not wasted work; a backfill script (Jeremy's `learning_log_ingest.py`) is built specifically to convert exactly this kind of markdown entry into ledger rows once the ledger is live.

## Links

- relates: 2026-08-04-mandate-9-compounding-assets-ratified
- relates: 2026-08-05-capability-ledger-live-tested-on-supabase
