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
first. See "Ratification" below for what that pass actually checks.

## Note format

Every note carries:

- `id` — unique identifier
- `type` — one of `finding`, `decision`, `lesson`, `correction`, `ruling`, `artifact`,
  `question`, `spec`, `note`
- `status` — `candidate` or `ratified`. This is the Core's confidence tier, not just a
  workflow marker. See below.
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

## Ratification

The operator's pass on a candidate note isn't a rubber stamp — it's the same adversarial
pattern this fleet already uses on code: an independent check trying to refute the claim,
not just read it and nod. Before a candidate moves to `notes/`:

1. **Search-and-compare, not a rebuild.** Check the candidate against what's already in
   `notes/` — same topic, same tags, overlapping claim. This is meant to be cheap: a
   targeted search, not a full audit of the whole Core every time one note ratifies.
2. **Restates an existing ratified note, no new information?** Don't ratify a duplicate —
   link to the note that already says it. A second note saying the same thing doesn't add
   confidence, it adds a place for the two copies to quietly drift apart later.
3. **Actually contradicts an existing ratified note?** That's not a silent ratify either.
   Either the candidate sets `supersedes` to name what it replaces (and the ratifier
   updates that note's `superseded_by` in the same pass, per the rule above), or the
   contradiction gets resolved as an explicit decision before either note stands as
   ratified — never left for a future retrieval to discover on its own.
4. **No conflict, no duplicate?** Ratify normally.

This applies to every candidate, not just the ones that look consequential — the whole
point of catching a contradiction here is that it's cheap now and expensive later, once a
session has already retrieved and acted on the stale claim.

## Status

Scaffold only — awaiting the first import of notes from the operator's local
`knowledge-home` folder.
