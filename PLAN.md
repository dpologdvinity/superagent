# Final milestone plan and verification

## Goal

Make the repository a clean, from-scratch reproducible artifact for the accepted two-page
milestone in [`paper/milestone/main.pdf`](paper/milestone/main.pdf). A fresh clone must
install with `uv sync --frozen`, pass `make test` without network or GPU, rebuild the
committed levels from pinned public datasets, and trace every reported number to a committed
artifact.

## What is complete

- **Data foundation.** Pinned HumanEval+ (`d32357cf`), MBPP+ (`b2d74c91`) and BigCodeBench
  (`b74c0d0b`) downloads; mechanical field parsing into intent, signature/types, examples,
  constraints and error behaviour; L0–L3 plus `L2_c` deletion levels; canonical validation
  against visible and hidden suites; a seeded source-stratified 500/200/300 split plus a
  disjoint 100-task pilot. The committed artifact keeps 1,100 tasks from 1,682 source rows
  in 666 seconds on eight cores.
- **Harness.** A four-tool ReAct loop (write the file, run the visible tests, read the last
  error, ask the stakeholder), twelve turns, a fresh workspace per task, no repository
  browsing, and nine conditions: B1, H0–H4, B2, B3 and H3⁻. The operator path is
  [`notebooks/colab_a100_vllm.ipynb`](notebooks/colab_a100_vllm.ipynb) with the full runbook
  in [`COLAB.md`](COLAB.md).
- **Detector.** Frozen Qwen3-Embedding-0.6B encoder plus a five-label linear head, trained
  with BCE and L2, calibrated out of fold, with a question policy that ranks calibrated
  presence times utility and asks 2–3 questions per task. The final smoothed refit is in
  `results/detector-smoothed/`.
- **Measured pilot.** One A100-SXM4-40GB session served Qwen3-8B-AWQ on vLLM 0.34.0,
  completed 2,700/2,700 units on the 100 development tasks, used 2.902 GPU-hours and \$0
  paid API, and touched no held-out task. The traces, aggregates and bootstrap are in
  `results/runs/r2b-pilot/`.
- **Papers.** The accepted final milestone is 2 pages of body plus references on page 3. The
  extended measured report is `paper/main.pdf`. The submitted milestone is preserved
  byte-identically under `paper/milestone/submitted/`.

## Verification of the cleanup

1. Fresh clone into `/tmp`, then `uv sync --frozen` and `make test`: the full CPU test suite
   and committed-artifact checks.
2. `make levels` in that clone: pinned downloads, 1,100 kept tasks, `parsing.visible_tests =
   inputs_only`, and the committed `results/levels/tasks.jsonl` and `manifest.json` hashes.
3. Optional CPU refit with `make detector-smoothed` against the committed smoothed wishes.
4. Page count of `paper/milestone/main.pdf` (3 pages: 2-page body, references on page 3) and
   a text comparison against the accepted `COMS4705_Milestone_final.pdf`.
5. A relative-link check over the Markdown documents and repository tree.

## What remains

The pilot is a measured development run, not the final evaluation. The remaining work is the
300 held-out tasks with a second seed and a second session; H5, offline harness evolution;
and a refit on corrected labels, since two of the five detector labels are near-constant.
The headline result is relative: targeting beats generic questioning, but it does not close
the specification gap or separate from H0 and H4 at 100 tasks.

## Risks and mitigations

- **Dependency drift in BigCodeBench validation.** Sources are pinned and
  `requirements-validation.txt` fixes the validation library set; the manifest records the
  environment and every exclusion.
- **Benchmark test fragility.** Canonical validation runs in isolated subprocesses with
  timeouts and records failures; tasks that need unavailable libraries are excluded with the
  library named, not replaced.
- **Held-out leakage.** The 300 held-out tasks are data-only and never enter training,
  calibration, threshold selection or the pilot; the report checks held-out usage is zero.
- **GPU cost.** The pilot is capped at 100 development tasks and three samples, and cached
  units make interruptions cheap to resume.
- **BigCodeBench residual.** Its visible tests are assertion-based, so the examples field is
  not fully deleted for that subset; the papers state the residual and interpret the
  per-category examples row accordingly.
