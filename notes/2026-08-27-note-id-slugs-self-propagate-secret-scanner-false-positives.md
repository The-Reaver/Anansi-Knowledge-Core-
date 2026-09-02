---
id: 2026-08-27-note-id-slugs-self-propagate-secret-scanner-false-positives
type: finding
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: fleet
tags: [security, secret-scan, false-positive, anansi, naming-convention, append-only, adr-0005]
sources:
  - ref: "Second occurrence, 2026-08-27: scripts/gates/secret_scan_gate.py failed with 1 NEW finding in research/knowledge-home/raw/2026-08-27-live-c69335ef.jsonl; targeted regex confirmed the match is a fragment of a real note-id slug, not a credential. First occurrence was 2026-08-25-live-cb849e2f.jsonl, already baselined 2026-08-26 for the identical reason"
    reliability: high
    origin: "bridge-cse stag session, 2026-08-27; reproduced directly by running the gate and then locating the match with a targeted regex over the archive"
provenance:
  archive: research/knowledge-home/raw/2026-08-27-audit-report-standard-mandate.jsonl
  turns: [3, 3]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The fleet's own note-id naming convention manufactures secret-scanner false positives that spread to every session which discusses an affected note

## Body
`security/secret_scan.py`'s recall-first key pattern is `sk-[A-Za-z0-9_-]{20,}`. The fleet's note
ids are long kebab-case slugs. Any slug containing a word ending in `s` immediately followed by a
word starting with `k` — `risk-`, `task-`, `desk-`, `disk-`, `ask-` — produces a literal `sk-`
run followed by 20+ slug characters, and matches.

The live instance: a real, ratified note whose id contains `...calibration-ri` + `sk-generator-tuned-...-audit-gate` (deliberately split: writing the
real slug contiguously here would make this note trip the very scanner it documents)
yields a 41-character match. It is not a credential. It is the middle of a sentence.

**The part that makes this compound rather than merely annoy.** The Stop hook captures every
session into `research/knowledge-home/raw/` as an append-only ADR-0005 archive. So:

1. A session discusses an affected note by id — which is exactly what agents are *supposed* to do
   when citing prior work.
2. The Stop hook writes that id into that session's live archive.
3. `raw/` is append-only under ADR-0005. **The line can never be edited or removed.**
4. The gate now fails on a brand-new file, and the only available disposition is another baseline
   entry.

Every conversation that responsibly cites one of these notes permanently adds one more baselined
finding. It is now at **two** (`2026-08-25-live-cb849e2f.jsonl`, baselined 2026-08-26;
`2026-08-27-live-c69335ef.jsonl`, baselined 2026-08-27) and it will grow monotonically for as
long as the affected notes stay worth citing. The security cost is real but indirect: a baseline
that accumulates known-benign noise is a baseline people stop reading carefully, and this scanner
is the fleet's only backstop against a *real* key reaching an immutable store.

**What is NOT the fix.** Narrowing the regex. That has been tried twice on this exact pattern and
failed both times — most severely on 2026-08-26, when a same-day precision tweak silently stopped
matching **7 of 7 real committed keys** and was caught only by the `--assume-append-only`
regression check. `security/secret_scan.py`'s own comments record this and forbid re-narrowing
without validating against the full baseline first. For a security scanner a missed real secret
is strictly worse than an extra flagged non-secret. **Do not touch the regex.**

**Options that would actually work**, cheapest first:

1. **Exempt the archive path from this one pattern, structurally** — allow `sk-` matches
   consisting only of `[a-z-]` (no digits, no uppercase, no underscore) inside `raw/*.jsonl`. A
   real base64/alphanumeric key effectively never has that shape; a kebab slug always does. This
   narrows the *disposition*, not the *detection*, so it does not repeat the 2026-08-26 failure —
   but it does need the same validate-against-the-real-corpus discipline before shipping.
2. **Rename the offending notes** so no slug contains an `sk-` run. Cheap for future notes as a
   naming rule; retroactively it does not help, because the archives already contain the old ids
   and cannot be rewritten.
3. **Accept and keep baselining.** Zero risk, zero work per occurrence, and the honest cost is
   baseline erosion over time. Viable only if someone actually re-reviews the baseline
   periodically.

**Standing rule regardless of which option is chosen:** a new finding in `raw/` must be *looked
at* before it is baselined — locate the match with a targeted regex rather than by reading the
archive, confirm its shape, and record the reason in the baseline's `note` field. Both entries so
far were reviewed this way. The gate's own message says it: *"Never silently baseline a finding
you have not looked at."*

## Links
- extends: notes/2026-08-23-secret-scan-false-positive-recurred-inside-note-describing-itself.md
  — that note covers the Generic-Secret regex re-triggering inside the note documenting it,
  and its fix (describe the shape in prose, never reproduce it). This note covers a *different*
  regex and a mechanism that prose discipline cannot fix: the id propagates into an
  append-only archive by way of the Stop hook, where it can never be edited out.
- relates-to: notes/2026-08-22-secret-scan-regex-false-positive-token-assignment-shape-in-code.md
- relates-to: notes/2026-08-14-secret-scan-gate-catches-quoted-fixtures-in-curriculum-prose.md —
  the earliest instance of prose, not code, tripping this hook.
- caused-by: the interaction of ADR-0005's append-only rule for raw/ with the fleet's kebab-case
  note-id convention — neither is wrong alone.
- relates-to: 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally — both are
  consequences of the archive being the fleet's system of record.
- see-also: security/secret_scan.py's module comments, which record the two failed attempts to
  fix this by narrowing the pattern and forbid a third.
