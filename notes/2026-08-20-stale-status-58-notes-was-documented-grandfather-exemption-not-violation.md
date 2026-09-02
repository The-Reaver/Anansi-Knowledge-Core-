---
id: 2026-08-20-stale-status-58-notes-was-documented-grandfather-exemption-not-violation
type: correction
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 9/10 on the promotion rubric (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Directly verified this session against .ratified-allowlist.txt and core_ratification_gate.py. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, governance, schema]
sources:
  - ref: "This session's own review, verification, and gate-closure work, 2026-08-20"
    reliability: high
    origin: "direct observation and verification, this session"
provenance:
  archive: research/knowledge-home/raw/2026-08-20-anansi-candidate-promotion-and-gate-closure-session.jsonl
  turns: [1, 20]
links:
  - "2026-08-20-archive-notes-separation-gate-failing-151-notes-adr0005-schema"
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Fifty-eight pre-existing Core notes that appeared to carry a stale, unreviewed status field turned out to be legitimately covered by an explicit, documented grandfather exemption, not a governance violation

## Body

A concern raised mid-session that fifty-eight pre-existing notes already living in the Knowledge Core's permanent notes folder still carried a status field of candidate or open, despite already being part of the ratified Core, was investigated further and found to be a non-issue rather than a governance violation. The actual ratification gate script that enforces which notes are allowed in the Core does not check the status field's text value at all; it checks whether a note is either listed in an explicit, dated grandfather allowlist of 347 notes frozen on 2026-08-09 (whose own header openly discloses that every one of those notes is exempt because it predates the gate, not because it was individually reviewed) or carries a real ratified marker line. All fifty-eight flagged notes were confirmed to be legitimately on that grandfather allowlist, and the real gate passes cleanly. The status field text was simply stale, cosmetic leftover wording, not evidence of anything actually wrong; it was relabeled to a clearer grandfathered value for readability, with no change to any note's actual content.

## Links
- relates, 2026-08-20-archive-notes-separation-gate-failing-151-notes-adr0005-schema
