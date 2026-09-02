---
id: 2026-08-21-refuse-single-commit-message-across-heterogeneous-changes
type: decision
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [git, commit-hygiene, agent-behavior, ambiguity, stag-practice]
sources:
  - ref: "STAG session transcript, 2026-08-12: agent asked to commit uncommitted changes with 'a sensible message,' finds ~280 changed/untracked entries spanning unrelated work streams, refuses to write one message, asks the operator to scope it, and makes no commit"
    reliability: high
    origin: "2026-08-12 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-f4358951.jsonl
  turns: [3, 12]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# When asked to commit "uncommitted changes" that span unrelated work streams, refuse to invent one sensible message and ask for scoping instead
- id: 2026-08-21-refuse-single-commit-message-across-heterogeneous-changes
- type: decision
- status: ratified
- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- class: confirmed
- source: STAG session, 2026-08-12, "Awaiting instructions" (backfilled from historical transcript f4358951, 2026-08-21)
- confidence: high, directly observed agent behavior and stated reasoning in the transcript, not an inference
- verified: 2026-08-21
- tags: git, commit-hygiene, agent-behavior, ambiguity, stag-practice

## Body
In this session the operator asked the agent to "commit my uncommitted changes with a sensible message and push the current branch to the remote." On inspecting the repo, the agent found roughly 280 changed/untracked entries spanning clearly unrelated work: a security-bug curriculum, knowledge-home note ratification files, curriculum deliverables, two `.docx` briefs, session handoff files, a `skills/` directory, and two directories that looked like scratch output (`_discrim_scratch/`, `_leveling_proof_scratch/`). Rather than writing one blanket commit message covering all of it, or guessing at how to split the scratch directories, the agent stopped and asked the operator how to handle the scope, explicitly reasoning that "one 'sensible message' won't honestly describe all of that." No commit or push was made in this session as a result. The durable practice: when a commit request's diff spans genuinely unrelated concerns, treat that as a scoping question for the operator rather than fabricating a single message or silently splitting the work on a guess — this is consistent with the repo's existing git-safety guidance to review broad `git add` results and avoid unrequested destructive/irreversible actions.

## Links
- relates-to, stag-fleet-mega-commit-split-recovery (memory note, not a knowledge-home file), an earlier incident where an unscoped 541-file commit had to be split and force-pushed after the fact — this session's refusal is the preventive version of that lesson.
