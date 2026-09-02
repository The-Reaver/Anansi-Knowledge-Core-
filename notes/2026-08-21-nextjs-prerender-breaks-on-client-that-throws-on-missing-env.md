---
id: 2026-08-21-nextjs-prerender-breaks-on-client-that-throws-on-missing-env
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, nextjs, supabase, prerender, build, env-vars]
sources:
  - ref: "Archive turn 145: 'TypeScript compiles and the whole webpack/type-check pass succeeds. The build now fails only at static prerender time: lib/supabaseClient.ts (and useSession.ts) throw at module load when Supabase env vars are absent, so Next can't prerender /login, /signup ... The repo's own env.ts already establishes the convention fall back to a placeholder'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [145, 145]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A Supabase client that throws at module load when env vars are absent broke Next.js static prerendering of /login and /signup even after tsc and webpack both passed clean
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly observed and fixed: build failed only at the static-prerender step after tsc/webpack succeeded, and switching to a placeholder-fallback pattern (already used in lib/env.ts) fixed it
- verified: 2026-08-21
## Body
Even after `npx tsc --noEmit` reached zero errors and the webpack/type-check pass of `npm run build` fully succeeded, the STAG-generated frontend's production build still failed at Next.js's static-prerender step for pages like `/login` and `/signup`. The cause: `lib/supabaseClient.ts` and `useSession.ts` both threw an exception at module load time when the required Supabase environment variables (like `NEXT_PUBLIC_SUPABASE_URL`) were absent — and a Next.js production build statically prerenders pages using the same environment the build runs in, so any module a prerendered page imports that hard-throws on a missing env var will crash the build itself, well before the real runtime environment (with real Supabase credentials) is ever reached. The fix was to make both modules follow the repo's own existing convention (already used in `lib/env.ts`) of falling back to a placeholder value instead of throwing, since the real values only need to be present at actual runtime, not at build time. General lesson: any client-side module used by a page that gets statically prerendered must tolerate missing environment variables gracefully, because the build environment and the deploy environment are not guaranteed to have the same variables set.
## Links
- related, 2026-08-21-nextjs-build-type-checks-by-default-making-tsc-gate-mandatory.md, the other Next.js build-gate fact discovered in the same session
