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
notes/            permanent, ratified atomic notes — the Core itself
candidates/       unratified captures, one dated subfolder per session (candidates/<date>/)
templates/        the note template new captures should start from
```

Nothing enters `notes/` without the operator's pass. Everything lands in `candidates/`
first.

## Note format

Every note carries:

- `id` — unique identifier
- `type` — one of `finding`, `decision`, `lesson`, `correction`, `ruling`, `artifact`,
  `question`, `spec`, `note`
- `status` — e.g. `candidate`, `ratified`
- `source` — where the lesson came from (session, chat, document)
- `tags` — free-form
- `supersedes` / `superseded_by` — the bidirectional link between a note and whatever
  replaces it. See below.
- `## Body` — what happened, why, and what to do differently. Plain language. Name the
  file, the command, the error.
- `## Links` — ids of notes this one extends, contradicts, or depends on. Links are what
  turn a pile of notes into a graph.

One lesson per note. A note holding three lessons gets found for none of them.

**Supersedes is bidirectional, not a status flag.** A note being outdated isn't enough —
if the note that replaces it doesn't point back, a later retrieval can surface the stale
note and its correction side by side with no signal which one wins. So the rule at
ratification time: when a new note ratifies with a non-empty `supersedes` list, the
ratifier updates every note named there to set its `superseded_by` to the new note's id,
in the same pass. A note is never left pointing nowhere while something else already
replaced it.

**Title** states the lesson itself, not the topic — "A silent empty artifact is a bug, it
must fail loud" beats "Notes on the ERD renderer".

**Project** is `geo`, `cippe`, `ci`, `lords-of-cian`, `fleet`, or the real project name.

See `templates/note-template.md` for the starting shape of a new note.

## Status

Scaffold only — awaiting the first import of notes from the operator's local
`knowledge-home` folder.
