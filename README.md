# The joke about the demo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-brightgreen.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)

Entry for the [make.fun bounty "The joke about the demo"](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112) — a one-line joke about working beside AI coding agents.

## The joke

> I asked my agent to refactor the demo; it returned 'Hello, World' — with 97% test coverage.

## How it works

`main.py` (Python 3.13) writes that single line to `/output/entry.txt`. No network, no input, fully deterministic.

```sh
python3 main.py
cat /output/entry.txt
```
