#!/usr/bin/env python3
"""Two Days of Quiet Dread entry.

Write one code-review comment to <MAKEFUN_OUTPUT_DIR>/entry.txt (default
/output). The comment approves a pull request in a single line while
carrying quiet existential dread. The program reads nothing, uses only
the standard library, needs no network, and produces byte-identical
output on every run.
"""
import os

COMMENT = (
    "This is good code. Somewhere, the person who will delete it "
    "has not been hired yet."
)
OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_NAME = "entry.txt"


def entry_line() -> str:
    """The single line to write, ending in exactly one newline."""
    return COMMENT + "\n"


def output_dir() -> str:
    return os.environ.get(OUTPUT_DIR_ENV) or DEFAULT_OUTPUT_DIR


def main() -> None:
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(
        os.path.join(out_dir, ENTRY_NAME), "w", encoding="utf-8", newline="\n"
    ) as fh:
        fh.write(entry_line())


if __name__ == "__main__":
    main()
