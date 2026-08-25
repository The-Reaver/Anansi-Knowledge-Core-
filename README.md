# Anansi — the Knowledge Core

Anansi is the operator's Zettelkasten: several hundred (and growing) atomic notes holding
every lesson, ruling, decision and mandate the STAG fleet has produced. This repo is the
git-tracked home for that Core.

## The rule this Core exists to enforce

**Recall before you guess. Capture after you learn.**

Answering a question from reasoning alone when the Core already holds the answer is the
failure this repo prevents. Finishing substantial work without writing the lesson back is
the other half of the same failure — every session owes the Core its lesson, unasked
(Mandate 8).

## Layout

```
raw/              append-only archive: the literal, unedited transcript of every
                  session, one JSONL file per session (see raw/README.md)
notes/            permanent, ratified atomic notes — the Core itself
candidates/       unratified captures, one dated subfolder per session (candidates/<date>/)
templates/        the note template new captures should start from
docs/adr/         architecture decisions, starting with why raw/ and notes/ are
                  kept as two separate stores (ADR-0005)
scripts/          tooling — the append-only writer for raw/ lives here
```

Nothing enters `notes/` without the operator's pass. Everything lands in `candidates/`
first.

`raw/` and `notes/` are deliberately two different stores, not one. `raw/` is the
ultimate source of truth — the exact words of a session, appended and never edited.
`notes/` is the distilled, searchable Core built from it. A note that came from an
archived session should link back to it — see "Provenance" below and
`docs/adr/0005-two-store-memory-archive-and-core.md` for why.

## Note format

Every note carries:

- `id` — unique identifier
- `type` — one of `finding`, `decision`, `lesson`, `correction`, `ruling`, `artifact`,
  `question`, `spec`, `note`
- `status` — e.g. `candidate`, `ratified`
- `source` — where the lesson came from (session, chat, document)
- `tags` — free-form
- `provenance` — optional; the `raw/` archive file and line range this note was distilled
  from, if it came from an archived session. Omit entirely for notes with no archived
  session behind them.
- `## Body` — what happened, why, and what to do differently. Plain language. Name the
  file, the command, the error.
- `## Links` — ids of notes this one extends, contradicts, or depends on. Links are what
  turn a pile of notes into a graph.

One lesson per note. A note holding three lessons gets found for none of them.

**Title** states the lesson itself, not the topic — "A silent empty artifact is a bug, it
must fail loud" beats "Notes on the ERD renderer".

**Project** is `geo`, `cippe`, `ci`, `lords-of-cian`, `fleet`, or the real project name.

See `templates/note-template.md` for the starting shape of a new note.

## Status

`notes/` holds 108 ratified notes, imported and mined from the operator's Google Drive
note inbox and reviewed against the bar above. `candidates/` holds the rest of that
import, still awaiting further review or splitting. `raw/` is scaffolded (folder, ADR,
writer script, `provenance` field on the template) but empty — the historical sessions
behind the current notes weren't reachable turn-by-turn for backfill. Sessions going
forward should write their archive as part of closing out, so `raw/` and `notes/` grow
together from here.
