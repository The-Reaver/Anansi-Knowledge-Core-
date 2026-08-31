---
id: 2026-08-06-ci-lawyer-tool-build-layer-order
type: spec
status: ratified
source: "Cowork session, 2026-08-06; operator Abad overrode the \"attorney terms before any code\" gate and directed the slice-by-slice build of the lawyer-facing CI tool to start now (source status: active); mined from candidates/2026-08-25/2026-08-06-ci-lawyer-tool-build-roadmap-and-gate-override.md"
project: ci
tags: [ci, build-order, layers, atom-versioning, knowledge-core]
supersedes: []
superseded_by: null
---

# CI lawyer-tool build order: Layer 0 schema, Layer 1 lawyer review surface, Layer 2 correction integrity, Layer 3 one verified live feed, Layer 4 Knowledge Core integration, Layer 5 court/state coverage

## Body

Layer 0: the atom-versioning schema (see the locked field-set note) and label enforcement at render. Layer 1: the lawyer review surface built on the existing CI UI shell — per-finding confirm/correct/out-of-scope with an active source-verified affirmation, a return loop, and a severity lane. Layer 2: correction integrity — blind sampling of zero-finding pages and the red-then-green proof. Layer 3: one verified live feed, Federal Register then eCFR then the instrument state machine, pull-only. Layer 4: Knowledge Core integration, with the query-boundary contract landing before any second tool queries the base. Layer 5: court and state coverage, budgeted separately. As estimated on 2026-08-06: roughly 2.5-3 weeks of fleet build-time to a lawyer-usable, corrections-capable, provably-labeled internal tool, then another 2-3 weeks for live feed and Knowledge Core integration — build estimates, not calendar guarantees; the legal track runs on the operator and outside-counsel timeline.

## Links

- extends: 2026-08-06-ci-atom-versioning-schema-locked-field-set
- relates: 2026-08-06-ci-client-facing-gate-three-conditions
