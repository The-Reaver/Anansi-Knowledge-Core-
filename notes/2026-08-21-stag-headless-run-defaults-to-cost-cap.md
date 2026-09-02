---
id: 2026-08-21-stag-headless-run-defaults-to-cost-cap
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, meta_agent, cli, interview, cost-cap, tty]
sources:
  - ref: "Archive turns 135-141 show meta_agent.py's interactive cost-cap interview silently defaulting to $2 when launched with no attached tty, and the agent killing the backgrounded run and handing it back to the operator's own terminal."
    reliability: high
    origin: "STAG session, 2026-07-09, \"Task 8 continuation\" (backfilled from historical transcript e0fb412c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-09-backfill-e0fb412c.jsonl
  turns: [135, 141]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: medium — observed once in this session (agent noticed the default-$2 behavior when launching task 10 in the background and immediately killed/restarted it), not independently re-verified against the STAG source in this pass
- verified: 2026-08-21

# STAG's meta_agent.py needs a real terminal for its interactive cost-cap interview; run headless with no tty, it silently defaults to a $2 cap

## Body
`meta_agent.py` (STAG's task-generation entrypoint) normally runs an interactive interview before building a task, including a prompt for the dollar cost cap for that run. When the agent tried to launch task 10 in the background (via a backgrounded Bash call, with no attached tty and no piped stdin), STAG's interview did not block waiting for input as expected — it silently proceeded with a default $2 cost cap instead of the operator-intended $150. The agent caught this by checking on the background process shortly after launch, killed it, and reverted to the established pattern from tasks 8 and 9: handing the exact command and interview answers back to the operator to run in their own terminal, where a real tty is present and answers can be typed live (or where the operator was already piping the recipe in). General lesson for anyone driving `meta_agent.py` (or similar interactive CLIs) from an automated/background context: a missing tty during an interactive prompt does not necessarily raise an error — it may silently fall through to a hardcoded default, so a background/headless run of an interactive tool should be checked immediately for whether it's actually blocked on input or already running with unintended defaults.
