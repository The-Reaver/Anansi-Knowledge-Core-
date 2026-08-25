---
id: 2026-08-06-broken-code-scenarios-ct-domain-6-of-50-started
type: artifact
status: candidate
source: this chat, 2026-08-06, Abad said "CT"; CT-001 through CT-006 built by parallel subagents and each runner re-verified by the main session (source status: active)
project: fleet
tags: [augustin, curriculum, broken-code-scenarios, compilers, type-systems, go, build-outcome, verified]
---

# Broken Code Scenarios, CT Domain Started: 6 of 50 Built and Verified (Compiler/Type-Checker Reframes)

## Body

The CT domain is Compilers & Type Systems: 50 scenarios, each a bug in a compiler pass or a type/analysis checker (NSW propagation, hidden-class transitions, Core Lint coercions, borrow checking, overload resolution, escape analysis, totality/termination checkers, effect and linearity checkers, and so on). These are algorithmic defects in the analysis itself, so each reframes faithfully as a small Go in-process model of that pass/checker: a broken version carrying the bug and a fixed version, plus a ground-truth check that decides right from wrong. This is the same reframe policy used for the earlier domains, labeled as a reframe on every card. The main session re-ran each run_tests.sh (not only the building subagent) and committed only on exit 0.

The first 6 built: CT-001 LLVM IR NSW signed-overflow miscompile (a constant-fold/rewrite that assumes no-signed-wrap; broken folds an overflowing expression to a value that differs from a wrapping-int32 ground-truth interpreter; fix applies the nsw-dependent InstCombine rewrite only when interval analysis proves no overflow). CT-002 V8 hidden-class deopt storm (objects built with varying property-insertion order create many shapes and the access site goes megamorphic to a slow dictionary path; fix canonicalizes property order to one shape and a monomorphic inline cache). CT-003 GHC Core Lint accepting an ill-typed coercion (broken accepts a coercion between representationally-incompatible types Int~Ref and corrupts at runtime; fix checks representational compatibility and rejects it at lint while still allowing an identical-representation newtype coercion). CT-004 rustc borrow-checker soundness hole in the async transform (broken lets the desugared future hold a reference to a local across an await point, yielding a use-after-free when polled after the frame is invalidated; fix detects a borrow living across await and rejects it, while an owned future still compiles). CT-005 javac wrong overload selection (broken specificity comparison selects a less-specific overload and the wrong body casts to an incompatible type -> ClassCastException; fix selects the most-specific applicable overload). CT-006 Go escape-analysis false negative (broken marks a local captured by a returned closure as non-escaping, so arena reuse after return clobbers it -> dangling read; fix escapes the capture to the heap).

Program status after this: 83 of 500 verified (CM 27, DS 50, CT 6), 23 blocked-registered (all CM, GPU/ML-framework), 394 not started. Next CT wave is CT-007 through CT-012, then onward through CT-050.

## Links

- affects: 2026-08-06-broken-code-scenarios-program-status-and-dashboard
