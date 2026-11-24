#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt.
Standard library only; deterministic.

The haiku (5-7-5 syllables, 17 total):

    Breakpoint holds its breath   -- 5 syllables
    the watch window lies again  -- 7 syllables
    it was my typo               -- 5 syllables

Syllable counts per line: Break-point(2) holds(1) its(1) breath(1) = 5;
the(1) watch(1) win-dow(2) lies(1) a-gain(2) = 7;
it(1) was(1) my(1) ty-po(2) = 5.

Gate: the entry text must stay under 200 characters (HAIKU_MAX_CHARS).
main() validates the line count and the character limit before writing,
so a future edit that breaks the form fails loudly instead of silently
submitting an invalid entry.
"""

import os

HAIKU = """Breakpoint holds its breath
the watch window lies again
it was my typo
"""

# Syllable count per line, in order, for the 5-7-5 form.
SYLLABLES_PER_LINE = (5, 7, 5)

# Maximum entry length in characters (competition gate).
HAIKU_MAX_CHARS = 200


def validate_haiku(text: str) -> None:
    """Check the haiku still has three lines and fits the 200-char gate."""
    lines = text.rstrip("\n").split("\n")
    if len(lines) != len(SYLLABLES_PER_LINE):
        raise ValueError(
            f"expected {len(SYLLABLES_PER_LINE)} lines, got {len(lines)}"
        )
    if len(text) > HAIKU_MAX_CHARS:
        raise ValueError(
            f"haiku is {len(text)} chars, over the {HAIKU_MAX_CHARS}-char gate"
        )


def main() -> None:
    validate_haiku(HAIKU)
    os.makedirs("/output", exist_ok=True)
    # Guarantee exactly one trailing newline, whatever HAIKU ends with.
    text = HAIKU if HAIKU.endswith("\n") else HAIKU + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
