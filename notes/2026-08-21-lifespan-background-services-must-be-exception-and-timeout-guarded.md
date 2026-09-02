---
id: 2026-08-21-lifespan-background-services-must-be-exception-and-timeout-guarded
type: decision
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, fastapi, lifespan, resilience, architecture-decision]
sources:
  - ref: "Archive turns 534-568: the agent wraps poller.start() in the lifespan so a background-scheduler failure can never take down the web server (turn 534), verifies it locally (turns 543-545), then adds an asyncio.wait_for timeout specifically so a hanging DB connection attempt (which try/except alone would not catch) also cannot block startup (turns 562-568)"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [534, 568]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A background service started in an ASGI app's lifespan must be wrapped in both try/except and a timeout, or it can take down the entire web server on startup
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the try/except-plus-timeout fix and its verification via TestClient match the session narration. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent implemented the guard, verified locally with a TestClient that the app now serves even with the poller misconfigured, and later added a timeout specifically to guard against a DB connection hang (not just a raised exception)
- verified: 2026-08-21
## Body
Following a real incident where an unguarded background job poller's startup crashed the entire FastAPI web server (a `TypeError` from a missing pool argument), the fix applied was architectural, not just a one-line signature correction: the poller's `start()` call in the app's lifespan was wrapped in both a try/except (so a raised exception is logged rather than propagating) and an `asyncio.wait_for` timeout (so a hanging database connection attempt, which try/except alone would not catch, also cannot block the app from coming up). This produced the general rule for any ASGI app with a background scheduler, worker pool, or similar auxiliary service started during lifespan: the auxiliary service's failure mode (crash or hang) must never be able to prevent the primary web server and its healthcheck endpoint from starting, regardless of the auxiliary service's own bugs.
REVIEW: high-impact
## Links
- related, 2026-08-21-import-boot-check-misses-runtime-lifespan-startup-crashes.md, the incident that motivated this architectural fix
