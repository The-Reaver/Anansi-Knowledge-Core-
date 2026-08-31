---
id: backups-cover-committed-history-only-so-uncommitted-working-trees-are-covered-by-nothing-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — VERIFIED directly against The-Reaver/Stag-Fleet at branch anansi-home-dashboard (b19dd5f), cloned and inspected; the claim as relayed is largely superseded by the code"
project: fleet
tags: [backup, working-tree, data-loss, uncommitted, coverage-gap]
supersedes: []
superseded_by: null
---

# The backup captures committed history, so roughly 112 uncommitted files across the project repos are protected by nothing

## Body

> **CORRECTION -- mostly already fixed.** `scripts/backup_fleet.py` on this branch already
> does what the relayed claim says is missing. `capture_working_tree()` (line 205) writes
> `git diff HEAD` as a patch **plus** a list of untracked-but-not-ignored paths. Stashes are
> exported **individually** by walking `git stash list`, and its own docstring documents the
> 1-of-5 incident as the reason. Bundles are verified by **actually cloning them and comparing
> against the live source**, not by `git bundle verify` alone.
>
> **What remains true:** it is **not scheduled** -- the script says so itself, printing what a
> scheduled invocation would look like and calling scheduling "an operator decision, not made
> by this script". So it is still a snapshot someone runs, not a mechanism.
>
> **The one real remaining gap** is narrower than claimed: untracked files are captured as
> **paths only, no contents**. A new file never `git add`-ed is listed in the backup and its
> contents are not in it.


The backup bundles committed history. Across the project repos there are roughly **112
uncommitted files** — 44 in one repo alone — and none of them is covered. They exist in
exactly one place: the disk the backup exists to insure against losing.

The gap is easy to miss because the backup is not broken. It captures precisely what it was
built to capture and reports success honestly. Coverage was simply defined as "the
repositories", and a repository's *working tree* is not part of its history until someone
commits.

This is the same shape as the stash defect — a backup enumerating refs and truthfully
reporting one stash of five. In both cases the tool's scope and the operator's mental model of
"backed up" differ, and nothing surfaces the difference.

**Three fixes, in order:** capture working-tree state for project repos, not just committed
history; schedule the backup so it is a mechanism rather than a snapshot someone took once;
and assert the off-machine sync actually completed, since a backup living on the disk it
protects is not a backup. A quarterly restore drill from the bundle alone proves all three,
on a cadence rather than once.

## Links

- relates-to: refs-stash-is-one-ref-so-a-backup-can-report-success-holding-one-of-five-stashes-2026-08-31
- relates-to: git-bundle-verify-reports-ok-on-a-corrupt-bundle-and-a-plain-clone-drops-refs-stash-2026-08-31
- relates-to: a-stale-git-lock-froze-a-repo-for-29-days-without-erroring-2026-08-31
