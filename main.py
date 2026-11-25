#!/usr/bin/env python3
"""Laugh Track entry: write one crypto-trading joke to /output/entry.txt.

Stdlib only, fully deterministic: the same single-line joke every run.
The joke is one line, well under the 200-character cap the contest sets.
"""

import os

JOKE = (
    "I bought the dip, averaged down twice, and now my group chat calls me "
    "'the dip' \u2014 my bags only pump the week after I sell."
)

MAX_CHARS = 200


def output_dir() -> str:
    """Where the grader wants the entry: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
