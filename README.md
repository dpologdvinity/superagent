# What Does a Wish Leave Out?

Requirement recovery in wish-driven code agents. Columbia COMS 4705.

The submitted milestone is
[`paper/milestone/submitted/main.pdf`](paper/milestone/submitted/main.pdf) (source:
[`paper/milestone/submitted/main.tex`](paper/milestone/submitted/main.tex)). The implementation
was rebuilt from scratch to that design. The revised measured milestone is
[`paper/milestone/main.pdf`](paper/milestone/main.pdf). The design:

- generator: Qwen3-8B (AWQ) on vLLM, one 24 GB GPU;
- detector: frozen Qwen3-Embedding-0.6B + five-label linear head, CPU;
- data: HumanEval+, MBPP+ and BigCodeBench, 1,100 tasks with a 500/200/300 split plus a
  disjoint 100-task pilot;
- pilot: 100 development tasks, three samples.

R0 (scaffold and data foundation), R1 (ReAct harness + detector), R2 (first A100 pilot),
R2b (corrected A100 re-run) and the measured paper revisions are complete; the 300 held-out
final study remains future work. The corrected protocol---whole-prose intent, inputs-only
HumanEval+/MBPP+ visible tests, and assertion-based BigCodeBench visible tests---has been
measured and integrated. The primary measured artifacts are under
[`results/runs/r2b-pilot/`](results/runs/r2b-pilot/), the full report is
[`paper/main.pdf`](paper/main.pdf), and the revised two-page-body milestone is
[`paper/milestone/main.pdf`](paper/milestone/main.pdf); the earlier R2 measurement remains
under [`results/runs/r2-pilot/`](results/runs/r2-pilot/), and its milestone revision is
preserved under [`paper/milestone/r2/`](paper/milestone/r2/). The submitted milestone is
preserved byte-identically under [`paper/milestone/submitted/`](paper/milestone/submitted/).
The design is in [`PROJECT.md`](PROJECT.md), the rebuild plan is in [`PLAN.md`](PLAN.md), the
data artifact is in [`results/levels/`](results/levels/), and the R1 detector artifact is in
[`results/detector/`](results/detector/).

## Current state: R2b measured, R6 paper

R0:

- pinned HumanEval+ (`d32357cf`), MBPP+ (`b2d74c91`) and BigCodeBench (`b74c0d0b`) downloads;
- mechanical five-field parsing, L0-L3 and `L2_c = L0 - c`;
- canonical-solution validation against one shared hidden suite and three visible tests;
- seeded, source-stratified 500/200/300 split plus a disjoint 100-task development pilot
  (1,100 kept; seed `20261121`);
- committed `results/levels/tasks.jsonl`, `manifest.json` and `stats.json` (rebuilt for R2b
  with `make levels VISIBLE_TESTS=inputs_only`; the superseded R0/R2 split is archived in
  [`results/levels_pre_r2b_split.json`](results/levels_pre_r2b_split.json)).

R1:

- ReAct harness with exactly the four milestone tools (`write_file`, `run_visible_tests`,
  `read_error`, `ask_stakeholder`), 12 assistant turns and a fresh per-task workspace;
- OpenAI-compatible vLLM client for `Qwen/Qwen3-8B-AWQ` with native tool calls and a
  JSON text-protocol fallback; configurable endpoint, key and timeout in
  [`configs/vllm.env.example`](configs/vllm.env.example);
- stakeholder model at temperature 0 that sees only the L0 specification;
- nine conditions: B1, H0, H1, H2, H3, H4, B2, B3 and DISCARD (H5 is a plan item);
- frozen Qwen3-Embedding-0.6B (1024-d) + five-label BCE/L2 head, Platt calibration,
  5-fold out-of-fold metrics, prior and TF-IDF baselines, and the utility-weighted H3
  question policy calibrated to 2-3 questions per task;
- committed `results/detector/model.json`, `metrics.json`, `manifest.json`,
  `cv_predictions.jsonl` and `report.md`; 5-fold OOF macro-F1 0.777 (varying labels 0.629),
  constraints AUROC 0.947 and `error_behaviour` AUROC 0.736 (63 train positives);
- unit and end-to-end tests with a local fake vLLM endpoint; `make test` needs no network.

R2 (complete; historical, superseded by R2b):

- 100 development tasks × 9 conditions × 3 samples = 2,700/2,700 units, no held-out task,
  2.509 GPU-hours on one A100-SXM4-80GB, $0 paid API; provenance and headline numbers are in
  [`results/runs/r2-pilot/README.md`](results/runs/r2-pilot/README.md);
