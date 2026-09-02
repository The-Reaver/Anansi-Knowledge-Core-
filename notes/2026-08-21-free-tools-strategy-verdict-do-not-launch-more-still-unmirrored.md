---
id: 2026-08-21-free-tools-strategy-verdict-do-not-launch-more-still-unmirrored
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — added explicit operator routing for the unresolved Batch-2-scope question. Operator retains veto per Mandate 1."
project: fleet
tags: [free-tools, small-business-tools, sbt, pass-through, byo, tcpa, strategy, unmirrored, ratification-gap]
sources:
  - ref: "Archive turns 218-229: STAG master-checklist refresh sweep, 2026-08-21, workstream 'Free tools pipeline' — direct read of C:\\Users\\abadm\\Downloads\\STAG_FREE_TOOLS_STRATEGY_2026-08-16.md and a repo-wide search confirming it is still unmirrored"
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Free tools pipeline\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

- class: confirmed
- confidence: high that the document exists and says this (read in full at
  `C:\Users\abadm\Downloads\STAG_FREE_TOOLS_STRATEGY_2026-08-16.md`); medium on how it should
  reconcile with the original 5-idea consumer pipeline, since the two documents scope different
  tool sets (see Body)
- verified: 2026-08-21
- REVIEW: high-impact

# A 2026-08-16 strategy review's headline verdict, "do not launch new free tools now," is not in the Knowledge Core and the source document is still only in Downloads

## Body

Separately from the "Batch 2 never delivered" staleness finding, a substantive strategic reversal
exists that the Knowledge Core does not currently reflect. `STAG_FREE_TOOLS_STRATEGY_2026-08-16.md`
(eight research seats, one adversarial seat, one fact-check seat; explicitly "candidate,
ratification pending, no Brain Trust review has run against this document") concludes: the
pass-through/BYO-telephony free-tier mechanic the operator proposed does not work economically or
legally (TCPA exposure, A2P 10DLC carrier registration taking 1-4 weeks with no expedite path, cost
to serve inverting rather than falling once support tickets are counted), and its explicit
recommendation is "do not launch new free tools now." It ranks the six small-business-tools suite
(Missed-Call Text-Back, Review Engine, Booking Recovery Bot, Database Reactivation, Payment
Recovery, AI Voice Receptionist) and recommends shipping only Tool 1 to one paying customer,
building Review Engine next, deferring three tools (Booking Recovery Bot, AI Voice Receptionist,
and Database Reactivation Engine — the last flagged high-risk since consent on an aged customer
list is stale by definition), and killing Payment Recovery outright.

This document is still sitting only in the user's Downloads folder
(`C:\Users\abadm\Downloads\STAG_FREE_TOOLS_STRATEGY_2026-08-16.md`) and, confirmed today
(2026-08-21, five days after it was written), has never been copied into the repo. One existing
ratified note, `research/knowledge-home/notes/2026-08-16-sbt-tool1-never-deployed-and-tools-2-6-already-have-code.md`,
cites this file as a source link but only for its Tool-1-readiness recommendation — it does not
capture the document's actual headline verdict ("do not launch new free tools now," kill/defer
four of the six tools, the pass-through mechanic fails at any conversion rate). So anyone reading
the Knowledge Core today would not learn that this review happened or what it concluded.

Scope note, not silently resolved: the strategy document explicitly frames itself against "your
2026-08-02 doctrine" (the same `FREE_TOOLS_PIPELINE_ASSIGNMENT_AND_BATCH_1_2026-08-02.md` this
sweep also examined) and says "keep your doctrine... it was right on 2026-08-02, this research
strengthens it." But the six tools it evaluates (small_business_tools repo, `STATUS.md` last
updated 2026-07-30, predating the free-tools-pipeline assignment) are a different, pre-existing
tool set from the five consumer ideas actually delivered in Batch 1 (AI Answer-Engine Scanner,
Credential Tracker, Notary Finder, Local Business Audit, Contract Reader). The document treats the
2026-08-02 doctrine as governing both lines, but whether the operator intends "Batch 2 of 5"
(ideas 6-10, the original consumer-tool track) to also be paused by this "do not launch new free
tools now" verdict, or whether that verdict is scoped only to the BYO/pass-through question for the
six-tool SBT suite, is not stated anywhere and was not independently resolved by this sweep. This
question is explicitly routed to the operator for a decision as part of this promotion — it is not
resolved here and should not be read as settled by this note's promotion into the Core.

## Links

- extends: `C:\Users\abadm\Downloads\STAG_FREE_TOOLS_STRATEGY_2026-08-16.md`, the un-mirrored source document.
- extends: `reports/FREE_TOOLS_PIPELINE_ASSIGNMENT_AND_BATCH_1_2026-08-02.md`, the doctrine the strategy document says it is honoring.
- relates: [[2026-08-16-sbt-tool1-never-deployed-and-tools-2-6-already-have-code]], the existing ratified note that cites this document but not its headline verdict.
- relates: [[2026-08-21-free-tools-pipeline-batch-2-never-delivered]], the companion staleness finding from this same sweep.
