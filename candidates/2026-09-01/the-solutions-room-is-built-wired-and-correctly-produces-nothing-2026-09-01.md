---
id: the-solutions-room-is-built-wired-and-correctly-produces-nothing-2026-09-01
type: finding
status: candidate
source: "Recovery session, 2026-09-01 — VERIFIED by running scripts/knowledge_home/solutions_intake.py against a clone of The-Reaver/Stag-Fleet at branch anansi-home-dashboard"
project: fleet
tags: [curiosity-room, solutions-room, provenance, retrofit, fail-closed, anansi]
supersedes: []
superseded_by: null
---

# Both rooms exist and the loop runs — it emits zero because the approved provenance retrofit was never executed

## Body

> **RESOLVED, 2026-09-01, same day.** The room now emits **92 proposals**. The diagnosis below was
> right that nothing was broken and wrong about the cause: the blocker was not the Evidence Standard
> retrofit, it was that `solutions_intake.py` never implemented mandate
> `pre-provenance-grandfather-exemption` (operator ruling 2026-08-30). `curiosity_intake.py`
> references that ruling in 32 places; `solutions_intake.py` referenced it **zero** times and
> predated it, so it refused every pointer the ruling had just made eligible. One half of a ratified
> ruling shipped and the other half never did — the Amaya/Oluwole pattern, in code, nameable to the
> line.
>
> Fixed by an explicit `_is_grandfathered()` branch requiring the marker to be literally present and
> true. The no-fabrication refusal is untouched: a pointer with neither real provenance nor the
> marker is still refused, verified with a purpose-built test pointer that was scanned, refused, and
> produced no file. `archive_notes_separation_gate.py` passes with the room populated.
>
> **Pass One was still worth completing** (75% → 97%) — the classification the loop reads is real
> work — but it was not what unblocked this room, and I said it would be. Correcting that here.


The Curiosity Room and Solutions Room are **built, literal, and wired**. The operator made them
literal on 2026-08-25 — *"two rooms, literal running components: a scheduled agent, a background
process, a folder structure with its own intake pipeline"*. Both live at
`research/knowledge-home/{curiosity,solutions}/`, both are listed in `.rooms-index.txt`, and
`archive_notes_separation_gate.py` schema-checks them exactly as it checks `notes/`. The code
exists: `curiosity_intake.py` (28KB) and `solutions_intake.py` (11.5KB).

**Measured, by running it:** the Curiosity Room holds **92 pointers**. The Solutions Room holds
**nothing but its README**. Running `solutions_intake.py` produces:

```
solutions_intake: 0 proposal(s) written, 92 skipped for lacking real provenance
```

Every one of the 92 is skipped with *"cannot be written into the Solutions Room without fabricating
a citation."*

**Nothing is broken.** The room fails closed on an upstream data gap and refuses to invent
provenance — which is exactly right, and is the behaviour the rest of the gate battery should be
audited against. The producer half runs; the responder half correctly declines.

**The actual blocker is upstream and already approved.** `STAG-Evidence-Standard-v1.0.md` §7 and
§9 carry a three-pass retrofit runbook, **approved 2026-08-09**, whose own text reads *"Builder
executes. No further instruction needed."* Pass one is explicitly cheap — mechanical
classification, one session, no re-verification — and it is *"what makes the automatic loop start
running."* 335 of 845 notes already carry provenance, so the retrofit is partly done and stopped.

So the Solutions Room has been dead for **23 days** waiting on a runbook that needed no further
instruction. This is the fleet's dominant failure mode in its purest observed form: not a missing
design, not a broken mechanism, but an approved procedure nobody ran, with a silent zero
downstream and nothing raising a hand.

## Links

- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
- relates-to: the-amaya-fold-step-has-never-run-so-six-oluwole-briefs-sit-unfolded-2026-08-31
- relates-to: a-stale-git-lock-froze-a-repo-for-29-days-without-erroring-2026-08-31
- relates-to: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
