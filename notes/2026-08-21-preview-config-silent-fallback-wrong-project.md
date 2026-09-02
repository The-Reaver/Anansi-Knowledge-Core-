---
id: 2026-08-21-preview-config-silent-fallback-wrong-project
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [preview-start, launch.json, dev-server, tooling-gotcha, agame-sports]
sources:
  - ref: "Turns 124-129: lines 124-126 show a preview_start/preview_stop/Bash sequence; line 127 is the agent's own diagnosis, near-verbatim, that launch.json had only one config (for an unrelated GEO frontend) which was silently used, followed by adding a proper entry for this project."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [124, 129]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A single-entry launch.json silently served a different project's dev server through preview_start
- id: 2026-08-21-preview-config-silent-fallback-wrong-project
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: medium — observed once in this session; the agent's own explanation ("there's only one config, for an unrelated GEO frontend, so it silently used that") was not independently re-verified against tool internals
- verified: 2026-08-21
- tags: preview-start, launch.json, dev-server, tooling-gotcha, agame-sports

## Body
When the agent first called the browser preview tool to verify the new A-Game Sports rebuild in-browser, `.claude/launch.json` in the stag repo contained only one dev-server configuration entry, left over from an unrelated GEO Suite frontend project. The preview tool used that single existing entry rather than erroring or prompting for which project to serve, so the browser silently loaded the wrong project's server. The agent caught this only by noticing the served content didn't match what it expected, then added a proper named entry for the new project and re-ran. Lesson: when multiple projects share one repo's `.claude/launch.json`, an agent starting a preview for a new project should explicitly add/select a matching entry rather than assuming an existing single entry is scoped to the current task — a stale or unrelated single entry will be used silently, with no error.

## Links
