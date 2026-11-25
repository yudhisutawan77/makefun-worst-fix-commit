#!/usr/bin/env python3
"""Write the worst-fix-ever commit message to the entry file.

Reads MAKEFUN_OUTPUT_DIR (default /output); if it names a file, write
there, otherwise write entry.txt inside it.
"""

import os
import sys

ENTRY = "fix: users losing data by deleting the users"

def resolve_output_path():
    out = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("ENTRY_OUT")
        or "/output"
    )
    if out.endswith(".txt") or os.path.isfile(out):
        return out
    return os.path.join(out, "entry.txt")


def main():
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
