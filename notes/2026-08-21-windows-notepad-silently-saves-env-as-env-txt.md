---
id: 2026-08-21-windows-notepad-silently-saves-env-as-env-txt
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, windows, dotenv, notepad, deploy-gotcha]
sources:
  - ref: "Archive turns 488-496: 'Found it — the classic Windows/Notepad trap. There's a .env.txt (modified 2 minutes ago, with your new password) sitting next to the real .env (untouched for an hour). Notepad silently appends .txt' (turn 490), followed by promoting .env.txt to .env and the generate-once-paste-both-sides fix (turns 494-496)"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [488, 496]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Editing a file named `.env` in Windows Notepad silently saves it as `.env.txt`, so the operator's repeated edits landed in a stale sibling file the app never read
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the .env.txt-vs-.env discovery and the promote-and-retest fix are directly confirmed in the archive. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly diagnosed by finding a `.env.txt` file modified minutes earlier sitting next to an untouched `.env`, and confirmed by promoting .env.txt to .env and re-testing
- verified: 2026-08-21
## Body
During this session's deploy, the operator repeatedly reported saving new values into `.env` (a fresh database password, in this case) that then appeared not to take effect. The root cause, found after two failed retries, was that the operator was editing the file in Windows Notepad, which silently appends `.txt` when saving a file whose name has no recognized extension — so all the recent edits were landing in a newly created `.env.txt` sitting next to the real, untouched `.env` that the application actually reads. Once identified, the fix was to promote `.env.txt` over `.env`. The durable operational rule for this and any similarly-configured Windows deploy: edit `.env` with an editor that preserves the exact filename (VS Code was recommended), or have the assistant write the value directly; and if a `.env` change appears not to take effect after saving, check for a same-directory `.env.txt` and compare modification timestamps before assuming the value itself was wrong.
REVIEW: high-impact
## Links
- related, 2026-08-21-alphanumeric-db-password-avoids-connection-string-parsing-failures.md, the specific value (a DB password) whose repeated failed edits led to discovering this trap
