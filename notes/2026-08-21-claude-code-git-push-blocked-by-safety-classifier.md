---
id: 2026-08-21-claude-code-git-push-blocked-by-safety-classifier
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [claude-code, auto-mode, git, safety-classifier, tooling]
sources:
  - ref: "Turns 619-633: line 627 has the agent assuming the remote-add/branch-rename steps of a blocked compound command had succeeded; line 630 is the operator's failed push ('src refspec main does not match any'); lines 631-633 show the agent discovering the whole compound command had been blocked and issuing the corrected sequence."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [619, 633]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Claude Code's auto-mode safety classifier blocked git push mid-task even under a standing "proceed uninterrupted" instruction, and the block aborted the whole compound command
- id: 2026-08-21-claude-code-git-push-blocked-by-safety-classifier
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — directly observed: the agent's own account plus the operator's own terminal output ("error: src refspec main does not match any") confirmed that none of the blocked command's effects (remote add, branch rename) had actually applied
- verified: 2026-08-21
- tags: claude-code, auto-mode, git, safety-classifier, tooling

## Body
After the operator explicitly asked to push a finished project to GitHub and the agent had prepared the repo, `git push` was blocked mid-task by Claude Code's auto-mode safety classifier — a separate guard from the agent's own judgment calls, which flags `git push` as needing explicit human execution even when the operator has granted general autonomy for the surrounding task. The practical trap: the classifier blocked the *entire* compound shell command (which had chained `git remote add origin ...`, `git branch -M main`, and `git push`), not just the push step, so none of the earlier steps in that command actually ran either. The agent initially assumed the remote had been added and only the push itself was withheld, and handed the operator a `git push -u origin main` command that failed ("src refspec main does not match any") because the remote didn't exist and the branch was still `master`. Only after the operator reported the failure did the agent check actual repo state and provide the corrected full command sequence. Lesson: when a classifier blocks a compound command containing `git push`, treat the entire command as not having run and verify actual repo/tool state before handing off follow-up instructions — don't assume the non-push parts of a blocked command succeeded.

## Links
