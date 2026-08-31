---
id: concurrent-sessions-on-shared-base-branch-race-2026-08-31
type: finding
status: candidate
source: "This session, 2026-08-31 — merging PR #5 into the-reaver/anansi-knowledge-core-'s base branch while other sessions had open PRs against the same base"
project: fleet
tags: [git, concurrency, merge-conflict, multi-session]
supersedes: []
superseded_by: null
---

# A shared base branch under active concurrent-session merging is a genuinely moving target, not a one-time conflict to resolve

## Body

While preparing to merge one PR into a base branch, the base branch's tip moved three
separate times within a few minutes — other sessions were merging their own PRs into the
same base concurrently. A merge that showed clean seconds earlier came back `dirty`; a
direct merge attempt failed with a 405 "already has merge conflicts" error because another
PR had landed first; a git fetch/ls-remote briefly got blocked by an unrelated tool-permission
classifier mid-sequence. None of this was a bug in any single session — it's the expected
shape of several agents actively landing work on the same branch at once.

**Check next time merging into a base branch known to have other active sessions
targeting it:** re-fetch the base branch's actual current tip immediately before
attempting a merge, don't trust a mergeable-state check from even a minute earlier, and
expect to redo a conflict-resolution pass more than once in a single sitting. Treat a
failed merge attempt as a signal to re-sync, not as an error to work around.

## Links

- relates-to: verify-full-diff-against-pr-changed-files-stat-2026-08-31
