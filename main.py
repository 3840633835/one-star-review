#!/usr/bin/env python3
"""One-star review of something essential — entry program for make.fun.

Writes the one-line entry (a deadpan one-star review of sleep, 159
characters, under the 160-character gate) to ``<output>/entry.txt``
and prints it. Standard library only, no network, no randomness, no
clock: the same bytes come out on every run.

The grader runs this as ``python3 -P -s /bot/main.py`` and reads
``/output/entry.txt``; ``MAKEFUN_OUTPUT_DIR`` (used by the local test)
overrides the output directory, default ``/output``.
"""

import os
import sys

# The entry, byte-identical to entry.txt in this repository.
# A real complaint filed in earnest against a thing that cannot be
# fixed: sleep is paid eight hours a night and returns four hours of
# ceiling-staring plus a 3 a.m. replay of an embarrassment from 2014.
ENTRY = "One star. I give sleep eight hours a night and it pays me back in four hours of staring at the ceiling and a 3 a.m. memory of something embarrassing from 2014."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 160):
        raise SystemExit("entry must be 1 to 160 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone (0644), never the 0600 a temp file gets.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
