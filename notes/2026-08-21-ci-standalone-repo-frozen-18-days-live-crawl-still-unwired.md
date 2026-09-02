---
id: 2026-08-21-ci-standalone-repo-frozen-18-days-live-crawl-still-unwired
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (day-count updated 18→22 days, and the 'one trivial commit' characterization corrected to reflect a second, substantive commit — 77b647e, 2026-08-21, the Brain Trust Q2 security fix — that has since landed, without touching the crawler gap). Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, standalone-extraction, stall, live-crawler, go-live-gap]
sources:
  - ref: "Turns 226-229: operator relays the background sweep's task-notification output (turn 226) and assistant consolidates findings across workstreams, including the standalone CI repo's activity/crawl-wiring status, for the operator (turn 229)."
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

# The standalone CI repo has had one trivial commit in the 22 days since the checklist, and the live-crawler gap it named is still unwired today
- id: 2026-08-21-ci-standalone-repo-frozen-18-days-live-crawl-still-unwired
- type: finding
- status: ratified
- class: confirmed
- source: STAG master-checklist refresh sweep, 2026-08-21, workstream "Compliance Intelligence (platform + standalone extraction)"
- confidence: high — verified via git log inside the nested repo and a direct code read of the current tree
- verified: 2026-08-21
- tags: compliance-intelligence, standalone-extraction, stall, live-crawler, go-live-gap

## Body
The 2026-08-03 checklist said the live crawler and live GPT interpretation call were "designed but not running." Twenty-two days later that is still true, and the workstream itself has been largely idle: `git log --since=2026-08-03` inside `projects/compliance_intelligence` (a separate nested git repo, its own remote `The-Reaver/compliance-intelligence-tool`) returns two commits — `82fb2ae` on 2026-08-04, a smoke-test error-logging tweak, and `77b647e` on 2026-08-21, a substantive fix implementing the Brain Trust 2026-08-08 Q2 emergency security ruling (auth on KB endpoints, atom sign-off gate, binding/advisory render gate, real atom version history). Neither commit touches the crawler gap. Directly reading the current tree confirms that gap is unchanged: `shared/snapshot.py` defines `crawl_domain` (a BFS crawler honoring robots.txt/sitemaps), but `grep -rn "crawl_domain" api/` returns no hits — `api/app.py`'s only audit endpoint (`POST /clients/{id}/engagements/{id}/runs`) still takes pasted content, not a domain, exactly as it did on 2026-08-03. Separately, the operator's narrow 2026-08-03 ratification (`reports/OPERATOR_RATIFICATION_PART_D_REOPEN_2026-08-03.md`) authorized a scheduled, repeatable crawl of the seeded prospect list, with an explicit exit condition of "two scheduled runs, two timestamps." Since there is still no endpoint that invokes `crawl_domain` at all, that exit condition cannot have been met. The checklist's "designed but not running" status has not changed; it has simply persisted for 22 more days, with one substantive but unrelated security commit and no forward movement on the crawler itself recorded in this repo's history.

## Links
- confirms-unchanged, reports/STAG_MASTER_CHECKLIST_2026-08-03.md, "the live crawler and the live GPT interpretation call, both designed but not running"
- depends-on, reports/OPERATOR_RATIFICATION_PART_D_REOPEN_2026-08-03.md, whose exit condition (two scheduled crawl runs) requires the still-missing endpoint wiring
