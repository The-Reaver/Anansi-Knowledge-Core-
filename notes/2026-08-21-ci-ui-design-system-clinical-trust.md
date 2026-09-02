---
id: 2026-08-21-ci-ui-design-system-clinical-trust
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, design-system, ui, mockup, artifact]
sources:
  - ref: "Operator's AskUserQuestion choice of a \"clean clinical trust\" aesthetic and the resulting published Artifact mockup with its exact palette/typography/layout spec"
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (A)\" (backfilled from historical transcript c5583566, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-c5583566.jsonl
  turns: [181, 188]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — operator explicitly chose this aesthetic via an AskUserQuestion turn; mockup was built and published to this spec
- verified: 2026-08-21

## Body
When asked to make the CI audit report UI "beautiful," the operator chose a mockup-artifact-first approach with a "clean clinical trust" aesthetic (over other options the agent offered). The resulting design system, built into a published Artifact mockup: a cool-grey ground biased toward the accent (#F5F7F8, cards #FFFFFF), deep slate ink (#1B2A32, not black), and exactly one accent color — a clinical teal (#0E7C7B) — carrying the brand mark, citation links, and confidence bars. Severity is deliberately kept semantic and separate from the brand accent: clay-red for high, amber for medium, sage for low, shown both as a chip and as a left-border stripe on each finding row. Georgia serif is used for headings (chosen for gravitas, since a lawyer is a likely reader), system sans for UI/body text, and mono for the crawl-snapshot reproducibility hash — system faces only, no CDN font dependency. Layout order is branded header with posture badge, then an executive-summary band (risk meter, severity tiles, numbered top-3 prioritized fixes), then the detailed cited findings table, then an honesty footer carrying "candidate, not verdict" language plus the snapshot hash. The mockup renders the engine's real findings, including the lawyer-proof nuance inline (durable-authority citation with the June 2024 vacatur caveat on the tracking row; Section 508 marked "technical benchmark only" on the accessibility row). This is a chosen direction, not yet built into the live `ci-ui-shell` React app as of end of session — translating it into real components/token stylesheet was the recommended next step.

## Links
- extends, 2026-08-21-ci-ui-shell-chosen-over-nextjs.md, this is the visual layer for the frontend chosen earlier in the same session
