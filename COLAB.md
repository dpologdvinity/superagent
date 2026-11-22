# R2 Colab A100/L4 runbook

This runbook covers the R2 GPU pilot for *What Does a Wish Leave Out?*: L3 smoothing with
Qwen3-8B, a five-label detector refit on the smoothed wishes, a 5-task dry run, and the
100-task × 3-sample × 9-condition pilot on one Colab A100 or L4 runtime. The notebook is
[`notebooks/colab_a100_vllm.ipynb`](notebooks/colab_a100_vllm.ipynb).

**Scope:** prepare and run the pilot. Do not run the 300 held-out tasks here; they belong to
R3. No paid API is used: the only endpoint is the local vLLM server (or a tunnel to it).

## What is verified locally vs by the operator

Verified in the R2 PR by CPU-only local runs with a **fake OpenAI-compatible endpoint**:

- `scripts/local_fake_dry_run.py` exercises the notebook's path end to end: endpoint probe
  (both transports), 600-task smoothing over the real committed splits, detector refit with
  the real frozen Qwen3-Embedding encoder, a real 5-task × 9-condition dry run over the real
  derived hidden tests in two config-stable shards, and the aggregate report. It uses no
  GPU and no paid API.
- `uv run pytest` covers the smoothing artifact and overlay, the endpoint probe, sharded
  resumable runs, the report/recovery maths, and the fake-endpoint nine-condition pipeline.
- The notebook JSON is parsed and every code cell is compiled in `tests/test_notebook.py`.

**Not verified locally:** vLLM serving on a Colab A100 or L4, the real Qwen3-8B-AWQ download,
native tool-call availability, GPU memory/context limits, Colab session limits and the
Drive snapshot. The operator must verify those and record the results (checklist at the end).

## 1. Before you start

| Item | Requirement |
| --- | --- |
| Runtime | Colab **A100** preferred (40/80 GB). An **L4 (24 GB)** works and is accepted by the notebook, but is 2–3× slower; record the actual GPU in `data_provenance.json` and expect more GPU-hours. A T4 is out of scope. |
| Time | One 12 h session may not fit everything; the notebook runs the pilot in two config-stable shards and resumes. |
| Budget | Target **~18 GPU-hours** of vLLM time; shards are wall-clock measured and written to `gpu_time.json`. |
| Disk | ~60 GB free: project env, a separate vLLM env, Qwen3-8B-AWQ (~6 GB), Qwen3-Embedding (~1.2 GB), datasets, traces. |
| GitHub | A **repo-scoped** token with read + contents write, stored as the Colab secret `GITHUB_TOKEN` (notebook access enabled). Used for clone and the optional results branch; never printed. |
| Hugging Face | Public models; optional `HF_TOKEN` secret for rate limits. |
| Persistence | Optional Google Drive mount. `PERSIST_TO_DRIVE = True` snapshots results after each shard and restores them on reconnect. |

The repository token is read through an environment-backed git credential helper, so it does
not appear in a URL or command. If you cannot use a token, the notebook offers an uploaded
repository archive fallback; in that case the optional results push is unavailable.

## 2. Run order and expected wall-clock

Run the notebook top to bottom. These are planning estimates, not guarantees; record the
actual times in `gpu_time.json`.

| Step | What it does | Where | Expected time |
| --- | --- | --- | --- |
| 0 | Runtime/GPU check | Colab | <1 min |
| 1 | Token, clone at `main`, record commit | Colab | 1–2 min |
| 2 | Install `uv`, `uv sync --frozen` (CPU project env) | Colab | 3–8 min |
| 3 | Drive restore **or** `make levels` (downloads + canonical validation) | CPU | restore <2 min; fresh `make levels` 15–40 min |
| 4 | Install vLLM in `/content/vllm-env`, start server, download model | GPU | 10–30 min including download |
| 5 | Probe `/v1/models`, native tool calls, text fallback; write `endpoint.json` | GPU | <2 min |
| 6 | Smooth 500 train + 100 pilot wishes | GPU | 5–20 min |
| 7 | Detector refit on smoothed wishes (frozen encoder, CPU) | CPU | 5–20 min |
| 8 | 5-task × 9-condition dry run + traces/cost/time | GPU | 10–40 min |
| 9 | Pilot: 2 shards × (100 tasks × 3 samples × 9 conditions) | GPU | **A100 ~6–9 h per shard (18 GPU-h target); L4 ~2–3× longer** |
| 10 | Aggregate report and verification | CPU | <1 min |
| 11 | Zip download and optional results branch/PR | CPU | 1–10 min |

