---
id: 2026-08-07-ci-intelligence-source-tiers-locked
type: spec
status: ratified
source: "Cowork session 2026-08-07, operator on phone; asked for the plan to gather valid compliance information that the lawyer then validates, to feed the Knowledge Core; backbone sources verified via web search (source status: active); mined from candidates/2026-08-25/2026-08-07-compliance-intelligence-gathering-plan.md"
project: ci
tags: [ci, sources, rss, api, legiscan, federal-register, tiers]
supersedes: []
superseded_by: null
---

# CI raw-intelligence sources locked into four tiers, Tier 1 government APIs confirmed working

## Body

Tier 1, official government, free and machine-readable (verified working): Federal Register REST API and RSS, filtered by agency (HHS/OCR for HIPAA, FTC for advertising, FDA for medical claims); Regulations.gov API (GSA) for rulemaking dockets and public comments; LegiScan API for bill tracking across all 50 states and Congress with keyword monitors; GovInfo API and Congress.gov for federal bills and enacted law. Tier 2, agency and enforcement feeds (confirm each at setup): FTC releases, HHS/OCR HIPAA news and enforcement, FDA promotion/advertising guidance, state medical boards and AG advisories, CourtListener. Tier 3, curated professional (confirm each at setup): health-law firm client alerts aggregated through services like JD Supra, industry bodies (AMA, state medical associations, MGMA) and compliance vendors, Google Alerts keyword monitors, the lawyer's own memos filed into the Compliance Library. Tier 4, AI-search side, to keep readiness rules current: Google Search Central and Schema.org release notes, industry GEO research on AI citation behavior.

## Links

- relates: 2026-08-07-ci-intelligence-pipeline-raw-feed-to-validated-rule
