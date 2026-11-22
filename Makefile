UV ?= uv
PYTHON ?= .venv/bin/python
RUN_ID ?= r1-smoke

.PHONY: levels test detector smoke

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

# Fit the frozen Qwen3-Embedding detector on the 500 train tasks, calibrate it and write
# results/detector/.  CPU only; the encoder is cached locally and never trained.
detector:
	PYTHONPATH=src $(UV) run python -m wishrec.detector.train

# Small local smoke run.  Requires `make levels` for the gitignored hidden tests and a
# running vLLM endpoint (configs/vllm.env.example).  It writes results/runs/<run-id>/.
smoke:
	PYTHONPATH=src $(UV) run python -m wishrec.harness.runner smoke --run-id "$(RUN_ID)" --limit 3 --workers 1
