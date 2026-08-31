---
id: 2026-08-06-ci-knowledge-core-maintenance-roles-and-three-new-agent-gaps
type: decision
status: ratified
source: "Cowork session, 2026-08-06; operator Abad overrode the \"attorney terms before any code\" gate and directed the slice-by-slice build of the lawyer-facing CI tool to start now (source status: active); mined from candidates/2026-08-25/2026-08-06-ci-lawyer-tool-build-roadmap-and-gate-override.md"
project: ci
tags: [ci, knowledge-core, maintenance, agent-roles, mandate-7]
supersedes: []
superseded_by: null
---

# CI's Knowledge Core maintenance roadmap enumerates twelve recurring jobs; nine map to existing roles, three need new agents not yet created

## Body

Existing roles cover most of the twelve recurring maintenance jobs: Oluwole (source re-verification, feed ingestion health, the correction queue including the severity lane), Jeremy (version bumping, retraction, dedup, version-chain integrity), Jasiah (reviewer sign-off audit), Omar (backup infrastructure), Amadeus (verification). Three functions have no standing owner and need new maintenance agents to be created: an Embedding and Index Steward (re-embedding and re-indexing), a Blind-Sample and False-Negative Monitor (weekly zero-finding sampling and the false-negative rate), and a KB Integrity Monitor for continuous query-boundary conformance. Each new agent needs a proving artifact before its skill card claims the capability, per Mandate 7.

## Links

- relates: 2026-08-06-ci-lawyer-tool-build-layer-order
- relates: 2026-08-06-no-new-agent-without-a-real-defined-job
