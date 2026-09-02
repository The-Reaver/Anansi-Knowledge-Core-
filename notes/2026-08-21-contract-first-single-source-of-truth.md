---
id: 2026-08-21-contract-first-single-source-of-truth
type: decision
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, meta-lesson, contract-drift, single-source-of-truth, validation]
sources:
  - ref: "Archive turn 459: the delivered STAG_LIFECYCLE_AND_HARDENING.md summary states '§6 — the one rule: contract-first, single-source — .env.example is generated from config.py, the frontend is checked against the OpenAPI, seeds are checked against enums,' the direct source of this note's rule"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [459, 459]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# For every shared seam in a generated system, exactly one file should be the source of truth and a machine gate should prove every consumer matches it
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the stated operating rule and concrete examples match the session's own writeup and the fixes actually made. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — stated as the operating rule the session's diagnostic writeup (STAG_LIFECYCLE_AND_HARDENING.md) converged on, and it directly matches the fixes actually made
- verified: 2026-08-21
## Body
The general fix adopted for the class of contract-drift bugs found this session (database schema, HTTP API surface, environment-variable set, domain/tool catalog) is: designate exactly one file as the source of truth for each seam, and add a machine-checked gate that proves every consumer actually matches it, rather than hand-maintaining the same information in two or more places. Concretely: the backend's `config.py` module is the source of truth for environment variables, and `.env.example` should be validated against it (not hand-edited independently); the backend's own generated OpenAPI schema is the source of truth for the HTTP API surface, and the frontend's fetch calls should be diffed against it; the API's enum is the source of truth for a domain catalog (like the six tool slugs), and seed data plus price-lookup maps should be checked against the enum, not defined separately. No seam should be maintained by hand in two independently-edited places, because hand-maintained duplicates drift apart over time with no signal until something breaks at runtime or deploy time.
REVIEW: high-impact
## Links
- related, 2026-08-21-contract-drift-single-root-cause.md, the failure pattern this principle is the fix for
- related, 2026-08-21-env-example-drifts-from-config-source-of-truth.md, a concrete instance of this principle applied to environment variables
