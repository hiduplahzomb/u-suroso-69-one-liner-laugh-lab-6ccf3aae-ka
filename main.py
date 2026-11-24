#!/usr/bin/env python3
"""One-Liner Laugh Lab.

Writes one original sentence to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock, reported as a completed system
event. The humor comes from the fields, not from a sentence: a job
ID, a detection time, a suction reading, an intake percentage, and a
closed status code — the sock is gone, the floor is clean, and the
vacuum rates the meal delicious. Numbers first, status last.
"""

import os
import sys

TEXT = (
    "clean #2147: sock detected 09:12, suction 2400 Pa, intake "
    "100% blocked — sock consumed, floor 98% clean. status: delicious."
)


def main() -> int:
    # Gate: 1 to 200 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        print("entry text fails the 1-200 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # the program claims to have written.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
