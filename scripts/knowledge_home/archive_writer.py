"""Append-only writer for Anansi's raw session-transcript archive.

See docs/adr/0005-two-store-memory-archive-and-core.md. Each session gets
one JSONL file under raw/<date>-<slug>.jsonl. Every call to append_turn()
adds exactly one line and never rewrites a line that already exists — the
file is the literal, unedited record a distilled note in notes/ can always
be checked against.
"""

import json
import os


def append_turn(archive_path, ts, role, text, tool_calls=None):
    """Append one conversational turn to the archive as a single JSON line.

    Returns the 1-indexed line number the turn was written to. Only ever
    opens archive_path in append mode — never "w", never truncates or
    rewrites an existing line.
    """
    line_number = _count_lines(archive_path) + 1
    record = {
        "line": line_number,
        "ts": ts,
        "role": role,
        "text": text,
    }
    if tool_calls is not None:
        record["tool_calls"] = tool_calls

    directory = os.path.dirname(archive_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(archive_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    return line_number


def read_raw_lines(archive_path):
    """Return the list of already-written turn records, in order.

    Returns an empty list if the archive doesn't exist yet.
    """
    if not os.path.exists(archive_path):
        return []
    with open(archive_path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def verify_prefix_unchanged(archive_path, expected_lines):
    """Confirm no previously-written line in the archive has been altered.

    expected_lines is the list previously returned by read_raw_lines() (or
    a prefix of it), captured before doing further work. Raises ValueError
    naming the first mismatched line if the archive's current prefix no
    longer matches; returns True otherwise.
    """
    current = read_raw_lines(archive_path)
    for i, expected in enumerate(expected_lines):
        if i >= len(current) or current[i] != expected:
            raise ValueError(
                f"Archive prefix changed at line {i + 1} in {archive_path} "
                "— the raw archive must never be edited after the fact."
            )
    return True


def _count_lines(archive_path):
    if not os.path.exists(archive_path):
        return 0
    with open(archive_path, "r", encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())
