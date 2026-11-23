# What Does a Wish Leave Out?

Requirement recovery in wish-driven code agents. Columbia COMS 4705.

A wish-driven coding agent receives an intent and builds an artifact. When the wish leaves
a requirement implicit, the program can run, pass the tests the user remembered to mention,
and still violate what the user meant. This project degrades benchmark specifications into
*wishes* by mechanically deleting fields, trains a small **silence detector** that predicts
which requirement categories a wish leaves implicit, and uses those predictions to target
clarification questions. The milestone contract is
[`paper/milestone/main.pdf`](paper/milestone/main.pdf); its source is
[`paper/milestone/main.tex`](paper/milestone/main.tex).

This repository is the clean rebuild of the implementation to that design. R0 (data
foundation), R1 (ReAct harness + five-label detector), R2 (first A100 pilot), R2b (corrected
A100 re-run) and R6 (paper revision) are complete. The corrected measured run and its
artifacts are in [`results/runs/r2b-pilot/`](results/runs/r2b-pilot/); the full report is
[`paper/main.pdf`](paper/main.pdf), and the revised measured milestone is
[`paper/milestone/main.pdf`](paper/milestone/main.pdf) (submitted version preserved under
`paper/milestone/submitted/`, R2 revision under `paper/milestone/r2/`). The earlier R2
measurement remains in [`results/runs/r2-pilot/`](results/runs/r2-pilot/) as history. Earlier
work survives only in git history and is not part of the rebuild.

## Milestone design

- **Generator:** Qwen3-8B (AWQ) served by vLLM on one 24 GB GPU, temperature 0.7, top-p 0.95,
  at most twelve ReAct turns, three samples per task.
- **Detector:** frozen Qwen3-Embedding-0.6B encoder with a five-way multi-label head, trained
  with binary cross-entropy on the deletion labels (AdamW, learning rate `2e-4`, batch 32,
  three epochs) and calibrated on the development split.
- **Data:** HumanEval+, MBPP+ and BigCodeBench, about 1,000 tasks in a 500/200/300
  detector-train / evolution / held-out split, plus a disjoint 100-task development pilot.
- **Pilot:** the 100 development tasks with three samples per condition, about 18 GPU-hours.
- **Conditions:** H0 (plain loop), H1 (acceptance tests first), H2 (generic questions), H3
  (detector-targeted questions), H4 (sibling functions with doctests), H5 (offline harness
  evolution), B1 (full L0 specification, ceiling), B2 (samples instead of questions), B3
  (frontier model given only the wish); a discard condition separates asking from knowing.
- **Metrics:** pass@1 and *recovery*, the fraction of the L0-L3 gap closed, plus per-category
  recovery on the single-field drops and failure buckets by exception type.

## The five fields and the levels

Every source task is parsed mechanically into the five milestone fields:

| field | HumanEval+ / MBPP+ | BigCodeBench `doc_struct` |
| --- | --- | --- |
| `intent` | first docstring sentence | `description` |
| `signature_types` | typed def / canonical def | `params` + `returns` |
| `examples` | doctest block / `test_list` | `examples` |
| `constraints` | notes / constraints prose | `notes` + `reqs` |
| `error_behaviour` | Raises / exception prose | `raises` |

Empty fields stay empty. A field is never invented. The levels are built by mechanical field
deletion:

- **L0** keeps every present field (full specification).
- **L1** drops examples and type detail; the signature stays, untyped.
- **L2** additionally drops constraints and error behaviour, keeping intent and the untyped
  signature.
- **L3** keeps only the intent, i.e. the wish.
- **L2_c = L0 - c** drops exactly one field category and is used to attribute recovery to that
  category.

One stub, one hidden suite and three visible tests are shared by all levels of a task. The
hidden suite is therefore byte-identical across L0-L3, and any level difference is information
loss rather than test variation. The hidden suite is never shown to the generator or the
stakeholder.

## R0: scaffold and data foundation

R0 builds the repository scaffold and the complete data foundation, and deliberately stops
before the harness (R1), the detector (R1), the GPU pilot (R2) and the paper (R3).

