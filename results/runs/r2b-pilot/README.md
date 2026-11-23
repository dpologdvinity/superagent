# R2b corrected GPU pilot artifacts

Measured nine-condition pilot on the disjoint 100-task development split, run under the
corrected R2b protocol. This directory is the committed evidence for R6; the operator
produced it in one Colab A100 session and R6 integrated the artifact bundle unchanged,
apart from recomputing [`bootstrap.json`](bootstrap.json) / [`bootstrap.md`](bootstrap.md)
from [`results.jsonl`](results.jsonl) and writing this README.

**Correction to R2.** The R2 artifacts in `../r2-pilot/` are the earlier measurement on
the superseded levels. Their intent was the first docstring sentence and their
HumanEval+/MBPP+ visible tests carried expected values, so the R2 numbers must not be
mixed with these. R2b keeps the whole docstring prose before the examples as the intent
block and renders HumanEval+/MBPP+ visible tests as inputs only (observed output printed,
no expected values); BigCodeBench visible tests remain assertion-based because its
unittest methods assert expectations rather than listing `(inputs, results)` pairs.
[`results/levels/`](../../levels/) holds the corrected levels, and
[`results/levels_pre_r2b_split.json`](../../levels_pre_r2b_split.json) archives the split
the R2 run used.

## Provenance

| field | value |
| --- | --- |
| run id | `r2b-pilot` |
| source commit | `6b236eb71d2aba4d00b5ad30b3a7412ae5f23b08` (dirty working tree) |
| finished | 2026-11-23T15:56:32+00:00 |
| GPU | NVIDIA A100-SXM4-40GB |
| generator | `Qwen/Qwen3-8B-AWQ` on vLLM 0.34.0, temperature 0.7, top-p 0.95 |
| tool transport | JSON text protocol; native tool calls unavailable on this vLLM build |
| samples | 3 per (condition, task); B2 expands internally to 5 direct samples |
| units | 2,700 / 2,700 complete |
| held-out tasks used | 0 |
| GPU time | 2.902 h (shards 1.385 h + 1.517 h) |
| tokens | 19,356,531 (input 18,075,167, output 1,281,364) |
| paid API cost | $0.00 |
| levels | tasks SHA-256 `e4cf7564b38e17c040b8a37837c4757a8b5d4045791a1621331c91a15cd36436`; manifest SHA-256 `78278ea9851c8c6ee7a3905169992d198db18d928e3c5ac67046182b90020ac4` |
| parsing | `{"visible_tests": "inputs_only"}` |

The executed notebook is [`colab_a100_vllm.ipynb`](colab_a100_vllm.ipynb), the runbook
summary is [`COLAB_RUN.md`](COLAB_RUN.md), and [`environment.json`](environment.json)
records the exact software environment. The machine-readable record from the runner is
[`manifest.json`](manifest.json); [`endpoint.json`](endpoint.json) records the transport
probe, [`gpu_time.json`](gpu_time.json) the shard timing,
[`data_provenance.json`](data_provenance.json) the corrected-levels hashes, and
[`r1_detector.json`](r1_detector.json) the pre-refit detector hash.

## Headline numbers

From [`report.md`](report.md) and [`summary.json`](summary.json); `n = 100` tasks per
condition, 300 units per condition. Recovery is the fraction of the B1-H0 gap closed.

| condition | pass@1 | pass rate | recovery | questions | turns |
| --- | --- | --- | --- | --- | --- |
| B1 | 0.623 | 0.623 | 1.000 | 0.00 | 4.34 |
| H0 | 0.520 | 0.520 | 0.000 | 0.00 | 4.40 |
| H1 | 0.287 | 0.287 | -2.259 | 0.00 | 4.51 |
| H2 | 0.443 | 0.443 | -0.743 | 2.94 | 6.36 |
| H3 | 0.537 | 0.537 | 0.162 | 2.48 | 4.43 |
| H4 | 0.517 | 0.517 | -0.032 | 0.00 | 4.74 |
| B2 | 0.513 | 0.547 | -0.065 | 0.00 | 5.00 |
| B3 | 0.310 | 0.310 | -2.033 | 0.00 | 1.00 |
| DISCARD | 0.427 | 0.427 | -0.903 | 2.48 | 4.09 |

B2's pass rate is the fraction of tasks where any of its five direct samples passes; its
pass@1 is the first of those five. The pilot source mix is 54 BigCodeBench, 34 MBPP+ and
12 HumanEval+ tasks.

