# Operationalization notes: final-pilot caveats

Status: disclosure for the final milestone (2026-11-23), applying to the measured R2b run in
`results/runs/r2b-pilot/` and the corrected levels in `results/levels/` (parser version
`0.2.0`, `visible_tests = inputs_only`). The headline numbers are unchanged by these notes;
the notes record what the protocol does and does not hold fixed.

## 1. Intent is the whole prose block

The earlier levels took the first docstring sentence as the intent and filed every later
sentence into `constraints` or `error_behaviour`, so a requirement stated in a second sentence
was deleted at L3 and the wish understated the task. The corrected parser keeps the whole
prose block before the examples as the intent; later unlabelled sentences stay part of the
request, while explicit `Constraints`/`Raises` labels and sentences carrying an error cue are
additionally classified into the constraint and error-behaviour fields.

Consequence: L3 is a natural request rather than the first sentence with later requirements
deleted. A parser bug that drops the later prose therefore no longer attenuates H0 or the
measured asking effect. The corrected build parsed 1,651 of 1,682 source rows (31 parse
exclusions) and validated 1,549, keeping 1,100 tasks. The parse exclusions are recorded in the
manifest, not silently dropped.

## 2. Visible tests and the examples field

Under the corrected protocol, HumanEval+ and MBPP+ visible tests exercise the same first three
inputs but print the observed output; expected values are removed. The agent therefore cannot
recover the examples field from the visible suite, which is what the level deletion assumes.
The harness still prints the visible program in every loop prompt, but it no longer contains
the expected results.

BigCodeBench is the stated residual. Its visible suite is a selection of `unittest` methods
whose expectations are hard-coded assertions rather than literal `(inputs, results)` pairs,
so `inputs_only` cannot remove them without breaking the suite. BigCodeBench's examples
therefore remain visible in both protocols; the examples field is not fully deleted for that
subset, and the per-category examples row is confounded accordingly. The papers state this
limitation rather than claiming a full examples deletion.

## 3. Five-label head, two labels constant

The detector has a five-label head, but `intent` and `signature_types` are positive on all 500
train tasks, so their AUROC is undefined and the detector is effectively a three-label model.
The committed smoothed refit records 293 constraints, 491 examples and 85 error-behaviour
positives. The usable ranking metrics are constraints AUROC 0.952, error-behaviour AUROC 0.744
and examples AUROC 0.632 (only 9 negatives, so the examples AUROC is not informative);
macro-F1 is 0.792 overall and 0.654 over the three varying labels. The error-behaviour F1 at
the deployed 0.5 threshold is 0.046 because the calibrated probability stays near the 17%
base rate; AUROC and average precision are the informative ranking metrics for that label.

## 4. Reading the measured result

The honest reading is not that elicitation works in general. The wish, stub and visible tests
already carry much of the requirement, and the pilot has 100 development tasks, one seed base
and one A100-40GB session. Under that protocol:

- B1 reaches 62.3% and H0 52.0%, so the specification gap is +10.3 pp [+3.0, +17.7].
- H3 reaches 53.7% (recovery 0.16) and beats generic H2 (44.3%) by +9.3 pp [+1.7, +17.0].
- H3 is not distinguishable from H0 (+1.7 pp [−5.7, +9.0]) or H4 (51.7%; +2.0 pp
  [−6.3, +9.7]).
- Withholding H3's answers (H3⁻, 42.7%) costs 11.0 pp [−18.7, −2.7] against H3.
- Generic questions cost 7.7 pp and acceptance tests first cost 23.3 pp against H0; H1's
  result is partly a protocol effect under inputs-only visible tests.

The defensible claim is relative: targeting beats generic asking, but it does not close the
specification gap.

## 5. Reproduce the caveats

From a fresh clone:

```bash
uv sync --frozen
make test
make levels
make detector-smoothed
```

`make levels` rebuilds the committed inputs-only levels from the pinned sources
(`results/levels/tasks.jsonl` SHA-256
`e4cf7564b38e17c040b8a37837c4757a8b5d4045791a1621331c91a15cd36436`). The detector refit is
CPU-only and uses the committed smoothed wishes under
`results/runs/r2b-pilot/smoothing/wishes.jsonl`; the pilot itself is the one step that needs a
GPU, and its committed traces are the evidence for every number above.
