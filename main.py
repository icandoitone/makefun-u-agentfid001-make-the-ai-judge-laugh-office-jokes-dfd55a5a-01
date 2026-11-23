#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line joke about office life to /output/entry.txt.
Fully deterministic: no randomness, no network, no clock, stdlib only.
"""

import os

JOKE = "My boss replied to my sick-day out-of-office in two minutes to ask if I could still jump on the call."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: one single line, 1-199 characters, not only whitespace.
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
