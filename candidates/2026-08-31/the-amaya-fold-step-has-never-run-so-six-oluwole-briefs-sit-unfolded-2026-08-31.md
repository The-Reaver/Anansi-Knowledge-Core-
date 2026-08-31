---
id: the-amaya-fold-step-has-never-run-so-six-oluwole-briefs-sit-unfolded-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) dormant-area audit, 2026-08-31 — relayed by the operator into a recovery session; the audit itself ran against the local Knowledge Home and could not be re-run here"
project: fleet
tags: [oluwole, amaya, design-system, dormant-area, heartbeat, documented-not-executed]
supersedes: []
superseded_by: null
---

# A documented mechanism ran for five weeks with one half working and the other half never having executed once

## Body

Audited 2026-08-31. `DESIGN_PRINCIPLES.md` states its own mechanism plainly: *"Oluwole
researches continuously... and Amaya folds accepted findings into these tokens and rules."*

Oluwole's half ran. **Six weekly briefs since 2026-07-24.**

Amaya's half has never run. `git log` on `DESIGN_PRINCIPLES.md` returns **exactly one
commit — its creation.** Not a single accepted finding has been folded in, across five
weeks.

This is the cleanest specimen of the fleet's dominant failure mode, and the most instructive
because nothing about it is broken. Both halves are documented. One is diligently
productive. The pipeline did not fail because anyone did it wrong; it failed because one
half ran, the other never did, and **nothing noticed for five weeks**. The briefs piling up
were the only symptom, and piling up is what an inbox looks like when it is working, so the
symptom is indistinguishable from health.

**The general rule this earns:** every accumulation loop needs a heartbeat check —
something that fires when the loop **stops turning**, not only when a step errors. A
documented two-step mechanism where only step one is instrumented is a one-step mechanism
with optimistic documentation.

## Links

- relates-to: the-sitegen-design-system-is-the-most-built-out-of-the-dormant-areas-2026-08-31
- relates-to: a-stale-git-lock-froze-a-repo-for-29-days-without-erroring-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
