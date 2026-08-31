---
id: 2026-08-07-partner-financial-report-spec
type: decision
status: candidate
source: "Cowork session 2026-08-07, operator on phone during the GEO Suite demo build; asked for a SEPARATE financial report so there is no ambiguity on costs later. Produce with the other reports after the demo build wraps. (source status: active)"
project: fleet
tags: [financial-report, partner, costs, staffing, salaries, cloud, tools, savings, deliverable-spec, budget]
supersedes: []
superseded_by: null
---

# Spec for the standalone partner financial report, costs to build and maintain, staffing, tools, and money saved

## Body

## Must include
- Standalone financial report, separate from the GEO Suite update and the Knowledge Core report. No ambiguity, all costs and expenses covered now.
- Staffing: the three assistants and their salaries, range about $700 to $1000 per month each. Note the team grows later, but three is enough for now.
- Do NOT mention the operator's salary anywhere. The partner negotiates it on the operator's behalf. It appears on no page.
- Build costs (one-time / setup) versus maintenance costs (recurring monthly), split clearly.
- Cloud services, including the ones that run for maintenance: the Knowledge Core database (Supabase or equivalent) and hosting/deployment.
- Every tool with a line item: Claude (plans and/or API), Lovable (build credits), Google Antigravity, Cursor, plus any other tool worth adding on top of Claude.
- Money saved: what this same capability costs the traditional way (a hired dev team or an agency) set against what we spend. Make the saving the headline.
- Set expectations so there are no questions later.

## Research to do at production time (pull current prices)
- Supabase or equivalent managed Postgres + pgvector: free/pro tier pricing at our scale.
- Hosting/deployment (Lovable-hosted vs separate host).
- Claude: current plan tiers and API pricing relevant to our use.
- Lovable: credit pricing and monthly plan.
- Google Antigravity: cost/tier.
- Cursor: current plan (operator on the $20 tier).
- Any recommended additions on top of Claude (for example monitoring, a document/OCR tool for the Compliance Library ingestion, a scheduler for maintenance agents). Only recommend with a clear reason.
- Comparison figure: realistic cost of a traditional dev team or agency for the same build and upkeep, so the savings are concrete and defensible.

## Format
- Layman-readable financial report, likely docx or PDF, with a clear one-time vs monthly table and a savings summary. Match the voice of the prior partner reports.

## Links

- relates-to: 2026-08-07-knowledge-core-partner-report-spec
- relates-to: 2026-08-06-brain-trust-verdicts-and-operator-contributions
- relates-to: 2026-08-06-antigravity-role-verdict
