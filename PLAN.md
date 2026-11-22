# Rebuild plan: milestone contract to final report

The milestone contract is [`paper/milestone/main.pdf`](paper/milestone/main.pdf). The rebuild
runs in four phases. R0 and R1 are complete in this repository state; R2-R3 are not
started here.

Budget target: **18 GPU-hours** for the pilot, one 24 GB GPU, and **$0 paid API**. R0 and R1
use CPU and local network only.

## R0: scaffold + data foundation (complete)

**Goal.** Rebuild the repository from the null state to a validated data foundation that R1 can
consume, without building the harness, detector, GPU run or paper.

**Deliverables.**

- Python 3.12 project (`pyproject.toml`, `uv.lock`, `Makefile` with `levels` and `test`), source
  package under `src/wishrec/`, tests, `PROJECT.md` and this plan.
- Pinned downloads of HumanEval+ (164), MBPP+ (378) and BigCodeBench (1,140) with checksums.
- Mechanical five-field parsing and L0-L3 plus `L2_c = L0 - c` level construction.
- One shared stub, three visible tests and one hidden suite per kept task.
- Canonical-solution validation against both test suites, with exclusions and reasons.
- Seeded, source-stratified split: 500 detector-train / 200 evolution / 300 held-out, plus a
  disjoint 100-task development pilot (1,100 kept; seed `20261121`).
- Committed `results/levels/tasks.jsonl`, `manifest.json`, `stats.json`.

**Acceptance criteria.**

1. Every kept task's canonical solution passes its visible and hidden tests.
2. The hidden suite is byte-identical across L0-L3 for every task (one suite is stored per task
   and reused by every level).
3. The four splits are disjoint and have the requested sizes when the valid pool allows it;
   otherwise the exact shortfall is reported.
4. Field prevalence per source is reported, including BigCodeBench `error_behaviour` positives
   and the expected 296 `raises` rows.
5. The 300 held-out tasks are never used for training, calibration, threshold selection or the
   pilot.
6. `make test` passes without network access.

**Status.** Complete. The committed artifacts record 1,573 valid tasks and exactly 1,100 kept
tasks (157 HumanEval+, 377 MBPP+, 566 BigCodeBench; 500/200/300 plus a disjoint 100-task pilot,
no shortfall), 109 recorded exclusions, the environment and checksums. `make levels`
regenerates everything from the pinned revisions.

**R0 decisions and limitations.**

- L3 is the raw first intent sentence. Wish smoothing needs a language model; with a $0 API
  budget and no GPU in R0, the mechanical baseline is used and smoothing is deferred to R1/R2.
- BigCodeBench tests run against the solution module's public namespace, mirroring the official
  same-namespace harness. The derived tests add a wildcard import after the required
  `from solution import <entry_point>` line; without it, tests that use the solution preamble's
  imports or constants would fail even with a correct solution.
- HumanEval+ tasks with a `ref_func` reference implementation are excluded because their
  visible test would otherwise expose the reference. Other exclusions are recorded per task.
- Hidden tests and canonical solutions stay in gitignored `data/derived/levels/`; the committed
  records carry their hashes. Regeneration is deterministic apart from library-version drift,
  which the manifest records.
- The split contract fixes exact sizes only when at least 1,100 tasks validate. If an
  environment cannot install enough dependencies to reach that total, the pipeline records the
  shortfall instead of padding the pool, and the artifact is not presented as meeting the
  target.

## R1: harness + detector (complete)

**Goal.** Build the ReAct harness, the stakeholder, the nine conditions and the five-label
silence detector.

**Work (delivered).**

1. Harness: four tools (`write_file`; `acceptance_tests.py` in H1 only;
   `run_visible_tests`; `read_error`; `ask_stakeholder`), turn cap 12, no repository
   browsing, isolated per-task workspace and shared task/tool/test configuration across
   conditions.
2. Generator: an OpenAI-compatible vLLM endpoint (`Qwen/Qwen3-8B-AWQ`), configurable
   endpoint/key/timeout via `configs/vllm.env.example`, with native OpenAI tool calls and a
   JSON text-protocol fallback; the loop runs with either transport.
3. Conditions: B1, H0, H1, H2, H3, H4, B2, B3 and DISCARD. B2 uses five direct samples;
   B3 uses the frontier endpoint when configured and otherwise the same Qwen3-8B at
   temperature 0.7; H4 exposes five sibling functions with doctests. H5 remains a plan item.