The pilot has **2,700 units** (100 × 3 × 9), plus B2 expands each unit into 5 direct samples.
A unit is one `(condition, task, sample)` trace. The shard split is by unit index modulo the
shard count, so each shard contains a mix of conditions and the config hash stays identical.
The session guard starts no new shard with less than 30 min left.

## 3. Step details

### 3.1 Runtime, secrets, clone

- Runtime → Change runtime type → **A100 GPU** (preferred) or **L4**. The notebook checks for one of the two and records which was used.
- Runtime → Secrets → add `GITHUB_TOKEN` (repo-scoped: contents read/write) and enable
  notebook access. Optional `HF_TOKEN`.
- The clone is `--depth 1 --branch main`; the exact commit is printed and included in every
  manifest and the results `COLAB_RUN.md`.

### 3.2 `make levels`

`make levels` runs `uv sync`, installs `requirements-validation.txt`, downloads the three
pinned dataset revisions, validates every canonical solution, and writes the committed
`results/levels/` artifacts plus the gitignored hidden tests under `data/derived/levels/`.
The notebook requires **1,100 hidden tests** before continuing. If a Drive snapshot is
restored, `data/` is restored too and this step is skipped.

The committed R0 `tasks.jsonl` SHA-256 is pinned in the notebook
(`EXPECTED_LEVELS_SHA256 = b80c7f72…`). A different library set can rebuild a different
1,100-task composition; the notebook stops unless `ALLOW_LEVELS_DRIFT = True`. If you set
it, commit the run's `results/levels/` and `data_provenance.json` with the results, and
never mix the committed R0 stats with the rebuilt split.

If `make levels` reports a shortfall, do not pad the data: record the shortfall and stop.
The R0 artifact is deterministic apart from library drift, which the manifest records.

### 3.3 vLLM server

The notebook installs vLLM into a separate environment and starts exactly the ticket command:

```bash
/content/vllm-env/bin/vllm serve Qwen/Qwen3-8B-AWQ \
  --max-model-len 16384 --gpu-memory-utilization 0.90 --port 8000
```

It waits until `http://127.0.0.1:8000/v1/models` responds, logging to `logs/vllm.log`.
`ENABLE_NATIVE_TOOL_CALLS = True` adds:

```bash
--enable-auto-tool-choice --tool-call-parser hermes
```

Without those flags, vLLM normally rejects or ignores OpenAI `tools`, so the harness uses
the JSON text protocol. Do not guess: the next step records the working transport.

### 3.4 Endpoint probe (record the transport)

`python -m wishrec.harness.endpoint_check` checks `/v1/models`, then makes one native tool
call and one text-protocol call with a trivial `echo` tool. It writes
`results/runs/r2-pilot/endpoint.json` with:

- model ids from `/v1/models`;
- `native.ok` / `native.error` and `text.ok` / `text.error`;
- `selected_transport`: `native` or `text`;
- a sourceable `configs/vllm.env` with `VLLM_TOOL_MODE=<selected>`.

If neither transport works, the step fails; do not start the pilot. The probe never writes
a real key (`VLLM_API_KEY=EMPTY` for local vLLM).

### 3.5 L3 smoothing

R0's L3 is the raw first intent sentence. R2 smooths the **500 detector-train** wishes and
the **100 pilot** wishes with Qwen3-8B at temperature 0:

