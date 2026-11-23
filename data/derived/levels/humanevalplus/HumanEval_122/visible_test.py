from solution import add_elements
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
    inputs = [[[1, -2, -3, 41, 57, 76, 87, 88, 99], 3], [[111, 121, 3, 4000, 5, 6], 2], [[11, 21, 3, 90, 5, 6, 7, 8, 9], 4]]
    for inp in inputs:
        print(candidate(*inp))
check(add_elements)
