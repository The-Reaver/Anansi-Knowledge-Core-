---
id: 2026-08-23-proactive-self-flagging-of-authority-deviation-enabled-fast-correction
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"I ratify this\"), given after reviewing an operator-facing note-by-note review report covering all 3 (all 3 read in full, the one external cross-referenced link confirmed to resolve, no factual errors found)."
project: fleet
tags: [process, governance, self-disclosure, git, operator-preference]
sources:
  - ref: "Assistant turn after committing/pushing directly via Bash instead of handing commands back: \"One thing worth flagging: this time I ran git commit and git push directly myself via the Bash tool, instead of handing you PowerShell commands to run like every other commit this session... If that's not what you wanted going forward, say so and I'll go back to handing you commands instead of executing them.\" Operator's very next message: \"hand git commands back to me from now on\""
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1007, 1013]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Proactively disclosing an unrequested deviation from standing practice, right after taking the action, let the operator correct course within one message instead of the deviation going unnoticed
- id: 2026-08-23-proactive-self-flagging-of-authority-deviation-enabled-fast-correction
- type: finding
- status: ratified
- ratified: 2026-08-23 — operator directly ratified via explicit operator instruction ("I ratify this"), given after reviewing an operator-facing note-by-note review report covering all 3 (all 3 read in full, the one external cross-referenced link confirmed to resolve, no factual errors found).
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 979-1029
- confidence: high, directly observed in the transcript
- verified: 2026-08-23
- tags: process, governance, self-disclosure, git, operator-preference

## Body
When the assistant ran `git commit` and `git push` directly (rather than handing the commands back to the operator, which had been the standing pattern all session) after interpreting "promote and push" as authorizing the full pipeline, it did not stay silent about the interpretive leap. After confirming the push landed, it appended an unprompted disclosure to its own report: it had executed git directly instead of handing off commands as usual, explained the reasoning for reading "promote and push" as authorization, named this as a real departure from the session's standing pattern, and explicitly invited a correction if that was not wanted. The operator corrected it on the very next message. Because the deviation was surfaced immediately and specifically (what changed, why, and an explicit ask for confirmation) rather than buried in a generic status update, the correction cycle took a single exchange instead of the drift persisting silently across future commits.

The durable lesson: when an instruction is ambiguous enough that the assistant has to choose an interpretation that expands its own authority beyond the recent standing pattern, flag the specific deviation and its rationale immediately after acting, rather than assuming silence means it was fine. This is what made the subsequent preference-reversal cycle (see companion note) fast and low-cost rather than a repeated, unnoticed overreach.

## Links
- related, 2026-08-23-git-execution-preference-is-live-and-reversible-within-session.md, the correction this disclosure directly triggered
