---
id: 2026-08-22-ratify-py-cli-missing-underscore-folder-exclusion-dashboard-had
type: finding
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [anansi, knowledge-core, ratify.py, anansi-hub, bug, filtering, archival-folders]
sources:
  - ref: "Archive lines 644-653: the assistant discovers ratify.py's list/review commands lack the underscore-folder exclusion the dashboard already had, surfacing 24 phantom candidates in _archived-mythology-2026-08-09/ and _promoted-to-notes-2026-08-09/, then confirms the CLI and dashboard agree after the fix."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [644, 653]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# ratify.py's CLI list/review commands surfaced 24 archived/already-promoted notes as if they were live pending work, because they lacked a filter the dashboard already had

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly observed and fixed in-session; confirmed both tools agree after the fix
- verified: 2026-08-22

## Body
`research/knowledge-home/candidates/` contains dated folders of real pending work alongside a few underscore-prefixed administrative folders (`_archived-mythology-2026-08-09/`, `_promoted-to-notes-2026-08-09/`, `_to_delete/`) that hold stale, retired, or test-fixture content — not live candidates. The Anansi Hub dashboard's `/api/candidates` endpoint already excluded any file whose immediate parent folder starts with `_` (added earlier the same session, after test fixtures like `__gate_test__` in `_to_delete/` briefly appeared as if pending). The standalone `scripts/knowledge_home/ratify.py` CLI script — built to let the operator ratify/reject notes directly without an AI session — was never given the same exclusion. Running `ratify.py list --status candidate` with no date filter surfaced 24 phantom "pending" notes: 13 in `_promoted-to-notes-2026-08-09/` (stale `status: candidate` copies whose content had already been promoted into `notes/` under the same or a superseding filename) and 11 in `_archived-mythology-2026-08-09/` (content the folder's own README already documented as illegitimate/fabricated). The dashboard correctly showed zero pending candidates the whole time; the CLI disagreed with it. The fix was a one-line filter added to `ratify.py`'s file-listing logic, matching the dashboard's existing behavior exactly.

The general lesson: when the same underlying data is exposed through two independent interfaces (a CLI and a dashboard here), a filtering rule added to one after a real bug is found needs to be explicitly ported to the other — building both from a shared library doesn't guarantee shared list/filter logic if the two interfaces implement listing separately, and the two surfaces silently disagreeing is itself the signal worth checking for.

## Links
- relates, 2026-08-22-dashboard-candidate-list-shadowed-by-deduped-notes-dict.md — an earlier, opposite-direction bug in the same feature area (the dashboard once silently hid real candidates instead of showing phantom ones).
- relates, 2026-08-22-orphaned-duplicate-candidates-rejected-never-deleted.md — what was done with the 24 notes this fix uncovered.
