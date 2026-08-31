---
id: 2026-08-06-partner-update-budget-and-staffing-decisions
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone; asked for two partner-facing reports and stated budget, staffing, local-system, and security requirements to bring to the partner and the lawyer today. (source status: active)"
project: fleet
tags: [partner-update, budget, staffing, security, local, hipaa, contributions]
supersedes: []
superseded_by: null
---

# Partner update produced; build-local-now, budget, and staffing decisions logged

## Body

## Operator contributions and requirements logged
- Build for all scenarios now, including a local, private system, because clients (doctors) will likely hold private patient information. Do not build it later, build it now, including a pre-built path for bringing patients in.
- Run locally for clients where required. Orin considered; see verdict below.
- Justify all expenses to the partners and the lawyer.
- Stress the importance of the agents eloquently so the partners feel safe and understand why they need them.
- Staffing ask to the partner: three assistants at roughly 700 to 1000 dollars per month each, for accountability, production hardening, and security. Do not mention the operator's own salary; the partner negotiates that separately.
- Update the partner today on everything: the GEO Suite plan, what was learned, what will be instituted, clear goals and expected outcomes, and a separate simple-language report on the fleet.

## Deliverables produced this session
- GEO_Suite_Partner_Update.pdf: plan, three tools, goals and outcomes, security and local-by-design rationale, budget justification, and the three-assistant staffing ask. Operator salary intentionally omitted.
- The_Fleet_Explained.pdf: plain-language explanation of the fleet, the 1-to-9 school, graduation, the Wilson/Glicko/SPRT math explained simply, and the safety story (AJ plus the break-it team).

## Verdicts
- Local system: agreed and prudent for patient data. Build the software to run both cloud and local from the start. Store patient data locally on a modest secure server when a client needs it. Buy heavy local AI hardware only when a specific client requires that patient data never leave their office, decided with counsel. This keeps spend tied to a real need.
- Orin: an edge AI device, fine for light on-device work, limited for heavy building. For serious local model running a desktop GPU box is usually stronger. Decide exact hardware per client requirement, not preemptively.
- Budget numbers are ranges so the partner and lawyer can firm them up. Exact hardware quotes to be researched at the machine.

## Links

- extends: 2026-08-06-brain-trust-verdicts-and-operator-contributions
