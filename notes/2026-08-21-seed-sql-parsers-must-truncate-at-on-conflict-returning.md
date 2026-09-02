---
id: 2026-08-21-seed-sql-parsers-must-truncate-at-on-conflict-returning
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [meta_agent, sprint-a4, sql-parsing, false-positive, catalog-parity]
sources:
  - ref: |-
      Archive line 106: "Two false positives on Check 14 (metadata, slug) -- these are parser artifacts". Archive line 108: "slug -- the seed's on conflict (slug) do nothing clause; my VALUES extractor grabbed the (slug) paren group. metadata -- slug = (price.get('metadata') or {}).get(...) at stripe_prices.py:249; my list regex treated a parenthesized expression named slug as a literal collection. Let me fix both -- truncate VALUES at on conflict/returning, and require list sources to be pure string-literal collections."
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [106, 108]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A catalog-parity gate's SQL VALUES-clause parser produced false positives by picking up column names inside ON CONFLICT / parenthesized expressions as if they were catalog data

- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- class: confirmed
- source: STAG session, 2026-07-18, "A2 provisioning environment gates" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: medium — specific to one gate's regex-based extraction approach, useful mainly as a pattern for anyone parsing SQL seed files with regex rather than a real SQL parser
- verified: 2026-08-21

## Body

Sprint A4's Check 14 (catalog-parity gate) collects tool-catalog members from an `insert into tools ... values (...)` seed statement using a regex-based VALUES extractor. Against the real reconciled project it produced two false positives: `slug`, pulled from the seed's `on conflict (slug) do nothing` clause (the extractor's paren-group match wasn't scoped to stop at `ON CONFLICT`), and `metadata`, pulled from an unrelated parenthesized Python expression (`slug = (price.get("metadata") or {}).get(...)`) that a separate list-heuristic mistook for a literal string collection.

Fix: truncate VALUES extraction at `on conflict` / `returning` clauses, and require list-source heuristics to match only pure string-literal collections, not arbitrary parenthesized expressions. General lesson for anyone regex-parsing SQL `INSERT ... VALUES` or `ON CONFLICT` statements for a static-analysis gate: the parser needs an explicit stop boundary at trailing clauses (`ON CONFLICT`, `RETURNING`, `WHERE`), or it will silently absorb unrelated identifiers from those clauses as if they were data values.

## Links
