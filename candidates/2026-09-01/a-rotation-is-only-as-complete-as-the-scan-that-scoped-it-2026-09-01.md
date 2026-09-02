---
id: a-rotation-is-only-as-complete-as-the-scan-that-scoped-it-2026-09-01
type: lesson
status: candidate
source: "Recovery session, 2026-09-01 — reconciliation of the secret-scan baseline against the 2026-08-25 rotation closure row in reports/STAG_BRAIN_TRUST_LEDGER.md, on operator authorization"
project: fleet
tags: [credentials, rotation, secret-scanning, scope, stripe, false-positives, remediation-closure]
supersedes: []
superseded_by: null
---

# A rotation closes the findings it was scoped to, not the exposures that exist

## Body

On 2026-08-25 the fleet closed a blocking security condition. The ledger records it precisely: the
operator rotated both real Anthropic API keys and the Supabase database password, then — after being
told the database password does not invalidate a previously-issued JWT — separately rotated the Supabase
JWT secret. Sentinel's HOLD was cleared. The work was careful, the correction about JWTs was exactly
right, and an independent structural re-derivation a week later reproduced its arithmetic exactly:
2 Anthropic keys, not the 7 initially over-counted.

Reconciling that closure against the corpus found **a Stripe key with the `sk_live_` prefix**, in a
tracked and pushed transcript, never rotated.

It was not missed during remediation. **It was never in the scope of the scan that defined the
remediation.** Sentinel's originating finding enumerated *"2 real Anthropic API keys, a live Supabase
JWT, and 11 `postgres://user:pass@` strings."* Everything on that list was handled. Stripe was not on
the list, so it was not handled, and the closure row reads complete because against its own scope it is.

## The shape of the failure

A remediation inherits the blind spots of the scan that scoped it, and then **closes over them** — the
ledger row says *satisfied*, the HOLD lifts, and the unscanned class becomes invisible precisely because
the topic now looks finished. A later reader sees "credential rotation: closed" and does not re-ask.

This is worse than an open finding. An open finding attracts attention.

## The rule

**Close a remediation against the corpus, not against the finding list.** When a rotation is declared
complete, re-scan and enumerate *everything the scanner now reports*, then say explicitly which items
the rotation covered and which it did not — including the ones that turn out to be false positives.
"Sentinel's condition is satisfied" and "no live credentials remain" are different claims, and only the
first was ever established.

## The second-order finding

In this corpus **6 of 8** distinct `sk-` matches are kebab-case prose — documentation slugs and note IDs
that satisfy `sk-[A-Za-z0-9_-]{20,}`. That noise is what motivated the 2026-08-26 regex tightening, which
silently killed 7 of 7 real detections and was correctly reverted.

The answer to a high false-positive rate on a recall-first scanner is **classification at review time,
not a tighter pattern.** Segment shape separates them reliably and cheaply: a real key has one long
opaque run; a slug is a chain of short dictionary words. And a live-mode prefix — `sk_live_` — must never
sort alongside prose in the first place.
