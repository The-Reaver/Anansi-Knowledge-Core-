---
id: 2026-08-23-secret-scan-false-positive-recurred-inside-note-describing-itself
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i hereby ratify these notes\"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [git, pre-commit-hook, secret-scan, false-positive, self-reference, knowledge-core]
sources:
  - ref: "Commit attempt output on the 13-note ratification batch: \"PRE-COMMIT HOOK: Secret detected in staged files. Commit blocked. - Blocked: Possible Generic Secret found in staged file: research/knowledge-home/notes/2026-08-22-secret-scan-regex-false-positive-token-assignment-shape-in-code.md\", followed by the assistant identifying and fixing the recurrence in that same note."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [842, 854]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A ratified note whose own prose explained the secret-scan false-positive pattern re-triggered that exact same pre-commit hook a second time, because the explanatory prose reproduced the flagged shape rather than just describing it

- id: 2026-08-23-secret-scan-false-positive-recurred-inside-note-describing-itself
- type: finding
- status: ratified
- ratified: 2026-08-23 — operator directly ratified via explicit operator instruction ("i hereby ratify these notes"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found).
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 784-900
- confidence: high — directly observed the identical pre-commit hook block message naming the same file on a second, later commit attempt
- verified: 2026-08-23
- tags: git, pre-commit-hook, secret-scan, false-positive, self-reference, knowledge-core

## Body
After 13 candidate notes (including one titled around a secret-scan regex false positive on a token-assignment code shape) were ratified and staged for commit, the first commit attempt was blocked by the same repo pre-commit secret-scan hook, flagging that same note file again: `Possible Generic Secret found in staged file: .../2026-08-22-secret-scan-regex-false-positive-token-assignment-shape-in-code.md`. This was a distinct, later recurrence of the same underlying pattern already known from earlier in the session (a scanner regex matching a secret-shaped literal regardless of context) — but sharper, because this time the file being flagged was not a code fixture, it was the Knowledge Core note whose entire subject is that exact false-positive pattern. Its own explanatory prose, in illustrating the flagged shape for the reader, reproduced a literal instance of that shape closely enough to satisfy the same regex.

The fix was the same discipline as before: reword the prose to describe the pattern in words (e.g. "a token-named variable assigned a quoted string of 12+ characters") rather than writing out a literal instance of the shape, even inside a markdown note, even when the note's whole purpose is to document that shape.

General lesson: a blunt secret-scan regex does not distinguish code from documentation, and does not distinguish "an actual secret" from "an explanation of what a secret-shaped literal looks like." Any note or comment that needs to describe a token/secret/password-assignment shape for explanatory purposes must render that shape as prose description, never as a literal quoted-assignment fragment — and this holds with extra force for notes whose entire content is about this exact failure mode, since they are the most likely to accidentally reproduce it while explaining it.

## Links
- extends, 2026-08-22-secret-scan-regex-false-positive-token-assignment-shape-in-code.md — same underlying hook and pattern; that note covers the original two triggers (a test fixture variable, then its own fix's explanatory code comment); this note covers a third, separate trigger later in the same session, this time inside the Knowledge Core note documenting the first two.
- relates, 2026-08-14-secret-scan-gate-catches-quoted-fixtures-in-curriculum-prose.md — the earliest instance of prose (not code) tripping this same hook.
