#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun bounty entry.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line
written exactly as it was typed, with no explanation after it.

Stdlib only; no network, no dependencies.
"""

import os
import sys

ENTRY = (
    "To: Mara, who still texts me every birthday I stopped answering\n"
    "I still have the apology I typed the night you called and I let it ring, "
    "and every year since I've opened it, fixed one word, and closed it again"
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 260:
        print(f"gate fail: entry is {len(text)} chars, need 1-260",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is blank", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    if len(written.split("\n")) != 2:
        print("gate fail: entry must be exactly two lines", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
