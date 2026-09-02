---
id: 2026-08-23-editing-staged-file-does-not-restage-must-re-add-before-retry-commit
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i hereby ratify these notes\"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [git, pre-commit-hook, staging-index, gotcha]
sources:
  - ref: "git commit -F commit_msg.txt fails again with 'PRE-COMMIT HOOK: Secret detected in staged files' on a note the assistant had already fixed in the working tree; assistant explains the hook reads the staged blob not the working tree and re-adds before retrying; operator confirms 'it worked'"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [861, 866]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Editing a file after `git add` has already staged it does not update what is staged — a pre-commit hook re-run against the same stale staged blob will fail identically until you re-`git add` the fixed file
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 784-900
- confidence: high — directly observed: a fix was applied to a staged file's working-tree content, `git commit` was retried, and the exact same pre-commit hook failure recurred until the file was explicitly re-`git add`-ed
- verified: 2026-08-23

## Body
A commit was blocked by a pre-commit secret-scan hook flagging one staged file. The fix (rewording that file's content to remove the false-positive-triggering text) was made directly to the file on disk, and a second unrelated cosmetic bug was fixed across all 13 staged files at the same time. `git status --short` was checked and still showed the same 13 files staged, so the commit was retried directly — and it failed with the exact same hook error on the exact same file, even though the working-tree content had genuinely already been corrected.

The cause: `git add` stages a snapshot (a blob) of a file's content at the moment it is run. Editing the working-tree file afterward changes the file on disk but does not change what is already in the index — the pre-commit hook reads the staged blob (effectively `git show :path`), not the current working-tree content. `git status --short` showing the file as staged does not by itself confirm the staged content is current; it only confirms the path is tracked as staged, regardless of which version.

The fix was to explicitly re-run `git add` on the corrected file(s) before retrying the commit, which re-snapshots the current working-tree content into the index. After that, the commit succeeded.

General rule: whenever a staged file's working-tree content is edited after it was staged — including edits made specifically to satisfy a pre-commit hook that just failed — re-`git add` that file before retrying the commit. Do not assume `git status` showing a path as "staged" means the staged content reflects a just-made edit.

## Links
- extends, 2026-08-22-git-commit-stages-entire-index-not-just-recent-add.md — same root fact (a commit operates on the index, not the working tree, and not on assumptions about what a recent `git add` covers); that note's incident was an unrelated already-staged file from a different session, this one is a self-inflicted stale snapshot of the very file being edited to fix the problem.
- relates, 2026-08-13-git-add-does-not-reset-the-index-a-stale-staged-backlog-can-ride-along-into-any-commit.md — the same "index is a snapshot, not a live view of the working tree" principle, applied earlier to a much larger stale-backlog incident.
