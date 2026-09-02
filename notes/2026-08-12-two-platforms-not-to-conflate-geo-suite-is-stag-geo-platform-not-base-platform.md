---
id: 2026-08-12-two-platforms-not-to-conflate-geo-suite-is-stag-geo-platform-not-base-platform
type: correction
status: ratified
ratified: "2026-08-12, operator instruction, direct re-verification by this session's Claude; every claim below is independently re-checkable (gh repo view/list, git merge-base --is-ancestor, railway list --json, a direct curl of the cited URL), not resting on this session's say-so alone"
project: geo
tags: [geo, deploy, railway, supabase, disambiguation, env-manifest, port-gotcha, session-pooler, correction]
sources:
  - ref: "gh repo view The-Reaver/stag-platform; gh repo view The-Reaver/Stag-GEO-Platform; gh repo list The-Reaver"
    reliability: high
    origin: GitHub CLI, run live this session
  - ref: "git merge-base --is-ancestor 43528dc origin/main, run inside the (now-archived) projects/project_brief_step0_resolved clone"
    reliability: high
    origin: git, run live this session against the real local clone
  - ref: "railway list --json"
    reliability: high
    origin: Railway CLI, run live this session, authenticated as the operator's own account
  - ref: "curl https://stag-platform-production.up.railway.app/health"
    reliability: high
    origin: direct HTTP request, run live this session
  - ref: HANDOFF_DEPLOY.md (stag repo root)
    reliability: medium
    origin: prior session's handoff doc; source of the claim this note corrects, now confirmed stale
provenance:
  archive: research/knowledge-home/raw/2026-08-12-geo-poller-fix-and-platform-identity-session.jsonl
  turns: [1, 14]
risk_class: B
evidence_state: CORROBORATED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# CORRECTED: "Base Platform" and GEO Suite are the same repo, not two products; the Railway deploy in HANDOFF_DEPLOY.md is no longer live

## Correction (read this first)

This note originally claimed the stag tree holds two separate SaaS platforms — GEO Suite and a live
"Base Platform" — with two separate GitHub repos and two separate deploys. **That premise is wrong,**
verified directly rather than assumed:

- `The-Reaver/stag-platform` (the remote `projects/project_brief_step0_resolved` — the "Base
  Platform" clone — still points at) and `The-Reaver/Stag-GEO-Platform` (`projects/geo_platform`'s
  remote) are **the same GitHub repository**. `gh repo view The-Reaver/stag-platform` resolves to
  `Stag-GEO-Platform` — identical repo ID, identical `createdAt`/`pushedAt` — because the repo was
  renamed at some point and GitHub transparently redirects the old URL. `gh repo list The-Reaver`
  shows only 7 repos total; no separate `stag-platform` exists.
- `project_brief_step0_resolved`'s own last-synced commit (`43528dc`, "Trigger frontend deploy") is
  confirmed an ancestor of that same repo's real `origin/main` (`git merge-base --is-ancestor`
  returns true). It carries zero unique history — it is a stale, un-pulled clone of GEO Suite frozen
  before the rename, not a second product. It has been moved to `Archive/project_brief_step0_resolved`
  (outer stag repo commit `a6db415`); its one local-only commit (a redundant poller.py fix already
  applied upstream via geo_platform's own commit) was never pushed anywhere.
- **The "backend is LIVE on Railway" claim is also currently false, independently of the repo mixup.**
  `railway list --json` under this account shows exactly one project, "sandbox-small-business-tool-set"
  (unrelated) — no project matching stag-platform/Base Platform exists. A direct `curl` of the URL
  HANDOFF_DEPLOY.md cites, `https://stag-platform-production.up.railway.app/health`, returns Railway's
  own edge 404 (`{"status":"error","code":404,"message":"Application not found"}`) — the service does
  not currently exist under that domain, full stop, not merely unreachable from this account.

Net effect: there is **one product** (GEO Suite / Stag-GEO-Platform), and as of 2026-08-12 it is **not
deployed anywhere live**. GEO's own STATUS.md line "NOT on any public URL yet" was accurate all along
and simply applies to the whole thing, not to one of two products. The Supabase ref
`utohxigqstklqrkmfuyx` this note originally warned against reusing may still exist as an orphaned
Supabase project (Supabase projects don't vanish when a Railway service does), but nothing currently
live depends on it — unverified here, flagged rather than asserted, since Supabase wasn't checked
directly this pass.

## Body (original text, kept for the parts still true)

This session generated projects/geo_platform/RAILWAY_ENV_MANIFEST.md from the real code (Settings class
in backend/app/config.py, both .env.example files, both railway.json, and the actual process.env /
os.getenv reads). It is the deploy-ready env-var contract for the two GEO Railway services and carries
the three time-eating gotchas: never set PORT on Railway (it injects its own; a hardcoded PORT caused a
502-that-looked-like-a-crash the first time this exact repo was deployed, per HANDOFF_DEPLOY.md);
SUPABASE_DB_URL must be the Session-pooler IPv4 string, not the direct db host (Railway cannot reach
the direct host); and the frontend reads
`NEXT_PUBLIC_API_BASE_URL ?? NEXT_PUBLIC_API_URL ?? localhost`, so setting NEXT_PUBLIC_API_BASE_URL
alone is sufficient. Deploy order resolves the backend<->frontend CORS chicken-and-egg: push, deploy
backend, deploy frontend, then set FRONTEND_ORIGIN on the backend and redeploy.

## Links

- relates, HANDOFF_DEPLOY.md — the source of the "backend is LIVE on Railway" line; describes a real
  deploy that happened at some point against this same repo, since taken down or lost (Railway project
  no longer exists under this account, domain 404s). Historical record, not current state.
- relates, 2026-08-12-geo-job-poller-is-unwired-and-signature-drifted-battery-green-proves-nothing-about-it.md
  — same session's deeper read of the same GEO backend.
- depends, projects/geo_platform/RAILWAY_ENV_MANIFEST.md — the artifact this note points a future
  deploy session to; still the right starting point for the next real deploy of this one product.
