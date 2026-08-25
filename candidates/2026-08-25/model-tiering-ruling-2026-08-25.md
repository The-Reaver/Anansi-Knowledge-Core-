---
id: model-tiering-ruling-2026-08-25
type: ruling
status: candidate
source: Architecture, Redlined — Rev. 3 (artifact 924c39f2), Part IV; captured via GeoSuite session handoff, 2026-08-25
project: fleet
tags: [model-tiering, cost, agent-engineering]
---

# Model/effort tier is chosen by task class, not by default habit

## Body

Standing rule for which model/effort tier an Agent or Workflow call gets, so the choice
stops being re-derived per call:

| Task class | Tier | Why |
|---|---|---|
| Targeted grep-and-report, single-file lint pass, narrow lookup with one right answer | Cheapest/fastest available | No judgment call in the loop — cost of wrong is a re-run, not a bad decision shipped. |
| First draft: scaffolding, rough implementation to react to, exploratory research | Mid tier | Needs real reasoning but is a draft by definition — reviewed before it matters. |
| Synthesis across sources, architectural/product judgment call, anything that becomes the record | Full strength | A subtle wrong call compounds — every downstream decision inherits it. |
| Adversarial review, mutation-test verification, anything whose job is catching what the first pass missed | Full strength, never downgraded | A cheap reviewer is a reviewer that agrees. |

This is a going-forward habit, not a backlog: apply it to the next Agent/Workflow call
in any session, no retrofit of past calls needed.

## Links

- Architecture, Redlined Rev. 3, Part IV
- skill-eval-gate-2026-08-25
