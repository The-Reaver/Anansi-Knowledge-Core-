---
id: 2026-08-23-git-execution-preference-is-live-and-reversible-within-session
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"I ratify this\"), given after reviewing an operator-facing note-by-note review report covering all 3 (all 3 read in full, the one external cross-referenced link confirmed to resolve, no factual errors found)."
project: fleet
tags: [git, operator-preference, governance, process, standing-rule, self-correction]
sources:
  - ref: "Operator says 'check on the distillation agent. promote and push'; assistant runs git commit/push directly and flags the departure; operator says 'hand git commands back to me from now on'; assistant saves that as a standing rule; operator reverses within the same minute with 'i want you to execute the commands', and the assistant updates its own memory note to reflect the reversal"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [986, 1020]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# An operator's stated preference for who runs git commands (assistant directly vs. handed back to the operator) can flip twice within the same minute and must be treated as live state, not a permanently locked-in rule after one correction
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 979-1029
- confidence: high, directly observed in the transcript with exact operator wording and timestamps
- verified: 2026-08-23

REVIEW: high-impact

## Body
In this STAG-repo session on 2026-08-23, the assistant had been handing every git command back to the operator to run themselves for the whole session (the long-standing practice). Given the instruction "check on the distillation agent. promote and push," the assistant interpreted "promote and push" as authorization for the full pipeline and ran `git add`, `git commit`, and `git push` directly through its own Bash tool access, then proactively told the operator it had done so and that this was a departure from the session's standing pattern. The operator's very next message was an explicit correction: "hand git commands back to me from now on." The assistant acknowledged this and wrote it to its own separate cross-session memory system as a standing rule. Within roughly the same minute, the operator reversed again: "i want you to execute the commands" — meaning go back to running git directly. The assistant complied and also went back and edited its own memory-system note (both the note body and its one-line index entry) to describe the git-execution preference as a live, flippable setting rather than a fixed rule.

The durable lesson: a single operator correction about execution-vs-handback authority should not be encoded as a permanent policy after only one instance — it can be reversed again immediately, and the assistant needs to track "whatever was said most recently" rather than defaulting to either side once a correction has been given. This applies to any similarly execution-adjacent operator preference (not just git), and argues for keeping such preferences as explicitly timestamped/versioned state rather than baking the first correction in as gospel.

## Links
- related, 2026-08-23-concurrent-session-unreviewed-content-not-swept-into-ambiguous-run-it.md, same incident's follow-on where the reinstated direct-execution preference was tested against an ambiguous instruction
