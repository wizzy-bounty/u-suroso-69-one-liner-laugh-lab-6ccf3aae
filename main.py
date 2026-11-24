#!/usr/bin/env python3
"""One-Liner Laugh Lab — entry for u-suroso-69-one-liner-laugh-lab-6ccf3aae.

Writes a single short funny line — the excuse a robot vacuum gives
after eating a sock — to /output/entry.txt.

Deterministic, standard library only, no network.
"""

import os

LINE = "It wasn't a meal, it was a merger. The sock is now middle management in my dustbin."


def validate_line(text: str) -> None:
    """Validate the one-liner before it is written.

    Checks: (a) total length including the trailing newline is 1-200 chars,
    (b) exactly one line (no newline inside the text),
    (c) not whitespace-only. Raises ValueError with a clear message on failure.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line (no newline inside the text)")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) + 1 <= 200:
        raise ValueError(f"entry length including newline must be 1-200 chars, got {len(text) + 1}")


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
