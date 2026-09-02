---
id: 2026-08-20-raw-append-only-violation-two-files-open-item
type: question
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 5/10 on the promotion rubric (novelty 1, evidence 1, actionability 1, generality 0, non-contradiction 2). Observed as a side effect this session; not investigated further, genuinely open. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, adr-0005, raw-archive]
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

# A separate, pre-existing append-only violation on two raw archive files was noticed as a side effect of this session's gate investigation and left open, uninvestigated

## Body

A gate check enforcing that the Knowledge Core's raw transcript archive files may only ever be appended to, never edited or shortened once committed, was found failing for two specific archive files during this review: one from 2026-08-10 covering a ten-stage pipeline intake, and one from 2026-08-12 covering a Lords of Cian room intake. This failure predates this review session and was not caused by it; this session made no changes to either file. It was noticed only as a side effect of running the same gate script to check a different, unrelated issue, and was left uninvestigated and unresolved, flagged as an open item for a future session to look into.

## Links
(none)
