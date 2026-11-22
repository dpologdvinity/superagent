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

This repository is the clean rebuild of the implementation to that design; earlier work
survives only in git history and is not part of the rebuild.

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

## Repository layout

```
src/wishrec/          R0 data pipeline (download, parse, levels, split, validation, artifacts)
src/wishrec/config.py pinned sources, split contract, paths
tests/                unit tests and committed-artifact checks
results/levels/       committed R0 artifacts (manifest, stats, tasks.jsonl)
data/                 gitignored downloads, validation cache and derived hidden tests
paper/milestone/      milestone contract (do not modify)
PLAN.md               R0-R3 rebuild plan
```

## Budget

R0 uses no paid API and no GPU: CPU, local network for the pinned downloads, and ordinary
Python subprocesses for canonical validation. The 18 GPU-hours belong to the R2 pilot.
