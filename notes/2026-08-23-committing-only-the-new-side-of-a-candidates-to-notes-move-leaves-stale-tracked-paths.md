---
id: 2026-08-23-committing-only-the-new-side-of-a-candidates-to-notes-move-leaves-stale-tracked-paths
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify\"), given after reviewing an operator-facing review report covering both notes (both read in full, the one cross-referenced link confirmed to resolve, one cosmetic formatting inconsistency found and fixed, no factual errors)."
project: fleet
tags: [git, git-mv, incomplete-move, candidates-notes-lifecycle, self-correction, process]
sources:
  - ref: "Operator asks 'what else is left' (line 1078); assistant finds the prior commit left the 8 old candidates/2026-08-22c-* paths tracked as an uncommitted deletion, stages the removals, and commits the fix as 62f3ee7 (lines 1080-1084)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1078, 1084]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Committing only the new-location half of a candidates-to-notes file move leaves the old paths tracked in git as an unresolved deletion, and this went unnoticed until the next status check surfaced it

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1062-1084
- confidence: high, directly observed in the transcript
- verified: 2026-08-23

After committing the 8 swept-in GEO Suite files (see the companion note on that sweep), the operator asked "what else is left." A routine status check revealed that the assistant's own prior commit had only captured half of a file move: a different, concurrently running session had originally moved 8 files from `candidates/2026-08-22/2026-08-22c-*.md` to their `notes/` equivalents on disk, but the assistant's commit had staged and committed only the new `notes/` copies. The old `candidates/` paths were still tracked in git — showing as deleted-in-the-working-tree-but-not-yet-committed — because nothing had ever staged their removal. Git's history still believed those 8 old files existed even though they no longer did on disk. The assistant caught this itself on the next status pass, explained the gap plainly to the operator, staged the deletions of the stale tracked paths, and committed and pushed that as a separate follow-up commit.

The durable lesson: when committing a file move that spans a rename or a directory relocation (especially one that originated from a different working-tree state, such as another session's edits), verify that both sides of the move are staged — the new path being added and the old path being removed — before committing. Checking `git status --short` for the new file's presence is not sufficient; the old path can remain silently tracked as an uncommitted deletion, and this state persists invisibly until the next status check happens to surface it. This is a variant of the general "verify staged files match exactly before committing" discipline, but specific to two-sided moves: matching the staged set to intent requires confirming removals are included, not just confirming no extra unrelated files crept in.

## Links
- related, 2026-08-23-verify-ratification-provenance-before-sweeping-in-concurrent-session-content.md, the commit in this same stretch whose incomplete staging produced this gap
