---
id: 2026-08-30-research-knowledge-home-raw-jsonl-is-deliberately-gitignored
type: finding
status: ratified
ratified: "2026-08-31 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "Oluwole weekly design-research scheduled task, 2026-08-30 session, git commit troubleshooting with the operator"
project: fleet
tags: [git, gitignore, raw-archive, secrets, pii, knowledge-core, operations]
sources:
  - ref: ".gitignore line 146: 'research/knowledge-home/raw/*.jsonl'. Confirmed by a failed `git add` on the operator's own machine this session ('The following paths are ignored by one of your .gitignore files'), then confirmed as the exact, current line via direct grep of .gitignore."
    reliability: high
    origin: "direct git/file inspection, 2026-08-30, triggered by the operator's own git add output"
provenance:
  archive: research/knowledge-home/raw/2026-08-30-oluwole-design-brief-and-closeout.jsonl
  turns: [23, 24]
risk_class: B
evidence_state: SUPPORTED
next_review: 2027-02-28
classified: 2026-08-30
---

- class: confirmed
- confidence: high — reproduced directly, not inferred; the operator's own terminal output triggered the check
- verified: 2026-08-30

# `research/knowledge-home/raw/*.jsonl` is deliberately gitignored — do not `-f` it, and don't read a failed `git add` on it as an error

## Body

Attempting `git add` on any file under `research/knowledge-home/raw/` fails with "The following paths are ignored by one of your .gitignore files," because `.gitignore` line 146 explicitly excludes `research/knowledge-home/raw/*.jsonl` (and line 147 excludes `research/knowledge-home/raw/antigravity-imports/**/*.jsonl`). This is intentional, not an oversight to override with `git add -f`: this same repo's own Brain Trust ledger (2026-08-25 row, Anansi Knowledge Core / Option A) documents that raw session transcripts in this exact folder have previously been found to contain committed-looking real Anthropic API keys, a Supabase JWT, and PII (a third-party email address) — the raw archive is where accidental pastes of sensitive material actually land, because it captures full conversational turns verbatim by design (per `docs/adr/0005-two-store-memory-archive-and-core.md`). Keeping it out of git by default is a real control, not friction to route around.

Practical consequence for anyone closing out a session per `stag-closeout`: the Step 0 raw archive write still happens (it's local, on-disk, and that's sufficient for a candidate note's `provenance.archive` pointer to be checkable), but the commit command handed to the operator should never include the raw `.jsonl` path — Step 7 of that skill already says this implicitly ("stage only the notes and artifacts marked RATIFIED... plus the Step 0 raw archive file"), but that line is now known to be wrong in one detail: the raw archive file itself cannot be staged at all under the current `.gitignore`, so it should not appear in a commit command's file list going forward.

## Links
- relates-to: research/knowledge-home/skills/stag-closeout (the skill's Step 7 language should be corrected to not imply the raw archive file gets committed)
- relates-to: reports/STAG_BRAIN_TRUST_LEDGER.md, 2026-08-25 row (Anansi Knowledge Core — Option A) — the prior incident that is the actual reason this exclusion exists