```bash
PYTHONPATH=src .venv/bin/python -m wishrec.harness.smoothing \
  --run-id r2-pilot --splits train pilot --workers 4
```

The artifact is `results/runs/r2-pilot/smoothing/wishes.jsonl` (one record per task:
raw wish, smoothed wish, changed/fallback flags, model, timestamp, duration) plus a manifest
with the SHA-256. It is resumable: completed task keys are skipped. The 300 held-out tasks
are never sent to the endpoint.

Check the manifest: 600 records, `complete: true`, splits `{train: 500, pilot: 100}`, and a
fallback count you can explain. Fallbacks mean the model returned empty or unchanged text and
the raw wish was kept; a high fallback rate means the prompt/model is not behaving and should
be investigated before the detector refit.

### 3.6 Detector refit

The frozen `Qwen/Qwen3-Embedding-0.6B` encoder and the linear head are unchanged; only the
training text changes. The refit writes **`results/detector-smoothed/`** (model, metrics,
manifest, CV predictions, report) and leaves the committed R1 `results/detector/` intact:

```bash
PYTHONPATH=src .venv/bin/python -m wishrec.detector.train \
  --run-id r2 --smoothed-wishes results/runs/r2-pilot/smoothing/wishes.jsonl \
  --output results/detector-smoothed
```

Record whether the pre-smoothing R1 detector was retrained (`RETRAIN_R1_DETECTOR`, default
False uses the committed artifact) in `results/runs/r2-pilot/r1_detector.json`, with its
SHA-256. The pilot's H3/DISCARD conditions always use the smoothed refit. Compare the refit's
macro-F1 / AUROCs to `results/detector/metrics.json`; if they collapse, stop and inspect the
smoothed wishes rather than running 18 GPU-hours against a broken detector.

### 3.7 Five-task dry run

Every condition runs on the first five pilot tasks with one sample (45 units), using the
smoothed wishes and the refit detector. The notebook prints each unit's compact trace, token
totals, `$0` paid cost, GPU name and wall time, and requires exactly 45 units. A fresh dry run
is enforced: restored dry-run units and `results/cache` are cleared first, and the cell
refuses a result completed in under 60 s or with zero tokens (that is a cache/snapshot
replay, not an endpoint test). Do not start
the pilot if a condition fails systematically, the transport changes mid-run, or a 400
context-length error appears (see troubleshooting).

### 3.8 The pilot

```bash
PYTHONPATH=src .venv/bin/python -m wishrec.harness.runner pilot \
  --run-id r2-pilot --samples 3 --workers 2 --shards 2 --shard 0 \
  --smoothed results/runs/r2-pilot/smoothing/wishes.jsonl \
  --detector results/detector-smoothed/model.json \
  --output results/runs/r2-pilot
```

- `pilot` selects only the disjoint 100-task development split; `--split heldout` is refused.
- Units are written atomically under `results/runs/r2-pilot/units/<condition>/<sample>/`.
- Resume skips units already complete **and free of API errors**; a unit whose loop hit an
  API error is retried on the next invocation. The config hash covers tasks, conditions,
  samples, endpoint identity, smoothing artifact SHA-256 and detector SHA-256, so changing
  any of those without `--force` is refused instead of silently mixing runs.
- `--shards/--shard` only change which units this session executes; the manifest keeps the
  full plan and records each shard's finish. Each shard rewrites the aggregate `summary.json`
  and `report.md`.
- After each shard the notebook snapshots `results/runs`, `results/detector-smoothed`,
  `results/cache`, `data/` and `logs/` to Drive and appends a marker to
  `results/runs/r2-pilot/shards.jsonl`.

Change `WORKERS` only after checking vLLM throughput and memory; 2 is the documented
default. Do not change `SAMPLES`, `SHARDS`, `RUN_ID` or the task selection between sessions,
or the config hash will reject the run.

### 3.9 Report

```bash
PYTHONPATH=src .venv/bin/python -m wishrec.harness.report results/runs/r2-pilot --require-complete
```

The report writes `summary.json` and `report.md` with:

