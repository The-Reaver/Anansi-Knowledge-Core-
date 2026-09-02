---
id: 2026-08-21-sprint0-hardening-sequenced-before-first-revenue-tool
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, project-brief-step0, sequencing, sprint-planning, billing, webhook]
sources:
  - ref: "Archive turns 10-24: turn 10 first names 'B's secrets hygiene'; turn 15 confirms the webhook handler's code side needs no changes (the blocker is purely environmental); turn 20 confirms the router is mounted and reads STRIPE_WEBHOOK_SECRET correctly; turn 22 is the explicit recommendation; turn 23 is the operator's literal 'we will go with you recommendation'; turn 24 confirms 'Going with B'."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [10, 24]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, the operator explicitly adopted the agent's stated recommendation
- verified: 2026-08-21

# Sprint 0 billing/webhook hardening was sequenced before building the first revenue tool because it was credit-free and every tool's billing sits on the same webhook plumbing

## Body
With Anthropic account credits empty and two viable next steps available for `project_brief_step0_resolved` -- (B) finish Sprint 0 hardening (align the Stripe webhook's Sandbox-vs-Test-mode environment, fix the Nixpacks build-secret warning) versus (A) start building the first revenue tool (Missed-Call Text-Back) through the full Product->Design->Build->Verify SDLC -- the operator chose B first, on the agent's recommendation ("we will go with your recommendation").

Stated rationale at decision time: B is entirely credit-free repo/config work requiring no agent-generation runs, while A is a full multi-phase build sprint; and the Stripe webhook specifically is foundational plumbing that every tool's billing logic is built directly on top of, including the future Payment Recovery tool and the `account_state`/dunning path -- so building product tools on an unaligned webhook risked guaranteed rework later. A security fix (secrets hygiene) was also treated as something that shouldn't wait behind product work.

This is a project-specific sequencing call, not a universal rule, but the transferable heuristic is: when budget is constrained, fix shared foundational plumbing that later feature work will build on -- if doing so is free -- before spending scarce budget on net-new feature work that would have to be redone once the foundation changes.

## Links
- extends, 2026-08-21-nixpacks-bakes-railway-env-vars-into-build-image-accepted-low.md, one of the two Sprint 0 hardening items this sequencing decision was justifying.
