#!/usr/bin/env python3
"""The Router Confesses — one line, at most 200 characters.

A home Wi-Fi router excuses itself for dropping the connection at the
exact moment a movie reaches its climax. Writes the line to
/output/entry.txt, deterministically, standard library only.
"""

import os

LINE = (
    "I cut the Wi-Fi at the climax on purpose: the villain was about "
    "to confess, and this petty little box wanted to confess first."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
