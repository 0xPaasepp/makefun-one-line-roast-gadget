# One-Line Roast: The Gadget You Use Every Day — entry.
# Writes a single original roast line to /output/entry.txt.
# Standard library only, no network. Output is identical on every run.
# The gate wants 1-200 UTF-8 characters, not only whitespace; the line is
# checked here too so a typo can never ship an invalid entry.
import os

ROAST = "My charger cable only works at one exact angle, so every night I defuse a bomb just to keep my phone alive until morning."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(ROAST) <= 200 and ROAST.strip(), "roast line fails the gate"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
    handle.write(ROAST)
