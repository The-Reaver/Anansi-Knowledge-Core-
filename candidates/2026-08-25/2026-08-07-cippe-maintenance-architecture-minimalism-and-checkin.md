---
id: 2026-08-07-cippe-maintenance-architecture-minimalism-and-checkin
type: decision
status: candidate
source: "Cowork session 2026-08-07; operator asked about deeper minimalism, a built-in periodic interview feedback loop, explaining the Knowledge Core to the user in plain terms, and a local laptop-to-laptop maintenance system where her Core can improve ours without leaking her data. (source status: active)"
project: cippe
tags: [cippe, maintenance, usb, knowledge-core, privacy, minimalism, check-in, feedback-loop, explainer, handoff, confidential]
---

# CIPP/E copilot, USB local maintenance and Core-to-Core feeding, minimalism, periodic check-in, in-app plain explainer, and her handoff document

## Body

## Confidentiality
- The intended user's name is known to the operator and the app (stored locally on her device). It is kept OUT of the Knowledge Core, all documents, and anything shared. Refer to her only as "the intended user".

## Minimalism
- Clean is not enough; reduce what is visible by default. Light pass now: group the navigation, default the right record panel collapsed, keep essentials visible and the rest one tap away. Deep version in the nav research: a Notion-style drawer that hides complexity until reached for. The app asks her what to hide or show via the check-in.

## Periodic check-in (built-in interview / feedback loop)
- A gentle scheduled check-in asks a few specific questions about her days and what helped. Feeds her local Knowledge Core so the copilot keeps improving for her. This is the in-app feedback loop.

## In-app plain-language Knowledge Core explainer
- An in-app page in plain words, no jargon: your copilot remembers what matters, keeps it tidy in rooms, checks it stays true, gets sharper as it learns you, and stays on your computer. Same content goes in her handoff document. Never use technical jargon with her (neurodivergent, keep it simple).

## Maintenance architecture (USB local, and Core-to-Core feeding)
- Her work content (client/employer privacy data) NEVER flows to our Core; that would be a privacy breach and could break her job's confidentiality rules.
- What safely crosses: only de-identified improvement learnings (feedback-loop patterns, not content), which she reviews before they leave.
- Local only, by cable: maintenance is laptop-to-laptop over a direct USB cable, offline. The fleet runs a diagnostic on her local install, applies fixes, and takes back only the de-identified improvement bundle. Fixes go to her; learnings come to us; her data stays on her machine.
- Consent and employer first: before any connection, even by cable, she confirms what her employer allows, ideally in writing. Non-negotiable given her role. She must tell the operator what she does and what she is permitted to store and share.

## Close-out sequence
- Finish deep research + redesign, build the remaining pieces (check-in, in-app explainer, minimalism, local setup, USB maintenance) into the demo, write her a simple plain-language document explaining what it is and how it helps, lock the demo, send her the link.

## Build sequencing
- Next Lovable build (after the sizing fix): minimalism pass, periodic check-in, and the in-app plain-language explainer.
- Machine/Antigravity + research phase: the local single-container setup, the USB diagnostic-and-fix maintenance tool, the adaptation-engine tuning, the Notion-style nav, and the professional interview questions.

## Links

- relates-to: 2026-08-07-cippe-adaptation-engine-and-help-workflow-spec
- relates-to: 2026-08-07-cippe-personalized-user-profile-and-companion-spec
- relates-to: 2026-08-07-machine-session-plan-and-work-distribution