- pass@1 / pass rate per condition (B2's unit `pass` is any of its five samples; its
  `pass_at_1` is the first sample); recovery uses pass@1;
- **recovery** = `(pass@1(c) - pass@1(H0)) / (pass@1(B1) - pass@1(H0))`; B2 uses its
  first direct sample as pass@1;
- **per-category recovery** grouped by the L0 category that a task's L3 omits
  (`signature_types`, `examples`, `constraints`, `error_behaviour`). The 9-condition pilot
  does not run separate L2_c single-field-drop conditions, so this grouping is the
  attribution available without extra GPU hours; the report says so.
- failure buckets by exception, token totals, `$0` paid cost, wall-clock/GPU-hour estimate,
  missing unit counts, and a held-out-usage check (must be 0).

`--require-complete` exits non-zero unless all 2,700 units exist and no held-out task was
used. The notebook reruns without that flag on a partial run so you can see progress.

## 4. Resume after a disconnect or session end

1. Reconnect with an **A100** (or L4) runtime and rerun cells 0–7. The notebook mounts Drive,
   restores the latest snapshot (including `data/` and `results/runs/`), and restarts vLLM.
   Re-run the endpoint probe; it should select the same transport.
2. Rerun the shard cell. `shards.jsonl` skips completed shards; within a shard, completed
   units are skipped and API-error units are retried.
3. If Drive persistence is off, copy the whole `results/` tree and `data/` out of the dying
   session before it ends (the zip cell can still run if the runtime is alive), then restore
   them into the fresh clone before rerunning.
4. After the last shard, run the report and bundle cells. Do **not** change the config
   between sessions; if you must (e.g. raising `--max-model-len`), the config hash does not
   include the server flag, but record the change in the run notes and re-run affected units.

A 12-hour Colab session should fit two 6–9 GPU-hour shards with headroom for model load.
Decide `SHARDS` **before** the first pilot shard starts: if the dry run or the start of shard
0 suggests the current plan would exceed ~10 h, stop early, delete the shard markers and
restart the run directory with a higher `SHARDS` (the config hash does not include shard
count, so the markers, not the units, are what would be inconsistent). Once shards are
underway, keep the same `SHARDS` and continue across sessions; the restart cost is only the
units already completed, which are skipped.

## 5. Alternative: run vLLM in Colab, harness locally

If you prefer to keep the harness and detector on your laptop while the A100 only serves the
model:

1. Run cells 0–4 of the notebook to start vLLM, then expose the port with a tunnel:

   ```bash
   # cloudflared (no account needed for a quick tunnel)
   !wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O /usr/local/bin/cloudflared
   !chmod +x /usr/local/bin/cloudflared
   !nohup cloudflared tunnel --url http://127.0.0.1:8000 > /content/cloudflared.log 2>&1 &
   ```

   Read the `https://….trycloudflare.com` URL from the log. `ngrok http 8000` works the same
   way if you already have ngrok. Treat the tunnel URL as a temporary credential: anyone with
   it can use the endpoint, so stop the tunnel when done and never commit it.

2. On the local machine (CPU-only steps):

   ```bash
   make levels
   cp configs/vllm.env.example configs/vllm.env
   export VLLM_BASE_URL=https://<tunnel-host>/v1 VLLM_API_KEY=EMPTY VLLM_MODEL=Qwen/Qwen3-8B-AWQ
   PYTHONPATH=src uv run python -m wishrec.harness.endpoint_check --run-id r2-pilot
   PYTHONPATH=src uv run python -m wishrec.harness.smoothing --run-id r2-pilot --splits train pilot
   PYTHONPATH=src uv run python -m wishrec.detector.train --run-id r2 \
     --smoothed-wishes results/runs/r2-pilot/smoothing/wishes.jsonl \
     --output results/detector-smoothed
   PYTHONPATH=src uv run python -m wishrec.harness.runner pilot --run-id r2-pilot \
     --samples 3 --workers 2 --shards 2 --shard 0 \
     --smoothed results/runs/r2-pilot/smoothing/wishes.jsonl \
     --detector results/detector-smoothed/model.json
   ```

   Keep the Colab tab alive for the whole run; the 18 GPU-hour budget is unchanged. The
   notebook's Drive persistence does not apply to local runs, so keep `results/runs/` and
   `data/` locally.

