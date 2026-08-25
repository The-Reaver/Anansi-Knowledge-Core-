---
id: 2026-08-25-9-gate-precondition-tracker
type: note
status: active
source: this chat, tracking the six ratification preconditions from the 9-Gate verdict.
project: fleet
tags: [brain-trust, 9-gate, stars-dreams, fleet-leveling, tracker]
---

# Tracker: five of the six 9-Gate preconditions are done; the operator ratified the scope decision ahead of the last one (the crosswalk table), which stays open as follow-on work

## Body

`2026-08-25-9-gate-brain-trust-verdict.md` listed six items to work before ratification. The
operator ratified the verdict's scope decision on 2026-08-25 (see that note's Ratification
section) with item 1 still open — a deliberate choice, not an oversight. Status as of this
session:

**1. Draft the Gate-range-to-FLEET_LEVELING-label crosswalk table.** Blocked-in-part. The
mechanism is drafted below, but the actual gate-range boundaries can't be filled in until (a)
item 2 confirms what FLEET_LEVELING's four stages currently mean, and (b) item 3 settles the
real gate count. Filling this in prematurely would be exactly the kind of guess the original
proposal warned against. See the stub in "Crosswalk table (stub)" below.

**2. Check FLEET_LEVELING's actual current content — unblocked, real finding.** Both
`FLEET_LEVELING_2026-08-01.md` and `STARS.docx` were located in the `Stag-Fleet` repo (on
`session/knowledge-core-2026-08-06` and `session/augustin-2026-08-06`, identical bytes on both)
and are now added to this repo's root, plus the audit report FLEET_LEVELING itself points to
(`reports/AMADEUS_AUDIT_FLEET_LEVELING_2026-08-01.md`).

The actual content changes the picture the original notes gave. `FLEET_LEVELING_2026-08-01.md` is
**not** a standing scale definition — it's a dated ledger entry claiming 8 agents ascended
Seed/Designed → Active, Beta on 2026-08-01, each gated by a discrimination harness that must go
RED when the capability is broken and GREEN when restored (a real, documented per-transition
criterion — proof-based, not a rubber stamp). But the file carries its own audit note at the top:
an independent Amadeus audit found only 4 of the 8 claimed ascensions actually had a real, checked
proving artifact (Amaya, Jasiah, Omar, Jayden); the other 4 (Sentinel, Weaver, Kratos, Valen) were
returned to unproven, not disproven, status. The document's own "compiled and verified by
Amadeus" attribution is flagged false by the audit — Amadeus checked it independently, after the
fact.

**Effect on item 1 (the crosswalk table)**: FLEET_LEVELING isn't a stable, agreed-on ground truth
to crosswalk against as-is — it's a disputed claim with a live correction layered on top. The
crosswalk work needs to point at the audited, corrected status per agent, not the original
document's claims at face value.

**3. Bottom-up derivation of gate domains — done, candidate.** See
`2026-08-25-9-gate-domain-derivation.md`. Twelve citable capability/governance domains were
identified across the cited sources plus a few more found in research (Feng/McDonald/Zhang's
"Levels of Autonomy for AI Agents," OpenAI's four-dimension agentic framework). The most defensible
merge logic yields **10 gates (5 capability, 5 governance)**, not nine — reported honestly along
with a sensitivity table showing the real range is roughly 5-12 depending on specific, nameable
judgment calls. Two sourcing gaps (NIST's agentic-profile publication status, OWASP's exact
tier/level counts) need direct primary-document verification before ratification — this agent's
WebFetch access to primary sources was blocked in-session, so findings rest on search-engine-
mediated summaries. Not yet ratified; the table still needs to resolve three flagged boundary
placements (autonomy gate's axis, blast-radius classification's axis, Map/Measure merge) before
adopting a final count.

**4. Decide and ratify Gate 1's specific threshold — research done, decision still pending.** See
`2026-08-25-gate-1-threshold-candidates.md`: three concrete, cited candidates (METR-only,
DeepMind-only, combined either/or), with a recommendation for the combined candidate. Real gaps
flagged honestly (METR's own reliability ceiling, domain-skew toward software tasks, DeepMind's
ontology having no attached operational test). Still needs the table's actual decision — this is
input, not a ratified number.

**5. Adopt the "Gate N" documentation convention — done, candidate.** See
`2026-08-25-gate-n-documentation-convention.md`. No blocker; this is a naming rule, not a
governance judgment call, but it still isn't ratified until the operator's pass.

**6. Confirm the STARS.docx citation-only edit — done.** `STARS.docx`'s own header names its
ratification authority directly: "Owner: Abad Morel" — no separate edit-approval clause exists
elsewhere in the document. Since Abad Morel is the operator, that resolved the blocker. The
citation-only paragraph is now applied in the document (see
`2026-08-25-stars-citation-edit-draft.md` for the exact text, how it was inserted, and how it was
verified). STARS's substance is untouched: the 7-phase SDLC map, TRL 1-9, weighted 0-100
composite (weights 10/12/13/13/12/20/20), weakest-link floor cap, and ceiling-durability discount
are all exactly as the original notes described.

## Crosswalk table (stub)

```
Gate range   -> FLEET_LEVELING label
-----------------------------------
Gate 1 - ?   -> Seed
Gate ? - ?   -> Designed
Gate ? - ?   -> Active/Beta
Gate ? - N   -> Alpha
```

Cannot be filled in until items 2 and 3 resolve. Nine does not divide evenly into four regardless
of the final count — whatever mapping is chosen is a deliberate design decision, not a natural
one, and the ratified version of this table must say so explicitly (per the verdict).

## Links

- extends, `2026-08-25-9-gate-brain-trust-verdict.md`, the ruling these six items gate.
- affects, `2026-08-25-gate-n-documentation-convention.md`, item 5.
- affects, `2026-08-25-stars-citation-edit-draft.md`, item 6.
- affects, `2026-08-25-gate-1-threshold-candidates.md`, item 4.
