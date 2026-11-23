from solution import fruit_distribution
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
    inputs = [['5 apples and 6 oranges', 19], ['5 apples and 6 oranges', 21], ['0 apples and 1 oranges', 3]]
    for inp in inputs:
        print(candidate(*inp))
check(fruit_distribution)
