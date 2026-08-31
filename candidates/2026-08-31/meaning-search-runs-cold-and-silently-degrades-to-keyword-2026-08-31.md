---
id: meaning-search-runs-cold-and-silently-degrades-to-keyword-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) capability audit, 2026-08-31 — relayed by the operator into a recovery session; observed on the operator machine and NOT independently re-verified here"
project: fleet
tags: [knowledge-core, retrieval, embeddings, silent-degradation, anansi]
supersedes: []
superseded_by: null
---

# The Core's meaning-search was cold on every use and fell back to keyword without saying so

## Body

Every meaning-search against the Knowledge Core in a full working session found embeddings
cold and silently degraded to keyword matching. The queries returned results, so nothing
looked wrong — but the retrieval was lexical, and a Zettelkasten's whole value is matching on
meaning rather than wording.

This is a false green with unusually wide blast radius. The fleet's standing rule is "recall
before you guess", so every session that consulted the Core during that period believed it had
searched by meaning and had not. Any "the Core doesn't have this" conclusion drawn then is
unsafe: a note phrased differently from the query would simply not have surfaced.

**The fix is to warm embeddings in the SessionStart hook, not merely to start the hub** — and,
more importantly, to make the fallback **loud**. A degraded search that announces itself costs
one line of output; a silent one costs every conclusion drawn from it.

**Check next time a search layer has a fallback path:** the fallback must be visible in the
result, not just in a log. Silent degradation to a weaker mode is indistinguishable from
correct operation, which is precisely what makes it expensive.

## Links

- relates-to: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
- relates-to: validate-the-measuring-tool-before-trusting-its-aggregate-2026-08-31
