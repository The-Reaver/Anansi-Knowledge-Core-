---
id: refs-stash-is-one-ref-so-a-backup-can-report-success-holding-one-of-five-stashes-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [git, backup, false-green, verification, stash]
supersedes: []
superseded_by: null
---

# A stash backup can report success while capturing one stash of five, because refs/stash is a single ref

## Body

A backup routine reported success having captured 1 of 5 stashes. The cause is a property
of git, not a bug in the script: `refs/stash` is **one ref**. It points at the most recent
stash entry; the older entries exist only as that commit's second-parent reflog chain. Any
backup that enumerates refs — the obvious, correct-looking way to back up a repository —
sees exactly one stash and reports having backed up "the stash", truthfully and
uselessly.

The failure is silent because the count the tool reports is the count it found, and it
found everything it looked for. Nothing errors. The gap only appears when someone
independently asks how many stashes the repo actually has (`git stash list`) and compares.

**Check next time a backup covers stashes:** compare the backed-up stash count against
`git stash list | wc -l` and fail loud on a mismatch. Enumerating refs is not enumerating
stashes. More generally, a count a tool reports about its own work proves only that the
tool is internally consistent — it is not evidence the work is complete.

## Links

- relates-to: git-bundle-verify-reports-ok-on-a-corrupt-bundle-and-a-plain-clone-drops-refs-stash-2026-08-31
- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
