---
id: 2026-08-20-archive-notes-separation-gate-failing-151-notes-adr0005-schema
type: finding
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 9/10 on the promotion rubric (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Directly reproduced by running the real gate script this session. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, adr-0005, gate, governance]
sources:
  - ref: "This session's own review, verification, and gate-closure work, 2026-08-20"
    reliability: high
    origin: "direct observation and verification, this session"
provenance:
  archive: research/knowledge-home/raw/2026-08-20-anansi-candidate-promotion-and-gate-closure-session.jsonl
  turns: [1, 20]
links:
  - "2026-08-20-only-nine-notes-have-real-raw-archive-backing"
  - "2026-08-20-legacy-allowlist-extended-151-notes-decision"
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The gate enforcing the Knowledge Core's two-store archive-and-notes architecture was found failing for 151 notes lacking the real provenance schema that architecture requires

## Body

A separate gate script, distinct from the ratification gate and enforcing a 2026-08-10 architecture decision that splits the Knowledge Core into an append-only raw transcript archive and a curated notes folder, was found during this review to be failing for 151 notes. Each of those notes lacks the real, delimited YAML frontmatter that decision requires, specifically a provenance field that must point at an actual archived session-transcript file with a valid line-range of turns cited from it. This failure was not caused by this review session alone; notes added by earlier, separate review sessions before this one also fail the same check, meaning it had been silently accumulating for roughly ten days before being noticed.

## Links
- relates, 2026-08-20-only-nine-notes-have-real-raw-archive-backing
- relates, 2026-08-20-legacy-allowlist-extended-151-notes-decision
