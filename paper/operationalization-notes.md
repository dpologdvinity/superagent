# Operationalization notes: measured-pilot caveats

Status: R4 disclosure (2026-11-23), applying to the measured R2 pilot at commit
`24c0f7c` with parser version `0.1.0`. The measured numbers are unchanged; this ticket
did not re-parse, re-run the detector or re-run the GPU pilot. These notes record the
code-level issues so the revised milestone and report can disclose them and the final
study can fix them.

## 1. Intent is the first sentence

`src/wishrec/parse.py::_classify_prose` (lines 211--235) sets

```python
intent = re.sub(r"^\s*Task\s+", "", sentences[0]).strip()   # line 216
```

and files every later sentence into `constraints` or `error_behaviour`. `parse_mbppplus`
repeats the pattern (`parse.py:487--495`: `intent = sentences[0]`). L3 keeps only the
intent (`src/wishrec/levels.py:9`, `render_level` at lines 64--100; `src/wishrec/artifacts.py:159`
asserts `L3 == fields["intent"]`). A requirement stated in the second sentence is
therefore classified as a constraint and deleted at L3.

Quantification on the 100 pilot tasks (`results/runs/r2-pilot/smoothing/wishes.jsonl`,
`split == "pilot"`; `raw_wish` is the parser intent):

- **0/100** raw intents have fewer than 5 whitespace tokens (minimum 6).
- **6/100** have fewer than 9 words: HumanEval/80, /160, /56, /58, /92 and
  BigCodeBench/467.
- Input-only examples: HumanEval/80 is exactly `You are given a string s.`; /160 is
  `Given two lists operator, and operand.`; /56 is `brackets is a string of "<" and ">".`
  The requirement is in the deleted constraint text (e.g. HumanEval/80's L0 constraint
  says to check whether the string is happy).
- The smoothed pilot wishes give **0/100 under five tokens and 8/100 under nine words**;
  smoothing does not restore the requirement that the parser put in constraints.

**Direction:** this attenuates H0 (the wish understates the task) and dilutes any measured
asking effect. The null should not be read as evidence that elicitation cannot work in
principle. The measured artifacts remain from parser `0.1.0`; a separate parser change
(whole-prose intent plus an `inputs_only` visible-test mode) is in review as PR #22 and is
not part of this run.

## 2. Visible tests re-supply examples

`src/wishrec/parse.py::_humaneval_visible_test` (lines 309--354) truncates the `check()`
`inputs` and `results` lists to the first three pairs (lines 330--336), then builds the
visible test and `visible_asserts` from those pairs. `parse_mbppplus` uses
`visible_asserts = "\n".join(test_list[:3])` (`parse.py:501`), and `_bcb_visible_test`
keeps the first three `test_*` methods (`parse.py:626--670`, `selected = tests[:3]` at
line 636).

The harness prints the visible test in every loop prompt
(`src/wishrec/harness/prompts.py::visible_block`, lines 76--82, included at line 182);
B3 is the only condition that omits it (`src/wishrec/harness/loop.py:449`). Example: the
H0 HumanEval/80 prompt in `results/runs/r2-pilot/units/H0/0/humanevalplus__HumanEval__80.json`
shows `inputs = [['a'], ['aa'], ['abcd']]` and `results = [False, False, True]`.

Consequence: the examples field is effectively never deleted in loop conditions. All 100
pilot tasks have `visible_asserts_count == 3` and 97/100 carry an `examples` field at L0
(`results/levels/tasks.jsonl`). Deleting examples at L1/L2/L3 or in an L2$_c$ examples drop
still leaves three input/expected-result pairs with the agent, so an examples effect cannot
be attributed cleanly.

## 3. Five-label head, two labels constant

`results/runs/r2-pilot/detector-smoothed/metrics.json` records
`data.label_counts = {intent: 500, signature_types: 500, examples: 487, constraints: 317,
error_behaviour: 63}` over the 500 train tasks. `detection.encoder.per_label.intent.auroc`
and `detection.encoder.per_label.signature_types.auroc` are both `null`, because those
labels are positive on every task.

The detector is therefore a **five-label head with two constant labels**, effectively a
three-label model; only the examples/constraints/error-behaviour AUROCs are usable, and
constraints (317 positives) and error behaviour (63) are sparse. The milestone and report
describe a five-label head with two constant labels rather than implying five usable AUROCs.

## Reading the measured null

The honest reading is not "elicitation does not work". The wish, stub and visible tests
already carry most of the requirement (H0 reaches 82% of B1), the parser deletes
second-sentence requirements at L3, and the visible tests re-supply examples. Under that
operationalization asking does not add: H3 is within noise of H2 and H4, H4 is at best a
+1.7 pp nudge (95% CI crosses zero), H1 costs 9.7 pp, and withholding answers costs 6.7 pp
against H3. These numbers trace to `results/runs/r2-pilot/summary.json`,
`bootstrap.json` and `report.md`.

## Reproduce

```bash
cd results/runs/r2-pilot
python3 - <<'PY'
import json, re
pilot = [json.loads(line) for line in open("smoothing/wishes.jsonl")]
pilot = [row for row in pilot if row["split"] == "pilot"]
words = lambda text: re.findall(r"[A-Za-z0-9_']+", text)
for field in ("raw_wish", "smoothed_wish"):
    under5 = [row["task_key"] for row in pilot if len(row[field].split()) < 5]
    under9 = [row["task_key"] for row in pilot if len(words(row[field])) < 9]
    print(field, "under5", len(under5), under5)
    print(field, "under9", len(under9), under9)
PY
```

The PDFs are rebuilt from `paper/milestone/` and `paper/` with
`TEXINPUTS=..:$TEXINPUTS BIBINPUTS=..:$BIBINPUTS latexmk -pdf main.tex` (milestone) and
`latexmk -pdf main.tex` (report).

## Submitted-milestone edits verified (do not regress)

The five text edits from the submitted-milestone audit are present in
`paper/milestone/main.tex` and are preserved:

1. Table 1 is the measured table (pass@1/recovery/questions/turns, $n=300$, source
   `results/runs/r2-pilot/`).
2. No 59/19 framing; the abstract uses the measured 58.3/47.7 and null contrasts.
3. The five-field code category list (intent, signature and types, examples, constraints and
   edge cases, error behaviour).
4. Detector metrics and failure attribution (macro-F1 0.772; AUROC 0.931 constraints,
   0.739 error behaviour; F1 at 0.5 is 0.000 with 63 positives and AP 0.276).
5. 2.509 GPU-hours, A100-SXM4-80GB, and the one-call B3 baseline (31.7%).
