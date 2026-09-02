---
id: 2026-08-21-duplicate-helpers-over-modifying-tested-existing-gate
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [meta_agent, spec-interpretation, sprint-a5, code-reuse, regression-safety]
sources:
  - ref: |-
      Archive line 129: the agent notes Check 12 defines its helpers (_norm_path, _match) inside its own conditional block, that section 7 of the spec forbids changing any existing gate, and resolves the conflict by defining "the shared helpers for my two new gates in a prelude right after section 12 (leaving section 12 untouched), and reuse them across both."
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [127, 129]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# When a spec asks to reuse an existing gate's helper functions but also forbids modifying that gate, duplicate the helper logic into the new gate rather than touching the tested existing code

- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- class: confirmed
- source: STAG session, 2026-07-18, "A2 provisioning environment gates" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: medium — a single reasoned instance (Sprint A5), not re-verified as a repeated pattern across other conflicts
- verified: 2026-08-21

## Body

Spec A5 (the nav-target and dependency-route gates in `meta_agent.py`) asked the new gates to reuse Check 12's helper functions (`_norm_path`, `_match`) for consistency. But those helpers were defined inside Check 12's own conditional block, and the same spec's section 7 forbade changing any existing gate. These two instructions conflict whenever the reusable code lives inside the gate you're forbidden to touch.

The resolution taken: hold the harder constraint (never modify a gate already shipped and tested) and give the new gates their own self-contained copies of the helper logic, rather than refactoring Check 12 to expose shared helpers. Regression tests confirmed Check 12's behavior was unaffected. General principle for future conflicts of this shape: prefer duplicating a small amount of logic over touching code that already has test coverage and is live, unless the operator explicitly asks for a refactor.

## Links
