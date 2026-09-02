---
id: 2026-08-21-tailwind-v4-group-marker-class-responsive-prefix-noop
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [tailwind, css, tailwind-v4, group-hover, technical-gotcha]
sources:
  - ref: "Turns 367-486: lines 367, 369, 371, and 384 each independently confirm, across four different finder-angle agents, that md:group compiles to nothing because group is a marker class with no responsive variant, each citing matching dist/ HTML+CSS evidence; line 486 confirms the fix (md:group -> group) resolved the dead desktop nav hover."
    reliability: high
    origin: "STAG session, 2026-08-13, \"Agame sports rebuild brief\" (backfilled from historical transcript a343a321, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-13-backfill-a343a321.jsonl
  turns: [367, 486]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# In Tailwind v4, prefixing the `group` marker class with a breakpoint (`md:group`) compiles to nothing
- id: 2026-08-21-tailwind-v4-group-marker-class-responsive-prefix-noop
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-13, "Agame sports rebuild brief" (backfilled from historical transcript a343a321, 2026-08-21)
- confidence: high — independently confirmed by at least 5 separate review-agent passes, each checking the actual compiled CSS and rendered HTML in the built dist/ output, not just source
- verified: 2026-08-21
- tags: tailwind, css, tailwind-v4, group-hover, technical-gotcha

## Body
`group` in Tailwind CSS is a marker class (it exists only so a descendant selector like `.group:hover .child` can target it), not a real utility class — so responsive variant prefixing, which only applies to actual utilities, does nothing to it. Writing `class="relative md:group"` produces the literal, unprefixed string `md:group` in the rendered HTML; Tailwind never generates a `.md\:group` rule, and no element ever carries a bare `.group` class for `.group:hover`/`.group:focus-within` selectors to match. In the A-Game Sports rebuild this silently killed the entire desktop nav dropdown's hover/keyboard-focus behavior — confirmed in the built HTML (`class="relative md:group"` present) and built CSS (the `.group[data-astro-cid-...]:hover ...` rule present but unreachable) across two independent review passes and multiple finder agents within each pass. The correct approach for "only enable group-hover at a breakpoint" is a wrapper query or an explicit breakpoint-scoped alternative — never `<breakpoint>:group`.

## Links
- see-also, 2026-08-21-dual-blind-adversarial-review-passes-converge.md, the review process that surfaced and re-confirmed this bug
