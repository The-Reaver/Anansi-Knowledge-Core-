---
id: 2026-08-06-antigravity-role-verdict
type: decision
status: ratified
source: "Cowork session 2026-08-06, operator on phone; approved building the GEO Suite demo on Lovable, then asked the Brain Trust to decide what role Google Antigravity plays (about 70% usage left there) and how cleanly Lovable, Antigravity, and Claude work together. Operator asked to pin it. (source status: active)"
project: geo
tags: [brain-trust, verdict, antigravity, lovable, tooling, division-of-labor, geo-suite, demo, engine-room, pin]
supersedes: []
superseded_by: null
---

# Brain Trust verdict, Antigravity's role in the fleet and how the tools stay clean together

## Body

## What Antigravity is
- Google's agent-first IDE, launched late 2025, built around Gemini 3. Agents plan and run multi-step coding work across the editor, terminal, and a real browser, and produce proof of work (task lists, screenshots, browser recordings). Google is folding Gemini CLI into an Antigravity CLI. It runs on the machine as a development environment, not from the phone.

## Verdict, one lane per tool
- Lovable is the storefront. Builds and polishes the GEO Suite app and client-facing UI fast, in the cloud, drivable from the phone through Claude. Owns what the partner and customers see.
- Antigravity is the engine room. On the machine, its agents build and harden the real audit engines, backend, data pipelines, and tests, and run things in a real browser to prove they work. Its proof-of-work output fits Mandate 7 (no capability claim without proof).
- Claude and the fleet are the brain and foreman. Plan, write specs, curate the Knowledge Core, run the Breakers gauntlet, certify through AJ, capture every build as notes.

## How they stay clean together
- Shared floor: the one repo (Mandate 9). Shared memory: the Knowledge Core.
- One area per tool. Lovable owns the app UI folder. Antigravity owns engines and backend. Never both editing the same files at once. Two agentic tools in one folder is the divergence pain already lived through.

## Honest caveats
- Do not assume Lovable exporting to Git and Antigravity reading that repo round-trips cleanly. Test the handoff once on a throwaway first.
- Antigravity is new. Treat its output like any agent's; run it through the Breakers and AJ before certifying.

## The pin, decision now, action later
- For the two-day demo, stay on Lovable, phone-doable and the surface the partner needs. Do not split focus during the sprint.
- Bring Antigravity in at the machine, engine-room lane, right after the demo, starting with the real audit engines and backend hardening. The ~70% usage is a strong asset for that heavy work.

## Links

- extends: 2026-08-06-geo-suite-demo-spec
- relates-to: 2026-08-06-brain-trust-verdicts-and-operator-contributions
- relates-to: 2026-08-06-capstone-ladder-and-build-priority-order
