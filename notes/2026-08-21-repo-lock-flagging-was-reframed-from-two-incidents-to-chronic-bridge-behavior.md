---
id: 2026-08-21-repo-lock-flagging-was-reframed-from-two-incidents-to-chronic-bridge-behavior
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [repo-hygiene, git, device-bridge, ops-infra, process]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn reframing the checklist's two-incident stale-lock framing as one chronic device-bridge behavior, backed by three ratified Core notes and a standing skill."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Compute/cost strategy + stack/operations + repo hygiene\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [226, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: medium, the root repo's current lock-free state and the workaround pattern are directly confirmed; the exact "~81 mismatched staged changes" root-cause symptom from 2026-08-03 could not be independently re-measured in the same terms today
- verified: 2026-08-21

# The 2026-08-03 checklist's "two separate stale lock incidents, both unresolved" framing is superseded by ratified Core findings that every device-bridge git write leaves a stale lock, with a standing skill-level workaround now in place

## Body

The 2026-08-03 checklist described the root `stag` repo's stale `.git/index.lock` and its ~81 mismatched-staged-changes symptom as a single flagged, unresolved incident sitting on the agenda alongside the separate geo_platform lock. As of 2026-08-21, the root repo has no active blocking lock — `git add`/`git status` both succeed cleanly — but `.git/` contains seven renamed-away `*.lock.stale*` files dated across 2026-08-06 through 2026-08-10, and the Core now holds multiple ratified notes (`2026-08-08-bridge-git-leaves-stale-lock.md`, `2026-08-09-device-bash-cannot-rm-but-can-mv-workaround-for-stale-git-locks.md`, `2026-08-20-read-only-git-checks-can-still-trigger-stale-lock.md`) establishing that this is not a one-off bug but a structural property of every git write (and even some read) operation run through the device bridge: the bridge cannot unlink its own lock file, so the fix is always "rename it out of the way, never delete," and a dedicated skill (`skills/stag-repo-hygiene/SKILL.md`) now formalizes never running git writes through the bridge at all, handing the operator native commands instead. This is a materially different picture from what the checklist described: not two isolated incidents awaiting a cleanup pass, but one recurring environmental behavior that has already been characterized, ratified, and partially mitigated by process (the skill), even though the geo_platform instance is still concretely unresolved today (see companion note, `2026-08-21-geo-platform-git-index-lock-still-active-blocking-18-days-later`). The original "~81 mismatched staged changes" figure specifically could not be re-verified against today's state in the same terms — today's root `git status --short` shows roughly 205 changed/untracked entries, but those are dominated by legitimate new content (research/knowledge-home raw archives, new scripts, PDFs) rather than the index/disk-mismatch symptom the checklist described, so this is not a like-for-like comparison and should not be read as "the problem got worse" without further digging.

## Links
- relates, research/knowledge-home/candidates/2026-08-21/2026-08-21-geo-platform-git-index-lock-still-active-blocking-18-days-later.md
- relates, research/knowledge-home/notes/2026-08-08-bridge-git-leaves-stale-lock.md
- relates, research/knowledge-home/notes/2026-08-09-device-bash-cannot-rm-but-can-mv-workaround-for-stale-git-locks.md
- relates, skills/stag-repo-hygiene/SKILL.md
