UV ?= uv
PYTHON ?= .venv/bin/python

.PHONY: levels test

# Rebuild results/levels/ from the pinned datasets.  Downloads are cached in data/raw/,
# canonical-solution checks are cached in data/cache/validation/, and hidden tests plus
# canonical solutions are written to gitignored data/derived/levels/.
levels:
	$(UV) sync
	$(UV) pip install --python .venv -r requirements-validation.txt
	PYTHONPATH=src $(PYTHON) -m wishrec.build

# Fast checks: no network, no downloaded datasets, no BigCodeBench validation libraries.
test:
	$(UV) run pytest
