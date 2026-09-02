---
id: 2026-08-22-orphaned-duplicate-candidates-rejected-never-deleted
type: decision
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [anansi, knowledge-core, governance, orphaned-duplicate, rejection-policy, ratify.py]
sources:
  - ref: "Archive lines 631-636: the operator reports a real 'a file already exists' collision at notes/2026-08-11-cloud-sandbox-green-does-not-prove-native-green-real-instance.md; the assistant explains the orphaned-duplicate cause and confirms the candidate was rejected (not deleted) and disappeared from every pending list."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [631, 636]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Orphaned-duplicate candidate notes (same content already ratified elsewhere) get rejected with the specific twin cited, never deleted

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly observed and executed in-session for 26 total files across three batches
- verified: 2026-08-22

## Body
An "orphaned duplicate" candidate note is a file still carrying `status: candidate` in `research/knowledge-home/candidates/` whose exact `id`, or whose content, already exists as `status: ratified`/`status: note` in `research/knowledge-home/notes/` — a stale leftover from before that ratification happened (or, in one case, an earlier version later superseded by a corrected/re-verified rewrite under a different filename). Ratifying such a file directly fails ("a file already exists" at the destination path), so the established handling is: reject it via `ratify.py`/the dashboard (status flips to `rejected`, file stays in place, never deleted), with the reason citing the specific ratified twin or successor by filename, confirmed via an actual file comparison rather than assumed from the filename pattern alone. This was applied across three batches this session: 2 individual 2026-08-11 notes the operator named directly, then 13 files in `_promoted-to-notes-2026-08-09/` (11 exact-filename twins already in `notes/`, plus a "nova" pair confirmed superseded by reading both sides), then 11 files in `_archived-mythology-2026-08-09/` that the folder's own README had already characterized as fabricated governance content.

Two verification disciplines were followed throughout, worth keeping as the standard: never bulk-reject on a folder name or pattern alone — each file's claimed duplicate/superseded status was individually confirmed (reading both the candidate and its supposed twin, or grepping for the twin's existence) before rejecting; and a rejection reason should state what was actually found, not just copy a blanket framing that turns out not to hold for every file in the batch (see the companion note on two files in this same sweep where the README's fabrication claim didn't survive direct verification).

## Links
- relates, 2026-08-22-ratify-py-cli-missing-underscore-folder-exclusion-dashboard-had.md — the bug fix that surfaced the 24-file batch handled here.
- relates, 2026-08-22-dashboard-candidate-list-shadowed-by-deduped-notes-dict.md — the earlier bug that hid the first 2 orphaned duplicates from the dashboard.
- relates, 2026-08-22-readme-fabrication-framing-didnt-hold-for-two-of-eleven-notes.md — the verification-before-bulk-reject discipline applied to one batch in this sweep.
- extends, 2026-08-20-rejected-candidates-never-deleted-status-flipped-in-place-rule.md — the general "never delete, flip status in place" rule this decision follows.
