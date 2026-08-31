---
id: geosuite-build-ledger-proposal-2026-08-25
type: finding
status: candidate
source: "Architecture, Redlined — Rev. 3, Part V; this session's own GeoSuite roadmap-gaps slices; captured via GeoSuite session handoff, 2026-08-25"
project: geo
tags: [geosuite, build-ledger, site-generator]
superseded_by: geosuite-build-ledger-ruling-2026-08-25
supersedes: []
---

# One atomic note per non-obvious build decision, not a commentary on every line

## Body

Proposal: one atomic note per real, non-obvious decision a GeoSuite build surfaces — not a
running commentary on every line changed (git history already is that). Two real entries
already exist from the session that drafted this proposal, proving the format before
scaling it:

1. `site_pipeline.py`'s `_persist()` globs every `*.html` file unconditionally, so a new
   page type can't ship its rendering half without its persistence half in the same commit
   (discovered landing the Terms of Service page — see The-Geo-Suite- commit 01340f5).
2. A 10th hero-bearing theme file, `trust_panel.py`, hardcoded the same
   `background-image:url('assets/hero-bg.svg')` reference the first theme-sweep pass
   missed — only 9 of 10 were caught initially (see commit d575ff1 / d7ff8da).

Purpose: not making any single generated site more creative — GeoSuite's own
`compute_seed()`/`select_theme()` mechanism already owns that job (proven by a passing
test, `test_hero_bg_actually_differs_between_two_real_generated_businesses`). This is
about not making the next agent re-derive a decision that's already been paid for once.

This is a finding, not yet ratified — whether and how to build this is a decision for the
operator, not something to silently treat as decided.

**Update, 2026-08-25 — concretized into a real, decidable proposal.** The original version
named a principle and two examples but left four load-bearing questions unanswered — the
kind of gap that made the other three Part V proposals buildable and left this one stuck.
Answers below; still `status: candidate`, since deciding whether the overhead is worth it
is a fifth question that stays the operator's call, not something a concrete spec answers
on its own.

**1. Where an entry lives.** Not in this Anansi repo as the primary copy — GeoSuite is a
different repository, and sessions working in it typically have no Anansi access (this has
been true of every GeoSuite session referenced in this thread). A ledger only a
disconnected session can't reach fails at the one thing it's for. So: the authoritative copy
is a single append-only file inside `The-Reaver/The-Geo-Suite-` itself —
`docs/build-ledger.md` — grep-able by any session working there regardless of whether
Anansi is reachable. A cross-reference note in this repo (`project: geo`, linking to the
in-repo entry) is a secondary index for fleet-wide search when Anansi *is* reachable, never
the only copy.

**2. When an entry gets written.** Not "whenever something feels non-obvious" — a concrete
trigger: an entry is written when a fix or discovery meets *any* of —
  - understanding it required reading code outside the file actually being changed (a
    hidden coupling, the way `_persist()`'s unconditional glob wasn't visible from the new
    page-type code itself);
  - a count or assumption turned out wrong only once actually checked (9 themes, not 10; 2
    no-hero templates, not 3);
  - nothing in the existing test suite would catch the same mistake if a future change
    reintroduced it.
A routine bug with an obvious, local root cause doesn't qualify — this is deliberately
narrower than "every fix," matching the original proposal's own "not a running commentary
on every line" framing.

**3. Enforcement.** No new tooling: fold it into the adversarial-review pass this fleet
already runs on GeoSuite fixes. One more question on that reviewer's checklist — "does this
fix meet the ledger-trigger criteria above, and if so, is there a `docs/build-ledger.md`
entry in this commit?" — the same way `skill-eval-gate` made "did this ship without a
re-run" a hard gate rather than a hope.

**4. Retrieval.** Each entry names the specific file(s)/function(s) it concerns in a
consistent, greppable line (e.g. `Files: site_pipeline.py (_persist)`), so a keyword search
against the ledger file surfaces it without needing semantic search. `The-Geo-Suite-`'s own
`CLAUDE.md` gets one added line pointing agents at the ledger before touching site-generator
internals, the same way it already points agents at other standing conventions.

**What's still genuinely open:** whether this is worth building at all. The other three
Part V fixes were free — documentation only. This one has a real recurring cost (writing an
entry every time the trigger fires), against a fleet mandate that already argues against
speculative process. That tradeoff, now that the mechanism itself is concrete enough to
actually weigh, is the operator's call — and building the actual `docs/build-ledger.md` file
means touching the GeoSuite repo, which is out of scope for this session while another
session is active there.

**Ruling, 2026-08-31 — approved, conditionally.** See
`geosuite-build-ledger-ruling-2026-08-25`: approved on the terms above, on the condition
that enforcement is wired into the adversarial-review pass as an actual checklist line,
not left as prose intent. Building `docs/build-ledger.md` itself remains a separate
follow-up in `The-Reaver/The-Geo-Suite-`.

## Links

- Architecture, Redlined Rev. 3, Part V
- The-Reaver/The-Geo-Suite- commits 01340f5, d575ff1, d7ff8da
