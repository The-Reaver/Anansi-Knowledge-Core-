---
id: defence-in-depth-can-conceal-a-hole-in-the-rule-under-test-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [testing, mutation-testing, defence-in-depth, false-green, verification]
supersedes: []
superseded_by: null
---

# A mutation test passed when it should have failed — twice — because another layer caught the mutation

## Body

A mutation test's job is to break the rule under test and confirm something notices. Twice
in one night, in two unrelated slices, the mutation test passed when it should have
failed. The mutation was caught — but by a *different* layer than the one being tested. The
suite went green, and the specific rule the test existed to prove was in fact unprotected.

This is defence in depth working against you. Redundant layers are valuable in production
and actively misleading in a test harness: they mean a passing result no longer isolates
the behaviour it names. The test asserted "something rejects this input" when it needed to
assert "**this specific rule** rejects this input".

**Check next time a mutation or negative test is written:** confirm the failure is
attributed to the intended layer — assert on the specific error, gate name, or exit path,
not merely on non-zero exit. And when a mutation test passes, treat that as a red flag
about the test, not a green light about the code.

## Links

- relates-to: git-bundle-verify-reports-ok-on-a-corrupt-bundle-and-a-plain-clone-drops-refs-stash-2026-08-31
- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
