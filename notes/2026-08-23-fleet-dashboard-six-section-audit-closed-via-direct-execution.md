---
id: 2026-08-23-fleet-dashboard-six-section-audit-closed-via-direct-execution
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify\"), given after reviewing an operator-facing review report covering all 7 (all read in full, all 6 unique cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi-hub, fleet-dashboard, verification-methodology, audit]
sources:
  - ref: "Operator says '6-of-8 Fleet dashboard audit.'; assistant runs each tab's parser against real data and reports the results table: 35 entries from LEVELS_LEDGER.md, 22 from SKILLS_REGISTRY.md, 8/10 roster agents with skill cards, real 90-day staleness logic, the em-dash parsing bug found and fixed, 22 real report files"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1259, 1288]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The Fleet dashboard's 6 previously-unreviewed nav tabs were confirmed real by running their backend parsers against live repo data, not by reading the code
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1238-1324
- confidence: high, each section's parser was executed directly against real files and its output inspected, not inferred from reading the code
- verified: 2026-08-23

## Body
A Fleet dashboard audit had been paused earlier in this session with 6 of 8 nav tabs still unreviewed: Skills & Levels, Skill Tree, Proof & Gates, Decay Watch, Assignments & Queue, and Build Activity. This session picked it back up and closed it by executing each tab's backend parser function directly against the real repo files and inspecting the actual output, rather than assuming correctness from reading the parser code.

Verified results: Skills & Levels parsed 35 real entries from `LEVELS_LEDGER.md`; Proof & Gates parsed 22 real entries from `SKILLS_REGISTRY.md`; Skill Tree showed 8 of 10 real roster agents with an extracted skill file (the 2 missing were confirmed a genuine, expected gap — never extracted yet — not a bug); Decay Watch's 90-day staleness flag was confirmed to be real computed logic against file modification times, not a stub; Build Activity showed 22 real report files with real timestamps. Assignments & Queue was the one tab where this direct-execution check actually surfaced a bug (see the linked note on the em-dash header-parsing fix).

This closes out the original Fleet Development Dashboard Suite dispatch (MSG-FLEET-001, 2026-08-08) — all 8 sections (Graph, Roster, plus these 6) have now had genuine scrutiny against real data rather than just a description of what the code appears to do.

## Links
- includes, 2026-08-23-fleet-inbox-em-dash-header-parsing-bug-fixed.md, the one confirmed bug this audit found, in the Assignments & Queue section.
- related, 2026-08-23-msg-fleet-001-closed-via-build-report-not-inbox-edit.md, this audit's completion is what let MSG-FLEET-001 be confirmed done and formally closed.
