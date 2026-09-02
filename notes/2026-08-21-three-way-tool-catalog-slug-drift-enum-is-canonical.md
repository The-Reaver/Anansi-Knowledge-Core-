---
id: 2026-08-21-three-way-tool-catalog-slug-drift-enum-is-canonical
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, tool-catalog, stripe, slug-drift, decision]
sources:
  - ref: "Archive turns 253-281: 'resolve_price_id(slug) -> TOOL_PRICES.get(slug), but TOOL_PRICES is keyed by hyphen slugs while the enum/API sends underscores ... the lookup_key function already normalizes -->_, so the underscore slugs are canonical' (turns 253-255), then the agent rewrites stripe_prices.py to underscore slugs and seed_tools.sql to the canonical six tools (turns 277-281)"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [253, 281]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The six-tool catalog was defined three incompatible ways (enum, Stripe price map, SQL seed); the API enum's underscore slugs were made canonical and the other two reconciled to match
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — confirmed by reading ToolSlug, stripe_prices.py, and seed_tools.sql directly, and the fix was verified via a fake-Supabase harness plus a live tool_slugs query after deploy
- verified: 2026-08-21
## Body
The backend's domain catalog of six tools (`ai_voice_receptionist`, `booking_recovery_bot`, `database_reactivation_engine`, `missed_call_text_back`, `payment_recovery_engine`, `review_engine`) was defined three incompatible ways: the `ToolSlug` API enum used underscore-separated slugs, `stripe_prices.py`'s `TOOL_PRICES` dict was keyed by hyphen-separated slugs, and `seed_tools.sql` defined an entirely different set of products with different names and prices. Because the API contract (what `/api/tools/toggle-on|off` and `/api/tools/entitlements` actually accept and return) is defined by the enum, the enum was made canonical and the other two catalogs were rewritten to match it: `TOOL_PRICES` was rekeyed to underscore slugs (the Stripe lookup-key helper already normalized `-` to `_`, so the real Stripe keys stayed byte-identical), and `seed_tools.sql` was rewritten to the six real tools with enum-matching slugs and descriptions consistent with the frontend. General lesson: when a domain catalog exists in several independently-maintained forms, the request/response validation layer (an enum, a Pydantic model) is the one that actually gates what the running system accepts, so it is the correct canonical source — every other copy of the catalog (seed data, price maps, docs) should be checked against it.
## Links
- related, 2026-08-21-entitlements-canonicalized-on-tool-id-over-tool-slug.md, the related entitlement-table decision made in the same reconciliation
