#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no input, fully deterministic.
"""

import os

JOKE = (
    "My AI coding agent fixed the demo bug live \u2014 "
    "by deleting the feature we were about to demo."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
