---
id: 2026-08-23-agent-breakers-context-request-lacked-timeout-exception-handling
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify this\"), given after reviewing an operator-facing review report covering all 6 (all read in full, all 6 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [agent-breakers, security-testing, bug-fix, error-handling, anansi-hub]
sources:
  - ref: "Assistant confirms /api/datascience?study=growth_trend takes ~19.5s past the harness's 10s timeout and Context.request() catches no exception at all (line 1156), then edits context.py/findings.py/agent_breaker.py to record request_errors instead of crashing (lines 1158-1168)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1154, 1168]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# agent_breakers' Context.request() caught no request exceptions at all, so one slow real route timed out and crashed the entire harness run instead of being recorded as a finding

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1085-1237
- confidence: high, directly reproduced the crash, fixed it, and verified no regression against the harness's own fixture self-test
- verified: 2026-08-23

When `AJ/agent_breakers` (a real-HTTP self-red-team harness previously only ever tested against its own deliberately-vulnerable fixture app) was pointed at the real, live Anansi Hub server for the first time, it crashed uncaught partway through the run. Direct investigation confirmed the cause: one real route, `/api/datascience?study=growth_trend`, took about 19.5 seconds to respond, well past the harness's hardcoded 10-second client timeout, and the harness's `Context.request()` method had no exception handling around the underlying request call at all — any request exception, timeouts included, propagated straight up and killed the whole process, discarding every finding already collected in that run. This is exactly the class of gap a fixture app built to simulate specific injected vulnerabilities would never exercise, since the fixture had no genuinely slow endpoint to trigger it.

Fixed by wrapping the request call, recording timeouts/errors into a new `request_errors` list on the `Context` object, and wiring that list through into the report output (`context.py`, `findings.py`, `agent_breaker.py`) so a real-world timeout now shows up as a visible, reported condition instead of silently crashing the process. Before trusting the fix, the harness's own fixture self-test was re-run to confirm no regression — it reproduced the exact same pre-fix baseline (18 findings total, 4 critical/high) — and only then was the harness re-run against the live Hub, this time completing successfully and surfacing the slow route as a reported request error rather than a crash.

## Links
- relates, 2026-08-22-agent-breakers-self-test-independently-reproduced-exact-finding-counts.md, the prior verification of this same harness's fixture-based self-test, which this fix's regression check reused as its baseline
- relates, 2026-08-21-lifespan-background-services-must-be-exception-and-timeout-guarded.md, the same general architectural pattern (an unguarded slow/hanging call able to take down an entire process) found earlier in a different codebase
- relates, 2026-08-23-anansi-hub-semantic-search-first-call-blocked-by-synchronous-full-corpus-embedding.md, the real bug on the Hub side that this harness fix was what first made visible as a reportable finding instead of a crash
