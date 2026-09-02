---
id: 2026-08-21-fleet-roster-ledger-archived-as-mythology
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [fleet, leveling, governance, mythology, roster, ledger, archive, stale-checklist]
sources:
  - ref: "Turns 218-229: assistant launches an 18-workstream background re-verification sweep of the 2026-08-03 master checklist (turn 218) and consolidates the sub-agents' findings, including the Fleet Advancement Pipeline / roster-ledger archival workstream, for the operator (turn 229)."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Fleet Advancement Pipeline\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The named-agent roster/skill-ledger the old checklist's "10 Active entries" figure came from was archived by direct operator decision on 2026-08-09 as governance mythology, not deleted or updated since
- id: 2026-08-21-fleet-roster-ledger-archived-as-mythology
- type: finding
- status: ratified
- class: confirmed
- source: STAG master-checklist refresh sweep, 2026-08-21, workstream "Fleet Advancement Pipeline"
- confidence: high — verified directly against the archived file, the archive commit, and its README, not inferred
- verified: 2026-08-21
- tags: fleet, leveling, governance, mythology, roster, ledger, archive, stale-checklist
REVIEW: high-impact
## Body
The 2026-08-03 master checklist's claim "LEVELS_LEDGER.md showed 10 Active entries" actually sources its per-agent Active/Designed/Seed status from `STAG_Fleet_Roster_and_Skill_Ledger.md` (not `reports/LEVELS_LEDGER.md`, which logs skill-level *moves*, not agent Status). That roster file — along with `FLEET_DOCTRINE.md`, `STAG_MANDATES_AND_PRIORITIES.md`, and `ORLOK_FLEET_USE_PROTOCOL.md` — was moved by direct operator instruction on 2026-08-09 (commit `9196c1b`, "Archive fleet mythology files") to `_to_delete/fleet-lore-superseded-2026-08-09/`. The archive's own README states the operator asked to "clean up the fleet-governance mythology layer that had grown large enough to hurt the actual work: named agents, personas, mandates, rituals, mythological tier names, a self-referential ratification system." Nothing was deleted — the files are intact and recoverable — but they no longer live in the working tree the fleet's day-to-day docs point to, and two real facts (compliance-standards list, actual API spend) were extracted separately into `EXTRACTED_REAL_FACTS_2026-08-09.md` before the archive.

The archived roster's actual row count still supports the checklist's number: counting Status=Active rows as of the 2026-08-09 snapshot gives exactly 10 (Amadeus, Celestina, Elijah, Augustin, Anirak, Oluwole, Bink, Moonshadow, Jasiah, Orlok), with Omar at Designed. So the figure itself is not wrong — but the document it depends on has since been characterized by the operator as ceremony that outgrew its usefulness, and nothing has replaced it as the canonical place to read agent Status from. Anyone re-verifying "how many agents are Active" today has to know to look in `_to_delete/`, not the repo root, and should weigh that the file hasn't been updated (no new Active/Designed changes) since the 2026-08-09 archival itself.
## Links
- extends, research/knowledge-home/candidates/_archived-mythology-2026-08-09/README.md, the parallel archival of the candidate-notes side of the same mythology layer
