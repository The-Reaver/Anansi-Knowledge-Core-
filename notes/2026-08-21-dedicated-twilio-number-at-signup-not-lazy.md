---
id: 2026-08-21-dedicated-twilio-number-at-signup-not-lazy
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [small-business-tools, twilio, a2p-10dlc, provisioning, product-decision]
sources:
  - ref: "Turns 102-105: turn 102 poses the lazy-vs-dedicated fork, turn 103 first recommends lazy, turn 104 is the operator's decide-and-explain directive, turn 105 reverses to dedicated-at-signup with the A2P 10DLC lead-time reasoning and the ~$1.15/mo cost."
    reliability: high
    origin: "STAG session, 2026-07-07, \"Master Build Document v1.1 verification\" (backfilled from historical transcript 3b51843d, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl
  turns: [102, 105]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Every Small Business Tools client gets a dedicated Twilio number at signup, not lazily on first telephony-tool activation, because A2P 10DLC registration takes days to clear
- id: 2026-08-21-dedicated-twilio-number-at-signup-not-lazy
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-07-07, "Master Build Document v1.1 verification" (backfilled from historical transcript 3b51843d, 2026-08-21)
- confidence: high, explicit reversal decision made and reasoned through in-session, baked into the approved build plan
- verified: 2026-08-21
- tags: small-business-tools, twilio, a2p-10dlc, provisioning, product-decision
- REVIEW: high-impact

## Body
The initial answer to this design question was lazy provisioning (only give a client a number when they first toggle on a telephony tool, to avoid paying ~$1.15/mo per idle client). This was deliberately overturned in the same session, once the operator instructed the agent to make the best call for the project on its own and explain the reasoning: A2P 10DLC carrier registration, required for reliable SMS delivery in live mode, takes several days to clear, so lazy provisioning would leave a paying client's first telephony tool activation stalled for days at the exact moment they need it. The locked model instead provisions a dedicated voice-ready number for every client immediately at signup (right after the $19 base subscription goes active) and kicks off A2P 10DLC registration at that point in live mode, so the number is carrier-warm before any telephony tool is ever turned on. The ~$1.15/mo per-number cost is treated as an approved recurring cost line covered by the base fee. Step 0 itself runs on Twilio trial/test credentials, so live registration was deferred to a pre-live NEEDS-YOU checklist item.

## Links
- related, 2026-08-21-small-business-tools-per-tool-line-item-billing-locked.md, part of the same Step 0 interview locking the platform's billing and provisioning model.
