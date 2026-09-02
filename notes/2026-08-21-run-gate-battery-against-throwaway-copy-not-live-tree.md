---
id: 2026-08-21-run-gate-battery-against-throwaway-copy-not-live-tree
type: decision
status: ratified
ratified: |-
  2026-08-21 — ratified by explicit operator instruction ("ratify the 92 that hold up"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification.
project: fleet
tags: [meta_agent, validator, gate-battery, operating-procedure, geo_platform]
sources:
  - ref: |-
      Archive line 624: after restoring the corrupted main.py, the agent states "The validator isn't truly report-only -- it mutated live files. To honor 'report-only,' I'll re-run it against a throwaway copy so the real project stays clean." Archive line 629: "The copy missed .env.example (bash * skips dotfiles)... Let me do one authoritative full-copy run (including dotfiles) to capture the complete finding set."
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [624, 629]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Run STAG's gate battery against a throwaway copy of the project, never the live tree, to get a true report-only finding list

- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, fixed a wrong source date/session label (was misattributed to the "A2 provisioning environment gates" session; corrected to the "GEO Day 1-2 schema/auth build" session the events actually occurred in). This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-22, "GEO Day 1-2 schema/auth build" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: high — adopted in-session immediately after the validator corrupted a live file and was reverted
- verified: 2026-08-21
- REVIEW: high-impact

## Body

After discovering that the gate validator in `meta_agent.py` auto-mutates files even when invoked to produce a "report-only" finding list (see the corruption finding this decision follows from), the working procedure adopted was: copy the target project to a throwaway location first (including dotfiles — a first attempt using a bare `*` glob silently skipped `.env.example` and undercounted findings), run the validator against the copy, and treat only that output as the authoritative finding list. The live project tree is left untouched by the validator entirely.

This is the standing procedure for any future "run the gate battery" or "run the validator" request against a real project: copy-then-run, not run-in-place, and make sure the copy step captures dotfiles.

## Links
- follows-from, 2026-08-21-gate-validator-not-side-effect-free-in-report-only-mode.md, the corruption incident that made this procedure necessary.
