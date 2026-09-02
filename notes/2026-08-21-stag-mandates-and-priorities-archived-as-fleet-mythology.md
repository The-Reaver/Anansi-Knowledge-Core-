---
id: 2026-08-21-stag-mandates-and-priorities-archived-as-fleet-mythology
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, governance, stag-mandates, provenance, fleet-mythology-cleanup]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn establishing that STAG_MANDATES_AND_PRIORITIES.md was archived as fleet mythology six days after the checklist cited it, with the locked CI build sequence not carried forward."
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
- class: confirmed
- confidence: high — verified directly via git log, file location, and grep against the extraction file
- verified: 2026-08-21

# The document the 2026-08-03 checklist cited for CI's "locked build sequence" was archived as fleet governance mythology six days later, and the ordering was not preserved

## Body
The 2026-08-03 master checklist grounded CI's platform priority ("GEO finish and harden, then CI sales-agent validation, then Living Knowledge Core Phase 2, then Site Generator Phase 3") in `STAG_MANDATES_AND_PRIORITIES.md`. That file no longer exists at repo root: commit `9196c1b` ("Archive fleet mythology files, triage candidates, land promoted notes") moved it to `_to_delete/fleet-lore-superseded-2026-08-09/STAG_MANDATES_AND_PRIORITIES.md` on 2026-08-09, six days after the checklist was written. The archive's own README states the operator asked to strip out "named agents, personas, mandates, rituals, mythological tier names, a self-referential ratification system" because the mythology layer had grown large enough to hurt actual work, and that only content judged "real, non-lore" was pulled into `EXTRACTED_REAL_FACTS_2026-08-09.md` before archiving. A grep of that extraction file for "build sequence", "GEO harden", "sales-agent validation", "Living Knowledge Core Phase 2", and "Site Generator Phase 3" returns zero hits — the specific 4-step CI priority ordering was judged mythology, not fact, and was not carried forward anywhere. No replacement document was found stating an equivalent locked sequence. The ordering the old checklist treated as binding no longer has a canonical live home in the repo; whether the operator still intends that sequence is now an open question, not a documented fact.

## Links
- corrects, reports/STAG_MASTER_CHECKLIST_2026-08-03.md, whose CI entry cites STAG_MANDATES_AND_PRIORITIES.md as the source of the locked build sequence
