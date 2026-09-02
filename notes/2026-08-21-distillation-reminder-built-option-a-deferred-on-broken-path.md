---
id: 2026-08-21-distillation-reminder-built-option-a-deferred-on-broken-path
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (Option A status updated: the `claude` PATH issue that blocked it is fixed and headless auth independently verified, so Option A is now unblocked, awaiting only operator go-ahead). Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, mcp, hooks, distillation, adr-0005, knowledge-core, automation, open-item]
sources:
  - ref: "Turns 131-154: operator requests an automated raw-transcript-to-notes distillation process (turn 131), and the assistant weighs Option A (fully automatic, SessionEnd-triggered `claude -p` call) against Option B (SessionStart reminder hook, no LLM call) and confirms the Option B hook design is structurally correct (turn 154)."
    reliability: high
    origin: "STAG session, 2026-08-21, \"Anansi local API + MCP registration\" (continuation)"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [131, 154]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A SessionStart hook now flags undistilled Anansi raw-archive content automatically; full auto-distillation (Option A) is built but deliberately not wired -- originally blocked on a broken `claude` PATH, since fixed, now awaiting operator go-ahead

- id: 2026-08-21-distillation-reminder-built-option-a-deferred-on-broken-path
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-21, "Anansi local API + MCP registration" (continuation)
- confidence: high, pipe-tested end to end with a disposable scratch archive before touching real state
- verified: 2026-08-21
- tags: anansi, mcp, hooks, distillation, adr-0005, knowledge-core, automation, open-item

## Body

Following [[2026-08-21-live-transcript-capture-stop-hook-built]] (raw capture, mechanical, no judgment needed), the operator asked for the harder half: turning raw transcripts into atomic notes/artifacts/handoffs automatically, not just archiving them. Two designs were considered:

**Option A (fully automatic):** a `SessionEnd` hook shells out to headless `claude -p` to run the actual distillation reasoning. Ruled out for now, for two reasons found this session: (1) Claude Code's `prompt`/`agent` hook types, the only types that can invoke an LLM directly, are restricted to tool events (`PreToolUse`/`PostToolUse`/`PermissionRequest`) and cannot run on `SessionEnd` — so this design requires shelling out to the CLI itself, not a native hook capability; (2) testing `claude -p "..." --model haiku` in this session's Bash tool returned `command not found` — `claude` is not currently resolvable on PATH in a shell subprocess, most likely a side effect of the native-install reinstall run earlier this same session (`irm https://claude.ai/install.ps1 | iex`), which left `C:\Users\abadm\.local\bin` off PATH and may have disturbed the previously-working npm-based shim.

**Option B (built this session):** `scripts/knowledge_home/distillation_reminder.py`, a `SessionStart` command hook — no LLM call, so no PATH dependency. On every new session start in this repo, it diffs each `research/knowledge-home/raw/*.jsonl` file's current line count against a last-known-distilled count in `.claude/anansi_live_capture/distillation_state.json`, and if any file grew, injects a plain-text reminder into the new session's context (`hookSpecificOutput.additionalContext`) naming which files have undistilled material. The actual distillation (reading the new lines, drafting candidate notes with judgment, following the stag-closeout capture standard) is then done by the agent as normal work, not by the hook — output still lands as `status: candidate`, so Mandate 1's ratification gate is untouched. `scripts/knowledge_home/mark_distilled.py <archive-file>` is the paired tool an agent calls after actually completing a distillation pass, to advance the checkpoint and stop the reminder from re-firing on already-handled content.

Bootstrapped this session against the 7 raw-archive files that existed before this hook was built (`2026-08-10-ten-stage-pipeline-intake.jsonl` through `2026-08-21-amadeus-fleet-audit-ci-reconcile.jsonl`) — their baseline was set to their current line count at bootstrap time, not zero, so pre-existing history isn't retroactively flagged as a fake backlog. Only growth from 2026-08-21 onward is tracked.

**Explicit operator instruction, recorded verbatim so it is not lost: revisit Option A once PATH is fixed (`C:\Users\abadm\.local\bin` added) and headless `claude -p` invocation is verified to actually authenticate and run non-interactively end to end.** The same `distillation_reminder.py` hook also checks `shutil.which("claude")` on every session start specifically so this becomes self-surfacing — once PATH is fixed, the very next session start will flag "claude now resolves on PATH" as part of its reminder, rather than relying on anyone remembering to check back.

**Update (2026-08-25):** the blocking condition has since cleared. `claude` now resolves on PATH (`/c/Users/abadm/.local/bin/claude`), and headless `claude -p` invocation was independently verified this same day to authenticate and run non-interactively end to end. Option A is therefore no longer blocked on the PATH issue — it is unblocked and awaiting only the operator's go-ahead to actually wire it, not a technical fix.

## Links
- extends, 2026-08-21-live-transcript-capture-stop-hook-built.md, the capture half this distillation-reminder half is built on top of.
- relates, docs/adr/0005-two-store-memory-archive-and-core.md, this hook automates surfacing (not performing) the "distillation pass" ADR-0005 already describes as a manual step.
