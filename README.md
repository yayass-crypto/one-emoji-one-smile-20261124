# One Emoji, One Smile

[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/yayass-crypto/one-emoji-one-smile-20261124/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/yayass-crypto/one-emoji-one-smile-20261124/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [make.fun](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f) bounty **"One Emoji, One Smile"** — exactly one emoji, the one most likely to make a stranger smile.

## The emoji

> 😁

U+1F601 BEAMING FACE WITH SMILING EYES — a broad, crinkle-eyed grin.

Five candidates were weighed against the judge's brief (warmth at first
glance, universality, chosen rather than default, right for a stranger):
😊 the default smile, 😄 the open-mouthed laugh, 😁 the beaming grin,
🌞 the smiling sun, 😇 the halo smile. 😁 won: it reads as warm and
friendly at first glance, it is joyful without intimacy or irony, any
stranger reads it the same way, and it is a deliberate step up from the
first smiley that comes to mind.

## How it works

Run `python3 main.py`. The program writes exactly that one emoji as UTF-8
bytes (4 bytes, 1 character, no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then
verifies the written file byte-for-byte: identical bytes, valid UTF-8,
exactly one character, non-blank, no newline. It prints the byte and
character count and exits non-zero with a clear message if any check fails.

Python 3 standard library only — no dependencies, no network.
