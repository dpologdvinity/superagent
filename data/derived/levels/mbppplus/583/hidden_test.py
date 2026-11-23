from solution import catalan_number
candidate = catalan_number
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


inputs = [[10], [9], [7], [0], [1], [2], [3], [True], [4], [False], [5], [6], [8], [11], [12], [13], [15], [14]]
results = [16796, 4862, 429, 1, 1, 2, 5, 1, 14, 1, 42, 132, 1430, 58786, 208012, 742900, 9694845, 2674440]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(catalan_number(*inp), exp, 0)

