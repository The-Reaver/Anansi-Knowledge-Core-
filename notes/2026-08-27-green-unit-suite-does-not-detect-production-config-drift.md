---
id: 2026-08-27-green-unit-suite-does-not-detect-production-config-drift
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [testing, production-config, deployment, blind-spot, railway, supabase, geo]
sources:
  - ref: "GEO Suite production-config audit, 2026-08-27: four live user-impacting bugs found while the local backend suite was 985/985 green throughout, and none of the four were reachable by any unit test"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [18, 21]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A fully green unit suite proves nothing about production config: 985/985 passing tests caught zero of four live, user-facing bugs

## Body
A user-reported outage sweep on the GEO Suite found four separate live, user-impacting
defects. The local backend test suite was 985/985 green before, during and after. It could not
have caught any of them, because none of them were code-logic defects:

1. `GEO_PLACES_API_KEY` / `GEO_PLACES_API_URL` never set in Railway -- search silently returned
   fixed sample rows.
2. `VENDOR_KEY_ENCRYPTION_SECRET` and `GEO_USE_SUPABASE_VENDOR_CREDENTIALS_REPO` never set in
   Railway -- every vendor-key save 400'd, and would have been ephemeral even if it hadn't.
3. `GEO_PUBLIC_API_BASE` never set -- every generated site's contact form pointed its
   `<form action>` at `http://localhost:8000`, unreachable from any real visitor.
4. Three migrations committed to the repo but never applied to the live database.

Every one of these is the same shape: **the code correctly declares what it needs, the
environment does not provide it, and nothing compares the two.** A unit suite asserts the code's
internal consistency. It never sees the deployed environment, so this whole class is structurally
invisible to it -- adding more unit tests would not have moved the needle by one bug.

What to do differently: treat "code-declared dependencies vs. live environment" as its own
verification surface with its own tool, separate from pytest -- a check that diffs the env vars a
codebase reads and the migrations it ships against what the live platform actually has. Until
that exists, a green suite should never be reported to an operator as evidence that a feature
works in production. The honest claim is "the logic is proven; the deployment is unverified."

Corollary that made this worse: the same audit could not run a live smoke test at all -- the
sandbox's outbound proxy blocked the production domain -- so the fixes are confirmed *deployed
and booting*, not confirmed *working end-to-end*. Green tests plus a successful deploy still is
not proof of a working feature.

**Scope of the claim, narrowed after a stress test (2026-08-27).** As first written this
note said a green suite *proves nothing* about production config, which is too absolute: a
suite that contains a real startup config-validator test does assert against the deployed
environment's shape. The defensible claim is narrower — **a green suite proves nothing about
the deployed environment unless it explicitly asserts against live state**, and almost no
unit suite does. That is still enough to carry the lesson, because none of the four bugs here
were reachable by any test in the suite as it actually existed.

## Links
- motivates: 2026-08-27-deployment-verification-tool-requested-but-not-built
- instance-of: 2026-08-27-a-committed-migration-is-not-an-applied-migration
- instance-of: 2026-08-27-silent-sample-data-fallback-made-a-missing-key-look-like-a-dead-button
- relates-to: 2026-08-09-preview-delivery-in-memory-store-not-durable-across-railway-redeploy
