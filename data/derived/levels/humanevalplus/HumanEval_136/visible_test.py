from solution import largest_smallest_integers
import numpy as np

def is_floats(x) -> bool:
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all((isinstance(i, float) for i in x))
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False

def assertion(out, exp, atol):
    exact_match = out == exp
    if atol == 0 and is_floats(exp):
        atol = 1e-06
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match

def check(candidate):
    inputs = [[[2, 4, 1, 3, 5, 7]], [[2, 4, 1, 3, 5, 7, 0]], [[1, 3, 2, 4, 5, 6, -2]]]
    for inp in inputs:
        print(candidate(*inp))
check(largest_smallest_integers)
