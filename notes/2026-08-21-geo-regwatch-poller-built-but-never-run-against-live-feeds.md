---
id: 2026-08-21-geo-regwatch-poller-built-but-never-run-against-live-feeds
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, knowledge-core, regwatch, compliance, dormant-feature]
sources:
  - ref: "Turns 430-458: turn 430 is the agent acknowledging an operator-uploaded doc ('HBOT Compliance Gathering.md') ends in a question worth answering, turn 458 is the answer describing the regwatch module paths, 6-hour poll cadence, alert status set, and test-fixtures-only status."
    reliability: high
    origin: "STAG session, 2026-08-14, \"GEO Suite completion\" (backfilled from historical transcript b9b0acfa, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-14-backfill-b9b0acfa.jsonl
  turns: [430, 458]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# GEO Suite already has a real regulatory-change poller (`knowledge_core/regwatch/`) built to track bills/rules through Federal Register and Congress.gov every 6 hours with status-based alerting — but it has only ever run against test fixtures, never live feeds
- id: 2026-08-21-geo-regwatch-poller-built-but-never-run-against-live-feeds
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-14, "GEO Suite completion" (backfilled from historical transcript b9b0acfa, 2026-08-21)
- confidence: high — direct code inspection reported by the agent, same session
- verified: 2026-08-21
- tags: geo, knowledge-core, regwatch, compliance, dormant-feature
- REVIEW: high-impact

## Body
The operator asked how the product would track law changing over time — a bill moving through the House/Senate, a rule going final. The agent found that this exact architecture already exists in the codebase, unbuilt in the sense of not being wired to anything live: `knowledge_core/regwatch/` and `knowledge_core/feeds/regulatory/` are built to poll the Federal Register and Congress.gov on a 6-hour cycle, and already implement the status categories the operator was describing from first principles — `final_rule`, `passed_chamber`, and `enforcement_action` are designed to trigger an alert, while a bill that is merely introduced or a rule still in proposed form logs quietly as a draft note with no alert. As of this session, the poller has only ever been exercised against test fixtures, not real Federal Register/Congress.gov traffic — bringing it live is a real, scoped next step, not a design task. The agent also flagged that its output should go through the adversarial-review skill before being trusted, since "does this feed actually say what it claims" is exactly the failure mode that skill exists to catch.

## Links
- relates, 2026-08-16-good-faith-adversarial-review-skill-first-run-caught-real-issues.md, the review gate the agent recommended running before this poller's output is trusted.
