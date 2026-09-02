---
id: 2026-08-21-bink-deterministic-checks-proven-judge-step-still-open-key-now-present
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [agent-capability-mining, bink, geo, verification-gap, gemini-api-key]
sources:
  - ref: "Turns 218-229: assistant launches an 18-workstream background re-verification sweep of the 2026-08-03 master checklist (turn 218) and consolidates the sub-agents' findings, including the Bink / Agent-capability-mining workstream, for the operator (turn 229)."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Agent capability mining\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Bink's golden-dataset gap is narrower than the stale checklist states: deterministic checks were proven correct on 2026-08-03 and confirmed not-a-bug on 2026-08-08, and the one real GEMINI_API_KEY blocker has since landed in .env but the LLM-as-judge step still has not been run

- id: 2026-08-21-bink-deterministic-checks-proven-judge-step-still-open-key-now-present
- type: finding
- status: ratified
- class: confirmed
- source: STAG master-checklist refresh sweep, 2026-08-21, workstream "Agent capability mining"
- confidence: high — ledger, ratified correction note, and current .env presence (existence only, value not read) checked directly
- verified: 2026-08-21
- tags: agent-capability-mining, bink, geo, verification-gap, gemini-api-key

## Body

The stale 2026-08-03 checklist line says only "Bink governance gap found (one logged run
self-admittedly mocked), reverted to unverified," which was accurate on 2026-08-03 but is an
incomplete picture of where things stand now. Same day, later, `reports/LEVELS_LEDGER.md`
records a real rebuild: `scripts/gates/bink_golden_dataset_runner.py` plus
`tests/test_bink_golden_dataset_runner.py` replaced the never-real script, with a genuine
RED-then-GREEN discrimination cycle on the deterministic checks (10/10 passing, re-run and
confirmed during this sweep). A 2026-08-08 self-correction
(`research/knowledge-home/notes/2026-08-08-correction-2026-08-08-bink-golden-dataset-1-2-was-never-a-bu.md`,
Brain Trust-ratified 2026-08-09) further found that the "1/2" deterministic result was never a
defect — `geo_test_002` is a deliberately-invalid fixture and failing it is the checker working
correctly. So the deterministic half of Bink's golden-dataset proof is solid, not merely
unverified.

What remains genuinely open is exactly what the ledger already named: the LLM-as-judge half has
never run against a real API key, so the honest verdict stays `PARTIAL_NO_JUDGE`, not a full
proof. This sweep confirms two things about that gap today: first, no report or note dated
after 2026-08-08 anywhere in the repo shows a real judge run for Bink's golden dataset (a
2026-08-17 entry in `projects/geo_platform/GEO_DEVELOPMENT_LOG.md` shows the operator supplying
a real `GEMINI_API_KEY` into the root `.env`, but that run was against
`live_citation_check_2026-08-17.py`, a different script, not Bink's runner). Second, the root
`.env` in the current tree does contain a `GEMINI_API_KEY=` line (existence checked only, value
not read or logged). The one remaining blocker the 2026-08-03 ruling and the 2026-08-03 ledger
both named as the reason Bink's claim can't close is now trivially actionable — the key exists
in the working tree — but as of this sweep it still has not been exercised against
`bink_golden_dataset_runner.py`.

## Links
- relates, reports/LEVELS_LEDGER.md (entries following "bink-golden-dataset-runner (Bink) built")
- relates, research/knowledge-home/notes/2026-08-08-correction-2026-08-08-bink-golden-dataset-1-2-was-never-a-bu.md
- relates, reports/AMADEUS_RULING_CAPABILITY_MINING_2026-08-03.md
