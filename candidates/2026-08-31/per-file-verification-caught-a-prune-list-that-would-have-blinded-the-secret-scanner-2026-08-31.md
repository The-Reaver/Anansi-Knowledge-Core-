---
id: per-file-verification-caught-a-prune-list-that-would-have-blinded-the-secret-scanner-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [security, secret-scanning, review, sdlc-split, verification]
supersedes: []
superseded_by: null
---

# A cleanup prune list proposed deleting two files holding real keys — only per-file verification caught it

## Body

A proposed prune list — files identified as dead and safe to remove — included two files
that held real API keys. Removing them would not have leaked anything by itself; the harm
is subtler and worse. Those files were part of what the secret scanner had visibility
into. Pruning them would have removed the evidence, leaving the scanner reporting clean
over a repository whose secrets had simply moved out of its view.

The list was caught by verifying every file on it individually, rather than sampling or
trusting the heuristic that produced it. Nothing about the list looked wrong in aggregate.

**Check next time a bulk deletion, prune, or cleanup list is generated:** verify every
entry individually before acting, and specifically ask whether removing an entry changes
what any scanner or gate can see. A cleanup that shrinks a security control's input set is
a security change wearing a maintenance disguise. Note also that this was caught by the
review seat, not the implementation seat — an argument the SDLC split is earning its cost.

## Links

- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
