---
id: 2026-08-07-embedding-dimension-locked-nomic-768-cpu
type: note
status: ratified
source: "operator confirmed the Anansi host is a Dell Inspiron 14 5410, Intel Iris Xe integrated graphics, no dedicated GPU (source status: decided by operator host confirmation, 2026-08-07)"
project: fleet
tags: []
---

# Locked: embedding model Nomic-embed-text-v1.5 at 768 dimensions (CPU host)

## Body

The Anansi host is CPU-only (Intel Iris Xe is integrated graphics, dedicated GPU memory zero). Per the ratified I5 decision, the embedding model is Nomic-embed-text-v1.5, pinned at 768 dimensions, Apache 2.0, sub-10ms CPU inference, 8192-token context. The pgvector kc_note_vectors table must be created at vector(768), not the code's current 1536 default, so the dimension is set before any note is embedded. A local nDCG@10 plus latency benchmark on Anansi's own queries still confirms the pick before full corpus ingest (I5), and the model must be verified to run fully offline with no telemetry (I5, TYR). This closes Gate C2 of the Phase 0 runbook.

## Links

- 2026-08-07-embedding-model-decision-meta-analysis-hub
- 2026-08-07-brain-trust-decision-record-cycle-1