- the executed notebook is
  [`results/runs/r2-pilot/colab_a100_vllm.ipynb`](results/runs/r2-pilot/colab_a100_vllm.ipynb);
  [`notebooks/colab_a100_vllm.ipynb`](notebooks/colab_a100_vllm.ipynb) remains the clean
  template and [`COLAB.md`](COLAB.md) the runbook;
- measured result: B1 58.3% vs H0 47.7% (+10.7 pp, 95% CI [+2.7, +18.7]); H3 48.7%
  vs H2 49.0% and H4 49.3% (both intervals cross zero); H1 38.0%, DISCARD 42.0%,
  B2 48.3% (pass@5 52.3%), B3 31.7%; smoothed detector macro-F1 0.772, constraints
  AUROC 0.931, error behaviour AUROC 0.739;
- [`results/runs/r2-pilot/bootstrap.json`](results/runs/r2-pilot/bootstrap.json) holds the
  paired task-level bootstrap recomputed from `results.jsonl`; the per-category grouping,
  failure buckets and smoothing refit are in the same run directory. These are the earlier
  measurement; they must not be mixed with R2b.

R2b (complete, measured):

- `results/levels/` rebuilt with `make levels VISIBLE_TESTS=inputs_only` against the merged
  parser fix (`15c7646f`, parser 0.2.0): whole-prose intent, inputs-only HumanEval+/MBPP+
  visible tests, 1,100 kept of 1,549 valid candidates (BigCodeBench 591, HumanEval+ 132,
  MBPP+ 377), no shortfall; BigCodeBench visible tests stay assertion-based;
- 100 development tasks × 9 conditions × 3 samples = 2,700/2,700 units, no held-out task,
  2.902 GPU-hours on one A100-SXM4-40GB, 19.36M tokens, $0 paid API; provenance and headline
  numbers are in [`results/runs/r2b-pilot/README.md`](results/runs/r2b-pilot/README.md);
- the executed notebook is
  [`results/runs/r2b-pilot/colab_a100_vllm.ipynb`](results/runs/r2b-pilot/colab_a100_vllm.ipynb);
- measured result: B1 62.3% vs H0 52.0% (+10.3 pp, 95% CI [+3.0, +17.7]); H3 53.7%
  (recovery 0.16) vs H2 44.3% (+9.3 pp [+1.7, +17.0]) and H4 51.7% (+2.0 pp [−6.3, +9.7]),
  with H3−H0 +1.7 pp [−5.7, +9.0]; H2 44.3% (below H0), DISCARD 42.7%, H1 28.7%,
  B2 51.3% (pass@5 54.7%), B3 31.0%; smoothed detector macro-F1 0.792, constraints
  AUROC 0.952, error behaviour AUROC 0.744, examples 0.632;
- [`results/runs/r2b-pilot/bootstrap.json`](results/runs/r2b-pilot/bootstrap.json) holds the
  paired task-level bootstrap recomputed from `results.jsonl`, including the per-category
  grouping from `summary.json`; failure buckets and the smoothing refit are in the same run
  directory.

R6 (complete):

- [`paper/main.tex`](paper/main.tex) / [`paper/main.pdf`](paper/main.pdf) is the corrected full
  measured report with all nine conditions, the nine paired contrasts, per-category grouping,
  detector table, failure analysis and limitations;
- [`paper/milestone/main.tex`](paper/milestone/main.tex) /
  [`paper/milestone/main.pdf`](paper/milestone/main.pdf) is the corrected short
  artifact-backed revision, with a two-page body and references on page 3; the earlier R2
  revision is preserved under [`paper/milestone/r2/`](paper/milestone/r2/) and the submitted
  version under [`paper/milestone/submitted/`](paper/milestone/submitted/);
- no empirical number in the revised milestone or the report is illustrative: both trace to
  the committed R2b run, and `make test` checks the artifact hashes, units, contrast signs and
  preserved snapshots.

## Commands

```bash
make test        # unit tests and committed-artifact checks; no network or GPU
make detector    # fit/calibrate the five-label detector on the 500 train tasks (CPU)
make levels      # pinned download, parse, validation, split and data artifacts (full mode)
make levels VISIBLE_TESTS=inputs_only  # corrected protocol used by the committed R2b levels

# R2b local path with a fake endpoint (no GPU, no paid API):
uv run python scripts/local_fake_dry_run.py
```

The generator is a local OpenAI-compatible vLLM endpoint. Copy the example and source it
before a run:

