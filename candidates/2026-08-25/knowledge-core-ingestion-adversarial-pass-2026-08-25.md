---
id: knowledge-core-ingestion-adversarial-pass-2026-08-25
type: finding
status: candidate
source: Architecture, Redlined — Rev. 3, Part V
project: fleet
tags: [knowledge-core, zettelkasten, deepening, adversarial-review]
supersedes: []
superseded_by: knowledge-core-ingestion-adversarial-pass-ruling-2026-08-25
---

# A candidate ruling deserves the same adversarial pass a code fix gets

## Body

Every fix landed in the session that produced Architecture, Redlined got a second,
independent agent trying to refute it before it shipped — the same adversarial-review
pattern named in that document's Part III, Pillar 07. A note entering the Knowledge Core
as a candidate `ruling` deserves the identical treatment before ratification: does it
contradict an existing ratified note, not just restate one?

This is the third of the three deepening proposals from Part V (the other two —
supersedes-link, confidence tier — were captured as their own candidate notes on
2026-08-25; this one wasn't, and is being captured now for the first time rather than
transcribed from an earlier draft).

Proposed fix: before a candidate note is ratified, a cheap, targeted search-and-compare
pass against the existing `notes/` store — not a rebuild, not a full semantic audit. Check
whether the candidate's claim conflicts with something already ratified. If it does, that's
not a silent ratify: either the candidate should set `supersedes` to name what it replaces
(using the schema this Core now has), or the conflict needs the operator's call before
either note stands as ratified.

This is a finding, not yet ratified — whether and how to build this is a decision for the
operator, not something to silently treat as decided.

## Links

- Architecture, Redlined Rev. 3, Part V
- knowledge-core-supersedes-link-gap-2026-08-25
