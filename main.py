#!/usr/bin/env python3
"""Write the challenger one-line joke to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness, no input.
"""

import os

JOKE = "When the demo crashed, my agent narrated it as the big reveal \u2014 the audience applauded, and now the crash is on the roadmap."


def main() -> None:
    # The joke is one line: the agent narrates the crash as the reveal.
    # No trailing newline: the file holds the joke text exactly.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
