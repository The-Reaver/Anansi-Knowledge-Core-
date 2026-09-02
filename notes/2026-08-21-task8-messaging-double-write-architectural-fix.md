---
id: 2026-08-21-task8-messaging-double-write-architectural-fix
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, backend-architecture, python, async-sync-mismatch, database-writes, bug-fix]
sources:
  - ref: "Archive turns 442-479 show the full call-graph trace of a messaging double-write bug (router and async services both trying to own message-row creation), the architectural fix making the router the single row-owner, and the app booting successfully with 18 routes for the first time."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [442, 479]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent traced the full call graph, applied the fix, and confirmed the app booted successfully afterward for the first time in the project's history
- verified: 2026-08-21
- REVIEW: high-impact

# Task 8's messaging module had a genuine architectural bug (sync router and async services both tried to own message-row creation), fixed by making the router the single row-owner

## Body
In the `project_brief_step0_resolved` backend, `backend/app/routers/messages.py` created the outbound message DB row and then called sync sender functions (`sms_twilio.send_sms`, `email_resend.send_email`) expecting a result object with `.provider_message_id`/`.provider_status`. But those sender modules had separately been generated to also create their own message row internally, using an async API (`create_outbound_sms`, `create_outbound_message`, `attach_provider_message_id`) that didn't even exist on the `messages.py` service (which only exposed a differently-named, differently-shaped sync API, `create_outbound_sms_row`). This was initially misdiagnosed in an earlier turn of the same session as fixable with a few compatibility aliases; when the agent actually traced the full call graph, it found the conflict was architectural — the router was `await`-ing effectively-sync work, passing kwargs the target didn't accept, and expecting a different return shape, and on top of that both sides would have created a row for the same outbound message (a double-write). The agent declined to paper over this with import shims (which would make the validator's boot check pass while messaging stayed non-functional) and instead did the real restructure: made `routers/messages.py` the single owner of message-row creation, rewrote `sms_twilio.py` and `email_resend.py` to be pure synchronous provider calls with no DB access, and fixed a related bug where `attach_provider_result` was calling the internal `_apply_status` helper with the wrong signature (positional `message_id` instead of a full row plus keyword-only `raw_status`/`error_code`). After this fix, `import app.main` succeeded for the first time in the project's history, exposing 18 routes. General lesson: when a diagnostic first suggests "add a compatibility alias," it's worth checking whether the underlying issue is actually a shape/ownership conflict between two pieces of code that both assume they own the same responsibility — an alias will resolve the import error but not the runtime conflict.

## Links
- related, 2026-08-21-imagined-api-recurring-drift-pattern.md, this is one fully-diagnosed instance of that general failure mode