## Paired task-level bootstrap

[`bootstrap.json`](bootstrap.json) and [`bootstrap.md`](bootstrap.md) are recomputed by
`src/wishrec/harness/bootstrap.py` from [`results.jsonl`](results.jsonl) with 2,000
resamples and seed `20261121`; each task contributes the mean of its three pass@1
samples, and every contrast reuses the same resample of the 100 tasks. The artifacts also
carry the per-category grouping copied from `summary.json` (the unit table has no category
column); the condition pass rates in that grouping are checked against `results.jsonl`.

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

The operator's independent check agrees on every point estimate. Its percentile
endpoints were computed with a different resampling random stream and agree to within
1.0 pp. The one definitional difference is B2-H0: the independent check applies B2's
five-sample pass rate (54.7% vs 52.0%, +2.7 pp), while this directory follows the
committed pass@1 protocol first defined for R3 (-0.7 pp).

## Per-category grouping

Tasks are grouped by an L0 category their wish omits (the categories overlap, so the task
counts sum past 100). The nine-condition pilot does not run separate L2$_c$ single-field
deletions, so this is attribution by task subset, not a controlled one-field contrast.
Source: [`summary.json`](summary.json), `by_category`.

| category | tasks | B1 | H0 | H2 | H3 | H4 | H3 recovery |
| --- | --- | --- | --- | --- | --- | --- | --- |
| signature_types | 100 | 0.623 | 0.520 | 0.443 | 0.537 | 0.517 | 0.162 |
| examples | 99 | 0.623 | 0.522 | 0.448 | 0.532 | 0.522 | 0.100 |
| constraints | 57 | 0.632 | 0.450 | 0.380 | 0.485 | 0.450 | 0.194 |
| error_behaviour | 10 | 0.833 | 0.400 | 0.367 | 0.433 | 0.467 | 0.077 |

## Detector refit

[`detector-smoothed/`](detector-smoothed/) holds the R2b refit on the 500 smoothed train
wishes: frozen `Qwen3-Embedding-0.6B`, five-label linear head, 5-fold out-of-fold
evaluation. Key numbers from [`detector-smoothed/report.md`](detector-smoothed/report.md):
macro-F1 0.792 (0.654 over the three varying labels), AUROC 0.632 examples, 0.952
constraints and 0.744 error behaviour (85 positives, average precision 0.315); Brier
0.0439, ECE 0.0142. TF-IDF reaches macro-F1 0.789 (0.648 varying) and AUROC
0.871/0.947/0.695. The H3 policy asks 2.48 questions per task on average (260 tasks get
two, 240 get three), never asks about intent, and selects constraints on 70% and error
behaviour on 37% of tasks.

[`smoothing/`](smoothing/) holds the 600 smoothed wishes (500 train + 100 pilot; 12
fallbacks), which are the refit and pilot inputs.

[`dry-run/`](dry-run/) is the 5-task x 9-condition plumbing check run on the same A100
session, not a result.

## Layout and reproduction

```
results/runs/r2b-pilot/
  summary.json report.md results.jsonl manifest.json endpoint.json environment.json
  gpu_time.json data_provenance.json r1_detector.json bootstrap.json bootstrap.md
  units/<condition>/<sample>/<task>.json        2,700 per-unit traces
  smoothing/                                    600 smoothed wishes + manifest
  detector-smoothed/                            smoothed detector refit
  dry-run/                                      45-unit plumbing check
  COLAB_RUN.md colab_a100_vllm.ipynb            runbook summary + executed notebook
```

Recompute the aggregate report and bootstrap from the committed units (the report's
`generated_at` is the only field that changes when it is re-run):

```bash
PYTHONPATH=src uv run python -m wishrec.harness.report results/runs/r2b-pilot
PYTHONPATH=src uv run python -m wishrec.harness.bootstrap \
  results/runs/r2b-pilot/results.jsonl \
  --summary results/runs/r2b-pilot/summary.json \
  --output results/runs/r2b-pilot/bootstrap.json \
  --markdown results/runs/r2b-pilot/bootstrap.md
```

`results.jsonl` is the 2,700-row unit table written by the runner; `units/` is the
per-unit trace bundle. Only the disjoint `pilot` split appears here. The 300 held-out
tasks were not run, and no held-out content is committed.
