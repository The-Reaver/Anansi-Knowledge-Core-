---
id: 2026-08-07-compliance-intelligence-gathering-plan
type: decision
status: candidate
source: Cowork session 2026-08-07, operator on phone; asked for the plan to gather valid compliance information (RSS feeds and other working methods) that the lawyer then validates, to feed the Knowledge Core. Backbone sources verified via web search. (source status: active)
project: geo
tags: [knowledge-core, intelligence-gathering, compliance, rss, api, legiscan, federal-register, lawyer, pipeline, maintenance, geo-suite]
---

# How we gather the raw compliance intelligence before the lawyer validates it (sources plus pipeline)

## Body

## Sources, in tiers

### Tier 1, official government, free and machine-readable (verified working)
- Federal Register REST API and RSS: proposed and final federal rules, filter by agency (HHS/OCR for HIPAA, FTC for advertising, FDA for medical claims).
- Regulations.gov API (GSA): rulemaking dockets and public comments, early signal before a rule finalizes.
- LegiScan API: bill tracking across all 50 states and Congress with keyword monitors. Covers state, local, and pending laws.
- GovInfo API and Congress.gov: federal bills and enacted law.

### Tier 2, agency and enforcement feeds (confirm each at setup)
- FTC releases (advertising, endorsements, health claims).
- HHS / OCR HIPAA news and enforcement.
- FDA promotion and advertising guidance.
- State medical boards and state attorney general advisories.
- CourtListener for relevant litigation and enforcement decisions.

### Tier 3, curated professional (confirm each at setup)
- Health-law firm client alerts, aggregated through services like JD Supra.
- Industry bodies (AMA, state medical associations, MGMA) and compliance vendors.
- Google Alerts and keyword monitors on defined terms, as a catch-all.
- The lawyer's own memos, filed into the Compliance Library.

### Tier 4, AI-search side, to keep readiness rules current
- Google Search Central and Schema.org release notes, so the seven-category scoring tracks how AI engines read sites.
- Industry GEO research on AI citation behavior.

## The pipeline (raw feed to validated rule)
1. Ingestion agents pull each feed on a schedule.
2. A relevance agent filters for medical-practice marketing, AI visibility, and patient data; drops noise.
3. Each keeper becomes a candidate atomic note with source and date, status pending review.
4. Change detection diffs against existing rules; flags new, changed, superseded.
5. Candidate lands in the Compliance Library as Pending review. Lawyer approves, edits, or rejects. Approved becomes a live rule with the lawyer's certification and citation.
6. Each rule carries a re-review date and re-flags automatically when its source updates.
7. Provenance: every rule links to its source document and the certifying lawyer.

## Honesty note (Mandate 7)
- Tier 1 sources are confirmed to have working APIs and feeds. Tiers 2 and 3 confirmed one by one at setup; some offer clean feeds, some need a light scraper.

## Where it goes
- Knowledge Core document (task 13): the gathering-and-validation story.
- Compliance Library build: the Pending review queue and provenance reflect this pipeline.
- Financial document (task 14): any paid API tiers (for example LegiScan) become line items.

## Links

- relates-to: 2026-08-07-knowledge-core-partner-report-spec
- relates-to: 2026-08-07-partner-docs-key-message-core-scales-report-depth
- relates-to: 2026-08-06-antigravity-role-verdict
