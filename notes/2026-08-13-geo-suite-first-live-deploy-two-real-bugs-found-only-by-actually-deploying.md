---
id: 2026-08-13-geo-suite-first-live-deploy-two-real-bugs-found-only-by-actually-deploying
type: finding
status: ratified
ratified: "2026-08-14, same-session light pass (Mandate 8 / stag-closeout Step 4) -- a documentary finding of already-completed, independently verifiable facts (live health-check responses, commit 6d0b848, Railway runtime logs), not a proposed decision requiring full Brain Trust seats"
project: geo
tags: [geo, deploy, railway, infrastructure, end-to-end-proof, port-mismatch, lock-file-drift, sdlc]
sources:
  - ref: "projects/geo_platform/railway.json (backend, frontend), RAILWAY_ENV_MANIFEST.md"
    reliability: high
    origin: direct code read, this session
  - ref: "Railway project geo-suite (c3830ba3-c122-45b3-a96d-0fc44d090d06), services geo-suite (backend) and geo-frontend, live this session"
    reliability: high
    origin: created and deployed live, this session, operator confirmed before creation
  - ref: "projects/geo_platform/GEO_DEVELOPMENT_LOG.md, entry [DEPLOY/BUGFIX] 2026-08-13, 03:12 PM ET"
    reliability: high
    origin: written this session, same repo, commit 6d0b848
provenance:
  archive: research/knowledge-home/raw/2026-08-13-geo-first-live-deploy-session.jsonl
  turns: [1, 1]
risk_class: A
evidence_state: CORROBORATED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# GEO Suite's first real live deploy surfaced two bugs no offline battery or sandbox run had ever caught — a frontend lock-file drift and a Railway port-routing mismatch

## What was asked and why this matters

The operator asked for end-to-end proof that a real deployed GEO Suite instance exists, not
another offline `verify.py` run. Every prior status note in this Core said some version of "not
proven live" ([[2026-08-12-two-platforms-not-to-conflate-geo-suite-is-stag-geo-platform-not-base-platform]]
confirmed the old Railway URL 404s and no matching project exists). This session created the first
one that actually does, and the act of deploying — not any code review — is what found both bugs
below.

## What now exists, live

Railway project `geo-suite`, workspace "Abad Morel's Projects", two services deployed from the
real repo (`The-Reaver/Stag-GEO-Platform`) via `railway up <dir> --path-as-root` (not a
GitHub-connected monorepo root — that failed first, see gotcha below):

- Backend: `https://geo-suite-production.up.railway.app` — `/health` returns `200
  {"status":"ok"}`.
- Frontend: `https://geo-frontend-production-3b83.up.railway.app` — `/` returns `200` with real
  rendered HTML (Next.js 14.2.35, all 21 routes built clean).
- `FRONTEND_ORIGIN` / `NEXT_PUBLIC_API_BASE_URL` / `NEXT_PUBLIC_APP_URL` wired between them
  (non-secret URLs only).

**Not yet proven:** a live DB round-trip. Supabase/Stripe/Twilio secret values were deliberately
NOT entered by the assistant — per `RAILWAY_ENV_MANIFEST.md`'s own line, "fleet cannot do these,"
and the assistant's standing rule against ever handling credential values, even ones already
sitting in a git-ignored local `.env`. That step is now the actual remaining gap, not "nothing is
deployed."

## Bug 1: frontend `package-lock.json` was out of sync with `package.json`

First frontend deploy failed `npm ci` on a clean container: `ajv@6.15.0`, `fast-uri@3.1.5`, and
`require-from-string@2.0.2` missing from the lock file; `json-schema-traverse` pinned to an
incompatible version. Every prior verification of this repo ran on a dev machine with an existing
`node_modules` already present — nothing had ever run a clean install. `npm install` locally
regenerated the lock file, `npm ci` then passed clean (412 packages). Fixed in commit `6d0b848`.

