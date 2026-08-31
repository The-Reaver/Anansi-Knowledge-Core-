---
id: 2026-08-06-DEFINITIVE-BLUEPRINT
type: note
status: candidate
source: "Google Drive inbox capture, source chat not recorded in original note"
project: geo
tags: []
supersedes: []
superseded_by: null
---

# GEO Suite and The Fleet: The Definitive Blueprint (v1, 2026-08-06)

## Body

Note for the machine session: commit this as BLUEPRINT.md at the repo root and register the PDF (GEO_Suite_Definitive_Blueprint.pdf, delivered to the operator) as an artifact. This is the one document that ties the whole plan together. Detail lives in the linked design notes.

## 1. What we are building
GEO Suite, one platform for medical practices, three tools under one roof: Visibility (get found by patients and AI search), Compliance Intelligence (catch legal problems, attorney-reviewed), and Sales (ranked call list with evidence and talking points). All share one memory and one rulebook. The compliance tool is a standalone product under the umbrella, extractable later.

## 2. The Fleet and the Agent Development Life Cycle
An in-house AI team instead of a large outside dev team. Three parts:
- The Engine, per task: assign, build one slice, prove with a real test, capture a note, raise the score, repeat. No proof, no credit.
- The Ladder: Foundation (low-level, heavy focus), Architecture (Uber/TikTok backbone), Integration (whole apps), Certification, Deployment.
- The Big Loop: after deployment, real jobs become the next training. Work and training are the same loop.

## 3. How agents learn and graduate
Each agent has a STARS (curriculum) and a DREAMS (tracker), both in shared memory, so any chat continues where the last stopped. Train on a simple 1-to-9 scale; certify with proven math, explained simply: Wilson (a cautious pass rate so luck cannot fool us), Glicko (a chess-style rating that knows its confidence), SPRT (when we have tested enough). Log every pass and fail from day one so the math upgrade is ready when wanted.

## 4. Certification and security
A certificate requires every gate: full coverage, real reproducible proof, the math agrees, AJ (independent auditor) signs off on the work not the words, survives the Breakers, a provenance stamp, human sign-off for client clearance, and renewal on a schedule.
Breakers gauntlet: a Red Team that destroys each build before any client sees it, Security, Correctness, Scale, and Chaos Breakers, independent, different AI families, pass only when all come up empty. TYR, first agent from Seed, is the lead Breaker and Security Auditor.
Modeling: cheap fast models for easy and mechanical work, strong independent models for judging and certifying, real tests as the primary proof, escalate a stubborn task to a stronger model.

## 5. Path to building complex apps, the capstone ladder
One hard skill at a time: notes app, accounts and security, multi-user, real-time sync, payments, data pipelines, geolocation and matching, social feed, survive load and crashes, then the full capstone combining all of it and surviving the full Breakers gauntlet. Where possible each capstone is a real GEO Suite piece.

## 6. Build roadmap (order)
- Phase 0 setup: free disk space, push the repo, stand up Knowledge Core live in the cloud.
- Phase 1 the demo (two days): build the GEO Suite demo, which trains the Fleet as it goes.
- Phase 2 foundation: compliance atom-versioning schema, and the sales dashboard with real close-rate.
- Phase 3 the Fleet: birth TYR and the Breakers, build Jeremy's and Oluwole's curricula, add architecture and capstone tracks and the graduation bar.
- Phase 4 governance and hygiene: settle housekeeping, keep one clean copy, keep capturing lessons.

## 7. The two-day demo
One real practice end to end in about five minutes: dashboard, ranked prospect list, real audit with score and cited findings, prospect-facing report, improved AI-ready site before and after, sales call kit, pipeline. Real audit numbers from the built engine, never faked. Label anything not ready as a preview. One example done well beats five half-done.

## 8. Rules that keep it safe
One source of truth (GitHub); nothing is done until saved there; never copy folders over each other. Build one proven slice at a time; never overwrite a proven piece, work on a copy. Capture every lesson as a note. Every session declares online or offline first. Patient data can be kept local and private by design.

## 9. Budget and team (the bill)
- Cloud now, low cost, usage-based, no hardware purchase needed now.
- Local and private as clients require: a modest secure server for patient data, a dedicated AI machine only when a client requires data never leave their office, decided with counsel.
- People: three assistants at roughly 700 to 1000 dollars per month each, for accountability, production hardening, and security.

## The vision in one paragraph
GEO Suite gets medical practices found, keeps them compliant, and helps close them, and behind it an in-house AI Fleet learns on the job, proves itself with real tests and an independent auditor, is stress-tested by a team of Breakers, and keeps sensitive data private. It builds fast, safely, and affordably, gets smarter every day, and depends on far fewer outside people over time.

## Links

- extends: 2026-08-06-agent-development-lifecycle-adlc-gameplan
- extends: 2026-08-06-capstone-ladder-and-build-priority-order
- extends: 2026-08-06-graduation-bar-and-breakers-gauntlet-design
- extends: 2026-08-06-geo-suite-demo-spec
- extends: 2026-08-06-brain-trust-verdicts-and-operator-contributions
