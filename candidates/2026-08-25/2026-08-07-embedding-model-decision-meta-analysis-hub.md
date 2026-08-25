---
id: 2026-08-07-embedding-model-decision-meta-analysis-hub
type: note
status: candidate
source: two deep-research reports (one that retrieved live data, one that could not), reconciled 2026-08-07 (source status: hub note, candidates held, staged for Brain Trust vote, Celestina leads)
project: fleet
tags: []
---

# Embedding-model decision: two-tool meta-analysis, staged for the docket

## Body

Two independent deep-research tools were run on the local-embedding-model question. They converge on the same shortlist and the same testing order; the tool that could reach the web confirms the numbers and licenses the other left open. This substantially resolves the embedding-model decision that had blocked the Anansi and CIPPE stack, pending one local benchmark.

Provisional decision. CPU-only host: Nomic-embed-text-v1.5 (137M, 62.3 MTEB, 768 dims, 8,192 context, Apache 2.0, sub-10ms CPU). GPU host: BGE-large-en-v1.5 (335M, 63.6 MTEB, 1,024 dims, MIT, 512-token context) as the balanced pick, or Qwen3-Embedding-8B (70.58 MTEB, needs GPU) for top quality. Jina-v3 is disqualified by its non-commercial CC-BY-NC license. BGE, Nomic, and Qwen3 support Matryoshka truncation to keep the store small.

Not locked. Both tools require a local benchmark on Anansi's own retrieval queries (nDCG@10, p50 and p95 latency, RAM, index size, license fit) before final selection, and hardware and quantization effects must be measured on the target machine. The host being CPU-only or GPU is the fork that decides Nomic versus BGE. Full reconciliation and merged candidate notes are held for approval; this decision is on the Brain Trust docket with Celestina's seat leading.

## Links

- 2026-08-07-open-gap-legacy-formulas-and-z-method
- 2026-08-07-quality-and-performance-formulas
- 2026-08-07-pkm-meta-analysis-reconciled-hub
