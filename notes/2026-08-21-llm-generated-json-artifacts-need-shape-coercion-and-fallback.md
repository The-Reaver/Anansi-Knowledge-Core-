---
id: 2026-08-21-llm-generated-json-artifacts-need-shape-coercion-and-fallback
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [meta_agent, stage_architect, stage_plan, llm-output-robustness, geo_platform]
sources:
  - ref: |-
      Archive lines 480-527 (Sprint D5): the agent implements the G1 fix ("stage_architect's ERD generation is now truncation-robust... failure = falsy or empty entities list... deterministic fallback to _standing_geo_entities()... fails loud: _render_data_model(obj, fallback=) renders a WARNING banner... erd_fallback_used") and the G3 fix ("new _as_obj(x) coerces a generated artifact to a dict; routed through every .get on a generated artifact in stage_plan... stage_architect... stage_backlog, and stage_design"), both hardening fixes from the first real GEO dry-run retro.
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [480, 527]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Model-generated JSON artifacts in the STAG build pipeline (ERD, routes, PRD/SRS/backlog) can arrive truncated, empty, or shaped as a list instead of a dict, and every downstream .get() on them needs defensive handling

- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- class: confirmed
- source: STAG session, 2026-07-18, "A2 provisioning environment gates" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: high — both failure modes (empty ERD, list-shaped PRD) were reproduced from a real GEO dry-run retro and fixed with tests proving the fix (Sprint D5, gaps G1 and G3)
- verified: 2026-08-21

## Body

A real GEO dry-run of the STAG build pipeline (interview -> define -> backlog -> design -> architect -> plan) surfaced two related classes of bug in how the pipeline consumes its own model-generated JSON artifacts:

1. **Empty/truncated generation (G1).** The ERD-generation model call in `stage_architect` could return a falsy or empty `entities` list without raising an exception, silently producing an empty data model that broke everything downstream (route-entity coverage, OpenAPI `$ref` targets).
2. **Wrong top-level shape (G3).** Code across `stage_plan`, `stage_architect`, `stage_backlog`, and `stage_design` called `.get()` directly on generated artifacts (PRD, SRS, backlog, data model) assuming they were always dicts. When a model returned a list-shaped artifact instead, this crashed the pipeline at the first `.get()` call.

The fix pattern, not just the specific bugs: (a) treat "falsy or empty" as the failure condition for a generated collection, not just "raised an exception"; (b) on repeated failure, fall back to deterministic default data (`_standing_geo_entities()`) rather than propagating an empty artifact, and mark the fallback visibly (a WARNING banner in the rendered doc, a `_fallback_used` flag in the return dict, a console line) so a fallback never masquerades as a real generation; (c) wrap every `.get()` on a model-generated artifact in a shape-coercion helper (`_as_obj`) that normalizes to a dict before use. This is a general pattern for any pipeline stage that consumes JSON produced by a model call rather than by deterministic code.

## Links
- extends, 2026-08-21-run-gate-battery-against-throwaway-copy-not-live-tree.md, both were hardening responses to real failures found by actually running the pipeline/gates rather than assuming code correctness from passing unit tests.
