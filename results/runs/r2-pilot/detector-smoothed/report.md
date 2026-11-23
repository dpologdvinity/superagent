# R2 five-label silence detector

- Created: 2026-11-22T22:19:31+00:00
- Git commit: `8b355d660e61dfd6e8c0271a6d437153f314794d` (dirty)
- Data: 500 train tasks, split {'train': 500, 'heldout': 300, 'evolution': 200, 'pilot': 100}; held-out used: 0.
- Encoder: frozen `Qwen/Qwen3-Embedding-0.6B` (revision `97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3`), 1024-d, CPU.
- Head: linear 1024->5, BCE + L2, 600 full-batch AdamW steps, seed 20261121; deployed L2=0.3.

Label: 1 when the category has content in the full L0 specification, i.e. the wish
omits information the stakeholder can supply. `error_behaviour` has 63 positives in the 500 train tasks (147 across all 1,100 kept tasks); its metrics are reported, not declared undefined.

## Out-of-fold detection (5 folds, inner-fold L2/Platt calibration)

| method | macro-F1 | macro-F1 (varying labels) | AUROC examples | AUROC constraints | AUROC error | Brier | ECE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prior | 0.753 | 0.588 | 0.358 | 0.426 | 0.409 | 0.0741 | 0.0000 |
| tfidf | 0.777 | 0.629 | 0.746 | 0.944 | 0.699 | 0.0438 | 0.0089 |
| encoder | 0.772 | 0.621 | 0.803 | 0.931 | 0.739 | 0.0450 | 0.0155 |

## Per-category AUROC and Brier (encoder, calibrated OOF)

| category | positives | prevalence | AUROC | AP | F1@0.5 | Brier | ECE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| intent | 500 | 1.0000 | n/a | n/a | 1.000 | 0.0000 | 0.0025 |
| signature_types | 500 | 1.0000 | n/a | n/a | 1.000 | 0.0000 | 0.0025 |
| examples | 487 | 0.9740 | 0.803 | 0.993 | 0.987 | 0.0239 | 0.0111 |
| constraints | 317 | 0.6340 | 0.931 | 0.967 | 0.876 | 0.0997 | 0.0576 |
| error_behaviour | 63 | 0.1260 | 0.739 | 0.276 | 0.000 | 0.1013 | 0.0168 |

## H3 question policy

Score = calibrated presence probability x utility; one global threshold is
calibrated on deployed-style OOF scores and each task is clamped to 2-3 questions.

- Utility: {'intent': 0.0, 'signature_types': 0.5, 'examples': 0.2, 'constraints': 1.0, 'error_behaviour': 1.0}
- Threshold: 0.1972; mean questions 2.47; distribution {'2': 265, '3': 235}.
- Informative-pair precision 0.866, recall 0.573, utility recall 0.869.
- Selection rate by category: intent 0.00, signature_types 1.00, examples 0.48, constraints 0.80, error_behaviour 0.20

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