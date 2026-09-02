---
id: 2026-08-22-dashboard-candidate-list-shadowed-by-deduped-notes-dict
type: finding
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [anansi-hub, dashboard, bug, dedup, orphaned-duplicate, filtering]
sources:
  - ref: "Archive lines 555-562: assistant finds the root cause (two real 2026-08-11 candidates shadowed because the shared NOTES dict dedupes by id, 'first folder wins') and begins rewriting the endpoint to scan disk directly via a new _candidate_paths() helper."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [555, 562]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The Anansi dashboard's first candidate-list endpoint silently hid real candidates because it filtered a deduped in-memory dict instead of scanning disk

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly observed and fixed in-session; confirmed the fix surfaced exactly the two real missing notes
- verified: 2026-08-22

## Body
`anansi_hub.py` keeps a global `NOTES` dict, built by `reload_data()`, that reads `notes/` before `candidates/` and dedupes by note `id` — "first folder wins," so if a candidate's id already exists as a ratified note elsewhere, the candidate copy is invisible in `NOTES`. The first version of the new `GET /api/candidates` endpoint (built to power a Ratify page in the dashboard) filtered this same `NOTES` dict for `status: candidate` entries. That silently hid any orphaned-duplicate candidate — a stale `candidates/` copy whose `id` already existed as `status: ratified` in `notes/` — from the dashboard entirely, since the deduped dict never contained the candidates/ version in the first place. This was caught by testing: two genuine 2026-08-11 candidate notes were known to exist on disk but did not appear in the endpoint's output. The fix was to stop relying on the shared, deduped `NOTES` dict for this feature and instead scan disk directly (`_candidate_paths()`, using `glob` over the candidates folder and checking each file's own frontmatter for `status: candidate`), with a paired `_find_candidate_path()` helper so the ratify/reject endpoints also stopped depending on the shadowed dict.

The general lesson: an in-memory index built for one purpose (fast, deduped lookup by id, "most authoritative copy wins") can be actively wrong for a different purpose (finding every file matching a status, including ones the dedup logic is specifically designed to suppress). Reusing a shared cache/index for a new feature needs to be checked against what that index's own dedup/precedence rules would hide, not just whether it returns *some* data — a query that returns fewer, wrong results is easy to mistake for "just an empty case" until tested against a known non-empty example.

## Links
- relates, 2026-08-22-ratify-py-cli-missing-underscore-folder-exclusion-dashboard-had.md — a later, opposite-direction bug in the same feature area (the CLI over-showed rather than under-showed).
- relates, 2026-08-22-orphaned-duplicate-candidates-rejected-never-deleted.md — the two specific notes this bug hid, and how they were resolved once found.
