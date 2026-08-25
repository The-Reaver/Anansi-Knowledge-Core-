# ADR-0005: Two-store memory — archive and Core

## Status

Accepted. Already governing the operator's local Knowledge Home
(`C:\Users\abadm\stag\research\knowledge-home\`); this document and the
`raw/` folder it describes bring that same decision into this git-tracked
repo, which had only ever carried the Core half of it.

## Context

Anansi needs two things a single store can't both do well:

- A place that never lies — the exact, unedited words of a session, so a
  claim can be checked against what was actually said rather than trusted
  on faith.
- A place that's fast to search and reason from — small, single-idea notes
  a meaning-based search can match precisely, the way `notes/` already
  works (see the README's "Recall before you guess" rule).

A full, unedited transcript is trustworthy but not directly searchable —
one session can run thousands of turns, and a question about one decision
buried in it won't surface cleanly. A store of only distilled notes is
searchable but, if it's the *only* record, there is nothing to check a
distillation against: if a note is wrong, incomplete, or subtly reworded
from what was actually decided, nothing catches it.

## Decision

Keep two separate stores, tied together by explicit links, not one store
trying to do both jobs.

1. **`raw/`** — the archive. One JSONL file per session,
   `raw/<YYYY-MM-DD>-<short-session-slug>.jsonl`, one JSON object per line,
   one line per conversational turn, written in order. **Append-only**: a
   session's archive file is only ever opened to add a new line, never to
   rewrite, reorder, or edit a line already written. This is the ultimate
   source of truth. If a note in `notes/` and this archive ever disagree
   about what was actually said, the archive wins.

2. **`notes/`** (staged through `candidates/<date>/`) — the Core. Small,
   atomic, one-idea-per-note distillations, produced by a reviewer —
   human or agent — exercising real judgment about what's worth keeping
   and how to phrase it. A note distilled from a specific session should
   carry a `provenance:` field naming the archive file and the line range
   it was drawn from (see `templates/note-template.md`), so any claim in
   the Core can be traced back to the exact original turns it came from.

## Consequences

- Notes stay small and atomic — fast and precise to search — without
  becoming the only record of what was actually said.
- Nothing is lost to summarization. The full transcript is always
  recoverable, even for the parts that never became a note.
- A note can be verified, not just trusted. If a distillation is disputed
  or looks off later, the raw archive settles it.
- Cost: a session's transcript has to be captured before the session ends
  — an ephemeral chat that closes without an archive write is gone for
  good. And the raw store grows without bound by design (append-only,
  never pruned), so it needs its own storage discipline over time,
  separate from the curated, actively-maintained Core.

## Implementation notes for this repo

- `raw/<date>-<slug>.jsonl` per session — see `raw/README.md`.
- `scripts/knowledge_home/archive_writer.py` provides the append-only
  writer (`append_turn`) plus `read_raw_lines` and
  `verify_prefix_unchanged`, so nothing ever silently overwrites a prior
  session's history.
- `templates/note-template.md` carries an optional `provenance:` field for
  notes distilled from a specific archived session.
- As of 2026-08-25, `raw/` is scaffolded but empty here: the historical
  transcripts behind the 95 notes imported that day live in Google Drive
  and local files this repo doesn't have turn-by-turn access to, so they
  could not be backfilled. Sessions going forward should write their
  archive as they go (or in one batch at close-out, per the
  `stag-closeout` skill).
