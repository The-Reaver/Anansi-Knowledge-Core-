---
id: 2026-08-20-check-existing-ratified-note-schema-before-writing-new-one
type: lesson
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 9/10 on the promotion rubric (novelty 1, evidence 2, actionability 2, generality 2, non-contradiction 2). Learned the hard way this session, repeatedly, across multiple folders with drifted conventions. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, methodology, schema]
sources:
  - ref: "This session's own review, verification, and gate-closure work, 2026-08-20"
    reliability: high
    origin: "direct observation and verification, this session"
provenance:
  archive: research/knowledge-home/raw/2026-08-20-anansi-candidate-promotion-and-gate-closure-session.jsonl
  turns: [1, 20]
links:
  - "2026-08-20-three-note-schema-conventions-coexist-in-anansi-core"
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Before writing a new promoted note into the Knowledge Core, check an existing ratified note's actual frontmatter first, since schema conventions have drifted across the Core's history rather than trusting memory or documentation

## Body

Before writing a new promoted note into the permanent Knowledge Core, a reviewer should open an existing, already-ratified note and confirm the exact field names and conventions actually in current use, rather than assuming a schema from memory or from documentation alone. Across one review session covering the whole outstanding candidate backlog, the actual in-use status-field value for a fully promoted note was found to be "ratified" rather than the older "active" convention seen on some pre-existing notes, and other small conventions (whether a Links section uses wiki-style double-bracket references or plain comma-separated ids, whether frontmatter is delimited by a leading and trailing "---" fence) also varied across different parts of the Core's history. Guessing the schema risks writing a note that later tooling does not recognize as compliant.

## Links
- relates, 2026-08-20-three-note-schema-conventions-coexist-in-anansi-core
