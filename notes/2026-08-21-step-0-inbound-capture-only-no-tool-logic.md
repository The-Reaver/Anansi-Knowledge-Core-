---
id: 2026-08-21-step-0-inbound-capture-only-no-tool-logic
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [small-business-tools, twilio, scope-discipline, product-decision]
sources:
  - ref: "Turns 112-113 verbatim: turn 112 poses the inbound-handling question, turn 113 locks the exact capture-only model (inbound SMS logged with no reply, calls get a short default TwiML greeting then hang up, activity surfaces only in the admin/events log not the client dashboard) with the same 'auto-replies are tool logic, tool 1 is literally Missed-Call Text-Back' reasoning the note states"
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [112, 113]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, explicit scope decision made by the agent under the operator's "decide and explain" standing instruction, baked into the approved build plan
- verified: 2026-08-21
- REVIEW: high-impact

# Step 0 captures inbound SMS and calls to the client's dedicated number but sends no auto-reply or voicemail, since those are tool logic that ships later

## Body
Because every client gets a live, voice-ready Twilio number at signup but no tool logic ships in Step 0, a decision was needed for what happens when real SMS or calls reach that number before any tool is active. The call made: inbound SMS is logged against the owning client (routed via the phone_numbers table) with no auto-response, and inbound calls get a short default TwiML greeting ("please reach us by text or try again later") then hang up — no voicemail, no rejection. The explicit reasoning was that auto-replies and call handling ARE tool logic (Missed-Call Text-Back is literally tool 1 of the six), so building any of it into the shared infrastructure step would be scope creep into a tool's own territory; Step 0's job is only to prove the inbound plumbing works (routing, logging to `messages` and `events`) so the tools can layer real responses on top later. Inbound activity surfaces only in the operator admin view's activity log, never on the client-facing dashboard, which stays a clean six-tool-slot shell with no inbox.

## Links
- related, 2026-08-21-dedicated-twilio-number-at-signup-not-lazy.md, the provisioning decision that made this inbound-routing question necessary in the first place.
