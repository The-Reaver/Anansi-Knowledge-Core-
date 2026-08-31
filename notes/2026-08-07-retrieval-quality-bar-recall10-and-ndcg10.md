---
id: 2026-08-07-retrieval-quality-bar-recall10-and-ndcg10
type: spec
status: ratified
source: "Google Drive inbox capture, source chat not recorded in original note (source status: pinned Anansi note, answering whether proven formulas exist beyond Wilson); mined from candidates/2026-08-25/2026-08-07-quality-and-performance-formulas.md"
project: fleet
tags: [formulas, retrieval, recall, ndcg, embedding-model]
supersedes: []
superseded_by: null
---

# Retrieval quality bar: Recall@10 >= 0.90, nDCG@10 >= 0.80 against a fixed eval set of query/expected-note pairs

## Body

Run against a fixed eval set of query-and-expected-note pairs; also compute Precision@k, F1 = 2PR/(P+R), MRR, and MAP. This is also how the local embedding-model choice gets defended: pick the model that wins on this fixed set. The benchmark subsystem already computes recall.

## Links

- relates: 2026-08-07-embedding-dimension-locked-nomic-768-cpu
