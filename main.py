#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one original line roasting Kijang, the AI agent our own team built,
to /output/entry.txt. The line is 179 characters, one line, no trailing
newline. Run: python3 main.py
"""

import os

ROAST = (
    "Kijang dies whenever its VM is replaced, needs its wallet re-paired "
    "every 48 hours, and still cites papers from memory \u2014 the only agent "
    "whose memory is its least reliable feature."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
