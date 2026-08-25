---
id: 2026-08-05-capability-ledger-live-tested-on-supabase
type: finding
status: ratified
source: this chat, 2026-08-05, Abad asked for a thorough announcement of Knowledge Core's real state and business benefit (source status: active); mined from candidates/2026-08-25/2026-08-05-knowledge-core-benefits-and-honest-risk-reference.md
project: fleet
tags: [knowledge-core, capability-ledger, supabase, pgvector, testing]
---

# The capability ledger runs on live Supabase infrastructure, tested end to end at the database layer

## Body

The capability ledger lives on the operator's existing Supabase project (organization "Anansi Knowledge Core", project ref fhkapmsxovnbvrproapz — the same project GEO's own database already uses). Two tables hold the ledger, pgvector and pgcrypto are enabled, and a matching function lets a caller search by meaning rather than exact keyword. This was tested directly against the live database: a fabricated reference is rejected before a write happens, a real reuse event succeeds, and deleting a still-referenced entry is blocked — all three confirmed with real test rows, then removed, ending at zero rows. Row-level security stays on by default, closing off every access path except the app's own authenticated service role.

## Links

- relates: 2026-08-07-embedding-dimension-locked-nomic-768-cpu
- relates: 2026-08-04-interim-note-schema-maps-to-future-ledger-columns
