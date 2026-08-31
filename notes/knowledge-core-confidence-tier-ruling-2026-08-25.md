---
id: knowledge-core-confidence-tier-ruling-2026-08-25
type: ruling
status: ratified
source: Architecture, Redlined — Rev. 3, Part V; built and merged into this repo, PR #4
project: fleet
tags: [knowledge-core, zettelkasten, schema]
supersedes: [knowledge-core-confidence-tier-gap-2026-08-25]
superseded_by: null
---

# `status` is the Core's confidence tier, not just a workflow marker

## Body

GeoSuite's own audit rubric tags claims `documented` vs. `hypothesis` rather than
asserting everything with equal confidence — the Core owes its own consumers the same
discipline. No new field was needed: `status` already carried `candidate`/`ratified`, it
just wasn't documented as doing this job.

The rule now in force: `status: candidate` means one agent's unverified read — cite it as
*unconfirmed*, never as settled fact. `status: ratified` means a human has actually signed
off — it can be cited and relied on without that caveat. A session retrieving a note must
check `status` before treating its content as true. Collapsing the two into one
undifferentiated "truth" tier at retrieval time defeats the entire point of the
ratification gate upstream of it.

## Links

- Architecture, Redlined Rev. 3, Part V
- knowledge-core-confidence-tier-gap-2026-08-25 (the finding this ruling closes)
