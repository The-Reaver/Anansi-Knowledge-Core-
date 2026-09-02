---
id: 2026-08-21-import-boot-check-misses-runtime-lifespan-startup-crashes
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, fastapi, lifespan, startup, boot-check, testing-gap]
sources:
  - ref: "Archive turn 530: the agent pinpoints the crash — 'poller.py:60 -> JobsRepository() (no arguments); jobs_repo.py:65 -> __init__(self, pool: asyncpg.Pool) — requires a pool ... (This passed the import-time boot check because it only triggers at runtime startup.)'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [530, 530]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# An `import app.main` boot check passed even though the app crashed on startup, because import never runs the ASGI lifespan where the crash actually occurred
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the JobsRepository() signature-mismatch crash and the import-vs-lifespan distinction match the session's diagnosis exactly. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly observed: `import app.main` succeeded throughout the session while Railway's healthcheck failed on a lifespan-only crash that only a TestClient reproduction (running the full lifespan) revealed
- verified: 2026-08-21
## Body
The STAG validator's existing "boot check" (`import app.main` resolves without error) passed throughout this session's deploy, but the deployed app still failed Railway's healthcheck because the actual crash happened inside the FastAPI app's `lifespan` context, which only runs when the ASGI server actually starts serving, not at import time. The specific crash: the app's lifespan constructed a background job poller that called `JobsRepository()` with no arguments, but `JobsRepository.__init__` requires a `pool: asyncpg.Pool` argument, raising a `TypeError` during startup that killed the whole uvicorn process before it could ever answer `/health`. General lesson: an import-time boot check is a necessary but insufficient smoke test for an ASGI app — it verifies the module graph resolves, but not that the app's actual startup sequence (lifespan handlers, background service initialization) succeeds; this whole class of caller/callee signature drift only surfaces when the lifespan is actually exercised.
REVIEW: high-impact
## Links
- related, 2026-08-21-testclient-context-manager-exercises-full-lifespan-locally.md, the technique used to reproduce and verify the fix for this exact gap
- related, 2026-08-21-health-endpoint-always-200-makes-healthcheck-failure-mean-startup-crash.md, how this class of bug shows up externally as a Railway healthcheck failure
