---
id: 2026-08-21-agame-content-honesty-call-to-confirm-pattern
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [agame-sports, content-generation, hallucination-avoidance, fact-verification, multi-agent]
sources:
  - ref: "Turns 206-226: batch-agent completion reports at lines 214, 218, 220, 222, 226 (covering all 8 relaunched/surviving batches) each independently document the 'wrote around instead of inventing' / 'call to confirm' discipline, matching the note's specific examples (Flag Football tryout dates, Summer Camps phone-confirm line)."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [206, 226]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Parallel content-build agents consistently refused to invent missing facts, writing "call to confirm" instead
- id: 2026-08-21-agame-content-honesty-call-to-confirm-pattern
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — the pattern is explicitly self-reported by all 8 independent batch agents in their completion summaries, covering ~85 pages
- verified: 2026-08-21
- tags: agame-sports, content-generation, hallucination-avoidance, fact-verification, multi-agent

## Body
When building ~85 remaining content pages for the A-Game Sports rebuild, 8 parallel batch subagents were each instructed to crawl the live legacy site and use only verified facts. Every one of the 8 agents' completion reports independently documented the same discipline: where the live site did not state an age range, price, or exact date for a program, the agent did not invent one — it wrote copy directing the reader to call the facility's phone number to confirm, or (for schedule pages, e.g. the seasonal calendar and specials page) described the page's purpose without asserting stale or unconfirmed dates as current. Examples: softball/baseball team pricing with no published rate ("call ... to confirm current pricing"), Flag Football tryout dates that were tied to a stale prior year (kept the durable structural facts, dropped the dated specifics, added a call-to-confirm note), and a "Specials" page where several listed promotions were already expired relative to the session's date — the agent kept only the one confirmed evergreen fact (a 15% veteran discount) and described the general pattern of seasonal specials rather than asserting current terms. This is a durable, generalizable pattern for any agent-driven content-migration task: verified facts get reproduced verbatim; anything the source doesn't state gets an honest "call/confirm" pointer rather than a plausible-sounding invention.

## Links
- see-also, 2026-08-21-agame-sports-tech-stack-astro-tailwind.md, the shared content schema/template system this discipline was applied within
