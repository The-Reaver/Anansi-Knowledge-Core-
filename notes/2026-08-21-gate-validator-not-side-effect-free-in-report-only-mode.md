---
id: 2026-08-21-gate-validator-not-side-effect-free-in-report-only-mode
type: finding
status: ratified
ratified: |-
  2026-08-21 — ratified by explicit operator instruction ("ratify the 92 that hold up"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification.
project: fleet
tags: [meta_agent, validator, gate-battery, tooling-risk, geo_platform, safety]
sources:
  - ref: |-
      Archive lines 620-621: "The validator auto-mutated main.py (it's not purely report-only) and corrupted it -- flag [1] shows an IndentationError... The validator's router-wiring auto-fix misfired -- the routers were already correctly wired (lines 6-7), and it injected two bad indented lines with undefined names."
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [620, 621]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# STAG's meta_agent.py gate validator is not side-effect-free even when run for reporting purposes — it can auto-mutate and corrupt live files

- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, fixed a wrong source date/session label (was misattributed to the "A2 provisioning environment gates" session; corrected to the "GEO Day 1-2 schema/auth build" session the events actually occurred in). This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-22, "GEO Day 1-2 schema/auth build" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: high — directly observed and reproduced in-session; the agent read the corrupted file, diagnosed the cause, and reverted it
- verified: 2026-08-21
- REVIEW: high-impact

## Body

During GEO Platform Day 1-2 work, the operator asked to run STAG's gate battery (the validator inside `meta_agent.py`, the same module extended across this whole session with the A2-A5/B/C/D/E gates) "in report-only mode" against the live `projects/geo_platform/` tree. The validator is not actually side-effect-free: on its first run it auto-mutated `backend/app/main.py` via a router-wiring auto-fix, and the auto-fix misfired — both routers were already correctly wired, but the fix injected two badly-indented lines referencing undefined names, producing an `IndentationError` that broke the file. The agent caught this only because it was watching for exactly that risk, diagnosed the corruption, and reverted the file with `Edit` before continuing.

Consequence: any future request to "run the gate battery" or "run the validator" against a real, live project tree should not be treated as guaranteed non-destructive just because the request framed it as a report or read-only check. The validator has real auto-fix side effects independent of how the invocation is described.

## Links
- prompts, 2026-08-21-run-gate-battery-against-throwaway-copy-not-live-tree.md, the operating fix adopted immediately after this corruption was discovered.
