---
id: 2026-08-21-agame-sports-tech-stack-astro-tailwind
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [agame-sports, astro, tailwind, tech-stack, decision, content-collections]
sources:
  - ref: "Turns 54-117: lines 54-55 confirm the Astro + Tailwind v4 + content-collections stack rationale; lines 116-117 confirm the operator's explicit WordPress question and the agent's near-verbatim denial that the rebuild touches WordPress."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [54, 117]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A-Game Sports rebuild chose Astro + Tailwind v4 with Markdown content collections, not WordPress
- id: 2026-08-21-agame-sports-tech-stack-astro-tailwind
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — stack was explicitly briefed to the operator, built out to a working 95-page site, and the operator separately confirmed it was not WordPress
- verified: 2026-08-21
- tags: agame-sports, astro, tailwind, tech-stack, decision, content-collections

## Body
For the ~90-page A-Game Sports rebuild (a youth-sports facility site, no registration/payments in scope), the agent chose Astro + Tailwind CSS v4 with page content stored as Markdown in Astro content collections, rather than any CMS or WordPress-based approach. Reasoning given to the operator: the site is content-heavy and mostly static, so Astro ships zero JS by default and generates static HTML per page; content stored as one Markdown file per page with schema-validated frontmatter keeps edits accessible to non-technical staff and fails the build on malformed frontmatter instead of silently breaking a live page; a single dynamic route (`[...slug].astro`) dispatches to one of a few templates by a `template` field rather than hand-writing ~90 page files, which is what let ~85 of the pages be generated later by parallel batch agents against a shared schema. No backend/database was added since registration/payments were explicitly out of scope. The operator later asked "you are aware i do not want this built on WordPress correct?" and the agent confirmed the stack was fully separate from the legacy WordPress/Enfold site.

## Links
- see-also, 2026-08-21-agame-content-honesty-call-to-confirm-pattern.md, the content-authoring discipline this template system enabled across parallel batch agents