3. If the tunnel dies mid-run, restart it and update `VLLM_BASE_URL`; the generator identity
   in the config hash includes the base URL, so use `--force` only for units that failed
   against the dead endpoint, or accept that the rerun will refuse a config change. Prefer
   the in-Colab path for a clean manifest.

## 6. Troubleshooting

### No A100 / CUDA out of memory at model load

- The notebook requires an A100 and stops if `nvidia-smi` does not name one.
- Qwen3-8B-AWQ is an AWQ checkpoint; install vLLM with AWQ support (the default wheel has
  it). If loading fails, first confirm the model id and that the weight format is AWQ.
- `--gpu-memory-utilization 0.90` assumes the A100 is otherwise idle. On a shared or
  pre-allocated GPU lower it to `0.85`; if 16k context still OOMs at load, try
  `--max-model-len 8192` for a smoke test, then restore 16384 for the pilot, or use
  `--enforce-eager` (slower, less memory overhead).
- Delete a stale vLLM process before restarting: `pkill -f "vllm serve"` and wait for the
  GPU memory to be released.

### Context-length errors during H4 or long loops

The H4 prompt includes five sibling implementations and can grow near 16k tokens across 12
turns. vLLM returns a 400 `maximum context length` error; the unit records `api_error` and
the runner retries it on a later invocation. If this recurs:

1. restart vLLM with `--max-model-len 32768` (AWQ 8B + 32k KV fits on a 40 GB A100 at
   `--gpu-memory-utilization 0.90` in most cases; verify with `nvidia-smi`),
2. rerun the affected shard; API-error units are retried, completed units are skipped.

Do not silently shrink the H4 sibling context: the condition is defined by that context.

### Native tool calls are unavailable / 400 "auto tool choice is not enabled"

