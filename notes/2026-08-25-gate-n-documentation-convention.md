---
id: 2026-08-25-gate-n-documentation-convention
type: spec
status: candidate
source: this chat, item 5 of the 9-Gate verdict's ratification preconditions.
project: fleet
tags: [brain-trust, 9-gate, stars-dreams, documentation-convention]
---

# Convention: fleet-wide gate stages are always written "Gate N," never bare "level N" or "stage N," to keep them unambiguous from STARS's own 1-9 TRL numbers

## Body

STARS.docx already uses a 1-9 TRL-style numbering for Augustin's per-phase maturity. The 9-Gate
ladder ratified in principle by `2026-08-25-9-gate-brain-trust-verdict.md` will also number its
stages, and — per that verdict — the final count may not even be nine. Two independently-run 1-9
(or similar) numbering schemes sitting next to each other, both referred to loosely as "level N"
or "stage N," is a predictable source of real confusion: "Augustin is at level 6" would be
genuinely ambiguous between his STARS TRL phase and his fleet-wide Gate status.

**The rule**: any reference to 9-Gate ladder standing is always written "Gate N" in full — never
abbreviated to a bare number, never "level N," never "stage N." STARS TRL references keep their
existing "TRL N" or phase-name convention unchanged. This is a naming rule only; it does not
resolve the crosswalk between the two systems (see
`2026-08-25-9-gate-precondition-tracker.md`, item 1).

Applies to: `notes/`, any dashboard or artifact that displays agent status, and ordinary STAG
fleet conversation about an agent's standing.

## Links

- extends, `2026-08-25-9-gate-brain-trust-verdict.md`, item 5 of its ratification preconditions.
