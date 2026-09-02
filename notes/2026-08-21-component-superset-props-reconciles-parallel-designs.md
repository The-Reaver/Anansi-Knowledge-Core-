---
id: 2026-08-21-component-superset-props-reconciles-parallel-designs
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, frontend, typescript, react, prop-design, refactoring]
sources:
  - ref: "Archive turn 163: the agent's own results summary names the components (ToggleConfirmDialog, ToolSlotCard, ToolSlotGrid, MemberList, StatusBanner, SuspendedBillingOnly, CardUpdateForm, ClientTable, SuspendReinstateControls, NumberReleaseControl, AdminNav) whose prop shapes were reconciled to a superset accepting both parallel designs"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [163, 163]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# When a code generator emits two parallel designs of the same component (self-fetching vs. parent-supplied data), make the props a superset that accepts both rather than picking one
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: medium — applied successfully to several named components this session (MemberList, ToolSlotCard, ToolSlotGrid, ToggleConfirmDialog), but the general applicability beyond this codebase is inferred, not independently tested elsewhere
- verified: 2026-08-21
## Body
Several components in the STAG-generated frontend had two competing prop shapes because different generation passes had written some callers to let the component self-fetch its own data and other callers to pass the data down as a prop (for example `MemberList` supporting both a self-fetch mode and a parent-supplied-data mode, and `ToolSlotCard`/`ToolSlotGrid` supporting both the grid's request-pattern and a direct `onToggle` callback). Rather than pick one design and rewrite the other callers, the reconciliation made each component's prop type a superset that accepts both shapes as optional props, deriving its actual behavior (controlled vs. uncontrolled, self-fetch vs. prop-driven) from whichever inputs are present at runtime. This unifies callers written against either of two parallel designs without discarding either caller's assumptions, at the cost of a component that has to branch on which mode it's in.
## Links
- related, 2026-08-21-adapt-few-lib-modules-to-many-consumers.md, the same reconciliation strategy applied at the shared-library layer instead of the component layer
