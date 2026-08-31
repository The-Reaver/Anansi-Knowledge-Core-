---
id: knowledge-core-ingestion-adversarial-pass-ruling-2026-08-25
type: ruling
status: ratified
source: Architecture, Redlined — Rev. 3, Part V; built and merged into this repo, PR #6
project: fleet
tags: [knowledge-core, zettelkasten, adversarial-review, ratification]
supersedes: [knowledge-core-ingestion-adversarial-pass-2026-08-25]
superseded_by: null
---

# Ratification runs a search-and-compare pass before a candidate note is promoted

## Body

Every fix landed in this fleet's code gets a second, independent agent trying to refute it
before it ships — the same adversarial-review pattern. A candidate `ruling` entering the
Knowledge Core deserves the identical treatment before ratification, not just a read and a
nod.

The procedure now in force, documented in `README.md`'s "Ratification" section:

1. Search-and-compare the candidate against what's already in `notes/` — cheap and
   targeted, not a full audit of the whole Core.
2. If it merely restates an existing ratified note, don't ratify a duplicate — link to the
   note that already says it.
3. If it actually contradicts an existing ratified note, that's not a silent ratify
   either — set `supersedes` and update the old note's `superseded_by` in the same pass, or
   resolve the conflict as an explicit operator decision first.
4. No conflict, no duplicate — ratify normally.

## Links

- Architecture, Redlined Rev. 3, Part V
- knowledge-core-ingestion-adversarial-pass-2026-08-25 (the finding this ruling closes)
- knowledge-core-supersedes-link-ruling-2026-08-25 (the mechanism this procedure relies on)
