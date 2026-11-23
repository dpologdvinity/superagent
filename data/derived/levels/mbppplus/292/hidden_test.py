from solution import find
candidate = find
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


inputs = [[10, 3], [4, 2], [20, 5], [0, 5], [0, 1], [-1, 1], [1, 1], [0, 2], [5, 1], [6, 1], [-1, -1], [0, -1], [2, 1], [5, 5], [2, 2], [6, 6], [2, 5], [1, 6], [2, 4], [1, -1], [6, 5], [6, 2], [7, 7], [-1, 2], [5, 6], [-2, 2], [7, 4], [1, 2], [1, 7], [0, 4], [4, -1], [2, -2], [7, 6], [0, -2], [7, -1], [-2, 3], [3, 3], [5, -1], [-2, 6], [-2, -2], [7, 5], [6, -2], [-2, -1], [6, 4], [6, -1], [3, 5], [0, 7], [4, 5], [5, -2], [0, 6], [1, 4], [3, -1], [2, 3], [4, 4], [2, 6], [7, 1], [6, 7], [3, 4], [3, -2], [1, 5], [-1, 3], [3, 1], [-2, 1], [-2, 7], [2, -1], [5, 4], [0, 3], [-3, 1], [41, 41], [-2, 4], [5, 7], [5, 3], [-2, -3], [-1, 7], [-3, -3], [8, 4], [-3, -2], [4, 41], [-4, -2], [-4, 3], [4, -2], [8, -2], [-1, 6], [41, -1], [40, 41], [5, 41], [-4, 4], [-4, -4], [40, 5], [0, 8], [1, -2], [1, 41], [-3, 6], [8, 2], [8, 8], [-3, 7], [39, 8], [2, 8], [4, 6], [39, 3], [-3, -4], [41, 4], [41, -3]]
results = [3, 2, 4, 0, 0, -1, 1, 0, 5, 6, 1, 0, 2, 1, 1, 1, 0, 0, 0, -1, 1, 3, 1, -1, 0, -1, 1, 0, 0, 0, -4, -1, 1, 0, -7, -1, 1, -5, -1, 1, 1, -3, 2, 1, -6, 0, 0, 0, -3, 0, 0, -3, 0, 1, 0, 7, 0, 0, -2, 0, -1, 3, -2, -1, -2, 1, 0, -3, 1, -1, 0, 1, 0, -1, 1, 2, 1, 0, 2, -2, -2, -4, -1, -41, 0, 0, -1, 1, 8, 0, -1, 0, -1, 4, 1, -1, 4, 0, 0, 13, 0, 10, -14]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(find(*inp), exp, 0)

