---
id: 2026-08-21-ci-part-d-reopening-not-written-back-into-binding-constraints-doc
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, documentation-drift, binding-constraints, part-d, conflict]
sources:
  - ref: "Turns 226-229: operator relays the background sweep's task-notification output (turn 226) and assistant consolidates findings across workstreams, including Compliance Intelligence's Part D reopening conflict, for the operator (turn 229)."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Compliance Intelligence (platform + standalone extraction)\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [226, 229]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The ratified Part D reopening (scheduled prospect-list crawl) was never written back into COMPLIANCE_INTEL_BINDING_CONSTRAINTS.md, so the canonical doc still reads as fully closed
- id: 2026-08-21-ci-part-d-reopening-not-written-back-into-binding-constraints-doc
- type: finding
- status: ratified
- class: confirmed
- source: STAG master-checklist refresh sweep, 2026-08-21, workstream "Compliance Intelligence (platform + standalone extraction)"
- confidence: medium — the two documents genuinely conflict on their face; low practical stakes since the crawl endpoint doesn't exist yet either way
- verified: 2026-08-21
- tags: compliance-intelligence, documentation-drift, binding-constraints, part-d, conflict

## Body
Two sources conflict and the conflict is named rather than resolved. `reports/OPERATOR_RATIFICATION_PART_D_REOPEN_2026-08-03.md` states the operator ratified, in chat on 2026-08-03, a narrow reopening of `docs/COMPLIANCE_INTEL_BINDING_CONSTRAINTS.md` section C6 to authorize a scheduled crawl of the seeded prospect list. But the live text of `docs/COMPLIANCE_INTEL_BINDING_CONSTRAINTS.md` itself, read today, still says under "C6 — Automations: Part D (operator choice 2026-07-29)": **"Do not set up automations for now"** — the original, unreopened prohibition, with no amendment noting the 2026-08-03 exception. A reader who opens only the binding-constraints doc (which calls itself "operator law" and "not suggestions") would not learn the scheduled-crawl exception exists at all; they would have to separately know to check the reports folder. This is lower-stakes in practice right now because the crawl endpoint the reopening authorized still doesn't exist (see companion finding on the unwired live crawler), so nothing is currently running under the reopened authority that the doc's text would incorrectly forbid — but if/when that endpoint is built, whoever builds it needs to know to check the ratification report, not just the binding-constraints doc.

## Links
- conflicts-with, reports/OPERATOR_RATIFICATION_PART_D_REOPEN_2026-08-03.md, which the binding-constraints doc's own live text does not reflect
