---
id: 2026-08-21-operator-directed-blanket-pragmatism-and-small-atomic-turns-under-usage-pressure
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, operator-preference, workflow, usage-limits, project-brief-step0]
sources:
  - ref: "Archive turns 296-316: turn 296 is the operator's literal 'pragmatism from here on out on all matters'; turn 309 is the literal 'i am at 99 percent usage until friday...worried you will be stopped mid work' quote; turn 310 records the adopted small-atomic-turn practice; turns 313 and 315 show the concrete example (fixing inbound_routing.py's log_event calls as one atomic commit, 14454f0) actually executed and committed."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [296, 316]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, explicit, direct operator instructions quoted in the transcript
- verified: 2026-08-21

# Operator directed blanket pragmatism going forward, and small self-contained turns specifically when near the usage limit so a cutoff never leaves the repo half-broken

## Body
The operator gave two related standing directives in this session that were framed as lasting beyond the immediate task, not one-off requests:

1. **"pragmatism from here on out on all matters"** -- the agent should act on its own judgment for routine sequencing and prioritization calls rather than pausing to ask for confirmation on every fork. (This is a general workflow preference, not a relaxation of the safety-relevant confirmations that remain required for genuinely risky or irreversible actions.)

2. Given while the operator was at 99% of their monthly Claude usage until the weekly reset, and worried the agent would be cut off mid-work: keep future work in **fewer, tighter turns and small, self-contained tasks**, specifically so that if usage runs out mid-work, the repository is never left in a half-broken state. The agent's stated practice adopted in direct response: avoid starting a large multi-file build (e.g. an entire new tool) right before a likely cutoff; prefer completing and committing one small, fully-verified, gate-clean fix as the deliberate stopping point, so the work is always safe to be interrupted at.

The concrete example the agent gave for this practice in the same turn: choosing to fix one specific latent bug (`inbound_routing.py`'s `log_event` call-signature errors) as a single atomic, tested, committed unit, explicitly instead of starting Tool 2 (Review Engine), because Tool 2 was a large multi-file build that could be stranded mid-way by a usage cutoff.