4. Stakeholder: a temperature-0 model that sees only the L0 specification.
5. Detector: frozen `Qwen/Qwen3-Embedding-0.6B` (1024-d) + five-label linear head,
   BCE + L2, trained on the 500 `train` tasks; Platt calibration and 5-fold out-of-fold
   metrics (AUROC, macro-F1, Brier/ECE) with prior and TF-IDF baselines; the
   `error_behaviour` label (63 train positives, 147 kept positives) is reported rather than
   declared undefined. The H3 policy ranks calibrated presence x utility (intent 0,
   examples 0.2, signature/types 0.5, constraints 1.0, error_behaviour 1.0) and calibrates
   to 2-3 questions per task.
6. Tests for the loop, four tools, stakeholder gating, question budget, conditions, detector
   and a local fake vLLM endpoint, plus an end-to-end runner test over all nine conditions.

**Acceptance.** All nine conditions run end to end in the fake-endpoint integration test;
the detector trains on the 500-task split and calibrates without touching the held-out
split; question selection is recorded per unit; the discard condition separates asking from
knowing.

**Status.** Complete. The detector artifact is in `results/detector/`; the harness package is
`src/wishrec/harness/` and the detector package is `src/wishrec/detector/`. L3 smoothing is
implemented as a separate endpoint call but deliberately not run in R1: the detector trains
on R0's raw first-sentence L3, and R2 will smooth the 500 train wishes, refit and use the
smoothed wishes for the pilot. No GPU or paid API is used in R1.

## R2: Colab GPU pilot (next)

**Goal.** Run the 100-task development pilot with Qwen3-8B AWQ on vLLM, three samples per
condition, within about 18 GPU-hours.

**Work.**

1. Provision one 24 GB GPU (Colab), install vLLM and the pinned generator revision, record the
   exact environment and GPU.
2. Run the pilot conditions on the development split only; never touch the 300 held-out tasks.
3. Cache generations and traces; rerun only missing units after interruptions.
4. Compute pass@1, recovery, per-category recovery and failure buckets; verify the sample count
   and cost.

**R2 command.** With `configs/vllm.env` sourced and the server running:

```bash
# CPU preparation: materialize derived hidden tests and fit the detector.
make levels
make detector
# GPU pilot: only the disjoint 100-task development split.
PYTHONPATH=src uv run python -m wishrec.harness.runner pilot \
  --run-id r2-pilot --samples 3 --workers 2
```

The runner refuses the held-out split, writes one trace per (condition, task, sample) under
`results/runs/r2-pilot/` and skips completed units on restart. `--samples 3` repeats each
condition unit three times; B2 itself expands to five direct samples per unit. The Colab
notebook must provide the 24 GB GPU, vLLM and the pinned Qwen3-8B-AWQ model, the CPU
environment for `make levels` / `make detector`, and the 18 GPU-hour budget; no paid API key
is used.

**Acceptance.** All pilot units complete or are reported missing; the main-table metrics are
computed from measured traces; the held-out split is untouched; the GPU-hour budget is recorded.

## R3: paper

**Goal.** Replace the milestone's illustrative numbers with the measured pilot results and the
full-run plan.

**Work.**

1. Update the paper with measured pass@1, recovery and question counts per condition.
2. Report detector metrics (macro-F1, per-category AUROC) and the error-attribution analysis.
3. State the limitations honestly: level construction, L3 smoothing, excluded tasks, sample
   size and the held-out protocol.
4. Run the 300 held-out tasks only for the final report, with two seeds as the milestone states.

**Acceptance.** Every headline number traces to a committed artifact; the paper and the
repository agree; no held-out task influenced training, calibration or threshold selection.

## Risks and mitigations

- **Dependency drift in BigCodeBench validation.** Pinned sources are stable, but canonical
  validation depends on installed library versions. The manifest records the environment, and
  `requirements-validation.txt` pins the set; exclusions are recorded rather than hidden.
- **Small-source ceiling.** HumanEval+ and MBPP+ contribute 542 rows at most; BigCodeBench must
  supply the remainder. The pipeline reports a shortfall instead of padding.
- **Benchmark test fragility.** Some tests depend on randomness, file-system layout, network or
  the solution preamble. Canonical validation runs each task in a subprocess with timeouts and
  records failures; tasks that need unavailable libraries are excluded with the library named.
- **Held-out leakage.** Splits are assigned once by seed and disjoint by construction; the
  held-out records are data-only in R0 and are excluded from every training/calibration path.
- **GPU cost.** The pilot is capped at 100 development tasks and three samples; cached
  generations make interruptions cheap to resume.
