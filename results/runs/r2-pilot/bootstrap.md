# R2 paired task-level bootstrap

- Generated: 2026-11-23T01:39:47+00:00
- Source: `results/runs/r2-pilot/results.jsonl` (sha256 `b4fc2ef9a325c79313e31731960a90903599f1ce3e18e283fc77aae7df1e1052`)
- 100 tasks; samples per task [3]; 2000 resamples; seed 20261121

| condition | pass@1 | tasks | units |
| --- | --- | --- | --- |
| B1 | 58.3 | 100 | 300 |
| B2 | 48.3 | 100 | 300 |
| B3 | 31.7 | 100 | 300 |
| DISCARD | 42.0 | 100 | 300 |
| H0 | 47.7 | 100 | 300 |
| H1 | 38.0 | 100 | 300 |
| H2 | 49.0 | 100 | 300 |
| H3 | 48.7 | 100 | 300 |
| H4 | 49.3 | 100 | 300 |

| contrast | difference (pp) | 95% CI (pp) | excludes 0 |
| --- | --- | --- | --- |
| B1-H0 | +10.7 | [+2.7, +19.0] | yes |
| H2-H0 | +1.3 | [-4.7, +7.3] | no |
| H3-H0 | +1.0 | [-5.7, +7.7] | no |
| H4-H0 | +1.7 | [-4.7, +8.0] | no |
| H3-H2 | -0.3 | [-6.3, +5.0] | no |
| H3-H4 | -0.7 | [-7.3, +6.3] | no |
| DISCARD-H3 | -6.7 | [-13.3, -0.3] | yes |
| B2-H0 | +0.7 | [-5.7, +6.7] | no |

## Notes

- Task-level means average each task's three samples; B2 uses pass@1, the first of its five direct samples.
- The same resample of the 100 tasks is reused for every contrast.
- The 300 held-out tasks are absent from the pilot results.
