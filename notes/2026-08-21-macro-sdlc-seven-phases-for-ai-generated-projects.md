---
id: 2026-08-21-macro-sdlc-seven-phases-for-ai-generated-projects
type: decision
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, sdlc, lifecycle, meta_agent, process]
sources:
  - ref: "Archive turn 459: the delivered STAG_LIFECYCLE_AND_HARDENING.md summary states '§1 Macro life cycle — the 7 phases (Brief -> Plan -> Generate -> Validate -> Reconcile -> Deploy -> Operate), every arrow a gate,' the direct source of this note's framework"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [459, 459]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A reusable seven-phase lifecycle (Brief, Plan, Generate, Validate, Reconcile, Deploy, Operate) was proposed for AI-generated STAG projects, with the Reconcile phase meant to shrink toward zero as Validate gets stronger
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the seven-phase framework and its stated intent match STAG_LIFECYCLE_AND_HARDENING.md as described in-session; confidence is already appropriately hedged as medium for durability beyond that document. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: medium — the lifecycle was written up and delivered as STAG_LIFECYCLE_AND_HARDENING.md this session, but its durability as a generally-followed operating framework beyond this one document was not observed in this transcript
- verified: 2026-08-21
## Body
In response to the operator's request for a "macro and micro full development life cycle" for STAG projects, the agent proposed and documented a seven-phase lifecycle — Brief → Plan → Generate → Validate → Reconcile → Deploy → Operate — with the explicit rule that every arrow between phases is a gate that must be green before advancing to the next. The Validate phase is where the generator's own post-task checks run and earn their keep; the Reconcile phase exists specifically to catch what Validate missed (as happened repeatedly this session with the entitlements, jobs, and tool-catalog drift), and the stated design intent is that as the Validate phase's gates get stronger (per this session's three new validator checks), the Reconcile phase should shrink toward zero rather than being a permanent fixture of every build. This framework was written into `STAG_LIFECYCLE_AND_HARDENING.md` alongside a companion micro-lifecycle (each phase's inputs → steps → gate → exit criteria) and a taxonomy of the session's actual failure classes.
REVIEW: high-impact
## Links
- related, 2026-08-21-contract-drift-single-root-cause.md, the failure taxonomy underlying the case for stronger Validate-phase gates in this lifecycle
