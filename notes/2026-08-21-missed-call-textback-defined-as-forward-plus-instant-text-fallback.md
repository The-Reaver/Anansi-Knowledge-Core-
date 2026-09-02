---
id: 2026-08-21-missed-call-textback-defined-as-forward-plus-instant-text-fallback
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, project-brief-step0, missed-call-text-back, product-spec, twilio]
sources:
  - ref: "Archive turns 209-268: turn 209 identifies the missing product definition; turn 215 records the exact v1 non-goals list; turn 217 records the operator's literal choice ('Forward + instant-text fallback'); turns 261-268 show the two-route implementation and 20 passing tests."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [209, 268]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, explicit operator choice, implemented and test-verified in the same session
- verified: 2026-08-21

# Missed-Call Text-Back (Tool 1) was defined as forward-to-business-then-fallback-text, not simple always-text, resolving what "missed" means for the product

## Body
For Tool 1 (Missed-Call Text-Back, $49/mo) in `project_brief_step0_resolved`, the voice webhook previously just greeted the caller and hung up, so "missed call" had no real product definition yet -- how it's defined materially changes the build and whether the business can still take live calls on that number. The operator resolved this with "Forward + instant-text fallback": if a client has configured a forward-to phone number in Settings, an inbound call to their Twilio number is forwarded (TwiML `Dial`) to that number, and the caller only receives the auto-text if the dial does not result in an answer (determined via a dial-status callback). If no forward number is configured, the caller is texted back immediately with no attempt to connect a live call at all.

This was implemented as two Twilio webhook routes -- `/twilio/voice` (branches on whether a forward number exists) and `/twilio/voice/dial-status` (handles the answered / missed / unrouted outcomes) -- backed by a new `missed_call_settings` table (per-client forward number, ring timeout, message template) and a `missed_call_textbacks` table unique on `call_sid`, guaranteeing exactly-once texting even under Twilio's webhook retry behavior.

Explicit v1 non-goals recorded alongside the decision: no AI conversation, no business-hours scheduling, no MMS, no multi-message drip -- just the single immediate text-back.
