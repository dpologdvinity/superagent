# What Does a Wish Leave Out?

Requirement recovery in wish-driven code agents. Columbia COMS 4705.

The milestone contract is [`paper/milestone/main.pdf`](paper/milestone/main.pdf); its source is
[`paper/milestone/main.tex`](paper/milestone/main.tex). The implementation is being rebuilt from
scratch to that design:

- generator: Qwen3-8B (AWQ) on vLLM, one 24 GB GPU;
- detector: frozen Qwen3-Embedding-0.6B + five-label linear head, CPU;
- data: HumanEval+, MBPP+ and BigCodeBench, 1,100 tasks with a 500/200/300 split plus a
  disjoint 100-task pilot;
- pilot: 100 development tasks, three samples.

R0 (scaffold and data foundation) and R1 (ReAct harness + detector) are complete; R2-R3
follow. The design is in [`PROJECT.md`](PROJECT.md), the rebuild plan is in
[`PLAN.md`](PLAN.md), the R0 data artifact is in [`results/levels/`](results/levels/), and
the R1 detector artifact is in [`results/detector/`](results/detector/).

## Current state: R0 + R1

R0:

- pinned HumanEval+ (`d32357cf`), MBPP+ (`b2d74c91`) and BigCodeBench (`b74c0d0b`) downloads;
- mechanical five-field parsing, L0-L3 and `L2_c = L0 - c`;
- canonical-solution validation against one shared hidden suite and three visible tests;
- seeded, source-stratified 500/200/300 split plus a disjoint 100-task development pilot
  (1,100 kept; seed `20261121`);
- committed `results/levels/tasks.jsonl`, `manifest.json` and `stats.json`.

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

## Commands

```bash
make test        # unit tests and committed-artifact checks; no network or GPU
make detector    # fit/calibrate the five-label detector on the 500 train tasks (CPU)
make levels      # pinned download, parse, validation, split and data artifacts
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
tests under `data/derived/levels/`. The harness needs those files; `make test` does not.

### R2 command (not run in R1)

`make levels` and `make detector` must complete first. Then, with the vLLM server running:

```bash
PYTHONPATH=src uv run python -m wishrec.harness.runner pilot \
  --run-id r2-pilot --samples 3 --workers 2
```

The pilot uses only the disjoint 100-task development split; the 300 held-out tasks are
refused. `--samples` repeats each condition unit; B2 itself expands to five direct samples
per unit. Per-unit traces are written under `results/runs/r2-pilot/` and an interrupted
run resumes from completed units. The Colab notebook must provide one 24 GB GPU, vLLM and the
pinned `Qwen/Qwen3-8B-AWQ` revision, a CPU Python environment for `make levels` /
`make detector`, and about 18 GPU-hours; no paid API key is used.
