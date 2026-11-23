# R2b paired task-level bootstrap

- Generated: 2026-11-23T16:19:31+00:00
- Source: `results/runs/r2b-pilot/results.jsonl` (sha256 `9c37535431b2da7d56f682ebbc2b17dfa5d57fb712af5c72201db262603b5c2d`)
- 100 tasks; samples per task [3]; 2000 resamples; seed 20261121
- Per-category grouping: `results/runs/r2b-pilot/summary.json` (sha256 `4032f68a015231500141d1e22cf05814e90ff184065c3ec7618366016120b20f`)

| condition | pass@1 | tasks | units |
| --- | --- | --- | --- |
| B1 | 62.3 | 100 | 300 |
| B2 | 51.3 | 100 | 300 |
| B3 | 31.0 | 100 | 300 |
| DISCARD | 42.7 | 100 | 300 |
| H0 | 52.0 | 100 | 300 |
| H1 | 28.7 | 100 | 300 |
| H2 | 44.3 | 100 | 300 |
| H3 | 53.7 | 100 | 300 |
| H4 | 51.7 | 100 | 300 |

| contrast | difference (pp) | 95% CI (pp) | excludes 0 |
| --- | --- | --- | --- |
| B1-H0 | +10.3 | [+3.0, +17.7] | yes |
| H2-H0 | -7.7 | [-14.3, -1.0] | yes |
| H3-H0 | +1.7 | [-5.7, +9.0] | no |
| H4-H0 | -0.3 | [-6.0, +5.3] | no |
| H1-H0 | -23.3 | [-31.3, -15.7] | yes |
| H3-H2 | +9.3 | [+1.7, +17.0] | yes |
| H3-H4 | +2.0 | [-6.3, +9.7] | no |
| DISCARD-H3 | -11.0 | [-18.7, -2.7] | yes |
| B2-H0 | -0.7 | [-6.7, +5.0] | no |

## Per-category grouping

From `summary.json`: tasks grouped by an L0 category their wish omits (categories overlap).

| category | tasks | B1 | H0 | H2 | H3 | H4 | H3 recovery |
| --- | --- | --- | --- | --- | --- | --- | --- |
| constraints | 57 | 63.2 | 45.0 | 38.0 | 48.5 | 45.0 | 0.194 |
| error_behaviour | 10 | 83.3 | 40.0 | 36.7 | 43.3 | 46.7 | 0.077 |
| examples | 99 | 62.3 | 52.2 | 44.8 | 53.2 | 52.2 | 0.100 |
| signature_types | 100 | 62.3 | 52.0 | 44.3 | 53.7 | 51.7 | 0.162 |

## Notes

- Task-level means average each task's three samples; B2 uses pass@1, the first of its five direct samples.
- The same resample of the 100 tasks is reused for every contrast.
- The 300 held-out tasks are absent from the pilot results.
- The per-category grouping is copied from summary.json because the unit table carries no category labels; its condition pass rates were checked against results.jsonl.
