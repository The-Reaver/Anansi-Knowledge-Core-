---
id: 2026-08-21-dont-downgrade-verification-for-subjective-process-skills
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (cleaned up inconsistent legacy ratification metadata that asserted operator ratification while status remained candidate; body content unchanged). Operator retains veto per Mandate 1."
project: fleet
tags: [process, skill-creation, verification, governance]
sources:
  - ref: "Turns 399-411: turn 399 is the operator's instruction to build the good-faith adversarial-review skill, turn 402 is the agent reasoning it can skip the eval-benchmark loop for a 'subjective process skill,' turn 408 is the operator's verbatim pushback ('dont skip the full benchmark if it hurts the process. am i doing too much?'), and turns 409-411 are the agent's correction and the operator-approved hybrid resolution (run the skill for real against the live note batch instead of a synthetic benchmark)."
    reliability: high
    origin: "STAG session, 2026-08-14, \"GEO Suite completion\" (backfilled from historical transcript b9b0acfa, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-14-backfill-b9b0acfa.jsonl
  turns: [399, 411]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A skill whose whole job is catching errors in content headed to a human reviewer should not have its own verification step skipped just because it is a "subjective process skill" rather than an objectively-gradable data transform
- id: 2026-08-21-dont-downgrade-verification-for-subjective-process-skills
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-14, "GEO Suite completion" (backfilled from historical transcript b9b0acfa, 2026-08-21)
- confidence: high — direct operator correction, quoted in the transcript, immediately acknowledged and acted on by the agent
- verified: 2026-08-21
- tags: process, skill-creation, verification, governance
- REVIEW: high-impact

## Body
When asked to turn the operator's spec for a good-faith adversarial-review skill into an actual skill file, the agent initially reasoned that it could skip the skill-creator process's full eval-benchmark loop, on the grounds that the loop "is built for objectively-gradable output-transform skills, not a process/governance skill like this." The operator pushed back directly: "dont skip the full benchmark if it hurts the process. am i doing too much?" The agent agreed the reasoning had been backwards — a skill whose entire purpose is catching errors before a lawyer reviews legally-sensitive content is exactly the kind of thing that should not skip its own verification step, subjective or not. The resolution, offered back to the operator as an explicit choice, was a hybrid: rather than run a synthetic benchmark, exercise the new skill for real against the actual batch of Knowledge Core notes just produced that session, which delivers real product value and real verification of the skill simultaneously. The operator chose that path. The durable rule: "this output is subjective/hard to grade" is not a valid reason to skip verifying a skill, especially one built specifically to check content before it reaches a human who will rely on it — and this kind of quiet downgrade is exactly the failure mode that late-session fatigue produces (trusting that a prior check was sufficient instead of actually looking).

## Links
- relates, 2026-08-16-good-faith-adversarial-review-skill-first-run-caught-real-issues.md, the real-batch run this decision produced instead of a synthetic benchmark.
