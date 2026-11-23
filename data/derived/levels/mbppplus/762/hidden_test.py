from solution import check_monthnumber_number
candidate = check_monthnumber_number
import numpy as np
from math import inf

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if out != exp and atol != 0:
        assert np.allclose(out, exp, rtol=1e-07, atol=atol)
    else:
        assert out == exp, f"out: {out}, exp: {exp}"


inputs = [[6], [2], [12], [1], [True], [3], [4], [5], [7], [9], [10], [8], [11]]
results = [True, False, False, False, False, False, True, False, False, True, False, False, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(check_monthnumber_number(*inp), exp, 0)

