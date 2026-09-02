---
id: 2026-08-12-geo-job-handlers-call-nonexistent-messaging-functions-poller-fix-alone-does-not-make-jobs-work
type: finding
status: ratified
ratified: "2026-08-12, operator instruction, direct re-verification by this session's Claude; every fix below was proven with a one-time end-to-end dry run (Twilio SDK, Resend HTTP client, Supabase client mocked at the true external boundary only, everything else real), not a signature check alone -- the note's own body explains why that distinction mattered"
project: geo
tags: [geo, scheduler, poller, jobs, messaging, twilio, resend, import-drift, deploy-readiness, resolved]
sources:
  - ref: "backend/app/scheduler/handlers.py, backend/app/services/messages.py, backend/app/services/sms_twilio.py, backend/app/services/email_resend.py, backend/app/services/missed_call.py, backend/app/services/twilio_numbers.py, backend/app/services/twilio_settings.py"
    reliability: high
    origin: direct code read, this session
  - ref: "backend/app/jobs/release_held_numbers.py (new file), worker/release_held_numbers_worker.py, backend/pyproject.toml"
    reliability: high
    origin: direct code read, this session, used to decide which release implementation to wire up and confirm the deploy-boundary reasoning
  - ref: "one-time, not-committed dry runs of handle_timed_send (SMS and email paths) and handle_number_release_check, Twilio SDK / Resend httpx.Client / Supabase client mocked at the true external boundary only"
    reliability: high
    origin: run live, this session, not preserved as a permanent test per this project's own mocked-boundary-tests lesson
  - ref: "ci_verify_geo.py battery run (67/67); commits 3202285, ba99537, 695b637 on origin/main"
    reliability: high
    origin: run live and pushed live, this session
provenance:
  archive: research/knowledge-home/raw/2026-08-12-geo-poller-fix-and-platform-identity-session.jsonl
  turns: [1, 21]
risk_class: B
evidence_state: CORROBORATED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Both real GEO job handlers called functions/modules that didn't exist; fixed and verified end to end same day, plus a third bug found along the way

## Resolved, same day

Both handlers rewritten to call real, existing code and verified end to end (not just
signature-checked): `handle_timed_send` now uses `app.services.sms_twilio.send_sms` /
`app.services.email_resend.send_email` with the same record/send/attach bookkeeping pattern
`app.services.missed_call.py`'s proven `send_text_back` already establishes.
`backend/app/jobs/release_held_numbers.py` now exists, a thin wrapper around
`app.services.twilio_numbers.TwilioNumberService.release_due_numbers()` -- the real implementation,
whose own docstring already named this exact module as its intended caller. Deliberately not wired
to `worker/release_held_numbers_worker.py` (a second candidate implementation at the repo root):
that module's code would not ship with the backend Railway service (`backend/pyproject.toml`
packages only `["app"]`; `worker/` sits outside `backend/`), and its `STATUS_HELD = "held"` doesn't
match the real schema (`'suspended'`, confirmed against the check constraint).

**A third, separate bug found only by verifying end to end rather than trusting a signature check:**
`TwilioNumberService.__init__` and four other call sites read `self._settings.account_sid` /
`.auth_token` / `.mode` / `.number_country`, none of which exist on `TwilioSettings` (real fields:
`twilio_account_sid`, `twilio_auth_token`, `twilio_mode`, `twilio_number_country`). This meant the
whole service crashed on construction for every caller -- provisioning, holding, reinstating,
releasing, not just this job. Fixed all five references in
`backend/app/services/twilio_numbers.py`. This is exactly what an `inspect.signature()`-only check
would have missed, since the bug fires inside the constructor body, not at the call boundary --
worth remembering: a signature match proves the call is well-formed, not that the callee runs.

Verified with a one-time, not-committed dry run per handler (Twilio SDK, Resend HTTP client, and
Supabase client mocked at the true external boundary, everything else real): real message rows
written with the right shape, a genuinely-due held number released with its row correctly flipped
to `released` and `released_at` stamped. Battery 67/67 after all three fixes, confirmed unaffected,
and confirmed a second time on GitHub Actions itself after this fix's own push.

## Original body (2026-08-12, before the fix)

`handle_timed_send` (the `timed_send` job type's own handler, `backend/app/scheduler/handlers.py`)
calls `app.services.messages.send_sms(...)` and `app.services.messages.send_email(...)`. **Neither
function exists in `app/services/messages.py`** — confirmed by grepping every `def`/`async def` in
that file; it holds message-row bookkeeping (`record_outbound_sms`, `set_twilio_message_sid`,
`update_status_by_twilio_sid`, and similar) but no function named `send_sms` or `send_email` at all.
The real sending functions live elsewhere, under different names, different signatures:
`app.services.sms_twilio.send_sms(*, to_number, body, from_number=None)` (sync, not async) and
`app.services.email_resend.send_email(*, to_address, subject, body, body_html=None)` (also sync).
`handle_timed_send` awaited its call and passed `client_id`/`to`/`phone_number_id` — none of which
the real functions accept.

`handle_number_release_check` had the same shape of gap: it did `from app.jobs import
release_held_numbers`, but `app/jobs/` was not a package anywhere in this repo at the time — no
`app/jobs/` directory existed at all.

**Net effect at the time: the same day's earlier poller fix (wiring `JobPoller` into `main.py`'s
lifespan, reconciling its `JobsRepository`/`handlers.dispatch()` signatures) made the scheduler
itself run correctly, but did not make either job type actually able to do its job.** A real
`timed_send` job with a fully valid payload would still have failed on every attempt —
`AttributeError` on the missing `messages_service` functions. A real `number_release_check` job
would have failed with `ModuleNotFoundError` on the missing `app.jobs` package. Both failures were
caught by `_execute_job`'s broad `except Exception`, so the app would not have crashed and the job
would have been correctly recorded failed, not silently dropped — but the original poller-drift
finding's own claim, "Missed-call SMS follow-ups and Twilio number auto-release never fire," was
still true at that point, for a completely different reason than the one already fixed.

Left here for the historical record of what was originally found; see "Resolved, same day" above
for what actually happened — fixed the same session it was flagged in, at the operator's explicit
instruction, not left as a follow-up.

## Links

- extends, 2026-08-12-geo-job-poller-is-unwired-and-signature-drifted-battery-green-proves-nothing-about-it.md
  — that note's fix made the scheduler run; this note is the next layer down, the handlers the
  scheduler now correctly reaches. Both layers are now fixed.
- relates, tests/test_scheduler_poller.py — the standalone test's checks 3 and 4 prove the real,
  current failure-recording behavior (an invalid payload, a genuinely unregistered type) without
  needing to exercise the send path; the send path itself is proven separately, by the one-time dry
  runs described in "Resolved, same day" above, not by a permanent mocked test.
- depends, backend/app/jobs/release_held_numbers.py — the new module this fix created.
- depends, backend/app/services/twilio_numbers.py — the third bug (wrong `_settings` attribute
  names) found and fixed while verifying this note's own fix end to end.
