---
id: 2026-08-07-cippe-lovable-version-build-scope
type: decision
status: candidate
source: Cowork session 2026-08-07; operator confirmed building the Lovable version from the Drive Ledger, Queue Entry, and Handoff, with a tour, a feedback loop, a bridge back to the team, and a private deploy on a domain the operator buys. (source status: active)
project: cippe
tags: [cippe, privacy-agent, lovable, neurodivergent, externalized-thread, gdpr, dsar, tour, feedback-loop, private-deploy]
---

# Build scope for the Lovable version of the TONY, LLC CIPP/E privacy copilot (dashboard-first, simpler UI)

## Body

## Relationship to the canonical build
- Canonical build: FastAPI + HTMX + Postgres 16/pgvector, single container, handed to Antigravity, spec v1.3 RATIFIED, five slice specs. That is the internal build.
- This Lovable version is the simpler, calmer, dashboard-first surface the operator finds easier to use. React/Tailwind/shadcn on Lovable. Same product intent, lighter UI.

## Product identity
- Private, single-user CIPP/E (GDPR) privacy copilot for a neurodivergent operator (ADD/ADHD). Provably cited. CIPP/E primary, CCPA/CPRA secondary, jurisdiction-tagged.

## Neurodivergent design (The Externalized Thread)
- Now-track dashboard: one large "right now" card with a single primary action, ambient clock, resume-where-you-left-off, a short upcoming list, and a low-distraction toggle that hides all but the right-now card.
- Calm, spacious, low-distraction. WCAG 2.2 AA plus COGA. Accessible auth (password manager or OS credential, paste allowed, no PIN/CAPTCHA).

## Screens
- Now (dashboard, signature screen).
- Ask (copilot chat, answers with provable citations to GDPR articles, EDPB, CCPA/CPRA).
- Knowledge (the jurisdiction-tagged legal corpus, plus manual knowledge capture).
- DSAR (deadline clock keyed to Ireland public holidays, identity proportionality bands low 0.80/0.50 high 0.95/0.70, R2 7-day pre-due window, auto-draft behind gates, never auto-send).
- Requests (the feedback loop and bridge: the operator talks to it and requests features, which flow back to the TONY fleet to build).
- Settings (auth, low-distraction default, calendar version).
- Built-in guided tour, calm and low-distraction.

## Operator's new requirements
- Built-in tour.
- Feedback loop: the operator can talk to it and request features to be created.
- Bridge back to us: feature requests flow to the team so we build the future features.
- Private deployment: operator buys a domain, we deploy, keep it private (auth-gated, single user).

## Intelligence gathering for this agent (distinct from GEO Suite medical)
- GDPR statutory text (EUR-Lex), EDPB guidance and opinions, CCPA and CPRA text, Ireland public-holiday calendar (version-pinned, Good Friday excluded), DPC and EDPB decisions. Gathered for the operator, stored jurisdiction-tagged, answers provably cited.

## Build method
- Slice by slice, plan mode first, in Morel's Lovable workspace. Sample data clearly labeled until the corpus is loaded.

## Links

- relates-to: 2026-08-07-compliance-intelligence-gathering-plan
- relates-to: 2026-08-06-antigravity-role-verdict
- source docs: Project Ledger (1-bjl5Q_67x4ANre5hJ1r_uANDYes4Xnz), Queue Entry (1IlD3WQl2jGwBStAZVY1_p15_pmwx-mgM), Handoff (1bzXoErpKdnYO9kCVxOw7hDF38ekU3S5O)
