from solution import last
candidate = last
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


inputs = [[[1, 2, 3], 1], [[1, 1, 1, 2, 3, 4], 1], [[2, 2, 3, 3, 6, 8, 9], 3]]
results = [0, 2, 3]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(last(*inp), exp, 0)

