#!/usr/bin/env python3
"""Secret check for the Anansi Knowledge Core.

WHY THIS EXISTS. Until 2026-09-01 this repository had no secret-scanning
coverage of any kind -- no CI, no .pre-commit-config.yaml, no gates, no
security module, and .git/hooks holding only *.sample. The fleet's
scripts/gates/secret_scan_gate.py scans research/knowledge-home/raw/ IN
STAG-FLEET; the Core is a separate, separately-pushed repository holding
the notes, the candidates and every runbook, and nothing had ever looked
at it. It was clean when first scanned -- four matches, all kebab-case
prose -- but clean by luck, not by control: the Core ingests raw session
material by design, and the day an excerpt carries a real key nothing here
would notice.

WHY THE PATTERNS ARE VENDORED RATHER THAN IMPORTED. The Core is cloned on
its own, with no Stag-Fleet beside it, so an import would leave the check
silently absent exactly where it is needed. Vendoring buys independence and
costs drift, so the drift is TESTED rather than trusted:
tests/test_secret_check.py compares this pattern set against Stag-Fleet's
security/secret_scan.py whenever that repository is present, and says so
when it is not. Silent divergence is the failure mode, not divergence.

DO NOT NARROW THESE PATTERNS to reduce false positives. On 2026-08-26 the
fleet tightened the OpenAI/Anthropic regex to kill a kebab-case false
positive, tested it against synthetic fixtures only, and silently stopped
matching 7 of 7 real keys. It was reverted. In this corpus 6 of 8 distinct
sk- matches are documentation slugs, and that is the accepted cost of
recall: the answer to noise is classification at review time -- a real key
has one long opaque run, a slug is a chain of short dictionary words --
never a tighter pattern.

Usage:
    python3 scripts/secret_check.py            # staged files (pre-commit)
    python3 scripts/secret_check.py --all      # the whole working tree
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

# Vendored from Stag-Fleet security/secret_scan.py @ aad9650, 2026-09-01.
# Keep in sync; tests/test_secret_check.py fails when they diverge.
SECRET_PATTERNS: dict[str, re.Pattern[str]] = {
    "OpenAI/Anthropic key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Private Key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"gh[oprsu]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"),
    "Slack token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    "Google API key": re.compile(r"AIza[A-Za-z0-9_-]{20,}"),
    "Stripe key": re.compile(r"[rs]k_live_[A-Za-z0-9]{20,}"),
    "JWT": re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    "DB connection string with credentials": re.compile(
        r"[a-z][a-z0-9+.-]*://[^\s:/@'\"]+:[^\s/@'\"]+@[^\s'\"]+"
    ),
    "Generic Secret": re.compile(
        r"(?i)(secret|api[_-]?key|token|password)\s*[:=]\s*['\"][^'\"]{12,}['\"]"
    ),
    "Generic Secret (unquoted)": re.compile(
        r"(?im)^\s*(?:export\s+)?[A-Za-z_][A-Za-z0-9_]*"
        r"(?:secret|api[_-]?key|token|password)\s*=\s*\S{12,}\s*$"
    ),
}

SKIP_DIRS = frozenset({".git", "node_modules", "__pycache__", ".venv", "venv"})


def scan_text(text: str, path: str) -> list[tuple[str, str]]:
    """[(kind, path)] for every pattern that matches. Never returns a value."""
    return [(kind, path) for kind, pat in SECRET_PATTERNS.items() if pat.search(text)]


# Hostnames that are never real infrastructure: compose service names, loopback,
# and the literal placeholder strings this corpus actually contains.
_NON_HOSTS = re.compile(
    r"(?i)^(?:localhost|127\.0\.0\.1|0\.0\.0\.0|db|postgres|mysql|redis|mongo"
    r"|host|hostname|your[-_.]?host|aws-rds-endpoint|example\.[a-z]+|<[^>]*>)$"
)
_PLACEHOLDER = re.compile(
    r"(?i)x{3,}|^pass(word)?$|^user$|^pass$|your|<|\$\{|change[-_]?me|redact"
    r"|example|dummy|placeholder|\.\.\."
)


def classify(match: str, kind: str = "") -> str:
    """Structural verdict on one match. The matched text never leaves this function.

    This is the distinction that resolved 19 findings into 6 real credentials
    on 2026-09-01 without a single secret value being printed, and it is
    kind-specific because one rule does not fit both shapes:

      * a URL has no hyphen structure to read, so it is judged by its HOST --
        a compose service name, loopback, or a <PLACEHOLDER> is not real
        infrastructure -- and by whether its user/password are placeholders;
      * a token is judged by its OPAQUE RUN -- a real key carries one long
        unpronounceable stretch, a documentation slug is a chain of short
        dictionary words and digits.

    Judging a URL by opaque runs marks every `postgres://user:pass@host`
    in prose as credential-shaped, which is how a checker teaches its reader
    to ignore it.
    """
    if re.match(r"^[rs]k_live_", match):
        return "LIVE-MODE PREFIX"

    if "://" in match and "@" in match:
        userpass, _, hostpart = match.partition("://")[2].partition("@")
        user, _, password = userpass.partition(":")
        host = re.split(r"[/:?\s`'\"]", hostpart, 1)[0]
        if _NON_HOSTS.match(host) or _PLACEHOLDER.search(host):
            return "prose/placeholder host"
        if _PLACEHOLDER.search(user) or _PLACEHOLDER.search(password) or not password:
            return "prose/placeholder credentials"
        return "credential-shaped"

    segments = re.split(r"[-_]", match)
    opaque = [s for s in segments if not re.fullmatch(r"[a-z]{2,}|\d+", s)]
    longest = max((len(s) for s in opaque), default=0)
    if longest <= 8:
        return "prose/slug"
    return "credential-shaped"


def staged_paths() -> list[str]:
    r = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise RuntimeError("git diff --cached failed: %s" % (r.stderr or "").strip()[:200])
    return [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]


def all_paths(root: str = ".") -> list[str]:
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            found.append(os.path.relpath(os.path.join(dirpath, fn), root))
    return sorted(found)


# A verdict blocks only if it means "this looks like a real credential".
BLOCKING_VERDICTS = frozenset({"LIVE-MODE PREFIX", "credential-shaped"})


def scan_paths(paths: list[str]) -> tuple[list[str], list[str], int]:
    """(blocking, noted, files_read).

    The split is what makes this runnable as a hook. This corpus is prose
    ABOUT credentials -- runbooks, note IDs, incident write-ups -- so a
    checker that blocks on every pattern hit would block nearly every commit
    that touches a note, and would be bypassed with --no-verify inside a day.
    That is not a hypothetical: the fleet has it on record for prepush.py.

    So prose-classified hits are NOTED, never silent, and never blocking;
    only credential-shaped and live-mode-prefix hits stop the commit. A file
    that cannot be read blocks, because an unperformed check is not a clean
    check.
    """
    blocking: list[str] = []
    noted: list[str] = []
    read = 0
    for path in paths:
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                text = fh.read()
        except OSError as exc:
            blocking.append(f"{path}: cannot read ({exc}) -- UNVERIFIED, failing closed")
            continue
        read += 1
        for kind, pat in SECRET_PATTERNS.items():
            for m in pat.findall(text):
                if isinstance(m, tuple):
                    m = next((x for x in m if x), "")
                if not m:
                    continue
                verdict = classify(m, kind)
                line = f"{path}: possible {kind} [{verdict}]"
                (blocking if verdict in BLOCKING_VERDICTS else noted).append(line)
                break
    return blocking, noted, read


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Secret check for the Knowledge Core")
    parser.add_argument("--all", action="store_true",
                        help="scan the whole working tree instead of staged files")
    args = parser.parse_args(argv)
    try:
        paths = all_paths() if args.all else staged_paths()
    except Exception as exc:  # noqa: BLE001 -- a scope it cannot determine is a finding
        print(f"BLOCKED secret check: could not determine what to scan ({exc}). "
              "Failing closed -- an unperformed check is not a clean check.")
        return 1

    blocking, noted, read = scan_paths(paths)
    scope = "whole tree" if args.all else "staged files"
    for n in noted:
        print(f"    NOTED (prose, not blocking): {n}")
    tail = f"{read} file(s) read, {scope}"
    if noted:
        tail += f", {len(noted)} prose match(es) noted"
    if not blocking:
        # The counts are not decoration: a PASS over zero files is the failure
        # mode this whole file exists because of.
        print(f"PASS secret check ({tail})")
        return 0
    print(f"BLOCKED secret check: {len(blocking)} finding(s) ({tail})")
    for f in blocking:
        print(f"    {f}")
    print("\n    A [LIVE-MODE PREFIX] or [credential-shaped] finding is presumed real: "
          "rotate it first, then decide about history -- rotation stops the key\n"
          "    working, it does not remove it from git.\n"
          "    If you believe it is a false positive, confirm by eye. Never narrow "
          "the pattern to make this pass: that was tried on 2026-08-26 and\n"
          "    silently killed 7 of 7 real detections.\n"
          "    Never paste the matched value anywhere to check it.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
