---
id: 2026-08-21-entitlements-canonicalized-on-tool-id-over-tool-slug
type: decision
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, supabase, entitlements, schema-decision, decision]
sources:
  - ref: "Archive turns 266-268: the agent presents Option A (tool_slug/tool_entitlements) vs Option B (tool_id/entitlements) with its reasoning, the operator replies 'option b', and the agent confirms it will rewire tool_toggle_service to the real entitlements table with the frontend unchanged"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [266, 268]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Tool entitlements were canonicalized on the real `entitlements` table keyed by `tool_id`, not the phantom `tool_entitlements` table keyed by `tool_slug`
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the operator's Option B choice and the implementation details match the session narration. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the operator explicitly chose this option ("option b"), the agent implemented and verified it against the schema and a fake-Supabase harness, and confirmed the frontend needed zero changes
- verified: 2026-08-21
## Body
The `project_brief_step0_resolved` backend had two parallel entitlement code paths that disagreed: `/api/tools/*` (used by the frontend) keyed by `tool_slug` against a phantom `tool_entitlements` table, while `/accounts/me/tools/activate` keyed by `tool_id` looked up from `public.tools` against the real `public.entitlements` table, which already had full RLS. Presented with two options — build the missing `tool_entitlements` table to match the frontend's existing calls, or repoint the tool-toggle service to the real `entitlements`/`tool_id` model — the operator chose the latter (Option B), because it matches the schema that actually exists, requires no new table or duplicate RLS, and lets the migration chain apply cleanly. `tool_toggle_service.py` was rewired to resolve slug↔id via `public.tools`, operate against `entitlements` by `tool_id`, and enrich the returned rows with `tool_slug` so the frontend's `/api/tools/*` response shape was unchanged and required no frontend code changes at all — only the implementation underneath the same endpoints moved to the real table.
REVIEW: high-impact
## Links
- related, 2026-08-21-phantom-tool-entitlements-table-blocked-supabase-db-push.md, the bug this decision resolved
