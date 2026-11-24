#!/usr/bin/env python3
"""One-Liner Laugh Lab — entry for u-suroso-69-one-liner-laugh-lab-6ccf3aae.

Writes a single short funny line — the excuse a robot vacuum gives
after eating a sock — to /output/entry.txt.

Deterministic, standard library only, no network.
"""

import os

LINE = "It wasn't a meal, it was a merger. The sock is now middle management in my dustbin."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
