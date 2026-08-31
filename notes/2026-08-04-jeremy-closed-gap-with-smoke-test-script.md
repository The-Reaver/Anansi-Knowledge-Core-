---
id: 2026-08-04-jeremy-closed-gap-with-smoke-test-script
type: artifact
status: ratified
source: "this chat, 2026-08-04, Jeremy resumed via SendMessage after Jasiah's review (source status: active)"
project: fleet
tags: [anansi, jeremy, jasiah, build-outcome]
supersedes: []
superseded_by: null
---

# Jeremy Closed Jasiah's Flagged Gap With an Automated Red-Green Smoke Test

## Body

Jeremy was resumed with instructions to close the gap Jasiah flagged and built scripts/smoke_test_red_green.py: a red check using a randomized nonsense query at a strict similarity threshold expecting empty results (deliberately not relying on an empty table, since the endpoint's default threshold would return closest matches regardless of relevance), a green capture as one agent, a green reuse from a genuinely different agent, and an independent re-verification querying the database directly rather than trusting the API's response. The script's own six-scenario test harness caught two deliberate anti-gaming failure modes on the first try: a phantom write where the API claims success but nothing lands in the database, and a misattributed reuse event where the consuming agent's name silently matches the writer's.

## Links

- extends: 2026-08-04-jasiah-gate-review-pass-with-conditions
