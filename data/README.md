# Committed data

This folder makes a fresh clone self-contained for the data pipeline and the harness. The
pilot's GPU generations are the only step that needs an A100; nothing here requires a
network once the repository is cloned.

## Layout

| path | contents |
| --- | --- |
| `data/raw/<source>/<revision>/<file>` | the three pinned dataset files, byte-identical to the sources below |
| `data/derived/levels/<source>/<task>/` | the 1,100 materialized tasks: `canonical_solution.py`, `stub.py`, `visible_test.py`, `hidden_test.py` |
| `data/manifest.json` | revisions, hashes, counts, split and derived-file summary |
| `data/raw/_hf-cache/` | local Hugging Face cache (gitignored) |
| `data/cache/` | validation cache (gitignored) |

## Pinned sources

| source | revision | file | bytes | rows | licence |
| --- | --- | --- | ---: | ---: | --- |
| HumanEval+ | `d32357cf319e50e9c8d8dab5ea876c72b0fd321b` | `test.jsonl` | 11,452,868 | 164 | Apache-2.0 |
| MBPP+ | `b2d74c91837c3f2a20c1299ae98133cbe7cfa077` | `test-00000-of-00001-d5781c9c51e02795.parquet` | 1,129,135 | 378 | Apache-2.0 |
| BigCodeBench | `b74c0d0bf70d2c0bc459be537895cca163007f1a` | `train-00000-of-00001.parquet` | 2,385,578 | 1,140 | Apache-2.0 |

The exact SHA-256 of each file is in `data/manifest.json` and is verified by
`wishrec.datasets.download_sources` before the file is used; a mismatch stops the pipeline.

## Levels and protocol

`data/derived/levels/` contains the materialized tests for the **corrected `inputs_only`
protocol** used by the measured R2b pilot: intent is the whole prose block, HumanEval+ and
MBPP+ visible tests print observed outputs rather than expected results, and BigCodeBench
keeps its assertion-based visible suite (documented residual). The 1,100 kept tasks, the
500/200/300 + 100 split and the exclusions are recorded in `results/levels/stats.json`;
`results/levels/tasks.jsonl` has SHA-256
`e4cf7564b38e17c040b8a37837c4757a8b5d4045791a1621331c91a15cd36436`.

## Use it offline

```bash
# verify the committed data and rebuild the levels artifact without dataset downloads
make levels

# run the test suite (CPU only, no dataset or model calls)
make test

# or materialize the derived tests directly (skips files that already match)
PYTHONPATH=src .venv/bin/python -m wishrec.materialize \
  --tasks results/levels/tasks.jsonl --visible-tests inputs_only
```

`wishrec.datasets.download_sources` verifies a committed raw file and returns without
touching the network; it only downloads when a file is missing. Delete
`data/raw/<source>/<revision>/` to force a fresh download on the next `make levels`.

## Regenerating

```bash
# full data rebuild from the pinned revisions (downloads only if raw files are absent)
make levels

# derived tests only
PYTHONPATH=src .venv/bin/python -m wishrec.materialize \
  --tasks results/levels/tasks.jsonl --visible-tests inputs_only
```

The committed `results/levels/manifest.json` also records build timestamps; a clean rebuild
reproduces the task hash, counts and derived hashes but not the manifest bytes.
