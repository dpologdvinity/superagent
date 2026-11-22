# What Does a Wish Leave Out?

Requirement recovery in wish-driven code agents. Columbia COMS 4705.

The milestone contract is [`paper/milestone/main.pdf`](paper/milestone/main.pdf); its source is
[`paper/milestone/main.tex`](paper/milestone/main.tex). The implementation is being rebuilt from
scratch to that design:

- generator: Qwen3-8B (AWQ) on vLLM, one 24 GB GPU;
- detector: Qwen3-Embedding-0.6B + five-label head;
- data: HumanEval+, MBPP+ and BigCodeBench, ~1,000 tasks with a 500/200/300 split;
- pilot: 100 development tasks, three samples.

R0 (scaffold and data foundation) is complete; R1-R3 follow. The design is in
[`PROJECT.md`](PROJECT.md), the rebuild plan is in [`PLAN.md`](PLAN.md), and the R0 data artifact
is in [`results/levels/`](results/levels/).

## Current state: R0 (scaffold + data foundation)

- pinned HumanEval+ (`d32357cf`), MBPP+ (`b2d74c91`) and BigCodeBench (`b74c0d0b`) downloads;
- mechanical five-field parsing, L0-L3 and `L2_c = L0 - c`;
- canonical-solution validation against one shared hidden suite and three visible tests;
- seeded, source-stratified 500/200/300 split plus a disjoint 100-task development pilot
  (1,100 kept; seed `20261121`);
- committed `results/levels/tasks.jsonl`, `manifest.json` and `stats.json`.

```bash
make test    # unit tests and committed-artifact checks; no network needed
make levels  # pinned download, parse, validation, split and committed artifacts
```
