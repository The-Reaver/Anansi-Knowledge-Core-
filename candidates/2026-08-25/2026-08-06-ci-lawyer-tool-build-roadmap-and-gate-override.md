---
id: 2026-08-06-ci-lawyer-tool-build-roadmap-and-gate-override
type: decision
status: candidate
source: "Cowork session, 2026-08-06; operator Abad overrode the \"attorney terms before any code\" gate and directed the slice-by-slice build of the lawyer-facing CI tool to start now (source status: active)"
project: ci
tags: [compliance-intelligence, ci, regulatory-pipeline, attorney-partnership, build-roadmap, gate-override, knowledge-core, maintenance-agents, handoff, operator-contribution]
supersedes: []
superseded_by: null
---

# CI Lawyer-Tool Build Roadmap and Operator Gate Override

## Body

On 2026-08-06 the operator overrode the gate that held the atom-versioning build behind condition 1. The build starts now, slice by slice, in parallel with the legal track. This note supersedes the do-not-build stance in 2026-08-06-ci-regulatory-pipeline-next-target-attorney-terms-first.

The full plan lives in the repo at reports/CI_LAWYER_TOOL_BUILD_ROADMAP_2026-08-06.md. A new chat with no memory of the originating session reads that file first, then starts Slice 0.1 (verify and baseline) before building anything. Route each slice to its named owner under Mandate 3.

The one boundary that still holds is the client-facing gate. Nothing the tool produces reaches the partner attorney as working product, and nothing reaches any of his clients, until three things are true: condition 1 (written attorney terms, drafted in reports/CI_ATTORNEY_PARTNERSHIP_TERMS_DRAFT_2026-08-06.md, finalized by outside counsel and signed), condition 5 (a professional-conduct read by an outside lawyer who is not the partner attorney), and the Layer 2 red-then-green proof green. Everything below that gate is internal build work and runs now.

Build order in the roadmap: Layer 0 foundation is the atom-versioning schema with the full field set (version, effective_start and effective_end, source_document_id, superseded_by, authority_type, jurisdiction, status, last_verified_date, reviewer_id and review_timestamp and review_decision) plus an audit_citation link table, then label enforcement at render. Nothing else starts until the schema exists. Layer 1 is the lawyer review surface built on the existing CI UI shell: per-finding confirm, correct, or out-of-scope with an active source-verified affirmation, a return loop, and a severity lane. Layer 2 is correction integrity: blind sampling of zero-finding pages and the red-then-green proof. Layer 3 is one verified live feed, Federal Register then eCFR then the instrument state machine, pull-only. Layer 4 is Knowledge Core integration with the query-boundary contract landing before any second tool queries the base. Layer 5 is court and state coverage, budgeted separately.

Completion estimate, fleet build-time with operator sign-offs between layers: a lawyer-usable, corrections-capable, provably-labeled internal tool in about 2.5 to 3 weeks, then live feed and Knowledge Core integration in about another 2 to 3 weeks. These are build estimates, not calendar guarantees, and the legal track runs on the operator and outside-counsel timeline.

Knowledge Core maintenance and new agents: the roadmap enumerates twelve recurring maintenance jobs that keep the Core true and assigns owners. Existing roles cover most of them: Oluwole for source re-verification, feed ingestion health, and the correction queue including the severity lane, Jeremy for version bumping, retraction, dedup, and version-chain integrity, Jasiah for the reviewer sign-off audit, Omar for backup infrastructure, Amadeus for verification. Three functions have no standing owner and need new maintenance agents to be created: an Embedding and Index Steward (re-embedding and re-indexing), a Blind-Sample and False-Negative Monitor (weekly zero-finding sampling and the false-negative rate), and a KB Integrity Monitor for continuous query-boundary conformance. Each new agent needs a proving artifact before its skill card claims the capability, per Mandate 7.

Augustin's own independently-generated response to Augustin_CI_Regulatory_Pipeline_Dispatch_2026-08-05.md had still not landed as of 2026-08-06, checked across Augustin_DEV_Findings, the repo root, and reports.

## Links

- supersedes: 2026-08-06-ci-regulatory-pipeline-next-target-attorney-terms-first
- derived-from: 2026-08-06-ci-regulatory-pipeline-opus-review-and-schema-spec
- relates-to: 2026-08-05-knowledge-core-benefits-and-honest-risk-reference
