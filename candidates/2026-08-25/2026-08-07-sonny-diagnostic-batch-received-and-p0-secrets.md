---
id: 2026-08-07-sonny-diagnostic-batch-received-and-p0-secrets
type: note
status: candidate
source: "SONNY / ShopOnlineNewYork repo diagnostic close-out, harvested 2026-08-07 (source status: hub note, batch held as candidates pending operator approval)"
project: fleet
tags: []
---

# SONNY diagnostic batch: received, held, and a P0 secret exposure

## Body

The SONNY diagnostic chat was closed out into 27 atomic candidate notes at about 97.6 percent Chao1 completeness. Reconciliation on 2026-08-07 found all 27 new to the Core with no duplicates, privacy clean, atomicity sound. This is a separate track from the two contribution chats and can be approved on its own.

Key structural finding: "SONNY" is the private GitHub org ShopOnlineNewYork, 22 repos, only 7 active and canonical (SonnyNY, sonny-admin-dashboard, SonnyBackEndRepo, CJ-dropshipping, sonny-app-flutter-2.0, Sonny-Python, devops), the other roughly 15 dead or duplicate. No source of truth is the biggest structural problem.

P0 security, does not wait on note approval: 11 private .pem keys committed in the devops repo, a tracked .env in SonnyNY, and build-output properties in devops, all present in git history and readable by every org-read user. Remediation order: rotate all affected credentials today, then rewrite history with git filter-repo, then archive dead repos after a dependency check, then run the deep Phase 2 review. A full runbook was written for the operator on 2026-08-07.

## Links

- 2026-08-07-open-gap-legacy-formulas-and-z-method
