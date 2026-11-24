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

### Fixed

- The README's milestone build recipe compiled `paper/main.tex` (8 pages) instead of
  `paper/milestone/main.tex` (3 pages), because `TEXINPUTS=..:` searched the parent directory
  first.
