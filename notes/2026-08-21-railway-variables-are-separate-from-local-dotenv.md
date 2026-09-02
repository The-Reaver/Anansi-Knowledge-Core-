---
id: 2026-08-21-railway-variables-are-separate-from-local-dotenv
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, railway, dotenv, deploy, env-vars]
sources:
  - ref: "Archive turn 508: the agent instructs pasting the whole .env into Railway's Variables Raw Editor and then overriding APP_ENV=production and BACKEND_BASE_URL to the deployed URL before saving, illustrating that Railway's Variables are a separate store from the local .env"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [508, 508]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Railway environment variables are entirely separate from the local .env file; editing .env locally does nothing to a deployed service until it's re-pasted into Railway's dashboard
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly acted on this session: local .env fixes (DB password reset, Stripe keys) each had to be separately re-pasted into Railway's Variables tab to take effect on the deployed service
- verified: 2026-08-21
## Body
Railway services read environment variables set in the Railway dashboard's Variables tab, which is entirely independent of the project's local, git-ignored `.env` file — changing `.env` on the operator's machine has no effect on a deployed Railway service until the operator manually re-pastes the updated values in. Railway's Variables tab has a "Raw Editor" mode that accepts a bulk paste of an entire `.env` file at once (it ignores `#` comment lines), which was used to seed the Railway service's variables from the local `.env`, but the operator then had to override several deploy-specific values in place after pasting (`APP_ENV=production` instead of `local`, the real public `BACKEND_BASE_URL` instead of `localhost`, and critically, removing any `PORT` value entirely). This distinction matters operationally: a fix made in the local `.env` is not "done" for the deployed environment until it is separately propagated to Railway's Variables.
## Links
- related, 2026-08-21-railway-never-set-a-manual-port-variable.md, the single most costly instance of a locally-appropriate .env value (PORT=8000) breaking the deployed service once pasted into Railway
