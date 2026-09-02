---
id: 2026-08-21-health-endpoint-always-200-makes-healthcheck-failure-mean-startup-crash
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, fastapi, health-endpoint, railway, diagnostics]
sources:
  - ref: "Archive turn 521: the agent reads the /health route and states 'Crucial detail: /health never returns a non-200 ... So a healthcheck failure means the app process isn't coming up at all ... it's crashing on startup, not returning a bad status'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [521, 521]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Because /health is designed to always return HTTP 200 (reporting DB status inside the body instead), a Railway healthcheck failure unambiguously means the process never started, not that it returned a bad status
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — this design property was confirmed by reading the /health route, and it correctly predicted that the healthcheck failure was a startup crash rather than a degraded-but-running app
- verified: 2026-08-21
## Body
The backend's `/health` endpoint was designed to always return HTTP 200 even when its own dependency checks (like the database connection) fail — it reports `"database": {"status": "degraded", ...}` inside the 200 response body rather than returning a non-200 status code. This design choice turns a platform healthcheck failure into an unambiguous diagnostic signal: since the endpoint itself can never produce a bad status code, a Railway healthcheck failure necessarily means the application process never came up at all to answer the request — i.e., a startup crash — rather than the endpoint reporting a bad state while still running. This correctly directed the agent to look at deploy/runtime logs for a Python traceback rather than debugging the health-check logic itself, and it was confirmed exactly right: the actual cause was an unguarded lifespan crash. A `"degraded"` body with HTTP 200 is cosmetic (missing placeholder secrets like RESEND_API_KEY) and still counts as a passing healthcheck.
## Links
- related, 2026-08-21-import-boot-check-misses-runtime-lifespan-startup-crashes.md, the specific startup crash this diagnostic property correctly pointed to
- related, 2026-08-21-railway-never-set-a-manual-port-variable.md, the other, unrelated cause of a Railway public-URL failure that this same signal helped distinguish from a real startup crash
