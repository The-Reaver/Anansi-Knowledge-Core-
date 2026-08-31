---
id: 2026-08-07-architect-nirjhar-doc-spec
type: decision
status: candidate
source: "Cowork session 2026-08-07, operator on phone; uploaded Nirjhar's resume, asked for a technical document giving him the full scope and a business opportunity to join as lead architect, tied to his current SONNY (monolith to microservices) work. (source status: active)"
project: fleet
tags: [architect, nirjhar, recruiting, technical-scope, opportunity, microservices, engine-room, deliverable-spec]
supersedes: []
superseded_by: null
---

# Spec for the technical scope document addressed to Nirjhar Das (lead-architect opportunity)

## Body

## Audience
- Nirjhar Das, addressed by name, written at engineer level (architecture, backend, data model, pipelines, deployment). He currently has no context on STAG/GEO Suite, so give the full picture.

## Must cover (the whole scope)
- TONY, LLC as parent; STAG as the studio; GEO Suite built for Smart Seed Tech (HBOT USA / Dr. Sonners; ThriveMedix.com).
- The product: the seven-plus screens, the two generators (site and report), the Compliance Library.
- The agent fleet and the training model (STARS/DREAMS), at a technical level.
- The Knowledge Core: shared memory, pgvector on Supabase, atomic notes, provenance.
- The compliance intelligence pipeline: Federal Register/Regulations.gov/LegiScan/GovInfo APIs, ingestion agents, relevance filter, lawyer validation, re-review.
- The tool stack and division of labor: Claude (orchestration/build), Antigravity (engine-room, machine), Lovable (product surface). One repo truth.

## His role and why he fits
- Lead architect of the engine room: audit engines, Knowledge Core services, the ingestion pipeline, backend and data model, deployment.
- Direct tie to his current SONNY job: hardened modular monolith to microservices. GEO Suite follows the same path, so this is a continuation and a step up.
- Resume mapping: NLP/LDA research-paper pipeline -> compliance intelligence ingestion; clean/layered architecture + REST/auth/caching -> backend and services; RL Q-learning agent -> the agent fleet; Docker/Linux/Git/Jira -> deployment and one-repo ops.

## The business opportunity
- One of the operator's assistant/lead roles (salary handled in the finances document, not this doc). Present the growth path: intern-level curiosity into lead architect of a real platform.
- Make it concrete and honest: what he owns, who he works with (the fleet and the tools), and the trajectory.

## Format
- Technical document, likely docx so he can read and annotate. Produce after the app build and the three partner documents.

## Links

- relates-to: 2026-08-07-ownership-and-entity-map
- relates-to: 2026-08-07-compliance-intelligence-gathering-plan
- relates-to: 2026-08-06-antigravity-role-verdict