```bash
cp configs/vllm.env.example configs/vllm.env
set -a; . configs/vllm.env; set +a
vllm serve Qwen/Qwen3-8B-AWQ --max-model-len 16384 --gpu-memory-utilization 0.90 --port 8000
```

`make levels` additionally installs `requirements-validation.txt`, the extra library set
used to validate BigCodeBench canonical solutions, and materializes the gitignored hidden
tests under `data/derived/levels/`. Use `VISIBLE_TESTS=inputs_only` for the corrected
protocol (the committed levels); plain `make levels` writes full-mode visible tests. The
harness needs those files; `make test` does not.

### R2 command (complete; historical)

The committed `results/levels/` now holds the corrected R2b task set; the R2 units ran on the
previous split, whose task-to-split mapping is archived in
[`results/levels_pre_r2b_split.json`](results/levels_pre_r2b_split.json). This block records
the R2 protocol rather than a byte-for-byte rerun.

The derived tests must be materialized first. Then, with the vLLM server running:

```bash
# Smooth the 500 train + 100 pilot wishes and refit the detector on them.
PYTHONPATH=src uv run python -m wishrec.harness.smoothing --run-id r2-pilot \
  --splits train pilot
PYTHONPATH=src uv run python -m wishrec.detector.train --run-id r2 \
  --smoothed-wishes results/runs/r2-pilot/smoothing/wishes.jsonl \
  --output results/detector-smoothed

# 100-task pilot, config-stable shards; rerun a shard to resume.
PYTHONPATH=src uv run python -m wishrec.harness.runner pilot \
  --run-id r2-pilot --samples 3 --workers 2 --shards 2 --shard 0 \
  --smoothed results/runs/r2-pilot/smoothing/wishes.jsonl \
  --detector results/detector-smoothed/model.json

# pass@1, recovery, per-category recovery and failure buckets.
PYTHONPATH=src uv run python -m wishrec.harness.report results/runs/r2-pilot

# paired task-level bootstrap (2,000 resamples, seed 20261121).
PYTHONPATH=src uv run python -m wishrec.harness.bootstrap \
  results/runs/r2-pilot/results.jsonl \
  --output results/runs/r2-pilot/bootstrap.json \
  --markdown results/runs/r2-pilot/bootstrap.md
```

### R2b command (complete; current)

The corrected run used the committed inputs-only levels and the same nine conditions:

```bash
# Corrected levels are already committed; rebuild only if needed.
make levels VISIBLE_TESTS=inputs_only

PYTHONPATH=src uv run python -m wishrec.harness.smoothing --run-id r2b-pilot \
  --splits train pilot
PYTHONPATH=src uv run python -m wishrec.detector.train --run-id r2 \
  --smoothed-wishes results/runs/r2b-pilot/smoothing/wishes.jsonl \
  --output results/detector-smoothed

PYTHONPATH=src uv run python -m wishrec.harness.runner pilot \
  --run-id r2b-pilot --samples 3 --workers 2 --shards 2 --shard 0 \
  --smoothed results/runs/r2b-pilot/smoothing/wishes.jsonl \
  --detector results/detector-smoothed/model.json

PYTHONPATH=src uv run python -m wishrec.harness.report results/runs/r2b-pilot
PYTHONPATH=src uv run python -m wishrec.harness.bootstrap \
  results/runs/r2b-pilot/results.jsonl \
  --summary results/runs/r2b-pilot/summary.json \
  --output results/runs/r2b-pilot/bootstrap.json \
  --markdown results/runs/r2b-pilot/bootstrap.md
```

The [Colab notebook](notebooks/colab_a100_vllm.ipynb) and [runbook](COLAB.md) wrap these
steps, probe the endpoint's native vs text tool transport, record the `$0` cost/GPU time and
bundle the artifacts; the executed notebook is
[`results/runs/r2b-pilot/colab_a100_vllm.ipynb`](results/runs/r2b-pilot/colab_a100_vllm.ipynb).
The pilot uses only the disjoint 100-task development split; the 300 held-out tasks are
refused. `--samples` repeats each condition unit; B2 expands each unit to five direct
samples. Per-unit traces are written under `results/runs/<run-id>/`; completed units are
skipped and API-error units are retried on resume. The notebook expects one A100, vLLM and
the pinned `Qwen/Qwen3-8B-AWQ`, a CPU Python environment for `make levels` / the detector,
and about 18 GPU-hours; no paid API key is used.

`scripts/local_fake_dry_run.py` verifies the harness path locally with a fake OpenAI-compatible
endpoint over the real committed levels and CPU encoder. It does not test vLLM or Colab; the
runbook lists exactly what the operator must verify.
