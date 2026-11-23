# R2 GPU pilot artifacts

Measured 9-condition pilot on the disjoint 100-task development split. This directory is
the committed evidence for R3; the operator produced it in one Colab A100 session and the
R3 ticket integrated it unchanged.

**Data revision (R2b).** These R2 numbers were measured on the levels committed at the time.
The committed `results/levels/` was later rebuilt for the corrected R2b protocol (whole-prose
intent and inputs-only HumanEval+/MBPP+ visible tests); the R2 artifacts are the earlier
measurement and must not be mixed with R2b numbers.
[`results/levels_pre_r2b_split.json`](../../levels_pre_r2b_split.json) archives the
task-to-split mapping and the old `tasks.jsonl` SHA-256 that these units used, so the held-out
audit remains checkable.

## Provenance

| field | value |
| --- | --- |
| run id | `r2-pilot` |
| source commit | `8b355d660e61dfd6e8c0271a6d437153f314794d` (dirty working tree) |
| finished | 2026-11-23T01:22:13+00:00 |
| GPU | NVIDIA A100-SXM4-80GB |
| generator | `Qwen/Qwen3-8B-AWQ` on vLLM 0.34.0, temperature 0.7, top-p 0.95 |
| tool transport | JSON text protocol; native tool calls unavailable on this vLLM build |
| samples | 3 per (condition, task); B2 expands internally to 5 direct samples |
| units | 2,700 / 2,700 complete |
| held-out tasks used | 0 |
| GPU time | 2.509 h (shards 1.238 h + 1.271 h) |
| tokens | 21,756,260 (input 20,367,165, output 1,389,095) |
| paid API cost | $0.00 |

The executed notebook is [`colab_a100_vllm.ipynb`](colab_a100_vllm.ipynb), the runbook
summary is [`COLAB_RUN.md`](COLAB_RUN.md), and [`environment.json`](environment.json)
records the exact software environment. The machine-readable record from the runner is
[`manifest.json`](manifest.json); [`endpoint.json`](endpoint.json) records the transport
probe, [`gpu_time.json`](gpu_time.json) the shard timing, and
[`r1_detector.json`](r1_detector.json) the pre-refit detector hash.

## Headline numbers

From [`report.md`](report.md) and [`summary.json`](summary.json); `n = 100` tasks per
condition, 300 units per condition. Recovery is the fraction of the B1-H0 gap closed.

| condition | pass@1 | pass rate | recovery | questions | turns |
| --- | --- | --- | --- | --- | --- |
| B1 | 0.583 | 0.583 | 1.000 | 0.00 | 4.86 |
| H0 | 0.477 | 0.477 | 0.000 | 0.00 | 4.88 |
| H1 | 0.380 | 0.380 | -0.907 | 0.00 | 5.35 |
| H2 | 0.490 | 0.490 | 0.125 | 2.75 | 6.66 |
| H3 | 0.487 | 0.487 | 0.094 | 2.52 | 5.35 |
| H4 | 0.493 | 0.493 | 0.156 | 0.00 | 5.42 |
| B2 | 0.483 | 0.523 | 0.062 | 0.00 | 5.00 |
| B3 | 0.317 | 0.317 | -1.501 | 0.00 | 1.00 |
| DISCARD | 0.420 | 0.420 | -0.532 | 2.52 | 4.79 |

Paired task-level bootstrap (2,000 resamples, seed `20261121`, mean over each task's
three samples) is in [`bootstrap.json`](bootstrap.json) and
[`bootstrap.md`](bootstrap.md), produced by
`src/wishrec/harness/bootstrap.py` from [`results.jsonl`](results.jsonl):

| contrast | difference (pp) | 95% CI (pp) |
| --- | --- | --- |
| B1-H0 | +10.7 | [+2.7, +19.0] |
| H2-H0 | +1.3 | [-4.7, +7.3] |
| H3-H0 | +1.0 | [-5.7, +7.7] |
| H4-H0 | +1.7 | [-4.7, +8.0] |
| H3-H2 | -0.3 | [-6.3, +5.0] |
| H3-H4 | -0.7 | [-7.3, +6.3] |
| DISCARD-H3 | -6.7 | [-13.3, -0.3] |
| B2-H0 | +0.7 | [-5.7, +6.7] |

The point estimates match the independent check in the R3 request. Its percentile
intervals were computed with a different resampling random stream and agree to within
0.7 pp; the qualitative reading is identical (only B1-H0 and DISCARD-H3 exclude zero).

## Detector refit

[`detector-smoothed/`](detector-smoothed/) holds the R2 refit on the 500 smoothed train
wishes: frozen `Qwen3-Embedding-0.6B`, five-label linear head, 5-fold out-of-fold
evaluation. Key numbers: macro-F1 0.772 (varying labels 0.621), AUROC 0.803 examples,
0.931 constraints, 0.739 error behaviour (63 positives, AP 0.276); TF-IDF reaches
macro-F1 0.777 and AUROC 0.746/0.944/0.699. The H3 policy asks 2.47 questions per task
on average and never asks about intent.

[`smoothing/`](smoothing/) holds the 600 smoothed wishes (500 train + 100 pilot; 18
fallbacks), which are inputs to the detector refit and the pilot runner.

[`dry-run/`](dry-run/) is the 5-task x 9-condition plumbing check, not a result.

## Layout and reproduction

```
results/runs/r2-pilot/
  summary.json report.md results.jsonl manifest.json endpoint.json
  environment.json gpu_time.json r1_detector.json bootstrap.json bootstrap.md
  units/<condition>/<sample>/<task>.json        2,700 per-unit traces
  smoothing/                                    600 smoothed wishes + manifest
  detector-smoothed/                            smoothed detector refit
  dry-run/                                      45-unit plumbing check
  COLAB_RUN.md colab_a100_vllm.ipynb            runbook summary + executed notebook
```

Recompute the aggregate report and bootstrap from the committed units:

```bash
PYTHONPATH=src uv run python -m wishrec.harness.report results/runs/r2-pilot
PYTHONPATH=src uv run python -m wishrec.harness.bootstrap \
  results/runs/r2-pilot/results.jsonl \
  --output results/runs/r2-pilot/bootstrap.json \
  --markdown results/runs/r2-pilot/bootstrap.md
```

`results.jsonl` is the 2,700-row unit table written by the runner; `units/` is the
per-unit trace bundle. Only the disjoint `pilot` split appears here. The 300 held-out
tasks were not run, and no held-out content is committed.
