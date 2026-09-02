---
id: 2026-08-21-ci-hbot-lexicon-coverage-gap
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, hbot, fda, uhms, lexicon, coverage-gap, sales-claim]
sources:
  - ref: "Agent's read of v1/rules/pack.py showing the hardcoded HIGH_RISK_DISEASE_TERMS list and the operator's stated goal for the audit engine"
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (A)\" (backfilled from historical transcript c5583566, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-c5583566.jsonl
  turns: [189, 196]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — stated directly by the agent after reading v1/rules/pack.py
- verified: 2026-08-21
- REVIEW: high-impact

## Body
The Compliance Intelligence audit engine's off-label-claim detector (`projects/compliance_intelligence/v1/rules/pack.py`) works by holding the ~14 UHMS/FDA-cleared HBOT indications as an allow-list and flagging disease terms outside it when paired with treatment verbs. As of 2026-07-31, that deny-list was only about 11 disease terms hardcoded directly in Python (autism, cancer, Alzheimer's, Lyme, ADHD, COVID, anti-aging, dementia, Parkinson's, HIV, MS) plus a handful of absolute-claim phrases. Real HBOT marketing violations range far wider than this — TBI/concussion, stroke recovery, fibromyalgia, chronic fatigue, "stem cell activation," longevity/biohacking, sports recovery, detox, immune boost, erectile dysfunction, inflammation "cure," and more. The operator's stated goal is to "quickly identify all Hyperbaric non-compliance across a website in relation to what is not allowed in terms of verbiage and jargon" — the engine cannot honestly support that "all" claim until this lexicon becomes a comprehensive, maintainable KB-driven allow-list/deny-list (data an operator can grow) rather than a short hardcoded Python list. This is the single gap standing between the current engine and the sales claim the operator wants to make.

## Links
- blocks, 2026-08-21-ci-cite-or-omit-law.md, cite-or-omit only protects findings that exist — this gap is about missing findings, not false ones