This is expected with the ticket's plain `vllm serve` command. The probe records native as
failed and selects `text`; the JSON text protocol is fully supported. To prefer native calls,
restart vLLM with `--enable-auto-tool-choice --tool-call-parser hermes` (Qwen3's parser) and
re-run the probe. If both probes fail, do not start the pilot: check the model id, the chat
template, and the vLLM log; the probe's recorded errors are the evidence.

### Model download is slow or fails

Set `HF_HOME=/content/models` (the notebook already does), retry with `HF_TOKEN` if rate
limited, and check free disk. Qwen3-8B-AWQ is ~6 GB and Qwen3-Embedding-0.6B ~1.2 GB. A
partially downloaded cache can be resumed; a corrupted blob should be removed and fetched
again. The vLLM wait loop allows 35 minutes.

### `make levels` fails or reports a shortfall

- Install/retry the pinned validation libraries (`requirements-validation.txt`); some
  BigCodeBench tasks need them for canonical validation.
- Network flakiness: rerun `make levels`; downloads are cached under `data/raw/` and
  validation results under `data/cache/validation/`.
- A shortfall is data, not a bug: record the exact shortfall from `results/levels/manifest.json`
  and stop; do not pad or substitute tasks.

### The detector refit looks wrong

Compare `results/detector-smoothed/metrics.json` with the committed R1
`results/detector/metrics.json`. A large macro-F1/AUROC drop usually means the smoothed
wishes are degenerate (empty, truncated, or all identical). Inspect a sample of
`smoothing/wishes.jsonl`, check the fallback count and the model id, and rerun the smoothing
with `--force` if needed. Do not change labels or the held-out boundary.

### Colab disconnects

Rerun from cell 0; restore is automatic when Drive is mounted. Completed units are skipped,
API-error units are retried, and completed shard markers prevent redundant shard runs. See
section 4.

### Results branch / token problems

The token is only passed through the git credential helper environment. If the push fails,
check that the token has **contents write** on `yb2630/superagent`; a read-only token can
still clone but not push. The notebook refuses to package any file containing the token.
Never paste a token into a cell, issue comment or the results directory.

### B3 frontier model

With no `VLLM_FRONTIER_*` variables, B3 reuses the same Qwen3-8B endpoint at temperature
0.7, which is the documented `$0` behaviour. The run manifest records the frontier identity;
do not add a paid endpoint for this pilot.

## 7. Operator checklist

Record each answer in the PR/issue thread:

- [ ] A100 GPU name and vLLM version recorded in `environment.json`; `/v1/models`
      returned `Qwen/Qwen3-8B-AWQ`.
- [ ] `endpoint.json` records native and text probe results and the selected transport; the
      pilot used that transport throughout.
- [ ] `make levels` completed with 1,100 hidden tests and the expected 500/200/300 + 100
      split, or the run stopped on a recorded shortfall.
- [ ] Smoothing manifest: 600 records, `complete: true`, splits `{train: 500, pilot: 100}`,
      fallback count explained; artifact SHA-256 recorded.
- [ ] Detector refit on smoothed wishes completed; `results/detector-smoothed/metrics.json`
      and `report.md` exist; R1 retrain choice and SHA-256 recorded in `r1_detector.json`.
- [ ] 5-task dry run: 45/45 units, traces/cost/GPU time printed, no systematic condition
      failure.
- [ ] Pilot: 2,700/2,700 units complete (or the exact missing units listed); B2 expands to
      five direct samples; held-out used = 0.
- [ ] `summary.json`/`report.md` contains pass@1, recovery, per-category recovery, failure
      buckets; GPU-hours are recorded and roughly match the ~18 h target; paid cost = $0.
- [ ] `r2-artifacts.zip` downloaded and/or a results branch/PR opened; it contains no token.
- [ ] The 300 held-out tasks were not run; `paper/milestone/` was not modified.

## 8. Artifact inventory

| Path | Contents |
| --- | --- |
| `results/runs/r2-pilot/smoothing/wishes.jsonl` | 600 smoothed wishes + provenance |
| `results/runs/r2-pilot/smoothing/manifest.json` | endpoint, splits, counts, artifact SHA-256 |
| `results/detector-smoothed/` | smoothed refit model, metrics, CV predictions, report |
| `results/runs/r2-pilot/endpoint.json` | `/v1/models`, native/text probes, selected transport |
| `results/runs/r2-pilot/r1_detector.json` | committed vs retrained pre-smoothing detector |
| `results/runs/r2-pilot/units/` | one trace per (condition, task, sample) |
| `results/runs/r2-pilot/results.jsonl` | compact per-unit results |
| `results/runs/r2-pilot/summary.json`, `report.md` | aggregate metrics |
| `results/runs/r2-pilot/gpu_time.json` | shard wall-clock and GPU-hour estimate |
| `results/runs/r2-pilot/environment.json` | GPU, vLLM, model, transport, hashes, commit |
| `results/runs/r2-dry/` | 5-task dry run traces, summary, dry_run.json |
| `r2-artifacts.zip` | downloadable bundle of the above (full traces included) |

## 9. Known limitations

- The 9-condition pilot does not run the L2_c single-field-drop conditions; per-category
  recovery is grouped by omitted L0 category and labelled as such in the report.
- The 100-task pilot is a development set; the 300 held-out tasks remain R3-only and every
  headline number must still average the seeds the milestone states.
- vLLM version, CUDA/torch stack and Colab hardware can drift; record them in the run
  manifest and the results branch. The repo pins datasets and the project environment, not
  the A100 runtime.
- `--max-model-len 16384` is the ticket's setting. If H4 context errors force 32768, record
  that operational change; it does not enter the run config hash.
- No paid API and no held-out leakage are enforced by the code and checked by the report;
  the operator still verifies the token/secret handling and the final artifact bundle.
