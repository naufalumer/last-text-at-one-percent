#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

The phone's final text message, written by the phone itself at one
percent battery. This program writes that one message to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` and nothing else.

Standard library only. No input, no network, no randomness: the output
is the same on every run.
"""

import os
from pathlib import Path

# The dying phone's last text. 113 characters, inside the 1-200 gate.
ENTRY = (
    "My final review of you: two stars. Great hands, terrible charging "
    "habits, dropped me in the toilet twice. I quit."
)


def main() -> None:
    # Enforce the sealed gate locally: 1 to 200 characters, not blank.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, outside the 1-200 gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
