# Credential reconciliation — 2026-09-01

**Authorized by the operator, 2026-09-01.** Closes runbook item `0a-7.3`: reconcile the secret-scan
findings against the rotation recorded in `reports/STAG_BRAIN_TRUST_LEDGER.md`, row *"Anansi Knowledge
Core — Option A credential rotation closure"* (2026-08-25).

**No secret value was printed, logged, or copied at any point.** Every classification below rests on
structural facts only — prefix, length, character-class counts, segment shape, host tail.

---

## The headline

> ### One live credential in the pushed repository has never been rotated, and was never in the scope of the rotation that closed Sentinel's HOLD.
>
> **A Stripe key with the `sk_live_` prefix**, in `research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl`
> — **tracked and pushed**. No redaction markers. `sk_live_` is Stripe's live-mode secret key prefix; a
> test key would read `sk_test_`.
>
> The 2026-08-25 rotation covered *"both real Anthropic API keys and the Supabase database password,
> then separately the Supabase JWT secret."* Sentinel's originating scan was scoped to *"2 real
> Anthropic API keys, a live Supabase JWT, and 11 `postgres://user:pass@` strings."* **Stripe appears
> nowhere in either.** It was not missed during rotation — it was never looked for.
>
> **Action: rotate this key in the Stripe dashboard, then check the API logs for use you do not
> recognise.** Rotation alone does not remove it from git history.

---

## Method

The live baseline holds 16 findings. Findings are keyed *kind + path*, so one file with three matches is
three findings — the count of **distinct credential values** is what matters, and it is 19. Each was
classified structurally:

- **DB connection strings** — by **host tail**. A real credential points at real infrastructure; a
  compose service name or a placeholder does not.
- **`sk-` matches** — by **segment shape**. A real key has one long opaque run (the confirmed Anthropic
  keys carry a 101-character body). A kebab-case slug is a chain of short dictionary words. This is the
  same false-positive class the ledger already documented on 2026-08-25 (`sk-curriculum-generator-…`).
- **Stripe / JWT** — by **prefix and body composition**.

---

## Result: 19 distinct values → 6 real credentials, 13 not credentials

### Real, and already rotated (5 of 6) ✅

| Credential | Where | Covered by |
|---|---|---|
| Anthropic key, `sk-ant-` + 101-char body | `2026-07-07-backfill-3b51843d.jsonl` | "both real Anthropic API keys" |
| Anthropic key, `sk-ant-` + 101-char body | `2026-07-15-backfill-23d1d7fe.jsonl` | "both real Anthropic API keys" |
| Supabase pooler DB string | `2026-07-10-backfill-ebf4b889.jsonl` | "the Supabase database password" |
| Supabase pooler DB string (same host) | `2026-07-10-backfill-ebf4b889.jsonl` | same password |
| Supabase JWT, 208 chars | `2026-07-15-backfill-23d1d7fe.jsonl` | "separately rotated the Supabase JWT secret" |

**The ledger's arithmetic checks out independently.** It records the real Anthropic count as exactly 2
after correcting an initial over-count of 7. Structural classification of the current corpus finds
exactly 2 keys with a genuine `sk-ant-` + long-opaque-body shape. Two methods, two years of transcripts
apart, same answer.

Both pooler strings point at the same host, so one password rotation covers both. The ledger's note that
rotating the DB password does **not** invalidate a previously-issued JWT — and that the JWT secret was
therefore rotated separately — is correct and was the right call.

### Real, NOT rotated (1 of 6) ❌

| Credential | Where | Status |
|---|---|---|
| **Stripe `sk_live_` key**, 20-char body, 10 digits / 10 lowercase, no redaction markers | `2026-08-21-live-f810b6ef.jsonl`, **tracked and pushed** | **Never in scope. Never rotated.** |

### Not credentials (13)

| Class | Count | Why |
|---|---|---|
| DB strings to compose service names (`db:5432`, `postgres:5432`, `aws-rds-endpoint:5432`) | 6 | Docker-compose service names and a literal placeholder string. No real host. |
| DB string to `127.0.0.1:54322` | 1 | Supabase's local-dev default port. |
| `sk-` kebab-case prose | 6 | Longest opaque segment is 5 characters; four contain no opaque segment at all. Documentation slugs, note IDs, dates. |

**Two of those six prose matches were classified "credential-shaped" in yesterday's omar review** — my
filter accepted "contains a digit" as evidence. Segment-shape analysis refutes that: one is
`word-word-word-2026-08-20`-shaped with a maximum opaque run of **zero** characters. Corrected here.

---

## The removed baseline entries: 11, none reconcilable

The entries removed when the baseline was regenerated cannot be classified at all — their values are not
in any committed content, so there is nothing left to inspect. What can be established is timing:

| File | Dated | Relative to the 2026-08-25 rotation |
|---|---|---|
| `2026-08-25-live-8962d687.jsonl` (3 entries) | 08-25 | same day — ambiguous |
| `2026-08-25-live-6b04c60c.jsonl` (2 entries) | 08-25 | same day — ambiguous |
| `2026-08-25-live-cb849e2f.jsonl` (1, never committed) | 08-25 | same day — ambiguous |
| `2026-08-27-live-c69335ef.jsonl` (3 entries) | 08-27 | **after — cannot be covered** |
| `2026-08-28-live-87ca0bf9.jsonl` (1, never committed) | 08-28 | **after — cannot be covered** |
| `2026-08-28-live-8f1c2106.jsonl` (1, never committed) | 08-28 | **after — cannot be covered** |

**5 entries across 3 files postdate the rotation entirely.** Their kinds were AWS Access Key, DB
connection string, Generic Secret, JWT, OpenAI/Anthropic key and Private Key — but a kind is not a
credential, and yesterday's evidence is that these matches came from a pre-commit local version of files
whose committed content carries nothing. **They may be entirely false positives of the same prose class,
or they may be real.** Nothing in the repository can settle it.

**The three never-committed transcripts still exist on your machine and have never been scanned by
anything but the machine that made them.** That is the only place the answer lives.

---

## Worklist

| # | Action | Priority | Done |
|---|---|---|---|
| R1 | **Rotate the Stripe `sk_live_` key** in the Stripe dashboard. | **Now** | ☐ |
| R2 | Review Stripe API logs for unrecognised use since 2026-08-21. | **Now** | ☐ |
| R3 | Run a secret scan over the three never-committed transcripts on your machine, and classify what the 5 post-rotation entries actually were. | High | ☐ |
| R4 | Decide history rewrite vs. rotation-only. Rotation stops the key working; it stays readable in git history forever. Inherited from lane `0a-7.4`. | High | ☐ |
| R5 | Add `sk_live_` / `sk_test_` prefix separation to the classification used in future reviews — a live-mode prefix should never sort alongside prose. | Medium | ☐ |
| R6 | Record this reconciliation as a ledger row, so the next reviewer inherits the answer rather than redoing it. | Medium | ☐ |

## What is now settled, and should not be re-derived

- The 2026-08-25 rotation was **correct and complete for its scope** — 2 Anthropic keys, the Supabase DB
  password, the Supabase JWT secret. Independently confirmed by structural analysis.
- Its scope simply **did not include Stripe**.
- The `sk-` false-positive rate in this corpus is high — **6 of 8** distinct matches are prose — which is
  exactly why the 2026-08-26 regex tightening was attempted, and exactly why reverting it was still right:
  it killed 7 of 7 real detections to remove noise. **The noise is real; the answer is classification at
  review time, not a tighter pattern.**
