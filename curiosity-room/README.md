# The Curiosity Room

Generates and holds genuinely open, unresolved, worth-investigating questions. Its only job is
to keep a live queue of curiosities — it does not answer them. That is the Solutions Room's job,
one folder over.

## Where curiosities come from

- Gaps noticed in ratified `notes/` — a claim with no citation, a decision with an unanswered
  "what does this concretely mean" tail, a `type: question` note nobody has picked up.
- Unresolved threads inside the 2x2 research program and future research batches.
- New questions the Solutions Room surfaces while it works a curiosity — solving one thing
  legitimately opens another; that new question comes back here, not straight into a solution.

## Queue format

Every entry in `queue/` is one curiosity, one file, using `template-curiosity-entry.md`. Filename:
`<date>-<slug>.md`.

## The loop

```
curiosity-room/queue/  --[Solutions Room reads]-->  solutions-room/queue/
        ^                                                    |
        |                                                    |
        +---------- new curiosities surfaced while solving --+
```

Claimed curiosities move to `curiosity-room/claimed/` (not deleted — the trail of what prompted
what is part of the record) with a link to the solution entry that answered them.

## Status

Both rooms produce **candidate** material only, same as everything in `candidates/`. Nothing
here is ratified until the operator's pass. See `../notes/2026-08-25-curiosity-solutions-room-spec.md`
for the full design and `../notes/2026-08-08-curiosity-and-solutions-room-proposal.md` for the
proposal this implements.
