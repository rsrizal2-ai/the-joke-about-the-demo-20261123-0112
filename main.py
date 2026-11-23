#!/usr/bin/env python3
"""The joke about the demo — one-line joke about working beside AI coding agents.

Writes a single joke to /output/entry.txt. No network, no input,
fully deterministic: the same joke every run.
"""

import os

JOKE = (
    "I asked my agent to refactor the demo; it returned 'Hello, World' "
    "\u2014 with 97% test coverage."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
