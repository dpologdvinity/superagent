# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and commits follow
[Conventional Commits](https://www.conventionalcommits.org/).

## [Unreleased]

### Added

- GitHub Actions CI: pre-commit hygiene hooks, ruff lint and format check, mypy, and pytest
  with a coverage summary.
- Paper workflow that compiles both papers and enforces the 3-page milestone limit.
- Dependabot (uv and GitHub Actions) and CodeRabbit review configuration.
- ruff, mypy, pytest-cov and pre-commit configuration; `make lint`, `format`, `typecheck`,
  `coverage` and `check` targets; `.editorconfig`.
- `ARCHITECTURE.md`, `CONTRIBUTING.md`, `SECURITY.md`, issue and pull request templates.
- `wishrec.analysis` and `make analysis`: a source-only detector baseline with per-source
  AUROC, and a breakdown of pilot NoSolution units by termination cause
  (`results/analysis/`).
- `build --derived` and `--allow-resplit`; the build refuses to change a committed split.

### Changed

- Source, tests and scripts formatted with ruff; docstrings and type annotations added
  throughout `src/` and `scripts/`.
- Harness source edits change `harness_source_hash` and therefore a run's `config_hash`:
  resuming a run directory created before these changes needs `--force`.
- Without `--detector`, the harness now uses `results/detector-smoothed/` (the final
  detector) instead of the earlier R1 artifact in `results/detector/`.

### Fixed

- The detector encoder is loaded at the pinned `ENCODER_REVISION` that the manifest,
  embedding cache key and model record; previously the hub's moving `main` was loaded.
- The detector report's limitation sentences are computed from `metrics.json` instead of
  hard-coded numbers from an earlier run.
- The ReAct loop gives feedback on unparseable, truncated or prose replies instead of
  treating them as finishing; only an explicit finish ends it.
- Auto tool mode falls back to the text protocol when an endpoint rejects tools with 400.
- A B3 frontier endpoint on another host no longer receives the generator's API key.
- api_error units are reported as missing instead of scored failures.
- Visible-test timeouts no longer hang on detached child processes.
- `--visible-timeout`/`--hidden-timeout` are honoured and part of the validation cache key.
- The default visible-tests mode is `inputs_only`; materialize verifies hashes and refuses
  to write mismatching files; downloads are checksummed before being moved into place.
- The Colab notebook deleted upstream is restored.

- The README's milestone build recipe compiled `paper/main.tex` (8 pages) instead of
  `paper/milestone/main.tex` (3 pages), because `TEXINPUTS=..:` searched the parent directory
  first.
