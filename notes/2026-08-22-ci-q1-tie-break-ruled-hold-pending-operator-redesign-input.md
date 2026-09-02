---
id: 2026-08-22-ci-q1-tie-break-ruled-hold-pending-operator-redesign-input
type: decision
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [compliance-intelligence, brain-trust, governance, decision, q1-tie-break]
sources:
  - ref: "Archive lines 298-301: assistant explains the 3-3 Brain Trust split on Q1 (SHIP_WITH_CONDITIONS vs HOLD), the operator's verbatim ruling ('hold because i have a lot to add to that. i have uploaded a document that must be put through our review process'), and the assistant recording Q1 as ruled HOLD, independent of Q2."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [298, 301]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Operator broke the CI Q1 3-3 Brain Trust tie: RULED HOLD, pending the operator's own redesign input via uploaded architecture documents

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — direct operator ruling, recorded in reports/STAG_BRAIN_TRUST_LEDGER.md in-session
- verified: 2026-08-22

REVIEW: high-impact

## Body
The 2026-08-08 Brain Trust review of Compliance Intelligence's legal-source retrieval and currency mechanism deadlocked 3-3 on Q1 (ship vs. hold) and was referred to the operator, with Sentinel's dissent insisting a tie must not default to "proceed" and must be broken on the state of the running system today, not the roadmap. The underlying split: the running code (`kb/atoms.py`) only supports CI's old, simpler promise to the partner attorney (grounded in real law); it's missing the schema fields the newer promise (kept current, correctable) depends on, and `STATUS.md`'s "15/15 green" claim tests the old schema, not the one the newer promise needs. Three seats read this as normal build sequencing (SHIP_WITH_CONDITIONS); three read it as the core promise currently being false, not a "later" problem (HOLD).

This session, after being walked through the tie-break in plain language, the operator ruled: **HOLD**, explicitly tying the hold to wanting to incorporate substantial input from two uploaded architecture documents ("hold because i have a lot to add to that. i have uploaded a document that must be put through our review process"). The ruling was recorded as a follow-up row in `reports/STAG_BRAIN_TRUST_LEDGER.md`. This ruling covers only Q1 (the legal-retrieval/currency mechanism's ship-readiness) — it does not affect Q2 (the separate emergency security fix for unauthenticated KB endpoints and active-by-default atoms), which had already CARRIED 4-0-2 as "not blocked, proceed immediately" and continued independently of this hold.

## Links
- resolves, 2026-08-08-stag-brain-trust-on-ci-legal-retrieval-currency-q1-deadlocke.md — the original 3-3 deadlock this ruling breaks.
- relates, 2026-08-22-ci-q2-emergency-security-fix-shipped-auth-signoff-authority-tier-history.md — the separate, unblocked Q2 fix that shipped the same session, independent of this HOLD.
