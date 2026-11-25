#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph of famous last words to
/output/entry.txt. Deterministic: every run writes the exact same bytes.
Standard library only; no network access.

The line is built as dying speech in the first person: the speaker's
actual last words are the reckless dare "hold my beer", and the twist
lands in the second sentence, where the tombstone itself turns out to
be the receipt for that dare. One read, one joke, no explanation, and
short enough to picture carved in stone.
"""

import os

LAST_WORDS = "hold my beer"
PUNCHLINE = "This stone is the receipt."

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Compose the epitaph: the dare, then the stone's verdict on it."""
    text = "My last words were '%s.' %s" % (LAST_WORDS, PUNCHLINE)
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 150, "entry must be 1-150 characters"
    return text


def main() -> None:
    text = build_entry().strip()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
