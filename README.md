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
- `status` — `candidate` or `ratified`. This is the Core's confidence tier, not just a
  workflow marker. See below.
- `source` — where the lesson came from (session, chat, document)
- `tags` — free-form
- `provenance` — optional; the `raw/` archive file and line range this note was distilled
  from, if it came from an archived session. Omit entirely for notes with no archived
  session behind them.
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

## Status

`notes/` holds 108 ratified notes, imported and mined from the operator's Google Drive
note inbox and reviewed against the bar above. `candidates/` holds the rest of that
import, still awaiting further review or splitting. `raw/` is scaffolded (folder, ADR,
writer script, `provenance` field on the template) but empty — the historical sessions
behind the current notes weren't reachable turn-by-turn for backfill. Sessions going
forward should write their archive as part of closing out, so `raw/` and `notes/` grow
together from here.
