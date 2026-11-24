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

- The README's milestone build recipe compiled `paper/main.tex` (8 pages) instead of
  `paper/milestone/main.tex` (3 pages), because `TEXINPUTS=..:` searched the parent directory
  first.
