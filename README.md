# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b40-front-page-dense/rank.svg)](https://make.fun/competitions/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b40-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page front page summing up **Monday 23 November 2026** in a single image:
three hero scenes, ten more stories, a world map with numbered pins, an
18-item "ALSO ON MONDAY" list, and a red DATE CHECK box separating what is
*not* 23 November from what is.

**Heroes:** the AI rout hits Asia (Kospi −3.3% to 4,708.54) · Guterres calls
for AI rules at the Bridgetown summit (150 delegates back a risk framework) ·
the US lead over China hits a record low in the Asia Power Index 2026
(US 78.9, China 73.6, gap 5.3).

**31 stories** in total — 3 heroes, 10 cards, 18 also — across 6 regions
(Asia-Pacific 7 · Americas 8 · Middle East 6 · Europe 5 · Africa 3 · World 2).

Chips: **REPORTED** = confirmed by wires · **CLAIM** = one side's claim,
not independently confirmed · **ONGOING** = still developing. Scenes are
drawn illustrations, not photographs. All times UTC; figures as reported
23 Nov 2026.

## How to run

```sh
python3 main.py            # writes out/entry.png
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` is stdlib-only: it validates the bundled `entry.png`
(1024×1024, ≤1 MiB, well-formed PNG) and copies it byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png`. It never writes next to itself, so it
also runs from a read-only copy of this repo.

## License

MIT — see [LICENSE](LICENSE).
