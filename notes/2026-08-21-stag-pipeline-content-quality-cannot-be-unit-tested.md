---
id: 2026-08-21-stag-pipeline-content-quality-cannot-be-unit-tested
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [meta_agent, stag-pipeline, testing-strategy, methodology]
sources:
  - ref: |-
      Archive lines 190, 216, 274, 299, 384: the closing line of each sprint's completion summary (B1, B2, C1, C2, D1) repeats the same deferral, e.g. line 190 "Content quality on a real seed is deferred to the operator-run GEO dry-run (paid), per the spec", line 274/299 "Screen-content quality on a real seed remains the deferred, operator-run GEO dry-run", line 384 "ERD quality on a real seed remains the deferred, operator-run GEO dry-run".
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [190, 384]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Passing unit tests on the STAG build pipeline's generated-doc renderers proves structure and wiring, not content quality — that's explicitly deferred to a real, operator-run dry-run

- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- class: confirmed
- source: STAG session, 2026-07-18, "A2 provisioning environment gates" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: medium — consistent, repeated stance taken across many sprints in this session (B1 through D4), not a single one-off statement
- verified: 2026-08-21

## Body

Across Sprint B (Define/backlog), Sprint C (design system, wireframes, hi-fi mockups), and Sprint D (architecture) of the STAG build pipeline in `meta_agent.py`, the consistent stance was: unit tests (FakeRunner-based, no real model calls) can verify that a stage's pure renderers produce structurally correct output, never-clobber files correctly, and wire coverage/traceability checks correctly — but they cannot verify whether the actual generated content (a PRD's requirements, a wireframe's screen layout, a design system's visual choices) is good. Every sprint's completion summary explicitly named this gap and deferred it to "the deferred, operator-run GEO dry-run" rather than treating passing unit tests as proof the pipeline produces usable output.

This is a durable methodological stance for this pipeline specifically: test suites gate structural correctness and regression safety on every merge; a real end-to-end dry-run against a real seed project is the only check that gates content quality, and it is intentionally out of scope for automated CI-style verification.

## Links
- extends, 2026-08-21-llm-generated-json-artifacts-need-shape-coercion-and-fallback.md, the D5 hardening fixes were what a real dry-run (not unit tests) actually caught.
