---
id: knowledge-core-supersedes-link-gap-2026-08-25
type: finding
status: candidate
source: Architecture, Redlined — Rev. 3, Part V; captured via GeoSuite session handoff, 2026-08-25
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

## Links

- Architecture, Redlined Rev. 3, Part V
