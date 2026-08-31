---
id: git-bundle-verify-reports-ok-on-a-corrupt-bundle-and-a-plain-clone-drops-refs-stash-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [git, backup, restore, false-green, verification, bundle]
supersedes: []
superseded_by: null
---

# The check meant to catch a bad backup was itself a false green, one layer down

## Body

Two defects stacked. `git bundle verify` returned "is okay" on a bundle that was
corrupted — the command validates the bundle's prerequisites and header, not that every
object in it is intact and restorable. Separately, a plain `git clone` from a bundle
silently drops `refs/stash`, because clone fetches `refs/heads/*` and `refs/tags/*` and
stash is neither.

So the restore drill — the control whose entire job is to prove the backup is real —
passed on a corrupt bundle and, even on a good one, would have restored a repository
missing the stashes the backup was supposed to protect. A verification step that shares a
blind spot with the thing it verifies is not verification; it is a second copy of the same
assumption.

**Check next time a backup is declared verified:** the restore drill must compare the
restored repository against the source by content — ref-by-ref counts including
`refs/stash`, and object counts — not merely exit zero from `git bundle verify`. And ask
of any control: what would it look like if this check were the broken one? If the answer
is "identical", the check is not yet a control.

## Links

- relates-to: refs-stash-is-one-ref-so-a-backup-can-report-success-holding-one-of-five-stashes-2026-08-31
- relates-to: defence-in-depth-can-conceal-a-hole-in-the-rule-under-test-2026-08-31
