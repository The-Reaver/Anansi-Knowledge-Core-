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
- `status` — `candidate` or `ratified`. This is the Core's confidence tier, not just a
  workflow marker. See below.
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

**Confidence tier: `status` is it, and it isn't optional to respect.** GeoSuite's own audit
rubric tags claims `documented` vs. `hypothesis` rather than asserting everything with
equal confidence — the Core owes its own consumers the same discipline. `status: candidate`
means one agent's unverified read: cite it as *unconfirmed*, never as settled fact.
`status: ratified` means a human has actually signed off: it can be cited and relied on
without that caveat. A session retrieving a note must check `status` before treating its
content as true, the same way it would check whether a source is a rumor or a fact —
collapsing the two into one undifferentiated "truth" tier at retrieval time defeats the
entire point of the ratification gate upstream of it.

See `templates/note-template.md` for the starting shape of a new note.

## Status

Scaffold only — awaiting the first import of notes from the operator's local
`knowledge-home` folder.
