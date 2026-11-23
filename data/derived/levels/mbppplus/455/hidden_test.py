from solution import check_monthnumb_number
candidate = check_monthnumb_number
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


inputs = [[5], [2], [6], [1], [12], [10], [11], [9], [8], [True], [7], [3], [4]]
results = [True, False, False, True, True, True, False, False, True, True, True, True, False]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(check_monthnumb_number(*inp), exp, 0)

