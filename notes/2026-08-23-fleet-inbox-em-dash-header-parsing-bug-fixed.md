---
id: 2026-08-23-fleet-inbox-em-dash-header-parsing-bug-fixed
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify\"), given after reviewing an operator-facing review report covering all 7 (all read in full, all 6 unique cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi-hub, fleet-dashboard, inbox-parsing, bug-fix, assignments-and-queue]
sources:
  - ref: "Assistant finds and diagnoses the Assignments & Queue em-dash parsing bug (only 2 of 70 messages use a 'date — title' format instead of comma-separated), fixes and verifies it, then reports the summary table confirming the fix and the byte-identical other 68 messages"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1270, 1288]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The Assignments & Queue dashboard tab mis-parsed 2 of 70 inbox messages because its header parser split every comma in the line
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1238-1324
- confidence: high, bug reproduced against real inbox files, fix verified against both header formats with no regression on the other 68 messages, and the commit is in git history
- verified: 2026-08-23

## Body
While closing out the paused "6-of-8 Fleet dashboard audit" (Skills & Levels, Skill Tree, Proof & Gates, Decay Watch, Assignments & Queue, Build Activity), the assistant ran each backend parser in `anansi_hub.py` directly against the real repo files rather than just reading the code, and found a real bug in the Assignments & Queue tab's inbox-message parser.

The parser built each message's date and title fields by splitting the message header line on every comma. Out of 70 total historical dispatch messages across 5 channel inbox files, 68 used the standard `date, title` comma-separated format and parsed correctly. Two messages — both in `ANTIGRAVITY_FLEET_INBOX.md` — instead used a `date — title` em-dash separator, and the title text in those two messages also contained its own internal comma. Splitting the whole line on every comma therefore put half the title into the date field and truncated the displayed title.

The fix: split off the message id first, then prefer an em-dash split for the remainder when an em-dash is present, otherwise fall back to the original comma split. This was written and tested against both real header formats (confirming the two previously-broken messages now parse correctly and the other 68 remain byte-identical) before being applied to `anansi_hub.py`. Committed as `ca8cabe` ("Fix Assignments/Queue tab misparsing inbox headers with an em-dash date-title separator"), and the live Hub process was restarted to load the fix.

## Links
- extends, 2026-08-21-fleet-dashboard-release-to-orlok-already-built-and-live.md, this bug was found while auditing the same Fleet dashboard that note covers as released.
- related, 2026-08-08-fleet-dashboard-migration-verified-live-in-anansi-hub.md, same dashboard, an earlier verification pass on different sections.
