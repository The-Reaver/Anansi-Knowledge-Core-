---
id: 2026-08-21-malformed-backend-env-shadowing-root-env
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, backend-config, env-vars, pydantic-settings, dotenv, deploy]
sources:
  - ref: "Archive turns 479-511 show backend/.env containing only pasted supabase status CLI output (no valid KEY=VALUE lines), the cwd-relative env_file path silently loading it over the real root .env, and the fix anchoring all three settings modules to __file__-relative paths."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [479, 511]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high — the agent read the file's full contents, confirmed it was entirely pasted `supabase status` CLI output with box-drawing table characters, and confirmed the parse warnings disappeared after the fix
- verified: 2026-08-21

# A malformed backend/.env file (pasted Supabase CLI output, not KEY=VALUE) silently shadowed the real root .env because settings used a cwd-relative path

## Body
In `project_brief_step0_resolved`, `backend/.env` existed but contained no valid `KEY=VALUE` lines at all — it was entirely a pasted `supabase status` terminal output (box-drawing table characters and a local Supabase CLI status dump, all pointing at 127.0.0.1 dev values), evidently created by accident. Because every Pydantic settings module in the project (`config.py`, `messaging_config.py`, `twilio_settings.py`) declared `env_file=".env"` as a bare relative path, and the app was run from the `backend/` working directory, Pydantic loaded this malformed file instead of the real, correctly-populated root `.env` — producing "dotenv could not parse" warnings on every boot and silently shadowing the intended configuration. The fix was two-part: delete the malformed file (after confirming it held only generic local dev values and no unique data worth preserving), and change all three settings modules to resolve the `.env` path relative to `__file__` rather than the process's current working directory, so the working directory the app happens to be launched from can no longer determine which env file is loaded. This also matters for production: in deployment, Railway injects real environment variables and no `.env` file exists at all, so the host environment correctly wins — but the cwd-relative bug meant local development behavior depended on an accident of which directory `python` was invoked from. General lesson: any settings/config loader that reads dotenv files by a relative path should resolve that path from a stable anchor (the module's own file location, or an explicit repo-root constant), not from the current working directory, because "run from a different directory" is an easy, silent way to load the wrong config file.

## Links
- related, 2026-08-21-stag-deploy-config-sanity-checks.md, found and fixed in the same deploy-readiness pass on 2026-07-09/10