### Pinned data

| source | revision | file | rows |
| --- | --- | --- | --- |
| HumanEval+ | `d32357cf319e50e9c8d8dab5ea876c72b0fd321b` | `test.jsonl` | 164 |
| MBPP+ | `b2d74c91837c3f2a20c1299ae98133cbe7cfa077` | `data/test-00000-of-00001-d5781c9c51e02795.parquet` | 378 |
| BigCodeBench | `b74c0d0bf70d2c0bc459be537895cca163007f1a` | `data/train-00000-of-00001.parquet` | 1,140 |

Downloads are checksum-verified against the SHA-256 recorded in `src/wishrec/config.py` and in
the artifact manifest, and are idempotent in gitignored `data/raw/`.

### Tests and validation

- **HumanEval+:** the visible test runs `check()` on the first three of the benchmark's
  `inputs`/`results` cases; the hidden test is the full `check()` over all cases. Tasks whose
  test embeds a `ref_func` reference implementation are excluded because the visible test
  would leak that reference.
- **MBPP+:** the visible test is the first three `test_list` assertions; the hidden test is
  the full `test` module.
- **BigCodeBench:** the hidden test is the full `unittest` class. BigCodeBench's official
  harness concatenates the solution and the test module, so tests may use imports and
  constants from the solution module; the derived hidden test therefore prepends
  `from solution import <entry_point>` and a `from solution import *` compatibility line. The
  visible test keeps the imports, the `unittest` class, `setUp`/`tearDown`, helper methods and
  class attributes, plus exactly three `test_*` methods chosen in source order. Tasks with
  fewer than three test methods are excluded.

Every kept task's canonical solution is executed against both its visible and hidden tests in
an isolated subprocess with hard timeouts. Run results are cached by task content, validator
version and installed package versions. Excluded tasks and the exact exception, missing
library or timeout are recorded in the manifest and `stats.json`; tasks are never invented to
cover a shortfall.

### Split

The fixed seed `20261121` drives selection and splitting. All valid HumanEval+ and MBPP+ tasks
are retained, and a seeded uniform BigCodeBench sample fills the 1,000-task main pool; the
pilot is a further disjoint 100 tasks (1,100 kept in total). Each split's size is spread over
the remaining per-source pools with largest-remainder apportionment, so all four splits are
source-stratified and exact. The 300 held-out tasks are never assigned to detector training,
calibration, threshold selection or the pilot.

### Artifacts

`results/levels/` commits:

- `tasks.jsonl` - one record per kept task: split, fields and presence, L0-L3, `deleted_fields`,
  `L2_c`, stub, visible assertions and hashes, hidden/canonical/stub/test hashes, third-party
  requirements and per-task metadata.
- `manifest.json` - provenance, pins, counts, split, exclusions, environment and artifact
  checksums.
- `stats.json` - per-source field prevalence (including the expected 296 BigCodeBench
  `raises` positives), split counts, library requirements, level lengths and validation
  summary.

Hidden tests and canonical solutions are written to gitignored `data/derived/levels/` and are
regenerated by `make levels`; `tasks.jsonl` records their SHA-256. This keeps the committed
artifact readable and avoids checking solutions into the data record while remaining fully
reproducible from the pinned sources.

### R0 outcome

The committed run parsed 1,676 of 1,682 source rows and validated all of them: 1,573 pass
their own visible and hidden tests. The kept pool is exactly 1,100 tasks: 157 HumanEval+, 377
MBPP+ and 566 BigCodeBench, split 500/200/300 plus the disjoint 100-task pilot with no
shortfall. There are 109 exclusions: 6 HumanEval+ `ref_func` parse exclusions, 88 visible-test
failures and 15 hidden-test failures, including 10 tasks whose only blocker is an uninstalled
library (`tensorflow`, `keras`, `geopandas`, `gensim`, `soundfile`, `textblob`, `pytesseract`).
Among kept tasks, `error_behaviour` is present for 147 (6 HumanEval+, 1 MBPP+, 140
BigCodeBench); over the valid pool it is 267. BigCodeBench has 296 rows with `doc_struct.raises`
(the expected count), of which 260 survive validation and 140 are kept.

