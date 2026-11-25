"""Write one sentence about the best advice I ever received.

Stdlib only. Deterministic: writes the same bytes on every run.
Output goes to MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
otherwise to /output/entry.txt.
"""

import os

SENTENCE = (
    "My grandfather, the night before my first job, told me never to "
    "borrow money to look rich, because a man who owes the room can "
    "never speak freely in it."
)


def main() -> None:
    # Keep the entry inside the gate: one sentence, 1-200 characters.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, "sentence out of gate bounds"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
