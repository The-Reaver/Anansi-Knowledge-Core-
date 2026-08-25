---
id: knowledge-core-supersedes-link-ruling-2026-08-25
type: ruling
status: ratified
source: Architecture, Redlined — Rev. 3, Part V; built and merged into this repo, PR #3
project: fleet
tags: [knowledge-core, zettelkasten, schema]
supersedes: [knowledge-core-supersedes-link-gap-2026-08-25]
superseded_by: null
---

# Every note carries a bidirectional supersedes / superseded_by link

## Body

A note being outdated isn't enough on its own — if the note that replaces it doesn't point
back, a retrieval can surface a stale ruling and its correction side by side with no signal
which one wins. The Core's schema now carries both directions:

- `supersedes` — ids of notes this one replaces (list, defaults empty).
- `superseded_by` — id of the note that replaced this one (defaults null).

The rule at ratification time: when a new note ratifies with a non-empty `supersedes`
list, the ratifier updates every note it names to set their `superseded_by` to the new
note's id, in the same pass. A note is never left pointing nowhere while something else
already replaced it. See `templates/note-template.md` and `README.md`'s "Note format"
section for the field definitions.

## Links

- Architecture, Redlined Rev. 3, Part V
- knowledge-core-supersedes-link-gap-2026-08-25 (the finding this ruling closes)