### Reproduction

```bash
make test    # unit tests and committed-artifact checks; no network needed
make levels  # pinned download, parse, canonical validation, split, artifacts
```

`make levels` additionally installs `requirements-validation.txt`, the extra library set used
to validate BigCodeBench canonical solutions. Python 3.12 is required.

### R0 limitations and decisions

- **L3 smoothing is deferred.** The milestone smooths the L3 wish with a language model. R0 has
  a $0 API budget and no GPU, so L3 is the raw first intent sentence; levels are the mechanical
  field-deletion baseline. R1/R2 can apply the generator-side smoothing and record it.
- **BigCodeBench namespace:** the derived hidden and visible tests import the solution module's
  public namespace, matching the official concatenation harness. Without that compatibility
  line, a large fraction of otherwise valid BigCodeBench tests raise `NameError` on constants
  and imports that live in the solution preamble.
- **Exclusions are data.** Tasks that fail parsing, need uninstallable libraries, hang, or fail
  their own canonical tests are recorded with the reason and are not replaced.
- **Held-out protection:** the held-out split is materialized as data only; R0 does not train
  or calibrate anything.

## R1: ReAct harness and five-label detector

R1 builds the harness, the stakeholder, the nine conditions and the silence detector, and
stops before the R2 GPU pilot.  It uses only CPU and a local OpenAI-compatible vLLM
endpoint; no paid API and no benchmark pilot run are involved.

### Harness

Each task is materialized in a fresh temporary workspace containing `solution.py` (the
stub) and `visible_test.py` (the derived three-method visible suite).  The agent can call
exactly four tools:

- `write_file` writes `solution.py`; `acceptance_tests.py` is writable in H1 only, and no
  test file is writable;
- `run_visible_tests` executes the derived visible file in a subprocess with a timeout and
  returns pass/fail;
- `read_error` returns the traceback of the most recent failed visible run;
- `ask_stakeholder` asks one question and consumes the condition's dialogue budget.

The loop allows at most 12 assistant turns and has no repository browsing or shell tool.
The hidden suite is never in the workspace; after the loop, a separate evaluator writes
`solution.py` and the hidden test into a fresh directory and runs the full suite.  The
stakeholder is a temperature-0 model whose prompt contains only the L0 specification; it
answers "That is not specified." when the specification does not contain the answer.

The generator is `Qwen/Qwen3-8B-AWQ` served by vLLM behind an OpenAI-compatible API.  The
client supports native OpenAI tool calls and a JSON text protocol
(`{"tool": ..., "arguments": ...}`) for builds that do not return tool calls; `auto` mode
probes native calls once, retries the turn under the text protocol when the endpoint
ignores tools, and remembers the working transport.  Endpoint, key, model, timeout,
transport, thinking mode and an optional B3 frontier endpoint are configured by
`VLLM_*` environment variables; [`configs/vllm.env.example`](configs/vllm.env.example) is
the documented example.  No credential is written to an artifact.

### Conditions

All conditions share the same tasks, tools and visible tests.  B1 sees the complete L0
specification; H0 is the plain wish loop; H1 may write acceptance tests first; H2 asks
generic stakeholder questions through the tool within a five-question budget; H3 asks the
detector-selected 2-3 questions before the loop and then runs one self-check-and-repair
call; H4 adds five sibling functions with doctests; B2 draws five direct samples instead of
asking; B3 calls the frontier endpoint (the same Qwen3-8B at temperature 0.7 when no
frontier endpoint is configured) with only the wish and stub; DISCARD asks H3's questions
but withholds the answers, separating asking from knowing.  H5 is a plan item and is not
implemented in R1.

### Detector

