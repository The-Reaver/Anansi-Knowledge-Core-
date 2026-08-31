---
id: validate-the-measuring-tool-before-trusting-its-aggregate-2026-08-31
type: lesson
status: candidate
source: "Recovery session, 2026-08-31 — own error, caught when three successive measurements of the same property disagreed"
project: fleet
tags: [measurement, verification-discipline, false-green, self-correction, tooling]
supersedes: []
superseded_by: null
---

# Three measurements of the same property disagreed, and every one of them was the tool's fault

## Body

Measuring how many Core notes have no outgoing links produced 15%, then 18%, then 6% — three
different answers about an unchanging corpus. All three were wrong, and none of the errors
was in the data.

The first regex required a link bullet to end at the note id, so any bullet with a trailing
parenthetical was counted as no link at all. Correcting that overshot: the second pattern let
the relation word itself (`relates-to`) match as an id whenever a bullet pointed at a
document rather than a note, so notes with no real links scored as linked. Only a third pass
— resolving each target against the actual id set, and separating the 135 legitimate
references to documents from note-to-note links — gave the true figure: **39%**, matching the
41% already recorded in the Core. The previously recorded number had been right the whole
time; the new measurements were the broken thing.

The damage was not the wrong number, it was the conclusion drawn from it: that an item on the
remediation plan had already improved and could be deprioritised.

**Check before reporting any aggregate:** run the extractor over a handful of cases whose
answer is known by hand and confirm it agrees, before trusting the total. A parser reports
confidently on what it failed to parse, and an aggregate is exactly where individual
misparses become invisible. When a new measurement contradicts a recorded one, the new
measurement is the more likely suspect.

## Links

- relates-to: defence-in-depth-can-conceal-a-hole-in-the-rule-under-test-2026-08-31
- relates-to: git-bundle-verify-reports-ok-on-a-corrupt-bundle-and-a-plain-clone-drops-refs-stash-2026-08-31
- relates-to: the-installed-hook-gate-already-fails-closed-on-zero-declared-hooks-2026-08-31
