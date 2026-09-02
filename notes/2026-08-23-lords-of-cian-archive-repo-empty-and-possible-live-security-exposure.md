---
id: 2026-08-23-lords-of-cian-archive-repo-empty-and-possible-live-security-exposure
type: finding
status: ratified
ratified: "2026-08-25 — anansi-promote skill run, 6/10 (novelty 2, evidence 1, actionability 2, generality 0, non-contradiction 1). Promoted WITH REVISION: the headline claim was independently checked on 2026-08-25 and is FALSIFIED. Original class was believed-unconfirmed and explicitly not verified in-chat; that verification is now done."
project: lords-of-cian
tags: [lords-of-cian, archive, security, supabase, lovable, rls]
sources:
  - ref: "Operator-supplied reconciled game plan dated 2026-08-20, secondhand; headline claims independently checked against the live GitHub repo and Supabase security advisor on 2026-08-25 and found falsified"
    reliability: medium
    origin: "2026-08-23 Lords of Cian session; re-verified 2026-08-25 anansi-promote run"
provenance:
  archive: research/knowledge-home/raw/2026-08-23-lords-of-cian-cult-network-and-archive-planning.jsonl
  turns: [1, 96]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# REVIEW: high-impact — the Lords of Cian interactive archive's GitHub repo is empty despite claimed "Complete" status, and the deployed app may have RLS and email confirmation both off, exposing reader data on a live public URL right now

- id: 2026-08-23-lords-of-cian-archive-repo-empty-and-possible-live-security-exposure
- type: finding
- status: ratified
- ratified: 2026-08-25 — anansi-promote skill run, 6/10 (novelty 2, evidence 1, actionability 2, generality 0, non-contradiction 1). Promoted WITH REVISION: the headline claim was independently checked on 2026-08-25 and is FALSIFIED. Original class was believed-unconfirmed and explicitly not verified in-chat; that verification is now done.
- class: believed-unconfirmed
- source: a fleet-reviewed strategy deliverable the operator supplied in this chat, 2026-08-23, dated 20 August 2026, "Lords of Cian Interactive Archive — Game Plan, Backlog & Engagement Roadmap," reconciled from three source documents against the real repository The-Reaver/My-Rivals-Distance-Archive
- confidence: medium, the underlying source document is itself a synthesis the operator supplied secondhand from another session; the repo-emptiness and RLS/email-confirmation contradictions are as that document states them, not independently re-verified in this chat
- verified: 2026-08-23
- tags: lords-of-cian, archive, security, supabase, lovable, rls
- project: lords-of-cian

## Body

The Lords of Cian interactive archive is a Lovable project (React, TypeScript, Tailwind, shadcn/ui, Supabase backend) already deployed to a `lovable.app` URL anyone holding the link can reach. Per the reconciled game plan the operator supplied, the connected GitHub repository, `The-Reaver/My-Rivals-Distance-Archive`, has zero commits and zero branches on origin, meaning every "Complete" claim made inside the Lovable workspace itself is currently unverifiable by anyone other than Lovable's own agent.

Two contradictions in the source material compound this: whether Row Level Security is actually enabled (one section claims it ships, another says it still needs re-enabling), and email confirmation is disabled by design for frictionless signup, meaning unlimited unverified accounts can currently inflate or fabricate the demand-signal data (request counts, referral chains, registered-user totals) the whole platform strategy is built to trust for multi-year writing decisions.

If RLS is in fact off or too permissive, reader emails, engagement rows, and the referral graph are exposed today, on a live, publicly reachable URL, not merely at some future launch. The reconciled plan sequences pushing the repo to GitHub and re-verifying RLS as the two blocking first steps, ahead of any further feature work, precisely because of this.

Not yet confirmed in this chat: whether this session's flagging of the risk has been acted on, or whether the repo push and RLS verification have actually happened.

## Links

- relates: 2026-08-23-lords-of-cian-archive-tech-stack-superseded-by-real-game-plan

## Revision, 2026-08-25 (independent verification)

Every load-bearing claim in the body above was checked directly. Result: **the headline risk did not
materialize, and the repo-emptiness claim is now stale.**

- **"Zero commits and zero branches" -- no longer true.** `The-Reaver/My-Rivals-Distance-Archive` has
  1 commit, pushed `2026-08-24T17:09:44Z`, the day *after* this note was written. P0-1 has at least
  partially landed.
- **"RLS may be off, exposing reader emails and the referral graph right now" -- FALSE.** The Supabase
  security advisor for project `dghkxaclaeluheahdsne` returns **no `rls_disabled_in_public` finding at
  all**. The committed schema contains 39 RLS/policy statements in `0001_operational_schema.sql` and 5
  more in `0002_knowledge_core_schema.sql`. There is no live data exposure of the kind this note feared.
- **The repo is PUBLIC**, and `apps/web/.env.example` contains a real project URL and a
  `sb_publishable_` key. This is **not** a leak: publishable/anon keys are designed for browser bundles,
  the file itself documents that RLS is what constrains them, and it explicitly warns against ever
  placing the service-role key there.

**Two real issues that verification did surface** (neither was in the original note):

1. **`public.is_admin()` and `public.current_clearance()` are `SECURITY DEFINER` and callable by the
   `anon` role** via `/rest/v1/rpc/`. Two WARN-level advisors. This matters more than usual here because
   the archive's entire spoiler-gating model rests on clearance checks -- an anon-callable
   SECURITY DEFINER clearance function deserves an explicit review.
2. **Five `knowledge_core.*` tables have RLS enabled but zero policies** (`kc_documents`, `kc_entries`,
   `kc_extractions`, `kc_fan_contributions`, `kc_references`). INFO-level, and fail-closed (deny-all),
   so it is safe -- but it may mean those tables are unreadable by the app, which could be a latent bug.

**Also contradicted:** the repo's committed stack is **Next.js** (`apps/web/next.config.mjs`), not the
TanStack Router the sibling note reports, and its schema is a `knowledge_core` operational schema -- not
obviously the reader-facing Lords of Cian archive at all. The single commit sits on a
`claude/lovable-build-review-nmep29` branch, which is also the repo's default branch. It is possible the
Lovable app's own code still has not been pushed and this repo currently holds a different effort.
That reconciliation is the real open item, not the RLS scare.
