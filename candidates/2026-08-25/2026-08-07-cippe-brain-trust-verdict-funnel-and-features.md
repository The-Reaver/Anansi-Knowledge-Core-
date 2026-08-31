---
id: 2026-08-07-cippe-brain-trust-verdict-funnel-and-features
type: decision
status: candidate
source: "Cowork session 2026-08-07; operator asked for deep research on the privacy intelligence funnel, what privacy professionals do day-to-day at top firms, and the tools they need, then a Brain Trust decision before continuing the build. Three parallel research agents ran; verdict synthesized here. (source status: active)"
project: cippe
tags: [cippe, privacy, intelligence-funnel, maintenance, gdpr, ccpa, dsar, ropa, dpia, feature-set, brain-trust, research]
supersedes: []
superseded_by: null
---

# Brain Trust verdict, the CIPP/E copilot intelligence funnel, maintenance mechanism, and the daily-work feature set (deep research)

## Body

## Verdict
Build the CIPP/E copilot as a "privacy office in a box" for a solo operator: the GEO Suite funnel philosophy (gather, validate, cite, keep current, human-in-the-loop) tuned to privacy law and to the privacy professional's daily work.

## Intelligence funnel: track the procedure, not just the document
Lifecycle stages (each law is a record with a status): proposed, in committee, enacted, published (OJ / session law), in force, effective/application date, amended, superseded, repealed, plus guidance and enforcement.

### Sources (verified)
EU (all free): EUR-Lex (CELLAR SPARQL API + RSS + SOAP web service), EU Official Journal L-series daily RSS, Parliament Legislative Observatory OEIL (pre-adoption, RSS per procedure), EDPB (guidelines/opinions/decisions), national DPAs (e.g. Ireland DPC).
US: LegiScan (all 50 states + Congress, normalized status; free 30k/mo Pull + weekly datasets; paid Push for 4h/15min updates), Congress.gov API, GovInfo API, California CPPA rulemaking, state AGs (e.g. Colorado), IAPP US State Privacy Legislation Tracker (paid, human-curated cross-check).

### Maintenance mechanism (never serve stale/untrue law)
- Data model: each rule versioned and time-bounded, with entry-into-force and effective date as separate fields, supersedes/superseded_by links, provenance (source URL, retrieved_at, content hash), confidence, review_status.
- Change detection: scheduled re-fetch; hash-diff to catch silent edits/corrigenda; status-transition detection (LegiScan status, EUR-Lex in-force/repealed); effective-date watch fires review N days before a law takes effect; supersession auto-links old versions.
- Freshness SLA: per-rule last_verified_at with a TTL (pending/active items daily-weekly, stable law monthly, deep re-validation quarterly). Past TTL -> copilot marks answer "verification pending" rather than asserting current.
- Human-in-the-loop: every candidate change lands in a pending-review queue with old/new diff, source + date, detected transition, and a confidence tier (primary official source = high; secondary tracker = medium, needs corroboration; unclear hash-diff = low). Cannot be approved without a primary-source citation. Approve writes a new version and preserves history. Conflicting signals escalate and block a definitive answer.

## What privacy professionals do (roles)
- Execution (analyst/associate): fills RoPA, processes DSARs, sends vendor questionnaires, drafts DPIAs, reviews access, monitors logs, delivers training.
- Risk/oversight (DPO): independent monitoring, DPIA advice, regulator contact, residual-risk sign-off.
- Strategy (CPO): program design, board reporting, budget, competitive positioning, crisis leadership.
- A solo operator wears all three hats; tooling that compresses execution frees them for risk and strategy.

## Feature set, ranked by daily centrality
Tier 1 (core daily): RoPA register / data map (the spine); DSAR tracker with per-jurisdiction statutory clock (GDPR 30d, CCPA 45d) [already in ratified spec]; DPIA/PIA wizard (7-stage, risk matrix, mitigation library, sign-off); vendor/TPRM assessment intake (tiering, questionnaire, scoring, evidence, DPA checklist, reassessment).
Tier 2 (recurring): incident/breach module with 72-hour clock (severity, authority + subject notices, register); regulatory-change feed / horizon scanning (jurisdiction-filtered, impact workflow linking changes to affected RoPA/policies, spawns tasks); report generator + board dashboard (DSAR SLAs, open DPIAs, vendor backlog, breaches, training).
Tier 3 (supporting): access-request & recertification register; privacy-by-design product gate; training tracker; website/cookie & activity scanner.
Design principle: interlinked, not siloed. RoPA is the spine; high-risk RoPA entry auto-triggers a DPIA; vendors link to RoPA entries; a breach scopes subjects via RoPA; the dashboard reads all.

## Where the AI copilot adds most value (assist tier)
Draft DPIAs from a plain description; answer law questions with real citations; summarize regulatory changes ("what changed and what it means"); triage and draft DSAR responses. Skip enterprise overkill (multi-cloud auto-discovery, thousand-system DSAR auto-fulfillment).

## Tooling landscape (context)
Enterprise suites: OneTrust, TrustArc, BigID, Securiti, Transcend. Lighter/SMB: Osano, DataGrail, Ketch, Enzuzo. Common modules: assessments (DPIA/PIA), DSAR automation, RoPA/data mapping, consent, vendor risk, incident/breach, regulatory-change management, reporting/audit. Vendors moving from assist to agentic (OneTrust breach agent on MS Security Copilot; Transcend Agentic Assist + MCP; DataGrail Vera).

## Cost implications (feed the finances doc)
Free: EUR-Lex/CELLAR, OJ RSS, OEIL, EDPB, DPC, Congress.gov, GovInfo, CPPA, state AGs, LegiScan free tier. Paid, worth it: IAPP tracker (curated US state cross-check), LegiScan Push (near-real-time state status).

## Recommended build order (slice by slice)
1. Finish copilot core in flight: Ask (citations), Knowledge (corpus + pending-review queue), Now ties in.
2. Tier 1 tools: RoPA register, DSAR tracker, DPIA wizard, vendor intake.
3. Tier 2: breach module, regulatory-change feed, report generator + dashboard.
4. Tier 3, tour, Requests feedback bridge, Settings.
Every legal answer cited; human-in-the-loop before anything is trusted.

## Links

- relates-to: 2026-08-07-cippe-lovable-version-build-scope
- relates-to: 2026-08-07-compliance-intelligence-gathering-plan
- relates-to: 2026-08-07-knowledge-core-partner-report-spec
