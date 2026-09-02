---
id: 2026-08-20-promotion-script-missed-status-field-caught-by-full-sweep
type: correction
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 9/10 on the promotion rubric (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Directly self-caught this session via a deliberate full sweep. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, methodology, self-critique]
sources:
  - ref: "This session's own review, verification, and gate-closure work, 2026-08-20"
    reliability: high
    origin: "direct observation and verification, this session"
provenance:
  archive: research/knowledge-home/raw/2026-08-20-anansi-candidate-promotion-and-gate-closure-session.jsonl
  turns: [1, 20]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A promotion script correctly replaced a stale placeholder line but missed updating a related status field on the same two notes, caught only by a deliberate full sweep after the fact, not by reviewing the script's logic beforehand

## Body

During this review session, a script used to promote two candidate notes that already carried a stale placeholder ratification line correctly replaced that placeholder with a real ratified line documenting the actual verification performed, but the same script failed to also update those two notes' separate status field from candidate to ratified. This was not caught by reviewing the script's logic beforehand; it was only found afterward by a deliberate full sweep checking every single file touched during the session for the literal stale field values. The general lesson is that a bulk-edit script's actual output should be independently swept and verified after running, not just its logic reviewed before running.

## Links
(none)
