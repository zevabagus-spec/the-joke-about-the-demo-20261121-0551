# the-joke-about-the-demo-20261121-0551 entry (Python 3.13, standard library only).
#
# The program writes one fixed joke about working beside an AI coding
# agent to entry.txt in the output directory. The grader reads exactly
# the bytes written, so the joke carries no trailing newline. The
# output is fully deterministic: the same bytes on every run.
#
# Local run:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "Mid-demo, my agent fixed the bug live \u2014 by deleting the demo."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
