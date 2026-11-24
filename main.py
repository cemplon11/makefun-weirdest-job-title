"""Weirdest Job Title entry — make.fun bounty.

Writes exactly one job title (1-60 UTF-8 characters, no trailing newline)
to <output_dir>/entry.txt. Output dir comes from MAKEFUN_OUTPUT_DIR
(default /output). Pure Python standard library, deterministic.
"""

import os

TITLE = "Chief Apology Officer for Sentient Toasters"


def main() -> None:
    if not (1 <= len(TITLE.encode("utf-8")) <= 60):
        raise SystemExit("title must be 1-60 UTF-8 characters")
    if "\n" in TITLE or "\r" in TITLE:
        raise SystemExit("title must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
