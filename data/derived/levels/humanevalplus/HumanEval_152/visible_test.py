from solution import compare
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
    inputs = [[[1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[1, 2, 3], [-1, -2, -3]]]
    for inp in inputs:
        print(candidate(*inp))
check(compare)
