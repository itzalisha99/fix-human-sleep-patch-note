#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes announcing that human sleep is fixed.
Standard library only; deterministic output.
"""

import os

ENTRY = "Fixed a bug where users woke up at 3 a.m. to review every decision they made since 2011."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-160 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > 160:
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")  # raises if not valid UTF-8
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry fails the bounty gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file is byte-identical to the entry.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit("written entry does not match")


if __name__ == "__main__":
    main()
