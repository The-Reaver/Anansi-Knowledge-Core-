---
id: 2026-08-23-preemptive-secret-scan-recheck-before-commit-on-recurring-topic
type: decision
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"promote and push\"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output."
project: fleet
tags: [git, pre-commit-hook, secret-scan, false-positive, knowledge-core, process]
sources:
  - ref: "Assistant turn, before handing over a commit command for 5 ratified notes: \"Let me re-verify these are clean against the secret-scan pattern one more time before handing you a commit command, given how many times this exact topic has tripped that hook already.\""
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [940, 945]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# After the secret-scan false-positive pattern had tripped the same pre-commit hook three times in one session, the practice shifted to proactively re-checking notes for the flagged shape before attempting a commit, instead of reacting only after the hook blocked it

- id: 2026-08-23-preemptive-secret-scan-recheck-before-commit-on-recurring-topic
- type: decision
- status: ratified
- ratified: 2026-08-23 — operator directly ratified via explicit operator instruction ("promote and push"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output.
- class: believed-unconfirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 901-978
- confidence: medium, one directly observed instance of the proactive check; not yet established as a standing rule anywhere in the repo's tooling
- verified: 2026-08-23
- tags: git, pre-commit-hook, secret-scan, false-positive, knowledge-core, process

## Body

Before this session, the same repo pre-commit secret-scan hook had already been tripped twice earlier by notes describing a token-assignment-shaped false-positive pattern, and a third time by a Knowledge Core note whose entire subject was that exact pattern (see the linked note on that third recurrence). When the operator asked to commit and push a newly ratified batch of 7 notes on the same general topic, the practice changed from reactive to proactive: before handing over a commit command, the notes were re-checked against the secret-scan pattern one more time specifically because of how many times this exact topic had already tripped that hook, and only handed over as a ready-to-run commit after confirming they were clean.

This is a single observed instance of the habit, not a codified rule (no repo tooling enforces a pre-commit grep pass before attempting `git commit`) — recorded as `believed-unconfirmed` because it reflects one session's in-context judgment call rather than a verified standing practice. The underlying reasoning is sound and reusable: when a batch of content is topically about a pattern a blunt scanner is known to flag, a self-check against that same pattern before the first commit attempt saves a round trip through a failed commit and manual rewording.

## Links
- extends, 2026-08-23-secret-scan-false-positive-recurred-inside-note-describing-itself.md, the third recurrence that prompted this proactive habit; that note documents the reactive fix (reword to prose), this note documents the shift to checking before attempting the commit at all.
- relates, 2026-08-22-secret-scan-regex-false-positive-token-assignment-shape-in-code.md, the original two triggers of this same pattern earlier in the session.
