# Rebuild plan: milestone contract to final report

The submitted milestone is
[`paper/milestone/submitted/main.pdf`](paper/milestone/submitted/main.pdf). The rebuild ran in
four phases: R0 (data), R1 (harness + detector), R2 (the operator's first A100 pilot) and R2b
(the corrected A100 re-run) are complete, and the R6 paper revision is written; the 300
held-out final study remains future work. The revised measured milestone is
[`paper/milestone/main.pdf`](paper/milestone/main.pdf) and the full report is
[`paper/main.pdf`](paper/main.pdf).

Budget target: **18 GPU-hours** for the pilot, one 24 GB GPU, and **$0 paid API**. R0 and R1
use CPU and local network only. The corrected pilot used 2.902 GPU-hours and $0 paid API.

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

## R2: Colab GPU pilot (complete, measured)

**Goal.** Run the 100-task development pilot with Qwen3-8B AWQ on vLLM, three samples per
condition, within about 18 GPU-hours.

**Delivered preparation.** The operator-facing path is
[`notebooks/colab_a100_vllm.ipynb`](notebooks/colab_a100_vllm.ipynb) and
[`COLAB.md`](COLAB.md). The notebook clones the pinned repository, materializes the data,
starts vLLM, probes native and text tool transports, smooths the 500 train + 100 pilot wishes,
refits the detector on the smoothed wishes, runs a 5-task dry run and the sharded 100-task
pilot, and bundles the artifacts. `scripts/local_fake_dry_run.py` runs the same harness path
locally against a fake OpenAI-compatible endpoint with the real levels and CPU encoder; no
GPU or paid API is used. The runner gained `--smoothed`, `--detector`, `--shard/--shards`
and retries API-error units on resume; the detector gained `--smoothed-wishes`; the new
`wishrec.harness.report` module computes pass@1, recovery, per-category recovery and failure
buckets across shards.

**Work.**

1. Provision one 24 GB GPU (Colab), install vLLM and the pinned generator revision, record the
   exact environment and GPU.
2. Run the pilot conditions on the development split only; never touch the 300 held-out tasks.
3. Cache generations and traces; rerun only missing units after interruptions.
4. Compute pass@1, recovery, per-category recovery and failure buckets; verify the sample count
   and cost.

**R2 command.** With `configs/vllm.env` sourced and the server running, the short version
is the notebook/runbook path; the equivalent manual commands are:

```bash
# CPU preparation: materialize derived hidden tests, smooth the wishes and refit.
make levels
PYTHONPATH=src uv run python -m wishrec.harness.smoothing --run-id r2-pilot \
  --splits train pilot
PYTHONPATH=src uv run python -m wishrec.detector.train --run-id r2 \
  --smoothed-wishes results/runs/r2-pilot/smoothing/wishes.jsonl \
  --output results/detector-smoothed
# GPU pilot: only the disjoint 100-task development split, sharded/resumable.
PYTHONPATH=src uv run python -m wishrec.harness.runner pilot \
  --run-id r2-pilot --samples 3 --workers 2 --shards 2 --shard 0 \
  --smoothed results/runs/r2-pilot/smoothing/wishes.jsonl \
  --detector results/detector-smoothed/model.json
# Aggregate after all shards; --require-complete enforces 2,700 units + no held-out.
PYTHONPATH=src uv run python -m wishrec.harness.report results/runs/r2-pilot \
  --require-complete
```

The runner refuses the held-out split, writes one trace per (condition, task, sample) under
`results/runs/r2-pilot/` and skips completed units on restart. `--samples 3` repeats each
condition unit three times; B2 itself expands to five direct samples per unit. The Colab
notebook must provide the 24 GB GPU, vLLM and the pinned Qwen3-8B-AWQ model, the CPU
environment for `make levels` / `make detector`, and the 18 GPU-hour budget; no paid API key
is used.

**Acceptance.** All pilot units complete or are reported missing; the main-table metrics are
computed from measured traces; the held-out split is untouched; the GPU-hour budget is
recorded. **Status:** complete (historical). The operator ran the prepared notebook on one
A100-SXM4-80GB (commit `8b355d66`, vLLM 0.34.0, `Qwen/Qwen3-8B-AWQ`, text tool transport):
2,700/2,700 units, 0 held-out tasks, 2.509 GPU-hours, 21.76M tokens, $0 paid API. The
committed run is [`results/runs/r2-pilot/`](results/runs/r2-pilot/). Headline result: B1
58.3% vs H0 47.7% (+10.7 pp, 95% CI [+2.7, +18.7]), while H3 48.7% does not beat H2 49.0%
or H4 49.3% (both intervals cross zero); H1 38.0%, DISCARD 42.0%, B2 48.3% (pass@5 52.3%),
B3 31.7%. These numbers are the earlier measurement; they must not be mixed with R2b. The
paired task-level bootstrap, per-category grouping, failure buckets and smoothed detector
refit are in the same run directory.

## R3: measured paper (pilot complete; held-out study pending)

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

**Status.** Complete for R2/R3 and superseded by R6 for the headline numbers. The corrected
[`paper/main.tex`](paper/main.tex) / [`paper/main.pdf`](paper/main.pdf) is the full measured
report (all nine conditions, the nine paired contrasts, per-category grouping, detector
table, failure analysis and limitations). The corrected milestone
[`paper/milestone/main.tex`](paper/milestone/main.tex) /
[`paper/milestone/main.pdf`](paper/milestone/main.pdf) is the short artifact-backed version
with a two-page body and references on page 3; the R2 milestone snapshot is preserved under
[`paper/milestone/r2/`](paper/milestone/r2/) and the submitted milestone byte-identically
under [`paper/milestone/submitted/`](paper/milestone/submitted/). The 300 held-out tasks and
the second seed remain for the full study: the pilot reports a measured result, not the final
evaluation.

## R4/R5/R6: operationalization disclosure, corrected levels and corrected run (complete)

R4 disclosed the measured pilot's intent/visible-test operationalization issues in the paper
and [`paper/operationalization-notes.md`](paper/operationalization-notes.md). R5 rebuilt
[`results/levels/`](results/levels/) against the merged parser fix (`15c7646f`, parser 0.2.0)
with whole-prose intent and `VISIBLE_TESTS=inputs_only` for HumanEval+/MBPP+, keeping the
BigCodeBench assertion-based visible-test residual. The superseded R0/R2 split is archived in
[`results/levels_pre_r2b_split.json`](results/levels_pre_r2b_split.json), so the R2 artifacts
remain auditable. R6 integrated the operator's corrected A100 run under
[`results/runs/r2b-pilot/`](results/runs/r2b-pilot/) and replaced the paper and milestone
numbers. The corrected run has 2,700/2,700 units, no held-out task, 2.902 GPU-hours and $0
paid API; B1 62.3% vs H0 52.0% (+10.3 pp [+3.0, +17.7]), H3 53.7% vs H2 44.3% (+9.3 pp
[+1.7, +17.0]) and H4 51.7% (+2.0 pp [−6.3, +9.7]), with H3−H0 +1.7 pp [−5.7, +9.0];
H2, DISCARD and H1 are below H0. The per-category grouping, failure buckets and detector
refit are in the same run directory.

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
