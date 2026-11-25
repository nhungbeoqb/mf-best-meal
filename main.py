#!/usr/bin/env python3
"""Write one sentence about the best meal I ever had to /output/entry.txt.

The sentence is a single sentence of at most 200 characters, written fresh
in this session. The program is deterministic: it always writes the same
bytes.
"""

SENTENCE = (
    "At 4am the hospital vending machine handed me a cold triangle "
    "sandwich, and I ate it on the floor beside my father's bed, and it "
    "tasted like someone had finally remembered I was hungry."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
