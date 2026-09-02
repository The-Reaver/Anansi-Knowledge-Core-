"""Tests for scripts/secret_check.py.

Standalone and pytest-free, matching the fleet's convention: run it directly.

The properties that matter are not "it passes on a clean tree". They are:
  1. it BLOCKS the shapes that are real -- specifically a Stripe live-mode
     prefix, which is the credential the 2026-08-25 fleet rotation never
     looked for and therefore never rotated;
  2. it does NOT block on prose, because this corpus is prose ABOUT
     credentials and a checker that blocks every note gets bypassed;
  3. prose is never SILENT either -- noted every run;
  4. it fails CLOSED when it cannot determine what to scan; and
  5. its vendored pattern set has not drifted from Stag-Fleet's.
"""
from __future__ import annotations

import io
import os
import re
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "scripts"))

import secret_check  # noqa: E402

# Every fixture is assembled at runtime so this file never itself contains the
# pattern it tests for. The fleet has already shipped a fixture that flagged
# itself, and a test that trips the checker teaches everyone to ignore it.
STRIPE_LIVE = "sk" + "_live_" + ("a1b2c3d4e5" * 2) + "f6g7"
ANTHROPIC = "sk-" + "ant-api03-" + ("Xk9" * 30)
SLUG = "sk-" + "curriculum-domains-status-del02-del10-complete"
PROSE_DB = "postgres" + "://user:pass@" + "localhost:5432/db"
# Host deliberately avoids the words _PLACEHOLDER treats as non-real
# ("example", "your", "changeme"): example.com is a reserved documentation
# domain, so a host containing it SHOULD classify as prose.
REAL_DB = "postgres" + "://svcacct:" + "Xq7vNb2LpR8w" + "@prod-db.acmecorp.net:5432/main"


def _scan_one(content: str) -> tuple[list[str], list[str]]:
    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "f.md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(content + "\n")
        blocking, noted, read = secret_check.scan_paths([p])
        assert read == 1, "the fixture file must actually be read"
        return blocking, noted


def run_checks() -> list[str]:
    checks: list[str] = []

    # 1. The one that was missed.
    blocking, _ = _scan_one(STRIPE_LIVE)
    assert blocking and "LIVE-MODE PREFIX" in blocking[0], (
        "a Stripe live-mode key must BLOCK: %r" % blocking
    )
    checks.append("Stripe sk_live_ blocks -- the credential the 2026-08-25 rotation missed")

    # The scanner's own pattern is [rs]k_live_, so it cannot match a test key.
    # Worth asserting: it means every Stripe hit is live-mode by construction.
    blocking, noted = _scan_one("sk" + "_test_" + ("a1b2c3d4e5" * 2) + "f6g7")
    assert not blocking and not noted, (
        "sk_test_ is out of pattern scope entirely; a hit here would mean the "
        "pattern changed and every past Stripe conclusion needs revisiting: %r"
        % (blocking + noted)
    )
    checks.append("sk_test_ does not match -- so any Stripe hit is live-mode by construction")

    # 2. A real key shape blocks.
    blocking, _ = _scan_one(ANTHROPIC)
    assert blocking and "credential-shaped" in blocking[0], (
        "a long-opaque-body key must BLOCK: %r" % blocking
    )
    checks.append("credential-shaped token blocks")

    # 3. Prose does not block -- but is never silent.
    blocking, noted = _scan_one(SLUG)
    assert not blocking, "a kebab-case slug must not block: %r" % blocking
    assert noted and "prose/slug" in noted[0], "prose must still be NOTED: %r" % noted
    checks.append("kebab-case slug is noted, not blocking")

    blocking, noted = _scan_one(PROSE_DB)
    assert not blocking, "a placeholder DB string must not block: %r" % blocking
    assert noted, "a placeholder DB string must still be noted"
    checks.append("placeholder DB string is noted, not blocking")

    # 4. A DB string to real-looking infrastructure with opaque credentials blocks.
    blocking, _ = _scan_one(REAL_DB)
    assert blocking and "credential-shaped" in blocking[0], (
        "a DB string to a real host with an opaque password must BLOCK: %r" % blocking
    )
    checks.append("real-looking DB string blocks")

    blocking, noted = _scan_one(
        "postgres" + "://svcacct:" + "Xq7vNb2LpR8w" + "@prod-db.example.com:5432/main"
    )
    assert not blocking, (
        "example.com is a reserved documentation domain -- a DB string pointing "
        "at it is illustration, not infrastructure: %r" % blocking
    )
    assert noted, "it must still be noted"
    checks.append("reserved documentation domain classifies as prose, not a credential")

    # 5. Undeterminable scope fails CLOSED, never quietly clean.
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        try:
            os.chdir(tmp)  # not a git repo, so staged_paths() cannot resolve
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc = secret_check.main([])
            assert rc == 1, "an undeterminable scope must fail closed, got %d" % rc
            assert "Failing closed" in buf.getvalue(), buf.getvalue()
        finally:
            os.chdir(cwd)
    checks.append("undeterminable scope fails CLOSED")

    # 6. A PASS always states its scope. A bare PASS hides a zero-file run.
    with tempfile.TemporaryDirectory() as tmp:
        blocking, noted, read = secret_check.scan_paths([])
        assert (blocking, noted, read) == ([], [], 0)
    buf = io.StringIO()
    with redirect_stdout(buf):
        secret_check.main(["--all"])
    out = buf.getvalue()
    assert "file(s) read" in out, "a PASS must state how much it read: %r" % out
    checks.append("output always states its own scope")

    # 7. Drift. The patterns are vendored on purpose -- the Core is cloned
    #    alone -- so divergence must be detected, not trusted.
    fleet = "/home/user/stag-fleet/security/secret_scan.py"
    if os.path.exists(fleet):
        sys.path.insert(0, "/home/user/stag-fleet")
        from security.secret_scan import SECRET_PATTERNS as FLEET  # noqa: E402
        ours = {k: p.pattern for k, p in secret_check.SECRET_PATTERNS.items()}
        theirs = {k: p.pattern for k, p in FLEET.items()}
        assert ours == theirs, (
            "vendored patterns have drifted from Stag-Fleet's. Missing here: %r; "
            "extra here: %r; differing: %r"
            % (
                sorted(set(theirs) - set(ours)),
                sorted(set(ours) - set(theirs)),
                sorted(k for k in set(ours) & set(theirs) if ours[k] != theirs[k]),
            )
        )
        checks.append("vendored patterns match Stag-Fleet's exactly")
    else:
        checks.append("drift check SKIPPED -- Stag-Fleet not present beside this clone")

    return checks


if __name__ == "__main__":
    try:
        results = run_checks()
    except AssertionError as e:
        print("FAIL test_secret_check: %s" % e)
        sys.exit(1)
    for c in results:
        print("  ok  %s" % c)
    print("PASS test_secret_check: %d/%d" % (len(results), len(results)))
