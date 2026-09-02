---
id: 2026-08-20-three-note-schema-conventions-coexist-in-anansi-core
type: finding
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 9/10 on the promotion rubric (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Directly observed across this session's work in notes/ spanning all three conventions. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, schema, governance]
sources:
  - ref: "This session's own review, verification, and gate-closure work, 2026-08-20"
    reliability: high
    origin: "direct observation and verification, this session"
provenance:
  archive: research/knowledge-home/raw/2026-08-20-anansi-candidate-promotion-and-gate-closure-session.jsonl
  turns: [1, 20]
links:
  - "2026-08-20-this-session-notes-used-legacy-schema-not-adr0005-self-critique"
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Three distinct, incompatible note-frontmatter schema conventions coexist at once in the Anansi Knowledge Core's permanent notes folder

## Body

The Anansi Knowledge Core's permanent notes folder currently contains at least three distinct, incompatible frontmatter schema conventions, all still present at once as of this review. The oldest is a flat convention with no delimiting fence: a single leading title line followed by a plain markdown bullet list of key-value fields such as id, type, status, and source, then a Body and Links section. A second, older-still convention used on some pre-existing notes uses the literal status value "active" instead of "ratified" for a fully promoted note. A third, stricter convention was introduced by ADR-0005 on 2026-08-10 and requires real, delimited YAML frontmatter (an opening and a closing "---" fence) with structured sources and provenance fields, and is the only one enforced by the archive_notes_separation_gate script for any note added after that date that is not otherwise exempted. A reviewer working across the Core needs to know which convention a given note or a given target folder actually expects before writing to it.

## Links
- relates, 2026-08-20-this-session-notes-used-legacy-schema-not-adr0005-self-critique
