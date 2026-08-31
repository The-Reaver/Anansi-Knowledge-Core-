---
id: 2026-08-04-blackfire-brain-trust-nine-questions-resolved
type: note
status: candidate
source: "this chat, 2026-08-04, Abad asked directly for the nine clarifying questions from the Brain Trust's Mandate 10 ruling to be answered and filed as a standing reference he can point future chats to by name (source status: active)"
project: fleet
tags: [blackfire, mandate-9, mandate-10, brain-trust, governance, operator-contribution, permanent-reference]
---

# Blackfire — STAG Governance Reference: Mandate 9, Mandate 10, and the Nine Open Questions Resolved

## Body

## What this document is

Abad named this document "Blackfire." It is meant to be a standing reference: he intends to tell a future chat "look at Blackfire" instead of re-explaining this session's governance decisions. It answers the nine open clarifying questions the simulated Brain Trust raised in its Mandate 10 ruling, and anchors the two governance mandates ratified on 2026-08-04.

**Two-line orientation for whoever reads this next:** Mandate 9 says a task only counts as a compounding asset if it is captured, reused by someone else, and produces a measurable delta. Mandate 10 says a Cowork chat should proactively write a handoff to Knowledge Core once it gets heavy, using honest heuristics rather than a token count Claude doesn't have access to, and treats a compaction happening with no prior handoff as a mandate violation, not a recoverable event.

## The nine questions, answered

**1. Is retrieval into new sessions from Knowledge Core actually confirmed working today?**
No. Not confirmed. This session wrote 22 atomic notes plus this document into the Anansi Atomic Notes Inbox on Google Drive, and separate handoff material into this Cowork session's own project memory. Neither has been tested by a genuinely fresh session reading it back and resuming without Abad re-explaining anything. The honest status is untested, not failed. The first time Abad tells a new chat "look at Blackfire," that is the real test. If that chat can orient itself from this document alone, retrieval works. If it can't, that is the concrete signal to fix, not a hypothetical risk.

**2. Should the historical diagnostic wait for the Anansi minimal slice's own schema/taxonomy?**
Yes, and this was already a ratified condition, not a new answer. The markdown format used for tonight's 22 notes (id, type, status, source, tags, Body, Links) is a deliberate interim schema chosen because it maps cleanly onto the ledger's real columns once deployed: type maps to artifact_type, source maps to source_type and source_ref, Body maps to lesson_summary, Links map to the reuse relationships. Notes written now under this format are not wasted work; Jeremy's learning_log_ingest.py script is built to backfill exactly this kind of entry once the ledger is live.

**3. Does "all types of chats" include chats with no governance-relevant decisions?**
No. Adopt Bink's triage filter as the standing rule. "All types" means no category of chat is excluded up front, coding chats, strategy chats, Lovable-build chats, personal reminders, all are eligible. It does not mean every chat regardless of substance gets a note. A chat that produced no real decision, commitment, correction, or reusable outcome gets skipped entirely, not even a stub. This keeps Knowledge Core's signal-to-noise usable.

**4. Who owns dedup/merge, and is there a retention policy?**
Celestina's seat owns this by lens, operationally meaning: before a future session writes a new atomic note, it should search Anansi/Drive for an existing note on the same decision or thread first, and flag a likely near-duplicate for Abad rather than silently merging or silently duplicating. There is no deletion policy yet. The status field is the mechanism: a note that gets superseded should be marked superseded with a "supersedes" link to the note that replaces it, not deleted. Revisit this once volume becomes a real problem, it is not one yet at 23 notes.

**5. What's the real underlying pain point, inefficiency in ongoing chats or inability to find past decisions?**
Based on what actually happened this session: inefficiency in ongoing chats. The concrete trigger for Mandate 10 was this very session hitting an automatic compaction. Nothing in this session showed Abad unable to locate a specific past decision. Mandate 10 (the weight-watch/handoff habit) directly addresses the real, observed problem. The historical diagnostic, mining everything ever decided across all past chats, is a different, second-order goal tied to Abad's stated wish to teach others how STAG got built, not proven yet to be the same problem as the compaction issue. Keep tracking them as two separate projects with two separate timelines, which is already how they're recorded.

**6. Can the historical diagnostic run passively, without Abad narrating?**
Partially, and this matters for scoping it. Claude can mine sources it can already reach without Abad in the loop: STAG's own project memory files, documents in Abad's connected Google Drive, and this session's own history. It cannot reach chats that live somewhere this session has no access to, for instance earlier conversations with Antigravity or older claude.ai chats not exported or shared into a reachable location. For those, Abad has to paste or export the source material in before it can be mined. So: passive wherever the source is already reachable, narrated only where it genuinely is not.

**7. What message/tool-call count should serve as the weight-watch proxy threshold?**
A concrete starting default, since nobody had picked one: treat a session as getting heavy once it crosses roughly 15 substantial tool calls, or 3 subagent dispatches, or 2 large file/document reads combined with either of the first two, whichever comes first. That is the point to self-check and consider offering a handoff. This is a starting number, not a fixed law; Abad can tighten or loosen it once he sees how it behaves in practice.

**8. Who audits the post-Friday note backlog for the accuracy sampling gate?**
AJ the auditor, the existing fleet role documented in stag_fleet_governance, not a new assignment to Abad or to a Brain Trust seat that already carries a full-time lens. Spot-checking roughly one note in ten against its source chat for accuracy is exactly what an auditor role exists to do. Abad can override this assignment if he wants someone else on it.

**9. What counts as "decided" for the historical diagnostic?**
The same bar already used for tonight's 22 notes: a real decision, ruling, ratified rule, concrete build outcome, or explicit correction or finding. Exploratory reasoning or brainstorming that never converged to an actual outcome does not get its own note. Only the resolution, if one was reached, does. This is not a new standard being introduced, it is naming the standard that was already applied tonight so it stays consistent going forward.

## Links

- extends: 2026-08-04-mandate-10-weight-watch-handoff-protocol-ratified-with-amendment
- extends: 2026-08-04-mandate-9-compounding-assets-ratified
- extends: 2026-08-04-historical-diagnostic-queued-not-yet-scoped (these nine answers are what unblocks that item's next real decision from Abad)
