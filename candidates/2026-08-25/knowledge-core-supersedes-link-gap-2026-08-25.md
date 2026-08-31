---
id: knowledge-core-supersedes-link-gap-2026-08-25
type: finding
status: candidate
source: "Architecture, Redlined — Rev. 3, Part V; captured via GeoSuite session handoff, 2026-08-25"
project: fleet
tags: [knowledge-core, zettelkasten, deepening]
---

# A superseded note needs a link back, or retrieval can surface it as current

## Body

A `ruling` note can presumably be marked outdated, but it's unconfirmed whether a
superseding note points *back* at what it replaces, and the old note points *forward*.
Without both directions, a retrieval can surface a stale ruling and its correction with no
signal which wins — reintroducing at the retrieval layer the exact contradiction
ratification exists to prevent at the write layer.

Proposed fix: a real bidirectional `supersedes` / `superseded_by` link, enforced at
ratification time.

This is a finding, not yet ratified — whether and how to build this is a decision for the
operator, not something to silently treat as decided.

**Update, 2026-08-25:** the operator approved building the fix. `templates/note-template.md`
and `README.md` now carry the `supersedes` / `superseded_by` fields and the bidirectional
enforcement rule (see `README.md`'s "Note format" section). This finding's own `status` is
left as `candidate` — building the schema field isn't the same as ratifying this finding,
and this session still has no Anansi access to run that gate. Once ratified, this note is a
candidate for its own `supersedes` field to point at whatever replaces it, since the gap it
names is now closed by the template change rather than by this note.

## Links

- Architecture, Redlined Rev. 3, Part V
