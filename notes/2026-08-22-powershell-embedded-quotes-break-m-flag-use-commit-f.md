---
id: 2026-08-22-powershell-embedded-quotes-break-m-flag-use-commit-f
type: finding
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [powershell, git, windows, commit-message, quoting, gotcha]
sources:
  - ref: "Archive lines 770-771: the actual PowerShell transcript of `git commit -m $msg` splitting mid-message at the embedded double quotes ('error: pathspec ...chars) ... did not match any file(s) known to git'), followed by the assistant's diagnosis and the git commit -F fix."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [770, 771]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A multi-line git commit message with embedded double-quotes, passed via `git commit -m $msg` in Windows PowerShell 5.1, gets mis-split at the quotes — use a temp file and `git commit -F` instead

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly reproduced (the exact PowerShell error output was captured) and directly fixed and confirmed committed clean
- verified: 2026-08-22

## Body
A commit message built as a PowerShell here-string (`$msg = @'...'@`) and passed to a native executable via `git commit -m $msg` works fine for plain text, but breaks if the message contains literal double-quotes — for example a code fragment like `token = "12+ chars"` quoted for explanatory purposes. Windows PowerShell 5.1 re-splits the argument at those embedded quote marks when passing it to a native exe, producing an error like `error: pathspec '...' did not match any file(s) known to git` where the "pathspec" is actually a truncated fragment of the commit message starting right after one of the quoted substrings. This is a different failure mode from the more commonly-known bash-heredoc-vs-PowerShell-here-string syntax mismatch — the here-string itself was correctly formed and assigned to `$msg`; the break happens specifically at the `-m $msg` argument-passing step when quotes are present in the content.

The reliable fix is to sidestep argument quoting entirely: write the message to a temp file (`$msg | Set-Content -Path commit_msg.txt -Encoding utf8 -NoNewline`) and use `git commit -F commit_msg.txt`, then delete the temp file. One related gotcha: `Set-Content -Encoding utf8` in Windows PowerShell 5.1 writes UTF-8 *with* a BOM by default, which shows up as an invisible character at the very start of `git log` output for that commit — harmless, but `-Encoding utf8NoBOM` avoids it if it ever matters.

General rule for this environment: any commit message that will contain a literal `"` character should be written via a temp file and `git commit -F`, not `-m $msg`, regardless of whether the message text itself parses fine in the here-string.

## Links
- relates, 2026-08-02-operator-environment-split-ubuntu-work-powershell-push.md — general PowerShell/Ubuntu environment-split context this gotcha sits within.
