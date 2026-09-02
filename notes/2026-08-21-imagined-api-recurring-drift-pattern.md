---
id: 2026-08-21-imagined-api-recurring-drift-pattern
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta_agent, api-contract-drift, code-generation, cross-module-consistency]
sources:
  - ref: "Archive turns 204-382 show four independent instances of generated code calling a hypothetical counterpart API that didn't match the real module's actual shape, across tasks 5, 8, 11, and 12."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [204, 382]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent independently identified and named this exact pattern at least four separate times across the session, in different parts of the stack
- verified: 2026-08-21
- REVIEW: high-impact

# Across this STAG build, generated code repeatedly called a hypothetical counterpart API that didn't match what the real module actually exposed

## Body
Across the 2026-07-09 build of `project_brief_step0_resolved`, the same class of bug recurred at every boundary between independently-generated pieces of code: one side was written against a plausible, hypothetical shape of its counterpart rather than the counterpart's actual shape. Concrete instances found this session: (1) task 5's `tool_toggle` router imported a `ToolToggleService` class and `get_tool_toggle_service()` factory that the service module never defined (it only had function-style `toggle_on`/`toggle_off`). (2) task 8's `sms_twilio.py`/`email_resend.py` called an async messages API (`create_outbound_message`, `attach_provider_message_id`, `mark_message_failed`) that didn't exist in `messages.py`, and separately both the router and the service tried to create the same DB row (a double-write). (3) task 11's frontend was written against an API roughly 60% larger than what the actual FastAPI backend exposed — for example the frontend called `GET /api/tools/slots` while the backend only had `GET /api/tools/entitlements`, and `POST /billing/subscription` while the backend had `POST /billing/subscriptions` (plural). (4) task 12's admin router imported an `AdminActionResult` schema class that didn't exist, while the actual schema module defined two different unused DTOs the service never populated. This is not a one-off bug but the dominant recurring failure mode of this multi-task generation run: whenever two files needed to agree on a name, shape, or path and were generated in different passes, they tended to independently converge on plausible-but-different versions of that contract. Any pipeline that generates interdependent files in separate passes (frontend vs backend, router vs service, service vs schema) should treat this as the default risk, not an edge case — a boot/import check and a frontend↔backend contract check are the two most direct mitigations observed working in this session.

## Links
- related, 2026-08-21-stag-boot-check-added-to-validator.md, the runtime boot check STAG added is the concrete backend-side mitigation for this pattern
- related, 2026-08-21-task8-messaging-double-write-architectural-fix.md, is one specific, fully-diagnosed instance of this pattern
- related, 2026-08-21-contract-drift-single-root-cause.md, the same generalized pattern independently re-observed and named in the follow-up session (2026-07-10, transcript ebf4b889) with a different set of concrete instances
