---
id: 2026-08-06-broken-code-scenarios-program-status-and-dashboard
type: artifact
status: candidate
source: "this chat, 2026-08-06, Abad asked whether atomic notes and artifacts were being created, then asked to set up both a persisted dashboard and Drive sync of the notes (source status: active)"
project: fleet
tags: [augustin, curriculum, broken-code-scenarios, program-status, dashboard, artifact, honesty]
supersedes: []
superseded_by: null
---

# Broken Code Scenarios Program Status: 45 of 500 Verified, Plus a Persisted Progress Dashboard

## Body

The 500 Broken Code Scenarios manual runs 10 domains of 50 (CM, DS, CT, ST, NT, SC, RT, AI, FE, BD). As of 2026-08-06, 45 scenarios are built and verified (CM 27, DS 18), 23 are registered as blocked with exact reasons (all in CM, GPU or ML-framework bound), and 432 are not started. CT through BD have not been read from the manual yet, so no titles are invented for them.

Standing method, unchanged: a language-agnostic bug is reframed faithfully into a buildable language and labeled as a reframe; a hardware or absent-framework bug is registered as blocked with the closest safe substitute rather than faked; scenarios are built in parallel subagent waves, and the main session re-runs each run_tests.sh and commits only on exit 0. The full per-scenario task cards (reproduction, fix, guard, real output, risks, next tightening) live as one markdown card per ID in the Curriculum folder of the stag repo. These cards are the atomic/integrated notes for this program; this Drive note set is the domain-level index over them.

A persisted Cowork artifact named augustin-curriculum-progress was created this session: a self-contained HTML dashboard with per-domain progress bars and verified per-scenario tables for CM and DS. It is updated in place each wave rather than rebuilt, so it is the single place to check program state.

Two honesty caveats worth keeping visible. First, the 9 percent complete figure counts verified-and-committed work only; blocked and not-started are not padding it. Second, before this session the per-scenario cards existed only in the repo and in this session's project memory, not in this Drive inbox and not as a persisted artifact; this note set and the dashboard close that gap.

## Links

- derived-from: 2026-08-06-broken-code-scenarios-cm-domain-27-done-23-blocked
- derived-from: 2026-08-06-broken-code-scenarios-ds-domain-18-of-50-verified
