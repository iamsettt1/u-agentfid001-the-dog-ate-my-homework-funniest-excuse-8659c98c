#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, of the excuse a dog gives after
being caught eating the homework, in the dog's own voice.

The dog is not sorry. The homework was stressing its human out, so the
dog removed the problem the only way a dog knows how -- and expects
thanks for it.
"""

import os

LINE = "It was stressing you out, so I removed the problem. You're welcome."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only whitespace, on a single line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() and "\n" not in LINE, "line must be a single non-blank line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
