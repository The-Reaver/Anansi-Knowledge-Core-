---
id: 2026-08-25-9-gate-precondition-tracker
type: note
status: active
source: this chat, tracking the six ratification preconditions from the 9-Gate verdict.
project: fleet
tags: [brain-trust, 9-gate, stars-dreams, fleet-leveling, tracker]
---

# Tracker: the six preconditions the 9-Gate verdict set before the operator can ratify it — one is hard-blocked on file access, the rest are in progress or done

## Body

`2026-08-25-9-gate-brain-trust-verdict.md` listed six items that must be done, not assumed,
before the hybrid-or-other verdict can be ratified. Status as of this session:

**1. Draft the Gate-range-to-FLEET_LEVELING-label crosswalk table.** Blocked-in-part. The
mechanism is drafted below, but the actual gate-range boundaries can't be filled in until (a)
item 2 confirms what FLEET_LEVELING's four stages currently mean, and (b) item 3 settles the
real gate count. Filling this in prematurely would be exactly the kind of guess the original
proposal warned against. See the stub in "Crosswalk table (stub)" below.

**2. Check FLEET_LEVELING's actual current content — hard blocked.** `FLEET_LEVELING_2026-08-01.md`
is not in this repository. A full search (`grep -r FLEET_LEVELING`, `find *FLEET*`) found nothing
— it exists only in the operator's local `knowledge-home` folder, per the README's own note that
imports from there are still pending. I cannot read a file I don't have; I am not guessing at its
contents. **Needs the operator**: either add the file to this repo, or paste its four stages'
actual per-transition criteria (if any exist) directly.

**3. Bottom-up derivation of gate domains.** In progress — a research agent is deriving candidate
capability/governance domains from the cited sources (METR Time Horizon, DeepMind Levels of AGI,
NIST AI RMF, ISO 42001, OWASP Agentic AI maturity), explicitly not targeting nine as the answer.
Result will land as a follow-up note once the agent completes.

**4. Decide and ratify Gate 1's specific threshold.** In progress — a separate research agent is
finding real published METR Time Horizon numbers and the specific DeepMind Levels-of-AGI rung
that would make a defensible, citable Gate 1 floor, as candidates for the operator/Brain Trust to
ratify. Result will land as a follow-up note once the agent completes.

**5. Adopt the "Gate N" documentation convention — done, candidate.** See
`2026-08-25-gate-n-documentation-convention.md`. No blocker; this is a naming rule, not a
governance judgment call, but it still isn't ratified until the operator's pass.

**6. Confirm the STARS.docx citation-only edit — drafted, not confirmed.** The exact proposed
citation text is in `2026-08-25-stars-citation-edit-draft.md`, ready to insert. Two real blockers
remain: (a) `STARS.docx` isn't in this repo either, so the edit can't actually be applied here;
(b) no note anywhere records *who* holds ratification authority over STARS.docx specifically
(the notes say only "Brain-Trust-ratified"). **Needs the operator**: name who signs off on
STARS.docx edits, and provide the file (or apply the drafted text directly).

## Crosswalk table (stub)

```
Gate range   -> FLEET_LEVELING label
-----------------------------------
Gate 1 - ?   -> Seed
Gate ? - ?   -> Designed
Gate ? - ?   -> Active/Beta
Gate ? - N   -> Alpha
```

Cannot be filled in until items 2 and 3 resolve. Nine does not divide evenly into four regardless
of the final count — whatever mapping is chosen is a deliberate design decision, not a natural
one, and the ratified version of this table must say so explicitly (per the verdict).

## Links

- extends, `2026-08-25-9-gate-brain-trust-verdict.md`, the ruling these six items gate.
- affects, `2026-08-25-gate-n-documentation-convention.md`, item 5.
- affects, `2026-08-25-stars-citation-edit-draft.md`, item 6.
