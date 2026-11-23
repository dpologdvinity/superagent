# R2 GPU pilot report

- Generated: 2026-11-23T01:22:18+00:00
- Tasks: 100; conditions: 9; samples per condition: 3
- Units: 2700/2700 (complete)
- Held-out tasks used: 0
- Tokens: 21,756,260 (input 20,367,165, output 1,389,095); paid API cost: $0.00
- Wall clock: 2.51 h (2.51 GPU-h estimate); unit time 5.0 h

| condition | pass@1 | pass rate | recovery | questions | turns | cap hits |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | 0.583 | 0.583 | 1.000 | 0.00 | 4.86 | 26 |
| H0 | 0.477 | 0.477 | 0.000 | 0.00 | 4.88 | 21 |
| H1 | 0.380 | 0.380 | -0.907 | 0.00 | 5.35 | 14 |
| H2 | 0.490 | 0.490 | 0.125 | 2.75 | 6.66 | 38 |
| H3 | 0.487 | 0.487 | 0.094 | 2.52 | 5.35 | 27 |
| H4 | 0.493 | 0.493 | 0.156 | 0.00 | 5.42 | 43 |
| B2 | 0.483 | 0.523 | 0.062 | 0.00 | 5.00 | 0 |
| B3 | 0.317 | 0.317 | -1.501 | 0.00 | 1.00 | 0 |
| DISCARD | 0.420 | 0.420 | -0.532 | 2.52 | 4.79 | 14 |

## Per-category recovery

Tasks grouped by a category their L0 carries (so L3 omits it). The 9-condition
pilot does not run the separate L2_c single-field-drop conditions.

| category | tasks | B1 pass | H0 pass | H3 pass | H3 recovery |
| --- | --- | --- | --- | --- | --- |
| signature_types | 100 | 0.583 | 0.477 | 0.487 | 0.094 |
| examples | 97 | 0.581 | 0.488 | 0.481 | -0.074 |
| constraints | 64 | 0.568 | 0.401 | 0.385 | -0.094 |
| error_behaviour | 13 | 0.538 | 0.333 | 0.231 | -0.499 |

## Failure buckets

- `AssertionError`: 934
- `AttributeError`: 19
- `CalledProcessError`: 2
- `ImportError`: 1
- `IndexError`: 23
- `KeyError`: 27
- `LookupError`: 5
- `NameError`: 22
- `NoSolution`: 170
- `NonZeroExit`: 9
- `OverflowError`: 5
- `RuntimeError`: 5
- `SyntaxError`: 6
- `Timeout`: 6
- `TypeError`: 71
- `UnboundLocalError`: 5
- `ValueError`: 137
- `_UFuncNoLoopError`: 2

## Notes

- Recovery is computed from measured units only; B1 and H0 are the ceiling and floor.
- Per-category recovery groups tasks by the L0 category that the wish omits; the pilot does not run separate L2_c single-field-drop conditions.
- The 300 held-out tasks must not appear in any pilot unit.
