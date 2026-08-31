---
id: 2026-08-07-canonical-source-is-chat-slug-convention
type: note
status: ratified
source: "operator directive, 2026-08-07 (source status: ratified by operator, 2026-08-07)"
project: fleet
tags: []
supersedes: []
superseded_by: null
---

# Convention: the chat slug is the canonical source string

## Body

Every harvested note's source field normalizes to the originating chat's slug as the single canonical source string. Any shorthand a harvest used is kept on record as an accepted alias, never deleted, so older references and search continuity do not break. On intake, notes are normalized to the canonical slug and their shorthand is logged as an alias for that slug.

## Links

- 2026-08-07-agent-naming-split-resolved-alias-kept
- 2026-08-07-chat-title-timestamp-convention
