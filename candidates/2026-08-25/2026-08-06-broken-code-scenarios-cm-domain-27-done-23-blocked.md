---
id: 2026-08-06-broken-code-scenarios-cm-domain-27-done-23-blocked
type: artifact
status: candidate
source: "this chat, 2026-08-04 to 2026-08-06, Augustin curriculum work on the 500 Broken Code Scenarios manual, CM domain (Concurrency and Memory Safety) (source status: active)"
project: fleet
tags: [augustin, curriculum, broken-code-scenarios, concurrency, memory-safety, build-outcome, verified]
supersedes: []
superseded_by: null
---

# Broken Code Scenarios, CM Domain: 27 Built and Verified, 23 GPU/Framework Scenarios Registered as Blocked

## Body

The CM domain (Concurrency and Memory Safety, 50 scenarios) stands at 27 built and verified plus 23 registered as blocked. Every DONE scenario ships four things: a reproduction that demonstrates the real bug, a working fix that passes the reproduction, a regression guard, and a completion card with real captured output. The main session re-ran each scenario's run_tests.sh and only counted it done on exit 0, which is the guard against fabricated results.

Where a language is not buildable in this container, the bug was reframed faithfully into a buildable language and labeled as a reframe, since these defects are language-agnostic. The 27 built: CM-001 ABA on a lock-free stack (C, tagged pointer), CM-002 Rust/C FFI use-after-free (C + valgrind), CM-003 Go goroutine leak, CM-004 C++ double-free (valgrind), CM-005 Java missing-volatile visibility loss, CM-006 OTP supervisor restart storm (Go model), CM-007 Swift actor reentrancy deadlock (Go model), CM-008 Zig SIMD misalignment (C, VMOVAPS SIGSEGV), CM-009 Kotlin coroutine dispatcher loss (native Kotlin), CM-010 TLS destructor ordering UAF (C + valgrind), CM-011 userspace RCU grace period (C), CM-012 GIL-release buffer race (C + valgrind), CM-013 GenServer late cast (Go), CM-014 C# async-void swallow (Java), CM-015 Mojo iterator invalidation (C++ + valgrind), CM-016 Node SharedArrayBuffer torn read, CM-017 Haskell STM starvation (Go), CM-018 Ruby fiber blocking native call (Go), CM-019 OCaml moving-GC FFI UAF (C + valgrind), CM-020 Dart isolate message truncation (Go), CM-021 PHP OPcache stale deploy (Go + real symlinks), CM-022 Lua coroutine yield across C (C + ucontext), CM-023 Perl XS refcount leak (C + valgrind), CM-024 Fortran OpenMP shared-SAVE race (C + OpenMP, TSan), CM-025 Ada priority inversion (C + SCHED_FIFO with priority inheritance), CM-026 SPARK weak postcondition null-deref (C, SIGSEGV), CM-027 WASM memory-growth detach (Node).

The remaining 23 (CM-028 through CM-050) each need a real GPU plus vendor SDK, or a specific ML framework or compiler that is absent with all package registries blocked. Rather than fake a GPU or framework artifact, these were registered with the exact blocker and closest safe substitute. Of them, 8 are truly hardware-bound with no faithful CPU substitute (CM-028, 029, 030, 031, 032, 034, 035, 037), 11 are reframable into a real CPU model on request because the bug is algorithmic and the framework is incidental (CM-036, 039, 040, 042, 043, 044, 045, 046, 047, 049, 050), and 4 are partially reframable at lower fidelity (CM-033, 038, 041, 048).

## Links

- affects: 2026-08-06-broken-code-scenarios-program-status-and-dashboard
