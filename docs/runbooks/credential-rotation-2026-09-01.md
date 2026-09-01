# Credential rotation — 2026-09-01

**Why this exists.** 48 raw session transcripts were committed to `The-Reaver/Stag-Fleet` in
`b19dd5f` (2026-08-31) and are now on the remote. Several carry live-shaped credentials. This
runbook is the working checklist and the record of what was rotated when.

**Fill in the date and initials as you go.** An unticked row is an unrotated credential.

> **Rotation is the remedy. History rewriting is not.**
> The repository has already been cloned and fetched since 31 August — at least one full copy
> exists outside the origin. Rewriting history cleans the *repo*; it does nothing about a key
> someone already holds. Rotate first. Rewrite afterwards, as hygiene, if you want to.

> **This is not a one-day exposure.** The `2026-07-07` transcript has held an Anthropic key since
> **July**. The ratified note `2026-08-21-anthropic-api-key-pasted-in-plaintext-into-chat-transcript.md`
> names that exact file and asks whether the key was ever rotated. No record says it was.

---

## Inventory

Verified 2026-09-01 by pattern match against the tracked transcripts at HEAD. **No values were
read or recorded** — types and file counts only.

| Credential type | Files | Blast radius |
|---|--:|---|
| Supabase `service_role` | 4 | Full DB read/write, **bypasses row-level security** |
| Postgres URI with embedded password | 6 | Direct database access |
| Anthropic API key (`sk-ant-api03-`, 80+ chars) | 2 | Billable spend on your account |
| JWT (`eyJhbGciOi`) | 1 | Whatever it was minted to grant |

**Confirmed absent** from those transcripts: OpenAI keys, AWS access keys, GitHub PATs,
`RAILWAY_TOKEN`.

The two files carrying Anthropic-shaped keys:
`research/knowledge-home/raw/2026-07-07-backfill-3b51843d.jsonl`,
`research/knowledge-home/raw/2026-07-15-backfill-23d1d7fe.jsonl`.

Separately in scope: **`RAILWAY_TOKEN`** is not in the transcripts but sits in GEO's Actions
secrets, reachable by anyone who can push to `main` (`deploy-verify.yml` runs `railway run` with
it on every push, and there is no PR gate). Rotate it in the same pass.

---

## Checklist — highest blast radius first

### ☐ 1. Supabase `service_role` key
Ignores row-level security entirely. This is the master key to the data; do it first.

- ☐ Supabase dashboard → Project Settings → API → roll the `service_role` key
- ☐ Update `SUPABASE_SERVICE_ROLE_KEY` in Railway
- ☐ Update any local `.env`
- ☐ Redeploy
- ☐ Old key confirmed revoked

Rotated: `____-__-__`  by: `______`  notes: `____________________`

### ☐ 2. Supabase database password
Changes `SUPABASE_DB_URL`, which appears in six transcripts.

- ☐ Supabase → Settings → Database → reset password
- ☐ Update `SUPABASE_DB_URL` in Railway
- ☐ Update any local `.env` / connection strings
- ☐ Verify the app reconnects

Rotated: `____-__-__`  by: `______`  notes: `____________________`

### ☐ 3. Anthropic API key
**Before revoking:** local agent scripts shell out to `claude -p`. Find every place the old value
is *stored* (not printed) first, or those scripts break silently.

- ☐ Located every consumer of the old key
- ☐ console.anthropic.com → API keys → create replacement
- ☐ Update `ANTHROPIC_API_KEY` in Railway and locally
- ☐ **Delete the old key.** Creating a replacement does not revoke the original — this is the
      step that gets skipped, and skipping it means nothing was actually rotated.

Rotated: `____-__-__`  by: `______`  notes: `____________________`

### ☐ 4. `SUPABASE_JWT_SECRET`
Rotating this **invalidates every existing session token — everyone is logged out.** Harmless, but
don't do it mid-demo.

- ☐ Chosen a moment where forced logout is acceptable
- ☐ Rotated in Supabase
- ☐ Updated in Railway
- ☐ Confirmed login works afterwards

Rotated: `____-__-__`  by: `______`  notes: `____________________`

### ☐ 5. `RAILWAY_TOKEN`
- ☐ Railway → Account Settings → Tokens → revoke and reissue
- ☐ Update the `RAILWAY_TOKEN` GitHub Actions secret in the GEO repo
- ☐ Confirm `deploy-verify.yml` still passes

Rotated: `____-__-__`  by: `______`  notes: `____________________`

---

## Do NOT casually rotate this one

**`VENDOR_KEY_ENCRYPTION_SECRET`** is the key-encryption key that decrypts stored **customer**
vendor credentials. It is **not** in the exposed transcripts, so it does not need rotating now.

If you ever do rotate it: swapping the value without re-encrypting the stored data first makes
every stored customer credential **permanently unreadable**. That is a data migration, not a
rotation. Plan it separately.

---

## Verify

- ☐ `railway run --service "The-Geo-Suite-" -- python scripts/deploy_verify.py --check-env`
      confirms the new values are set
- ☐ App loads, login works, a DB-backed page returns data

## Then check whether anyone used them

Rotation closes the door. These tell you whether anyone walked through it first.

- ☐ Anthropic console → usage, from **2026-07-07** onward. Look for spend you cannot account for.
- ☐ Supabase → logs → `service_role` connections from unfamiliar IPs
- ☐ Railway → deployment and activity log for actions you did not take
- ☐ GitHub → the Stag-Fleet repo's clone/traffic insights, if available

Result: `____________________________________________`

## Afterwards, optional

- ☐ Remove `research/knowledge-home/raw/` from branch history (needs a force-push and a rewrite of
      a commit you authored — governed by `PREFLIGHT_SAFETY_DISPATCH_v1.0.md`, operator decision)
- ☐ Confirm `.gitignore`'s `research/knowledge-home/raw/*.jsonl` rule still holds
- ☐ Scope the global Stop hook (`live_transcript_capture.py`) away from tracked repos

---

## What already stops the next one

`prepush.py` was fixed on 2026-09-01 (`claude/evidence-retrofit-pass-one-2026-09-01`). Its blocking
stage scanned `git diff --cached` — the index, which is **empty at pre-push time** — so it ran on
every push, inspected nothing, and reported clean. It returned clean on `b19dd5f`. It now scans the
outgoing push range as well, with `tests/test_prepush_push_range.py` (5/5, mutation-checked)
proving it catches a committed-but-unpushed secret.

That fix stops the next occurrence. It does nothing about this one, which is why this runbook exists.
