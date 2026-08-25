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
curiosity-room/   live queue of open questions — see curiosity-room/README.md
solutions-room/   live queue of worked solutions to those questions — see solutions-room/README.md
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

First import landed 2026-08-08: five notes from the STAG Research-role chat (the 2x2
troubleshooting-narrative research ratification, its handoff, an addendum, and the
Curiosity Room / Solutions Room proposal with its Shift Department correction). Further
imports from the operator's local `knowledge-home` folder are still pending.
