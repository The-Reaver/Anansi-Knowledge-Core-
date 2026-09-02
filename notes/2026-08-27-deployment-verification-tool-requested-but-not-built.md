---
id: 2026-08-27-deployment-verification-tool-requested-but-not-built
type: spec
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [geo, testing, deployment, tooling, open-work, operator-request]
sources:
  - ref: "GEO Suite session 2026-08-27, operator verbatim: 'we need end to end testing and you need to create a solution for that' and 'do we have end to end testing for all features and functions? I need to know what works and what does not'. Nothing built at the close of the session"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [25, 25]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The operator asked for an end-to-end production-readiness solution and it is not built: the shape it needs is a check that diffs code-declared env vars and migrations against live platform state

## Body
**Requested, not started.** The operator asked directly, in the context of being unable to
hand the product to anyone: *"do we have end to end testing for all features and functions? I need
to know what works and what does not"* and *"we need end to end testing and you need to create a
solution for that."*

Read the request precisely: this is a **production-readiness and testing-gap** complaint, not a
feature request. (The session initially risked reading *"i can not hand this over"* as a
user-invite feature; the operator's clarification corrected it.) What the operator wants is a
trustworthy answer to "what works right now, live."

**The gap is proven, not speculative.** The same session's audit found 4 real production bugs
while the unit suite was 985/985 green, because all four were missing env vars or unapplied
migrations rather than code-logic defects. More unit tests cannot close this.

**Shape of the solution needed**, as understood at the close of the session: a
deployment-verification check, **separate from pytest**, that diffs what the code declares
against what the platform actually has --
- every env var the codebase reads vs. what is set on the Railway service (this alone would have
  caught 3 of the 4 bugs);
- every migration in `supabase/migrations/` vs. the applied-migrations list on the live Supabase
  project (this would have caught the other one, three times over);
- ideally, a real authenticated smoke test against the live URL for the handful of user-visible
  paths -- noting that the cloud sandbox could not do this at all, since its outbound proxy
  blocks the production domain, so this part may need to run from somewhere else.

Treat the first two as the high-value, low-cost core; they are static diffs, need no test
fixtures, and directly address every bug actually observed.

**Time-bounded.** This records requested-but-unbuilt work. Once the deployment-verification
check exists, this note should be superseded by one describing what was actually built — the
durable part is the *gap argument* (unit tests cannot see the deployed environment), not the
not-yet-built status.

## Links
- motivated-by: 2026-08-27-green-unit-suite-does-not-detect-production-config-drift
- relates-to: 2026-08-27-a-committed-migration-is-not-an-applied-migration
- relates-to: 2026-08-27-infrastructure-changed-via-mcp-leaves-no-trace-in-the-repo
