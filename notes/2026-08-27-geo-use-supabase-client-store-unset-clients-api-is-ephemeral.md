---
id: 2026-08-27-geo-use-supabase-client-store-unset-clients-api-is-ephemeral
type: question
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [geo, production-config, railway, open-question, operator-action]
sources:
  - ref: "GEO Suite production-config audit, 2026-08-27: flag found unset in Railway and deliberately not flipped; public.clients holds 2 real rows whose origin (handle_new_user() auth trigger vs. the /clients API) was not determined"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [21, 21]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# GEO_USE_SUPABASE_CLIENT_STORE is unset in production, so anything created through the /clients provisioning API is lost on every redeploy — awaiting the operator's confirmation that the path is used

## Body
**Open question for the operator.** `GEO_USE_SUPABASE_CLIENT_STORE` is unset on the live
Railway service. The admin-only `POST/GET /clients` provisioning API (`routers/clients.py`) is
therefore running against an **in-memory store**: anything created through it is lost on every
redeploy.

This is the same shape as the three config bugs fixed in the same sweep, and the flag was
deliberately **not** flipped, which was the right call. The evidence is genuinely ambiguous: a
`public.clients` table already holds 2 real rows, but those may originate from the
`handle_new_user()` Supabase Auth trigger -- a completely different code path -- rather than from
this API. Turning the flag on blind would switch a live write path from one store to another
without knowing whether anything depends on the current behaviour, or whether the two stores
would then disagree.

**What is needed to close it:** confirmation of whether `/clients` is actually used day-to-day.
- If yes -> set the flag, and check whether anything already created in memory needs recreating.
- If no -> the flag stays off and this is documented as a dormant path, not a defect.

Worth resolving rather than leaving open: while it sits unset, the API silently accepts writes it
will lose, which is the failure mode with the longest gap between cause and discovery.

**Time-bounded.** This is an open question, not a durable lesson. Once the operator confirms
whether `/clients` is used and the flag is set or deliberately left off, this note should be
closed out with the answer rather than left standing.

## Links
- instance-of: 2026-08-27-green-unit-suite-does-not-detect-production-config-drift
- relates-to: notes/2026-08-09-preview-delivery-in-memory-store-not-durable-across-railway-redeploy.md
