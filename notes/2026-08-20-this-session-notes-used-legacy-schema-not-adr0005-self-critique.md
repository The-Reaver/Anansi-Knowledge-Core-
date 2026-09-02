---
id: 2026-08-20-this-session-notes-used-legacy-schema-not-adr0005-self-critique
type: correction
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 9/10 on the promotion rubric (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Self-observed directly; this very ratification pass is the corrective action it recommends. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, schema, adr-0005, self-critique]
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

# Every note this session promoted into the Core used the older flat schema rather than the stricter ADR-0005 schema formally required since 2026-08-10, which is exactly why a gate had to be closed with an allowlist extension rather than passing cleanly

## Body

Every note promoted into the permanent Knowledge Core during this review session used the older, flat bullet-list schema convention, matching the majority convention already in use across most of the existing Core including prior anansi-promote review sessions, rather than the stricter ADR-0005 schema (real YAML frontmatter with structured sources and provenance fields pointing at a real archived transcript) that has technically been the required convention for any note added after 2026-08-10. This is precisely why the archive_notes_separation_gate script failed against 151 notes including nearly all of this session's own output, and why closing that gate required extending a grandfather-style allowlist rather than reformatting the notes. A future session doing this same kind of candidate-promotion work should consider writing real ADR-0005-compliant schema from the start, if the operator wants this gap to actually close going forward rather than be extended again with each new batch.

## Links
- relates, 2026-08-20-archive-notes-separation-gate-failing-151-notes-adr0005-schema
