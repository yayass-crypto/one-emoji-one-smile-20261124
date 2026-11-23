#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji, and nothing else, to /output/entry.txt.

The chosen emoji: U+1F601 BEAMING FACE WITH SMILING EYES.
A broad, crinkle-eyed grin: the warmest first-glance smile a stranger
can read, joyful without intimacy, universal, and a deliberate pick
rather than the first default smiley.

Standard library only. Deterministic: the same bytes every run.
"""

import os
import sys

EMOJI = "\U0001F601"  # BEAMING FACE WITH SMILING EYES


def _out_dir():
    """Where the entry goes: the harness dir, /output, or local out/."""
    d = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if d:
        return d
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return "out"


def main():
    out_dir = _out_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = EMOJI.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify what was written: exactly one emoji, no newline, valid UTF-8.
    with open(path, "rb") as f:
        back = f.read()
    text = back.decode("utf-8")
    assert back == data, "bytes differ from the chosen emoji"
    assert len(text) == 1, "entry must be exactly one character"
    assert not text.isspace(), "entry must not be only whitespace"
    # No trailing newline, no extra bytes: the gate allows 1-8 chars,
    # and the brief wants exactly one emoji and nothing else.
    assert b"\n" not in back and b"\r" not in back, "no newline allowed"
    print(f"wrote {len(back)} bytes ({len(text)} char) to {path}: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
