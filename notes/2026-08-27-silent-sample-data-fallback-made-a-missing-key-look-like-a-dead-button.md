---
id: 2026-08-27-silent-sample-data-fallback-made-a-missing-key-look-like-a-dead-button
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [ux, failure-modes, silent-fallback, observability, production-config, geo]
sources:
  - ref: "GEO Suite, 2026-08-27: discoverProspects() in frontend/app/nova/actions.ts falls back to the same two fixed SAMPLE_ROWS on every non-live result, distinguished only by a small 'Sample data' badge in NovaShell.tsx ~line 1383; the operator reported this as 'i tried to conduct a new search but nothing happens'"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [18, 18]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A silent fallback to sample data turned a missing production API key into 'nothing happens', because the only signal was a badge the user never noticed

## Body
The operator reported: *"i tried to conduct a new search but nothing happens."* The search
was not broken and was not erroring. `GEO_PLACES_API_KEY` was simply never set in production, and
`discoverProspects()` silently falls back to the same two hardcoded `SAMPLE_ROWS` on **every**
non-live result. The search "worked" every time and returned the same two rows, which from the
operator's seat is indistinguishable from a dead button.

The system did disclose the truth -- a small "Sample data" badge. That was not enough. A
degraded-mode indicator that a user has to notice, recognise and interpret is not a functioning
error path; it is an error path that has been made easy to miss.

The design lesson: **a fallback that produces plausible-looking output is more dangerous than an
error.** An exception would have been reported accurately in seconds ("search throws"). Plausible
sample data instead produced a vague, hard-to-diagnose complaint and hid a missing production
key. If a fallback exists because the real source is unconfigured -- a config defect, not a
runtime condition -- it should be loud, blocking, and name the missing variable, not decorative.

Reserve silent graceful degradation for conditions that are genuinely expected at runtime
(a rate limit, a timeout). "The operator never set this key" is not one of those; it is a
deployment defect wearing a fallback's clothes.

## Links
- same-family-as: notes/2026-08-16-reconnect-drain-silent-failure-caught-by-live-testing.md —
  a drain that reported nothing on total failure, found only by exercising the real event.
  Both are silent degradations that produce plausible output instead of an error.
- instance-of: 2026-08-27-green-unit-suite-does-not-detect-production-config-drift
- relates-to: 2026-08-27-partial-update-requiring-resubmission-of-a-secret-reads-as-a-broken-feature
