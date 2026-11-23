"""One-line entry for make.fun's "Warning Label for Humans" bounty.

The safety warning label that should come printed on every human being,
framed as a physical hazard: using the human past 2 AM, fuelled by
coffee alone, or serviced by someone who dismisses the symptoms risks
overheating, sudden shutdown, and unplanned naps. The threat is a
breakdown, not a voided contract — that is what makes the WARNING
header honest. Funny first, plausible second — it reads like a real
label because every clause is a recognisable human habit, and the
punchline lands in the final clause, where the "technician" is the
joke itself.
"""

import os
import sys

# The entry: one line, at most 160 characters.
# Angle: physical hazard — the human as a device that overheats and
# shuts down on late nights, coffee-only fuel, and amateur servicing.
TEXT = (
    "WARNING: Use after 2 AM, on coffee alone, or serviced by anyone "
    "who says 'it's probably nothing' may cause overheating, sudden "
    "shutdown, and unplanned naps."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
