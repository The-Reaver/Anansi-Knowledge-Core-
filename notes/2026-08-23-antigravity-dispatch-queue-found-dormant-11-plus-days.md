---
id: 2026-08-23-antigravity-dispatch-queue-found-dormant-11-plus-days
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify\"), given after reviewing an operator-facing review report covering all 7 (all read in full, all 6 unique cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [antigravity, dispatch-queue, inbox, governance, coordination-mechanism]
sources:
  - ref: "Assistant filters the 70-message dispatch history and reports only MSG-FLEET-001 (2026-08-08) carries a queued marker, and the newest message in each of the 5 inbox channels ranges 2026-08-05 to 2026-08-12 (11+ days stale) (lines 1300-1303)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1300, 1303]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The ANTIGRAVITY dispatch-queue inbox system was found dormant: only 1 of 70 historical messages was marked queued, and every channel's newest message was 11+ days old

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1238-1324
- confidence: high, counted directly against the real inbox files rather than assumed
- verified: 2026-08-23
- REVIEW: high-impact

When the operator asked "what's in the queue," the assistant checked the real inbox/dispatch-queue files directly instead of assuming, and found the coordination mechanism itself appears to have gone dormant. Across the 5 ANTIGRAVITY inbox channel files (`ANTIGRAVITY_INBOX.md`, `ANTIGRAVITY_FLEET_INBOX.md`, `ANTIGRAVITY_CI_INBOX.md`, `ANTIGRAVITY_CIPPE_INBOX.md`, `ANTIGRAVITY_GEO_INBOX.md`) there were 70 total historical messages, but only 1 anywhere had an explicit "queued" status marker in its body (MSG-FLEET-001, dispatched 2026-08-08). More significantly, the single most recent message in every one of the 5 channels was already 11+ days old as of this session (2026-08-23), ranging from 2026-08-05 to 2026-08-12 — nothing had been dispatched into any of these files in over a week.

This was reported to the operator plainly as an observation rather than glossed over: the actual work happening in the current session (bug fixes, dashboard audits, build reports) was all happening through direct chat, not through this dispatch-queue mechanism. The assistant explicitly declined to unilaterally decide the queue mechanism was "dead" — whether it's still the intended coordination channel going forward, or has effectively been superseded by direct-chat work, was left as the operator's call.

## Links
- related, 2026-08-23-msg-fleet-001-closed-via-build-report-not-inbox-edit.md, the one genuinely-queued item found in this same check, investigated and closed in the immediate follow-up.
