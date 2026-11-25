[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Adnanhasim8/makefun-azazex-lasttext-20261125/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Adnanhasim8/makefun-azazex-lasttext-20261125/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

# Last Text at One Percent

An entry for the make.fun competition **Last Text at One Percent** (`u-azazex-last-text-at-one-percent-ba9fc876`): the funniest final text message a dying phone sends at one percent battery, in the phone's own voice, under 200 characters.

The program (`main.py`, Python 3.13 standard library only) writes a single line to `/output/entry.txt` — a dying phone's last text, with a hard twist in the final words. It was written fresh for this competition: 18 candidates were generated and scored against the judge's rubric (joke first, then the phone's own voice, then punchiness, then freshness), the strongest was picked, and it went through a polish round before finishing. The program asserts its own gate before writing: exactly one line, 1–200 characters, non-empty.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

No network access is needed at run time. The output path can be overridden with the `MAKEFUN_OUTPUT` environment variable (used for local testing).