**Generalizes:** a green CI battery and a working dev machine prove nothing about whether a fresh
clone can actually be built. This is the same shape of gap as the sandbox-vs-native drift already
in the Core ([[2026-08-11-cloud-sandbox-green-does-not-prove-native-green-real-instance]]), one
level further out: dev-machine-green does not prove clean-install-green either.

## Bug 2: Railway port routing did not match `$PORT` the way `railway.json` assumed

Both services' `railway.json` use `--port $PORT` / `--port ${PORT:-3000}`, and
`RAILWAY_ENV_MANIFEST.md` already warns (gotcha #1) that a hardcoded `PORT` var causes a 502 that
looks like an app crash. That gotcha's fix ("delete PORT, remove the domain, regenerate") assumes
the problem is a hardcoded var. Here no `PORT` var was ever set by this session, and the mismatch
happened anyway: both containers actually bound to port **8080** regardless of the nominal
`3000`/`$PORT` in their start commands (backend logs: `Uvicorn running on http://0.0.0.0:8080`;
frontend logs: `next start --port 3000 --port 8080` — the container's actual `$PORT` env value,
whatever Railway injects in this environment, evidently resolves to 8080 and the frontend's
`package.json` start script already hardcodes `--port 3000` ahead of the manifest's own
`${PORT:-3000}` append, so Next.js received two `--port` flags and the later one won). Manual
domain generation with an assumed port (8000, then 3000) both 502'd with `"Application failed to
respond"` even though `/health` returned 200 **inside** the container per the logs the whole time.
Fix each time: `railway domain delete <domain> --service <svc> --yes`, then `railway domain
--service <svc> --port 8080`. Not root-caused further this session — a real open question for
whoever deploys the next Railway service in this project: check the actual bound port from runtime
logs before generating the domain, do not trust the `railway.json`/`package.json` start command's
stated port.

## A real, working proof, not a claim: the 2026-08-12 poller fix held live

Backend runtime logs from this deploy show `asyncpg` failing to reach the still-placeholder
`SUPABASE_DB_URL` with `ConnectionRefusedError`, caught exactly as
[[2026-08-12-geo-job-poller-is-unwired-and-signature-drifted-battery-green-proves-nothing-about-it]]'s
fix intended: `"Job poller failed to start (or timed out); continuing without the background
scheduler. The API and /health stay up."` That fix was verified on GitHub Actions (67/67) but
never before under real container/network conditions. This is the first evidence it does what its
commit message claimed, in the environment it was written for.

## Deploy-mechanics notes, for whoever deploys the next Railway service here

- `railway up` from inside a subdirectory does NOT scope the archive to that subdirectory — it
  archived the whole parent repo (Railpack then failed to detect a single app). Use `railway up
  <subdir> --path-as-root` from the repo root instead.
- `railway up --service <name>` requires the service to already exist; it will not create one with
  that name. To create a second named service in an existing project, use `railway add --service
  <name>` first (creates an empty service), then `railway up <dir> --path-as-root --service
  <name>`.
- Setting `NEXT_PUBLIC_*` vars does not retroactively apply to a running deployment — they're
  baked in at build time, so a fresh `railway up` (rebuild) is required after setting them, not
  just `railway variable set`.

## Links

- extends, 2026-08-12-geo-job-poller-is-unwired-and-signature-drifted-battery-green-proves-nothing-about-it.md
  — this session is the first live-environment confirmation that fix holds.
- extends, 2026-08-12-two-platforms-not-to-conflate-geo-suite-is-stag-geo-platform-not-base-platform.md
  — supersedes its "not deployed anywhere live" status for the current session; GEO Suite now has
  a live deployment, distinct from the old, confirmed-dead Base Platform URL that note describes.
- relates, 2026-08-11-cloud-sandbox-green-does-not-prove-native-green-real-instance.md — same
  underlying shape of gap (green in one environment proves nothing about another), one level
  further out (dev-machine vs. clean-clone install).
- depends, projects/geo_platform/RAILWAY_ENV_MANIFEST.md — the deploy manifest whose secret-value
  boundary this session respected exactly ("fleet cannot do these").
