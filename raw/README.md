# raw/ — the append-only transcript archive

This is the "archive" half of Anansi's two-store design — see
[`docs/adr/0005-two-store-memory-archive-and-core.md`](../docs/adr/0005-two-store-memory-archive-and-core.md).
It holds the literal, unedited transcript of every session that fed the
Knowledge Core. Nothing here is judged, summarized, or cleaned up — that
happens on the other side, in `candidates/` and `notes/`. If a note ever
disagrees with what's written here about what was actually said, this
archive wins.

## Format

One file per session: `<YYYY-MM-DD>-<short-session-slug>.jsonl`

One JSON object per line, one line per conversational turn, appended in the
order the session happened (or written in one batch at close-out — see the
`stag-closeout` skill's Step 0). **Never rewritten, never reordered, never
edited after the fact — only ever appended to.**

Write to it with `scripts/knowledge_home/archive_writer.py::append_turn()`.
Never open an archive file in write ("w") mode by hand.

## Linking notes back to this archive

A note in `notes/` or `candidates/` that was distilled from a specific
session should carry a `provenance:` field (see
`templates/note-template.md`) naming the archive file and the line range it
came from:

```yaml
provenance:
  file: raw/2026-08-25-anansi-drive-import.jsonl
  turns: [12, 47]
```

This is what makes a note checkable rather than just trusted — anyone can
open the named file, read that exact line range, and see the original
words the note was drawn from.

## Status

Empty as of 2026-08-25. This folder already existed for the operator's
local Knowledge Home (`C:\Users\abadm\stag\research\knowledge-home\raw\`)
but had never been carried into this git-tracked repo — only the Core half
(`notes/`, `candidates/`) made it here. This scaffolding brings the archive
half into git; the historical transcripts themselves still live locally (or
in Google Drive, for the 2026-08-04 through 2026-08-07 sessions the current
`notes/` and `candidates/` were imported from) and have not been backfilled
here, since this repo has no turn-by-turn access to them. Sessions going
forward should write their archive as part of closing out, so nothing new
falls into that same gap.
