# R2b local fake-endpoint dry-run evidence (not a result)

CPU-only verification of the corrected R2b operator path, run on 2026-11-23 with:

```bash
PYTHONPATH=src .venv/bin/python scripts/local_fake_dry_run.py --output-dir .local-dry-run
```

It uses the corrected committed `results/levels/` (tasks SHA-256
`e4cf7564b38e17c040b8a37837c4757a8b5d4045791a1621331c91a15cd36436`,
`parsing.visible_tests = inputs_only`), the real derived hidden tests and the real frozen
`Qwen3-Embedding-0.6B` encoder on CPU. The endpoint is an in-process fake
OpenAI-compatible server: no GPU, no vLLM and no paid API are used.

| step | observed |
| --- | --- |
| endpoint probe | native `True`, text fallback `True`, selected `native`; dry-run transport `text` |
| smoothing | 600 records (train 500, pilot 100), 0 fallbacks; artifact SHA-256 `95a7758146ab2287d9385175afca8d969ca18338eb9f4a177d00621932f05d41` |
| detector refit | completed; macro-F1 0.788, constraints AUROC 0.961 |
| 5-task × 9-condition dry run | 45/45 units over 2 config-stable shards (23 then 22); `complete`; held-out tasks used 0 |
| aggregate report | generated; 2,250 tokens, $0 paid API, 0.0 h wall/GPU estimate |
| elapsed | 165.1 s |

The fake endpoint always writes a `def solution(*args, **kwargs): return None` implementation,
so every unit's hidden suite fails with `ImportError` and the reported pass rates are 0. That
is expected plumbing output, not a model, detector or pilot result. The A100 execution is the
operator's separate step; the full command log is in the PR description.

Re-running the command regenerates `.local-dry-run/`; only this summary is committed.
