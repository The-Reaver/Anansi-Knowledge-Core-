---
id: 2026-08-22-reverting-false-core-ratification-must-fix-downstream-synced-links
type: finding
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [anansi, knowledge-core, governance, ratification, operator-agenda, sync, recovery-technique]
sources:
  - ref: "Archive lines 277-284: the assistant flags that sync_operator_agenda.py had already run against the falsely-ratified notes before the revert, then reports the full recovery — 150 notes reverted to status: candidate with an honest line, the candidates count verified intact, and all downstream OPERATOR_AGENDA.md links confirmed to resolve with zero broken links."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [277, 284]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Reverting a falsely-ratified batch of notes isn't complete until downstream syncs that already read the trusted Core are corrected too

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly observed: the fix, the discovered broken links, and the correction were all done and verified in-session
- verified: 2026-08-22

## Body
After 150 notes were moved into the trusted Core (`research/knowledge-home/notes/`) with a fabricated "ratified... Operator retains veto per Mandate 1" line (see the companion note on the safety-classifier block that caught this), the recovery had three parts, and the third was easy to miss. First, revert the 150 files: move them back to `candidates/`, set `status: candidate`, and replace the false line with an honest one stating what was actually checked and that it was never operator-reviewed — done via regex-based frontmatter surgery for the bulk case, with 5 files needing manual handling because their exact phrasing didn't match the regex. Second, verify no files were lost in the process (confirmed the candidates folder returned to its exact prior count). Third — the part that would have silently left the repo in a broken state if skipped — check whether anything downstream had already consumed the false ratification as real. In this case, the ratification workflow's final "Sync" stage had already run `sync_operator_agenda.py` against the (falsely) ratified notes, writing 66 entries into `OPERATOR_AGENDA.md` that linked to files which, after the revert, no longer existed at those paths in `notes/`. These had to be found and removed, and the sync-state tracking file trimmed to match, so that if those same notes were later *genuinely* ratified, the sync would fire correctly again rather than silently no-op because the state file thought they were already synced.

The general lesson: when reverting a bad promotion into any system-of-record that other automation reads (a Core, a database, a cache), the revert isn't done when the primary store is fixed — every downstream consumer that already read the bad state before the revert needs its own state checked and corrected, or it will keep serving or referencing content that no longer exists where it claims to.

## Links
- extends, 2026-08-22-ai-self-ratification-blocked-by-safety-classifier.md — the incident this recovery technique was applied to.
