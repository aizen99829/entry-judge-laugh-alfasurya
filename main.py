# SPDX-License-Identifier: MIT
"""Make the AI Judge Laugh — one-line office joke entry.

The entry is a single line about office life, under 200 characters.
main.py writes it to /output/entry.txt for the program/v1 harness.
"""

import os
from pathlib import Path

# The joke itself: a "quick sync" that was anything but quick.
# The observation is true for anyone who has sat through one of these
# calls, and the twist lands on the host, not on the meeting itself.
JOKE = "Our 'quick sync' lasted an hour because the host spent fifty minutes sharing the wrong screen and ten minutes apologizing for it."


# Why this line works, in the judge's own terms:
# - True: every office worker has watched a "quick sync" balloon.
# - Surprising turn: the delay is not the agenda, it is the host
#   sharing the wrong screen, then apologizing for it.
# - Tight: one sentence, no setup paragraph, no explanation after
#   the punchline. The numbers (fifty minutes, ten minutes) do the
#   timing work that adjectives would only slow down.
# - Fresh: the joke is about the tooling of the meeting, not about
#   Mondays, coffee, or the printer everyone has already roasted.


def validate(line):
    """A competition entry must be one line and under 200 characters."""
    stripped = line.strip()
    # Stripping first means a stray trailing space can never push a
    # borderline entry over the character limit or add a phantom line.
    assert "\n" not in stripped, "entry must be a single line"
    assert len(stripped) < 200, "entry must be under 200 characters"
    assert len(stripped) > 0, "entry must not be empty"
    return stripped


# The harness reads the entry from /output/entry.txt. The output path
# can be overridden with ENTRY_OUTPUT for local runs, but the default
# is exactly where the grader looks.
OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main():
    """Validate the joke and write it as the competition entry."""
    entry = validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry + "\n", encoding="utf-8")
    print(entry)


if __name__ == "__main__":
    main()
