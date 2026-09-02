---
id: 2026-08-21-project-brief-step0-resolved-disk-state-conflicts-with-freshly-backfilled-history
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (the unresolved disk-state-vs-history conflict was resolved in-body: the real work lived in Archive/project_brief_step0_resolved/ and on GitHub as stag-platform, never lost). Operator retains veto per Mandate 1."
project: fleet
tags: [project-brief-step0-resolved, stag-platform, checklist-drift, conflicting-sources, repo-state]
sources:
  - ref: "Archive turns 226-229: the master-checklist refresh sweep turn that first surfaced the conflict between the empty projects/project_brief_step0_resolved/ stub and the same-day backfilled stag-platform build history."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Projects never individually status-checked (fleet_lab, lookct, sandbox_training_env, small_business_tools, creative_production_studio, geo_platform_brief, project_brief_step0_resolved)\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [226, 229]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high that the two facts genuinely conflict (both independently verified); low on which one explains the other -- see Body
- verified: 2026-08-21
- REVIEW: high-impact

# projects/project_brief_step0_resolved is currently just three empty nested directories, which conflicts with the rich stag-platform build history (Railway deploy, dashboard consolidation, Sprint 0 hardening) that other candidate notes backfilled from historical transcripts on this same day

## Body

Two things are both true and pull in opposite directions, named here rather than silently resolved in either direction. (1) On disk right now, `projects/project_brief_step0_resolved/` contains nothing but three empty nested directories -- `backend/`, `backend/supabase/`, `backend/supabase/snippets/` -- no code, no `railway.json`, no frontend, no `.git`, last modified 2026-08-19. (2) On this same date, 2026-08-21, a separate backfill pass (visible as ~20 other candidate notes in this same `candidates/2026-08-21/` folder, sourced from historical transcripts `ebf4b889`, `e0fb412c`, and `db88cef4`) describes `project_brief_step0_resolved` as a substantial, actively-developed repo called `stag-platform` (`github.com/The-Reaver/stag-platform`): two Railway services for backend and frontend, a Supabase-backed Postgres/Auth layer, Stripe/Twilio/Resend integrations, a working `/dashboard/*` route tree (with a since-deleted duplicate `/settings/team` implementation), and Sprint 0 webhook-hardening work -- all describing sessions from 2026-07-09, 2026-07-10, and 2026-07-17, i.e. before the 2026-08-03 checklist date. No sibling clone of a `stag-platform` repo was found elsewhere on this filesystem in a shallow search. Two explanations are both plausible and neither is confirmed: (a) the real, live `stag-platform` work happens in a standalone clone outside this monorepo entirely (the same pattern `lookct`, `small_business_tools`, and `sandbox_training_env` already use, each carrying its own `.git`), and `projects/project_brief_step0_resolved/` was always just a thin in-monorepo stub that got further pared down to an empty Supabase-CLI artifact; or (b) real work that once lived in this folder was deleted or reset (deliberately or not) sometime before 2026-08-19, and the only trace of it left in this repo is today's backfilled transcript notes. Because the checklist's own working rule is that a conflict between sources gets named, not silently resolved, this note does that rather than picking a side. Whichever explanation is correct, the checklist's original "never individually status-checked" framing for this project undersells the situation either way: there either is real history for it that just was not captured as a status line before today, or there is a disk-state gap worth the operator's direct attention.

**Resolution (2026-08-25, Brain Trust + Augustin + AJ review):** Explanation (a) confirmed. `Archive/project_brief_step0_resolved/` is a real, git-clean clone of the work — remote `github.com/The-Reaver/stag-platform.git`, 249 tracked files, real commit history through `42eb8e1`, matching exactly what the backfilled notes describe. Independently, `gh repo view`/`gh api commits` confirms a GitHub repo named exactly `The-Reaver/stag-platform` existed (since renamed `Stag-GEO-Platform`), with an early commit literally titled referencing that name. The original note's local-filesystem-only search missed this because the real work was never cloned into `projects/` at all — it lived in `Archive/` and on GitHub the whole time. `projects/project_brief_step0_resolved/` was always just a thin in-monorepo stub. Not lost work; a relocation this sweep's shallow search didn't reach. Sentinel raised an alternative hypothesis (deliberate secret-scrubbing, given other real leaked-credential incidents found the same day) as a reasonable caution, but it is outweighed by the convergent external evidence (local clone + independent GitHub API confirmation) and is not the leading explanation. Anyone consolidating `Archive/project_brief_step0_resolved/` with `projects/project_brief_step0_resolved/` later should not simply copy files over -- the Archive copy is a nested, non-submodule git repo with its own independent history, and a flat copy would detach that commit lineage.

## Links

- relates: `research/knowledge-home/candidates/2026-08-21/2026-08-21-railway-chosen-as-hosting-platform-for-stag-platform.md`
- relates: `research/knowledge-home/candidates/2026-08-21/2026-08-21-two-dashboard-implementations-consolidation-decision.md`
- relates: `research/knowledge-home/candidates/2026-08-21/2026-08-21-sprint0-hardening-sequenced-before-first-revenue-tool.md`
- relates: `reports/STAG_MASTER_CHECKLIST_2026-08-03.md` (the claim being corrected)
