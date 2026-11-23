# R2 five-label silence detector

- Created: 2026-11-23T12:58:30+00:00
- Git commit: `6b236eb71d2aba4d00b5ad30b3a7412ae5f23b08` (dirty)
- Data: 500 train tasks, split {'train': 500, 'heldout': 300, 'pilot': 100, 'evolution': 200}; held-out used: 0.
- Encoder: frozen `Qwen/Qwen3-Embedding-0.6B` (revision `97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3`), 1024-d, CPU.
- Head: linear 1024->5, BCE + L2, 600 full-batch AdamW steps, seed 20261121; deployed L2=0.3.

Label: 1 when the category has content in the full L0 specification, i.e. the wish
omits information the stakeholder can supply. `error_behaviour` has 85 positives in the 500 train tasks (158 across all 1,100 kept tasks); its metrics are reported, not declared undefined.

## Out-of-fold detection (5 folds, inner-fold L2/Platt calibration)

| method | macro-F1 | macro-F1 (varying labels) | AUROC examples | AUROC constraints | AUROC error | Brier | ECE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prior | 0.746 | 0.577 | 0.251 | 0.442 | 0.472 | 0.0806 | 0.0096 |
| tfidf | 0.789 | 0.648 | 0.871 | 0.947 | 0.695 | 0.0470 | 0.0131 |
| encoder | 0.792 | 0.654 | 0.632 | 0.952 | 0.744 | 0.0439 | 0.0142 |

## Per-category AUROC and Brier (encoder, calibrated OOF)

| category | positives | prevalence | AUROC | AP | F1@0.5 | Brier | ECE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| intent | 500 | 1.0000 | n/a | n/a | 1.000 | 0.0000 | 0.0025 |
| signature_types | 500 | 1.0000 | n/a | n/a | 1.000 | 0.0000 | 0.0025 |
| examples | 491 | 0.9820 | 0.632 | 0.990 | 0.991 | 0.0177 | 0.0007 |
| constraints | 293 | 0.5860 | 0.952 | 0.974 | 0.925 | 0.0734 | 0.0491 |
| error_behaviour | 85 | 0.1700 | 0.744 | 0.315 | 0.046 | 0.1285 | 0.0513 |

## H3 question policy

Score = calibrated presence probability x utility; one global threshold is
calibrated on deployed-style OOF scores and each task is clamped to 2-3 questions.

- Utility: {'intent': 0.0, 'signature_types': 0.5, 'examples': 0.2, 'constraints': 1.0, 'error_behaviour': 1.0}
- Threshold: 0.1974; mean questions 2.48; distribution {'2': 260, '3': 240}.
- Informative-pair precision 0.835, recall 0.554, utility recall 0.856.
- Selection rate by category: intent 0.00, signature_types 1.00, examples 0.42, constraints 0.70, error_behaviour 0.37

## R2 limitations

- The encoder is frozen and the head is a single linear layer; there is no
  fine-tuning. The reported OOF numbers are the detector evidence, not a pilot
  result.
- The `error_behaviour` F1 at the default 0.5 threshold is 0 because its
  calibrated probability stays near the 12.6% base rate; AUROC and average
  precision are the informative ranking metrics for that label.
- Platt calibration is fitted on nested out-of-fold predictions of the train split;
  the 300 held-out and 100 pilot tasks are untouched.

- This artifact is the R2 refit: the 500 train wishes were smoothed by the
  generator endpoint and the frozen encoder/training recipe are unchanged.