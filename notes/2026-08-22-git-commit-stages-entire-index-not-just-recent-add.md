---
id: 2026-08-22-git-commit-stages-entire-index-not-just-recent-add
type: finding
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [git, pre-commit-hook, staging-index, gotcha, multi-session-repo]
sources:
  - ref: "Archive lines 702-703: the actual pre-commit hook failure output ('Secret detected in staged files... Blocked: Possible Generic Secret found in staged file: AJ/agent_breakers/selftest/test_dummy_app.py') from a scoped git add, followed by the assistant diagnosing that git commit operates on the whole staged index, not just the recent add, and prescribing git reset then a rescoped add."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [702, 703]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# `git commit` commits everything currently staged, not just the files a preceding `git add` just added — an unrelated already-staged file with a flagged secret blocked an otherwise-clean commit

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly observed: the exact pre-commit hook failure message was captured, and the fix (git reset, then a scoped git add) was confirmed to produce a clean commit of only the intended files
- verified: 2026-08-22

## Body
In a repo where more than one working session/context can leave files staged (here: a concurrent Claude Code session had staged, but not committed, a large unrelated batch including `AJ/agent_breakers/selftest/test_dummy_app.py`), running `git add <specific files>` followed by `git commit -m ...` does not scope the commit to just those specific files — `git commit` operates on the entire current index, including anything staged earlier by a different process or session. In this session, a carefully-scoped `git add` of exactly 25 intended files still produced a pre-commit hook failure ("Secret detected in staged files... Blocked: Possible Generic Secret found in staged file: AJ/agent_breakers/selftest/test_dummy_app.py") because that unrelated file was already sitting staged in the index from before this `git add` ran.

The fix is `git reset` (no pathspec, no `--hard`) to unstage everything without touching any working-tree file content, then re-run the intended scoped `git add`, then verify with `git status --short` that only the intended files are staged before committing. This is safe specifically because plain `git reset` only affects the index, not file contents — nothing from the other session's in-progress work is lost by doing this.

General rule for any repo where staging can be shared across concurrent sessions or interrupted work: before committing a carefully-scoped set of files, confirm via `git status --short` that the staged set matches expectations exactly, rather than assuming a recent `git add` fully determines what a following `git commit` will include.

## Links
- relates, 2026-08-22-secret-scan-regex-false-positive-token-assignment-shape-in-code.md — the specific flagged file this incident involved, and why the flag itself was a false positive on a legitimate test fixture.
