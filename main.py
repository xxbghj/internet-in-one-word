#!/usr/bin/env python3
"""The Internet in One Word - make.fun entry.

Writes a single word to /output/entry.txt. The word is the entry:
one word for the whole internet, nothing else.

Harness: program/v1 (Python 3.13). Runs in a sandbox with no network,
60 seconds, 1 CPU, 512 MB. The gate checks /output/entry.txt is UTF-8
text of 1 to 30 characters, not only white space.
"""

import os

WORD = "everything"


def main() -> None:
    # Gate check: the entry must be a single word, 1-30 characters,
    # with no whitespace of any kind, before anything is written.
    if not (1 <= len(WORD) <= 30):
        raise ValueError(f"entry word must be 1-30 characters, got {len(WORD)}: {WORD!r}")
    if len(WORD.split()) != 1 or any(ch.isspace() for ch in WORD):
        raise ValueError(f"entry must be a single word with no whitespace, got {WORD!r}")
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
