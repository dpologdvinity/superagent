# Harness run

- Run: `r2b-dry`
- Tasks: 5
- Conditions: B1, H0, H1, H2, H3, H4, B2, B3, DISCARD
- Units: 45/45 (complete)
- Smoothed wishes: `293a4a8b2b53d792c9f219b7cbc7c8f388ad68e93264ad0db4575b7cfe9bc5ea`

| condition | passed | pass@1 | avg turns | avg questions | cap hits | buckets |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | 4/5 | 0.8 | 4.8 | 0.0 | 0 | TypeError:1 |
| H0 | 2/5 | 0.4 | 7.2 | 0.0 | 2 | AssertionError:2, ValueError:1 |
| H1 | 0/5 | 0.0 | 2.6 | 0.0 | 0 | AssertionError:1, NoSolution:3, XMLSyntaxError:1 |
| H2 | 2/5 | 0.4 | 7.4 | 2.8 | 1 | AssertionError:2, NoSolution:1 |
| H3 | 3/5 | 0.6 | 6.2 | 3.0 | 1 | AssertionError:1, ValueError:1 |
| H4 | 2/5 | 0.4 | 7.0 | 0.0 | 1 | AssertionError:1, TypeError:1, ValueError:1 |
| B2 | 2/5 | 0.2 | 5.0 | 0.0 | 0 | AssertionError:2, NameError:1 |
| B3 | 1/5 | 0.2 | 1.0 | 0.0 | 0 | AssertionError:1, AttributeError:1, TypeError:2 |
| DISCARD | 3/5 | 0.6 | 6.4 | 3.0 | 0 | AssertionError:2 |

Only the development split may be used for a pilot; held-out results belong to
the final R3 report.
