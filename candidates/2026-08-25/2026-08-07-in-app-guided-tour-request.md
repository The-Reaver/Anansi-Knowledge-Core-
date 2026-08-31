---
id: 2026-08-07-in-app-guided-tour-request
type: decision
status: candidate
source: "Cowork session 2026-08-07, operator on phone during the GEO Suite demo build; asked for a built-in interactive tour (highlight ring, arrows, click-this steps, what-to-expect) available to anyone, so a lawyer or salesperson learns the app with no training and no ambiguity. (source status: active)"
project: geo
tags: [geo-suite, onboarding, guided-tour, walkthrough, usability, driver-js, role-based, demo]
supersedes: []
superseded_by: null
---

# GEO Suite built-in guided tour, spotlight walkthrough with role paths so any untrained user learns the app

## Body

## What was requested
- A built-in interactive tour inside the app, not static docs.
- Each step: highlighted ring around the target, a pointer arrow, a card that says what the item is and what to expect, with Next/Back/Skip.
- Available to anyone who needs to learn the app: lawyer, salesperson, new hire. Thorough, no ambiguity.

## Design implemented
- Take a tour button in the top bar, always available, plus a first-visit welcome prompt.
- Spotlight dims the rest, ring + arrow + tooltip card (title, plain explanation, what to expect, Next/Back/Skip, step counter). Tour moves across screens as it explains them.
- Covers all screens in order and the key actions (Generate report, Generate site).
- Welcome card offers three paths: Full tour, For legal and compliance (Compliance Library, audit findings, reports), For sales (Prospecting, Sales Kit, Pipeline).
- Plain language for someone with zero training.

## Optional companion (not built unless asked)
- A printable screenshot guide with arrows for offline training. The live in-app tour is preferred because it never goes stale.

## Links

- relates-to: 2026-08-06-geo-suite-demo-spec
- relates-to: 2026-08-07-site-generator-mirrors-build-methodology