The detector is the frozen `Qwen/Qwen3-Embedding-0.6B` encoder (1024-d, CPU) plus a
five-label linear head trained with BCE and an L2 penalty.  Labels are the five fields'
presence in the full L0 specification, so a positive means the wish omits information the
stakeholder can supply.  It trains on the 500 `train` tasks only; the 200 evolution, 300
held-out and 100 pilot tasks are excluded from fitting, calibration, threshold selection
and model selection.  Five-fold out-of-fold evaluation uses inner-fold L2 selection and
Platt calibration, and compares against a prior-only predictor and TF-IDF + one-vs-rest
logistic regression.  Metrics are AUROC, average precision, F1 at 0.5, macro-F1, Brier,
ECE and log loss per category, including `error_behaviour` (63 positives in the train
split, 147 across all kept tasks).  The H3 policy ranks calibrated presence x utility
(intent 0, examples 0.2, signature/types 0.5, constraints 1.0, error_behaviour 1.0) and
calibrates a threshold to 2-3 questions per task; it never asks about intent.

L3 smoothing is implemented as a separate temperature-0 endpoint call but is not run in
R1: the detector trains on R0's raw first-sentence L3.  R2 will smooth the 500 train wishes,
refit the detector and use the smoothed wishes for the pilot.  This is recorded in
`results/detector/manifest.json`.

### R1 detector results

The committed 5-fold out-of-fold run (`results/detector/metrics.json`) on the 500 train
tasks:

| method | macro-F1 | macro-F1 (varying labels) | AUROC examples | AUROC constraints | AUROC error | Brier | ECE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prior-only | 0.753 | 0.588 | 0.358 | 0.426 | 0.409 | 0.0741 | 0.0000 |
| TF-IDF + logistic | 0.782 | 0.636 | 0.909 | 0.959 | 0.734 | 0.0408 | 0.0131 |
| frozen Qwen3 + linear head | 0.777 | 0.629 | 0.778 | 0.947 | 0.736 | 0.0421 | 0.0115 |

The encoder head is strongest for constraints (AUROC 0.947, Brier 0.0845) and reports
`error_behaviour` rather than declaring it undefined: 63 positives in the train split,
AUROC 0.736, average precision 0.270, Brier 0.102. Its F1 at the default 0.5 threshold is
0.000 because the calibrated probability stays near the low base rate; AUROC/AP are the
informative ranking metrics for that label. TF-IDF is a strong lexical baseline for
examples (AUROC 0.909 vs 0.778) and slightly higher macro-F1 (0.782 vs 0.777); the
encoder's advantage is that it scores a raw wish without fitting a task-specific lexical
model. The H3 policy calibrated on the deployed-style OOF scores asks 2.47 questions on
average (264 tasks get 2, 236 get 3), with informative-pair precision 0.879, recall 0.582
and utility recall 0.871; intent is never selected.

### R1 artifacts and verification

`results/detector/` commits `model.json` (encoder identity, head weights, calibrators,
threshold and utility policy), `metrics.json` (out-of-fold detection/calibration metrics,
baselines and policy diagnostics), `manifest.json`, `cv_predictions.jsonl` (per-task OOF
scores and selected categories) and `report.md`.  The harness tests cover the four tools,
sandbox paths, visible-test execution, turn cap, question budget, stakeholder gating, all
nine conditions, the runner's resume path, both tool transports and a local fake endpoint;
`make test` runs without network, GPU or the gitignored hidden tests.

## Repository layout

```
src/wishrec/          R0 data pipeline (download, parse, levels, split, validation, artifacts)
src/wishrec/harness/  R1 ReAct loop, four tools, conditions, stakeholder, vLLM client, runner
src/wishrec/detector/ R1 five-label detector, encoder, CV, calibration, metrics, policy
configs/              vLLM endpoint example (no secrets)
tests/                unit tests, fake-endpoint integration tests and artifact checks
results/levels/       committed R0 artifacts (manifest, stats, tasks.jsonl)
results/detector/     committed R1 detector artifacts
data/                 gitignored downloads, validation cache and derived hidden tests
paper/milestone/      milestone contract (do not modify)
PLAN.md               R0-R6 rebuild plan
```

## Budget

R0 and R1 use no paid API and no GPU: CPU, local network for the pinned downloads and the
cached encoder, and ordinary Python subprocesses for canonical validation and the ReAct
tools. The 18 GPU-hours belong to the R2 pilot.
