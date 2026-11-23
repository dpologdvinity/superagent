from solution import skjkasdkd
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
    inputs = [[[0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]], [[1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]], [[1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]]]
    for inp in inputs:
        print(candidate(*inp))
check(skjkasdkd)
