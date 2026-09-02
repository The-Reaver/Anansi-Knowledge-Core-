---
id: 2026-08-21-railway-never-set-a-manual-port-variable
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, railway, port, deploy, networking, gotcha]
sources:
  - ref: "Archive turns 574-589: turn 574 diagnoses the pasted .env's PORT=8000 as breaking Railway's public routing ('This is the #1 Railway gotcha: never set PORT yourself'); the saga runs through the nuclear domain-reset at turn 585; turn 589 confirms 'BACKEND IS LIVE' with HTTP 200 at 2026-07-12T04:48:21Z, ~67 minutes after the first confirmed 502 at turn 560 (2026-07-12T03:41:36Z)"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [574, 589]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Manually setting a `PORT` variable on Railway broke public routing for roughly an hour even though the app was internally healthy; the fix was deleting PORT and regenerating the domain
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, fixed the duration figure (archive timestamps show ~67 minutes between the first confirmed 502 at 03:41:36Z and resolution at ~04:48Z, not 45 minutes); rest of the mechanism and fix is directly confirmed. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly observed and resolved live: the runtime log showed "Uvicorn running" and an internal 200 on /health while the public URL 502'd, and removing PORT + regenerating the domain fixed it
- verified: 2026-08-21
## Body
Pasting the project's local `.env` (which included `PORT=8000` for local development) into Railway's Variables Raw Editor made the deployed app bind to port 8000, while Railway's public domain routing pointed at a different port — so the app was fully healthy internally (the runtime log showed `Uvicorn running on http://0.0.0.0:8000` and `GET /health 200 OK`) while the public URL returned 502 for roughly an hour (about 67 minutes). Setting `PORT` to match the domain's displayed target port (8080) still failed, because Railway's V2 runtime auto-detects and injects its own `$PORT` and fights a manually pinned value; the deterministic fix that finally worked was the "nuclear reset": delete the `PORT` variable entirely, remove the existing public domain, and generate a fresh domain, which let Railway auto-detect the app's actual listening port and wire the route to it cleanly. The diagnostic signature to recognize this failure mode: a deployment shows Active/green and the runtime log shows the app serving `/health` with 200 internally, yet the public URL still 502s — that combination means it's a port-routing mismatch, not an application bug, and manually setting PORT is more likely to cause this than fix it.
REVIEW: high-impact
## Links
- related, 2026-08-21-health-endpoint-always-200-makes-healthcheck-failure-mean-startup-crash.md, the companion diagnostic rule for the other class of Railway healthcheck failure (an actual startup crash)
