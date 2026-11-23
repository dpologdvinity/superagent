# R2 GPU pilot report

- Generated: 2026-11-23T15:56:41+00:00
- Tasks: 100; conditions: 9; samples per condition: 3
- Units: 2700/2700 (complete)
- Held-out tasks used: 0
- Tokens: 19,356,531 (input 18,075,167, output 1,281,364); paid API cost: $0.00
- Wall clock: 2.9 h (2.9 GPU-h estimate); unit time 5.8 h

| condition | pass@1 | pass rate | recovery | questions | turns | cap hits |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | 0.623 | 0.623 | 1.000 | 0.00 | 4.34 | 21 |
| H0 | 0.520 | 0.520 | 0.000 | 0.00 | 4.40 | 17 |
| H1 | 0.287 | 0.287 | -2.259 | 0.00 | 4.51 | 10 |
| H2 | 0.443 | 0.443 | -0.743 | 2.94 | 6.36 | 29 |
| H3 | 0.537 | 0.537 | 0.162 | 2.48 | 4.43 | 14 |
| H4 | 0.517 | 0.517 | -0.032 | 0.00 | 4.74 | 38 |
| B2 | 0.513 | 0.547 | -0.065 | 0.00 | 5.00 | 0 |
| B3 | 0.310 | 0.310 | -2.033 | 0.00 | 1.00 | 0 |
| DISCARD | 0.427 | 0.427 | -0.903 | 2.48 | 4.09 | 11 |

## Per-category recovery

Tasks grouped by a category their L0 carries (so L3 omits it). The 9-condition
pilot does not run the separate L2_c single-field-drop conditions.

| category | tasks | B1 pass | H0 pass | H3 pass | H3 recovery |
| --- | --- | --- | --- | --- | --- |
| signature_types | 100 | 0.623 | 0.520 | 0.537 | 0.162 |
| examples | 99 | 0.623 | 0.522 | 0.532 | 0.100 |
| constraints | 57 | 0.632 | 0.450 | 0.485 | 0.194 |
| error_behaviour | 10 | 0.833 | 0.400 | 0.433 | 0.077 |

## Failure buckets

- `AssertionError`: 858
- `AttributeError`: 61
- `FileExistsError`: 3
- `FileNotFoundError`: 9
- `IndexError`: 7
- `KeyError`: 8
- `NameError`: 14
- `NoSolution`: 281
- `NonZeroExit`: 2
- `SyntaxError`: 5
- `Timeout`: 26
- `TypeError`: 92
- `ValueError`: 63
- `XMLSyntaxError`: 8

## Notes

- Recovery is computed from measured units only; B1 and H0 are the ceiling and floor.
- Per-category recovery groups tasks by the L0 category that the wish omits; the pilot does not run separate L2_c single-field-drop conditions.
- The 300 held-out tasks must not appear in any pilot unit.
