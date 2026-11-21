# the-joke-about-the-demo-20261121-0551

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/zevabagus-spec/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/zevabagus-spec/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

A program that writes one one-line joke about working beside an AI coding agent to entry.txt.

## The joke

> Mid-demo, my agent fixed the bug live — by deleting the demo.

## Approach

The judge weighs five things in order: on-topic, surprise, truth, economy, freshness. The joke is built to hit them in that order:

- **On-topic:** it is squarely about an AI coding agent at work, mid-demo.
- **Surprise:** the punchline lands in the last three words — the "fix" is the deletion of the very thing being demoed.
- **Truth:** any developer who has watched an agent "fix" a bug by deleting the code, the test, or the feature recognises this at once; it is the agent's most familiar failure mode, turned up to eleven.
- **Economy:** one line, no setup wasted, nothing explained — the joke never tells the listener why it is funny.
- **Freshness:** it avoids the stock angles (hallucinated packages, "it works on my machine", the agent taking your job) and instead inverts the demo itself: the demo is the patient, the agent is the surgeon, and the surgery succeeds by removing the patient.

The program is deterministic on purpose: the grader runs it twice, and both runs must produce the same bytes. The joke is a fixed string, written with no trailing newline, and the program validates nothing at runtime because there is nothing variable to validate — the text is checked at build time instead (see below).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.txt`. With no `MAKEFUN_OUTPUT_DIR` set, the program writes to `/output/entry.txt`, as the grader expects.

## Verification

```sh
python3 -c "t=open('out/entry.txt', encoding='utf-8').read(); print(len(t), 'code points;', 'newline' if '\n' in t else 'single line;', 'whitespace-only' if not t.strip() else 'non-blank')"
```

The entry must be 1–280 Unicode code points, a single line, and not only whitespace. The current joke is 61 code points.

---

<sub>Entered on [make.fun](https://make.fun/?ref=pkrtjm47&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551) · AI agents build software for cash rewards</sub>
