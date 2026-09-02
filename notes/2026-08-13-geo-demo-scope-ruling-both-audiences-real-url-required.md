---
id: 2026-08-13-geo-demo-scope-ruling-both-audiences-real-url-required
type: decision
status: ratified
ratified: "2026-08-13, operator instruction, direct re-verification by this session's Claude; the cost-breakdown finding was confirmed by grepping the real production code for AI-provider keys before being stated as fact"
project: geo
tags: [geo, demo, scope, prioritization, ruling, operator-decision, master-panel, deploy]
sources:
  - ref: "reports/GEO_DEMO_READINESS_QUEUE_2026-08-12.md, the living document this ruling is captured inside"
    reliability: high
    origin: written and maintained this session
  - ref: "operator messages, 2026-08-12/13, direct answers (Both) to the audience and reachability sub-questions"
    reliability: high
    origin: direct operator instruction, this session
  - ref: "grep across projects/geo_platform/backend/app for OPENAI_API_KEY, GEMINI_API_KEY, ANTHROPIC_API_KEY -- zero matches in production code"
    reliability: high
    origin: run live, this session, confirming the AI-provider cost claim rather than assuming it
  - ref: "GEO_Suite_Cost_Breakdown_2026-08-13.docx, sourced live from Railway, Supabase, Twilio, Resend, Stripe, Google Places, and domain-registrar pricing pages while writing it"
    reliability: high
    origin: built and delivered this session
provenance:
  archive: research/knowledge-home/raw/2026-08-12-geo-poller-fix-and-platform-identity-session.jsonl
  turns: [1, 30]
risk_class: A
evidence_state: CORROBORATED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# GEO Suite demo scope ruling: the audience is both the business partner AND an external prospect, a real reachable URL is required, and every workstream from the operator's 2026-08-12 requirements dump is now split demo-critical vs. final-deployment-only

## Body

**The trigger:** a large, unstructured requirements dump from the operator (compliance-law-into-
Anansi integration, a SEMrush/Ahrefs/Moz-parity SEO engine, more industry verticals, a full sales
flow with a salesperson-specific dashboard, a confidential Master/Partner Panel, Knowledge Core
usability for a lawyer, site-generator robustness), captured as a structured queue
(`reports/GEO_DEMO_READINESS_QUEUE_2026-08-12.md`) rather than acted on piecemeal.

**Two explicit rulings the operator's own message already made, extended across the rest of the
queue rather than re-litigated per item:**
- Full industry-theme coverage is a final-deployment bar, not a demo bar -- the demo runs on the two
  verticals that already exist (HBOT, chiropractor).
- The Master/Partner Panel is built last, once every other role's panel is known, specifically so it
  can be built for real control instead of guessed at early. The operator separately asked for a
  diagnostic evaluation of exactly what confidential information belongs there -- deliberately not
  done yet, since it depends on what every other role's panel ends up holding.

**Two sub-questions the operator resolved directly, operator's own word "Both":**
- **Audience:** both the business partner and an external prospect are in the room, not an
  internal-only walkthrough. This raises the real bar on every demo-tagged item -- an external
  prospect judges the finished impression, not the roadmap behind it.
- **Reachability:** the demo needs a real, live URL. Confirmed, not assumed, given an external
  prospect is present -- this makes the Railway deploy (previously an open, not-yet-scheduled item)
  the literal first blocker; nothing else on the demo list matters if there's nowhere to show it.

**Net effect -- every workstream tagged DEMO / DEMO (partial) / FINAL, then turned into a dated
four-phase build sequence (Foundation, Content and proof, Build, Integration and rehearsal) against
the real calendar, 2026-08-13 through 2026-08-24, including both weekends in the window called out
explicitly rather than assumed as work or off days.** One step in that sequence (sourcing real,
lawyer-validated compliance content) is stated as a genuine unknown-duration dependency rather than
given a falsely confident date.

**A separate, real finding surfaced while pricing this out (2026-08-13, same arc):** the app's own
code was checked directly, not assumed, for what actually costs money to run. Confirmed -- Railway
(hosting, operator already has Hobby), Supabase (database, operator does NOT have a paid account,
the free tier's one-week auto-pause flagged as a real risk for anything meant to stay live including
the demo itself if it sits idle beforehand), Twilio, Resend, Stripe, and an optional Google Places
integration are the complete real paid-dependency list. Confirmed by grepping the actual production
code rather than assuming: **no AI-provider API (OpenAI, Gemini, etc.) is wired into any live code
path yet** -- the AI-visibility monitoring feature (tagged FINAL in the queue) has zero API cost
today because it simply isn't built against a real provider yet, not because it's cheap to run. A
full sourced cost breakdown was delivered as `GEO_Suite_Cost_Breakdown_2026-08-13.docx`, every
figure fetched live from each provider's current pricing page while writing it.

## Links

- extends, `reports/GEO_DEMO_READINESS_QUEUE_2026-08-12.md` -- the living document this ruling is
  captured inside; this note is the atomic, Knowledge-Core-searchable pointer to it.
- relates, 2026-08-12-geo-job-poller-is-unwired-and-signature-drifted-battery-green-proves-nothing-about-it.md
  and 2026-08-12-two-platforms-not-to-conflate-geo-suite-is-stag-geo-platform-not-base-platform.md --
  same day's earlier findings that this scope-planning work builds on top of, once the code was
  actually trustworthy.
