---
id: 2026-08-22-readme-fabrication-framing-didnt-hold-for-two-of-eleven-notes
type: finding
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [anansi, knowledge-core, governance, verification, epistemics, mandate-17]
sources:
  - ref: "Archive lines 687-691: the assistant reports that, despite the folder README's blanket 'fabricated' framing, the two Mandate 17 notes check out against a real governance/mandates.json entry (id 17, 'The Hot Gates, and Anubis within it'), so those two get an honest 'redundant with the real registry entry' rejection reason instead, and confirms all 11 rejected."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [687, 691]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A folder's own README calling its contents fabricated didn't hold up for 2 of 11 files on direct verification — the real Mandate 17 entry existed in governance/mandates.json

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly verified by reading governance/mandates.json and confirming mandate id "17" ("The Hot Gates, and Anubis within it") is live with real mechanism citations
- verified: 2026-08-22

## Body
`research/knowledge-home/candidates/_archived-mythology-2026-08-09/` holds 11 candidate notes its own README lumps together as "governance apparatus describing itself" — self-mythologizing content from a batch already independently found to contain fabricated per-persona verdicts ("seven independent reviewer" verdicts actually written by one model across multiple passes) and an unreconciled ruling-run claim ("223 agents, 43 promoted" with no corroborating trace elsewhere in the repo). When the operator instructed "reject all 11," rather than copying the README's blanket framing onto every file, each was checked individually first. Nine held up under the README's fabrication characterization (7 presentation-mode verdicts, 1 unreconciled ruling-run note, matching the prior independent finding). Two did not: a pair of notes describing "Mandate 17" turned out to reference something real — Mandate 17 ("The Hot Gates, and Anubis within it") is live today in `governance/mandates.json` with genuine citations to actual mechanism files, not an invented governance claim. Those two were still rejected (per the operator's instruction, and because they were redundant with the real registry entry), but with an honest reason — "redundant with the real registry entry" — rather than the "fabricated" framing that was accurate for the other nine.

The general lesson: a source document's own self-critical characterization of a batch of content (a README calling its own folder's contents fabricated) is still a claim to verify per-item, not a label to apply uniformly to everything inside it. A folder-level narrative can be correct in aggregate — 9 of 11 here really were fabricated — while still being wrong about specific items inside it, and the fix is not to leave the exception unrejected but to give it its own accurate reason rather than inheriting a characterization that doesn't hold for it specifically.

## Links
- extends, 2026-08-22-orphaned-duplicate-candidates-rejected-never-deleted.md — the broader rejection sweep this correction was applied within.
