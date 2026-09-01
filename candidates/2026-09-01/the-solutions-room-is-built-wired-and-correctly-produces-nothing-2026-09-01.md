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
