UV ?= uv
PYTHON ?= .venv/bin/python
RUN_ID ?= r1-smoke
VISIBLE_TESTS ?= inputs_only

.PHONY: levels test detector detector-smoothed smoke

# Rebuild results/levels/ from the pinned datasets.  Downloads are cached in data/raw/,
# canonical-solution checks are cached in data/cache/validation/, and hidden tests plus
# canonical solutions are written to gitignored data/derived/levels/.  The default
# `inputs_only` mode reproduces the committed levels (observed output, no expected values);
# pass VISIBLE_TESTS=full to rebuild the older full-mode visible tests.
levels:
	$(UV) sync
	$(UV) pip install --python .venv -r requirements-validation.txt
	PYTHONPATH=src $(PYTHON) -m wishrec.build --visible-tests "$(VISIBLE_TESTS)"

# Fast checks: no network, no downloaded datasets, no BigCodeBench validation libraries.
test:
	$(UV) run pytest

# Fit the frozen Qwen3-Embedding detector on the 500 train tasks, calibrate it and write
# results/detector/.  CPU only; the encoder is cached locally and never trained.
detector:
	PYTHONPATH=src $(UV) run python -m wishrec.detector.train

# Refit the final detector on the committed smoothed train wishes and write
# results/detector-smoothed/.  CPU only; this reproduces the reported detector.
detector-smoothed:
	PYTHONPATH=src $(UV) run python -m wishrec.detector.train --run-id r2b \
		--smoothed-wishes results/runs/r2b-pilot/smoothing/wishes.jsonl \
		--output results/detector-smoothed

# Small local smoke run.  Requires `make levels` for the gitignored hidden tests and a
# running vLLM endpoint (configs/vllm.env.example).  It writes results/runs/<run-id>/.
smoke:
	PYTHONPATH=src $(UV) run python -m wishrec.harness.runner smoke --run-id "$(RUN_ID)" --limit 3 --workers 1
