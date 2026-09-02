---
id: 2026-08-21-knowledge-core-default-embedding-is-free-nonsemantic-placeholder
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, knowledge-core, embeddings, cost, technical-debt]
sources:
  - ref: "Turns 286-342: turn 286 is the operator asking for durable Knowledge Core storage, turn 342 is the agent's finding that the default embedding client (LocalHashEmbedding) is a free, non-semantic placeholder and real search quality needs a paid OPENAI_API_KEY, deferred out of scope."
    reliability: high
    origin: "STAG session, 2026-08-14, \"GEO Suite completion\" (backfilled from historical transcript b9b0acfa, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-14-backfill-b9b0acfa.jsonl
  turns: [286, 342]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The Knowledge Core's default embedding client (LocalHashEmbedding) is a free, deterministic stand-in that proves the storage pipeline works but is not semantically meaningful — real search quality needs a paid OPENAI_API_KEY, deferred out of this session's demo-prep scope
- id: 2026-08-21-knowledge-core-default-embedding-is-free-nonsemantic-placeholder
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-14, "GEO Suite completion" (backfilled from historical transcript b9b0acfa, 2026-08-21)
- confidence: high — direct code inspection reported by the agent while building durable note-content persistence, same session
- verified: 2026-08-21
- tags: geo, knowledge-core, embeddings, cost, technical-debt
- REVIEW: high-impact

## Body
While building durable storage for the Knowledge Core (persisting note content in Postgres, not just embedding vectors), the agent found that the system's default embedding client is `LocalHashEmbedding` — a free, deterministic stand-in good enough to prove the ingestion/storage/retrieval pipeline actually works end to end, but not semantically meaningful for real search or similarity ranking. Genuine search quality would require switching to a real embedding provider via `OPENAI_API_KEY`, which is cheap and usage-based but was deliberately not bundled into this session's work, matching the pattern of deferring paid services until after the demo proves the pipeline functions. This means any Knowledge Core semantic-search or relevance-ranking behavior observed before `OPENAI_API_KEY` is configured should not be trusted as representative of real search quality — it is running on the placeholder embedding, not the real one.

## Links
- relates, 2026-08-16-knowledge-core-vector-store-never-persisted-note-content-only-embeddings.md, the same durable-storage build this embedding-quality gap was discovered during.
- relates, 2026-08-21-geo-demo-proof-path-needs-zero-new-paid-services.md, the same cost-deferral pattern applied to a different subsystem.
