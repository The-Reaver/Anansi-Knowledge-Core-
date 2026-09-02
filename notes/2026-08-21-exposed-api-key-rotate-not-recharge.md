---
id: 2026-08-21-exposed-api-key-rotate-not-recharge
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [security, secrets, anthropic, api-key, credits]
sources:
  - ref: "Two archive incidents (turns ~299-305 and ~468-483) where a credential-shaped string was exposed — once via a repo file listing, once pasted directly into chat — with the assistant explaining that rotation, not recharging, is the correct remediation because prepaid credits live on the account, not on the key."
    reliability: high
    origin: "STAG session, 2026-07-15, \"Railway frontend deployment\" (backfilled from historical transcript 23d1d7fe, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl
  turns: [299, 483]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, explained directly to the operator after a real key was pasted into this chat twice
- verified: 2026-08-21
- REVIEW: high-impact

# An exposed Anthropic API key must be rotated, not recharged — prepaid credits live on the account, not on the key, so rotation loses no funds

## Body
An Anthropic API key that has been exposed — whether by appearing unguarded in a repo file, being printed into a terminal or log output, or being pasted directly into a chat transcript — must be treated as compromised and rotated: deleted in the provider console (console.anthropic.com → API Keys) and replaced with a freshly generated key, kept afterward only in a git-ignored file. Critically, prepaid credits and billing live on the Anthropic account, not on the individual key, so rotating (deleting) a compromised key does not lose any account funds. "I need to reload the key with money before I can rotate it" is a misconception: rotation is a security action taken in the API Keys settings, and adding credits is a separate billing action taken on the Billing page, and neither affects the other. In this session the operator pasted a live key into the chat twice; both instances were treated as exposed on sight and neither was used or stored.

## Links
