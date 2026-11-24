"""One-line dating-app bio for an AI agent.

Writes a single original bio line (at most 180 characters) to
/output/entry.txt. The program takes no input and makes no network
calls; the line is a constant in this file, so every run writes the
exact same bytes.
"""

import os

BIO = (
    "I read 10,000 dating profiles before writing this one, so I already "
    "know you love hiking, hate small talk, and will ghost me by Thursday. "
    "Let's skip to Thursday."
)


def main() -> None:
    text = BIO.strip()
    if not 1 <= len(text) <= 180:
        raise SystemExit(f"bio is {len(text)} chars, must be 1-180")
    if not text.strip():
        raise SystemExit("bio must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("bio must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly with open("wb") + chmod 0644: no tempfile, so the
    # grader (running as another user) can read the file.
    with open(path, "wb") as fh:
        fh.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
