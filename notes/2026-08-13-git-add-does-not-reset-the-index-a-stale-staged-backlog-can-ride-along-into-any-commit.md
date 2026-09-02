---
id: 2026-08-13-git-add-does-not-reset-the-index-a-stale-staged-backlog-can-ride-along-into-any-commit
type: finding
status: ratified
ratified: "2026-08-13, operator instruction, direct re-verification by this session's Claude; the recovery technique described below was proven live on the real incident, not asserted -- file-count and mtime evidence, a byte-identical tree check before any force-push, and a successful push confirmed after"
project: fleet
tags: [fleet, git, governance, stale-stage, incident, recovery-technique, worktree, force-push, structural-lesson]
sources:
  - ref: "git log, git reflog, git diff --cached --stat against the real Stag-Fleet anansi-home-dashboard branch, commits 9da7014 through 2f77448"
    reliability: high
    origin: run live, this session, against the actual incident
  - ref: "operator message, 2026-08-12/13, naming the root cause directly (a cloud/dispatch chat committing and pushing whatever was staged)"
    reliability: high
    origin: direct operator report, this session
provenance:
  archive: research/knowledge-home/raw/2026-08-12-geo-poller-fix-and-platform-identity-session.jsonl
  turns: [1, 30]
risk_class: B
evidence_state: CORROBORATED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# `git add <path>` only ever adds to the index, never resets it -- a days-old stale-staged backlog rode along into an unrelated one-file commit and got pushed before anyone reviewed it

## Body

The operator caught this from the outside ("this is my fault again, started a cloud chat and it
committed and pushed whatever was there") before this session had fully diagnosed it -- a real
signal that this failure mode is recognizable and recurring, not a one-off.

**Root cause, confirmed by file mtimes, not assumed:** every one of the 538 unexpected files had a
filesystem modification time from 2026-08-07 through 2026-08-10, days before the commit that swept
them in. This matches an established fleet pattern documented elsewhere ("Anti-Gravity batches are
left uncommitted for the operator to review and commit after Amadeus verifies") -- the backlog was
real, finished work waiting for a review checkpoint that simply never happened, not corruption and
not someone else's live in-progress edits.

**Structural lesson:** a commit always commits everything currently staged, not just what the most
recent `git add` touched. In a shared working tree where sessions come and go, "nothing I explicitly
added" is not the same as "nothing staged" -- check `git diff --cached --stat` before every commit,
not just after something looks wrong.

**Recovery, done safely on a shared, already-pushed branch:**
1. `git reset --soft HEAD~1` to uncommit while keeping everything staged, exactly reproducing the
   pre-commit state.
2. Partitioned the staged file list into logical, honestly-described buckets by top-level directory
   (confirmed the partition was exhaustive -- bucket file counts summed to the original total).
3. Committed each bucket separately with a message that says what's actually in it and states
   plainly that the content was recovered, not authored, and was not independently reviewed.
4. **First attempt was interrupted mid-recovery** by a `git pull --rebase` this session did not
   initiate -- almost certainly a second concurrent session touching the same branch. Because the
   split commits' combined content exactly matched the still-pushed mega-commit, git's rebase
   machinery silently dropped all of them as empty. No content was lost (the mega-commit still had
   everything), but the attribution work was discarded. Session paused there since the operator had
   to leave -- mid-git-surgery is not a state to leave unsupervised.
5. **Resumed later with the operator present**, using an isolated `git worktree` (not a branch
   switch in the main checkout) specifically so a second concurrent session's live uncommitted edits
   in the main working tree were never touched or put at risk. Rebuilt the split history there,
   cherry-picking the surviving commit SHAs from git's reflog (still resolvable weeks after being
   orphaned, since nothing had run `git gc` yet).
6. **The one verification step that made the force-push safe to do at all:** `git diff <old-tip>
   <new-tip> --quiet` confirmed the rebuilt history's final tree was byte-identical to what was
   already live, before touching anything real. A force-push that changes content is a real risk; a
   force-push that only changes which commits produced identical content is not.
7. Force-pushed with `--force-with-lease` (not bare `--force`), re-fetching immediately beforehand
   to confirm the remote hadn't moved again -- fails safely instead of blindly overwriting if a third
   session had pushed in the meantime.
8. Local branch pointer moved via `git update-ref` directly, not `git reset --hard` -- since the
   final tree was proven identical, this changes zero working-tree bytes, which mattered because the
   main working tree still held a second concurrent session's live uncommitted edits that a hard
   reset would have destroyed.

**Fixed the same day, in code, not just this note:** `scripts/gates/stale_stage_guard.py`, a new
pre-commit hook -- see the companion note on that gate for detail.

## Links

- extends, 2026-08-12-two-platforms-not-to-conflate-geo-suite-is-stag-geo-platform-not-base-platform.md
  -- same session, same instinct (verify the real state directly rather than trust the visible
  surface) applied to a different problem.
- depends, `scripts/gates/stale_stage_guard.py` -- the coded fix this incident produced.
- relates, `stag-fleet-mega-commit-split-recovery.md` (Claude's own persistent memory, not an Anansi
  note) -- the full SHA-level recovery log kept there during the interrupted first attempt.
