# Harness run

- Run: `r2-dry`
- Tasks: 5
- Conditions: B1, H0, H1, H2, H3, H4, B2, B3, DISCARD
- Units: 45/45 (complete)
- Smoothed wishes: `6df69971144f3f4c7d18de3d8418a6b528aa93b1e6adebf8a6af2edf49a74a28`

| condition | passed | pass@1 | avg turns | avg questions | cap hits | buckets |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | 1/5 | 0.2 | 7.4 | 0.0 | 1 | AssertionError:2, NoSolution:1, ValueError:1 |
| H0 | 0/5 | 0.0 | 8.6 | 0.0 | 1 | AssertionError:4, ValueError:1 |
| H1 | 0/5 | 0.0 | 8.6 | 0.0 | 1 | AssertionError:2, NoSolution:2, ValueError:1 |
| H2 | 0/5 | 0.0 | 11.2 | 3.4 | 3 | AssertionError:3, ValueError:2 |
| H3 | 0/5 | 0.0 | 11.0 | 2.8 | 1 | AssertionError:4, ValueError:1 |
| H4 | 0/5 | 0.0 | 9.8 | 0.0 | 2 | AssertionError:4, ValueError:1 |
| B2 | 0/5 | 0.0 | 5.0 | 0.0 | 0 | AssertionError:4, ValueError:1 |
| B3 | 0/5 | 0.0 | 1.0 | 0.0 | 0 | AssertionError:2, TypeError:2, ValueError:1 |
| DISCARD | 0/5 | 0.0 | 8.8 | 2.8 | 0 | AssertionError:3, Timeout:1, ValueError:1 |

Only the development split may be used for a pilot; held-out results belong to
the final R3 report.
