from solution import test_duplicate
candidate = test_duplicate
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


inputs = [[[1, 2, 3, 4, 5]], [[1, 2, 3, 4, 4]], [[1, 1, 2, 2, 3, 3, 4, 4, 5]], [[2, 5, 1, 4, 3, 6, 7, 8, 9, 10]], [[]], [[-81, True, False]], [[-81, False, True, False]], [[2, 5, 1, 4, 3, 3, 6, False, 7, 8, 9, 10, 7]], [[False, -81, True, False]], [[False, -81, True, True, False, True]], [[False, -81, True, True, False, True, True]], [[-82, True, False]], [[False, -81, True, False, True, True, True]], [[5, 1, 4, 3, 6, 7, 8, 9, 10]], [[False, True, True, False, True, True]], [[-81, False, False]], [[2, 5, 1, 6, 4, 3, 6, 7, 8, 9, 10]], [[True, True, -81, True, False, True, True, True]], [[False, -81, True, False, True, True, True, False]], [[True, False, -81, False, True, True, True]], [[True, False, False, True, True, True, True]], [[2, 5, 1, 4, 3, 3, 6, False, 3, 8, 9, 10, 7]], [[False, -81, False, True, True, True, True]], [[-81, True, True, False, False]], [[False, False, True, True, False, True, True]], [[False, False, False]], [[False, -81, True, False, True]], [[True, False, False, True, True, True, True, True, True]], [[True, False, True, True, True, True, True, True]], [[True, True, True, -81, True, False, True, True, True]], [[2, 5, 1, 4, 3, 6, 7, 9, 10, 10]], [[-81, False, False, False, -81]], [[True, True, True, -81, True, False, True, True, True, True]], [[False, -81, True, False, True, True, True, False, -81, False]], [[False, True, False]], [[False, 9, False, True, False, True, True, True, False]], [[2, 1, 4, 3, 3, 6, False, 7, 8, 9, 10, 7]], [[False, -81, True, False, True, True, False, True, False]], [[False, False, -81, True, False, True]], [[-56, 3, 7, 10, 3, 7]], [[-56, 3, -82, 10, 3, 7]], [[False, False]], [[True, False, False, True, True, True, True, True]], [[False, False, -81, True, True, False, True, True]], [[-56, 3, -82, 4, 10, 3, 7, 10]], [[False, -81, True, False, True, True, True, True]], [[2, 5, 1, 4, 3, 1, 7, 9, 10, 10]], [[2, 5, 1, 6, 4, 3, 6, 7, 5, 9, 10, 7]], [[2, 5, 1, 4, 3, 6, 7, 8, 9, 10, 3]], [[-81, False, False, False]], [[False, -81, False, True, True, True, True, True]], [[-56, 3, 10, -56, 3, 7]], [[False, -81, True, True, False, True, True, True, True]], [[2, 5, 1, 6, 3, 4, 3, 6, 7, 9, 10, 8]], [[False, False, -81, False, False, False, False, True, False]], [[True, False, True, False]], [[-82, True, False, False, False]], [[2, -82, 1, 10, 3, 3, 6, False, 7, 8, 9, 10, 7, 10]], [[2, 5, 1, 9, 4, 3, 3, 6, False, 2, 8, 9, 10, 7, 3]], [[2, 5, 3, 4, 3, 3, 6, False, 3, 8, 9, 10, 7]], [[False, -81, True, False, True, True, False, True, False, False, False]], [[2, 5, 1, 9, 4, 3, 3, 6, False, 2, 8, 9, 10, 3]], [[2, -82, 1, 10, 4, 3, 6, False, 7, 8, 9, 10, 7, 10]], [[False, False, True, False, False, True, True]], [[2, 5, 1, False, 3, 4, 3, 6, 7, 9, 10, 8]], [[2, 5, 1, 6, 5, 3, 6, 7, 9, 10, 8, 9]], [[2, 5, 1, False, 3, 4, 3, 6, 7, 9, 10, 8, 3]], [[False, True, False, -81, True, True, False, True, True]], [[5, 1, 4, 3, 6, 7, 8, 9, 11]], [[False, -81, False]], [[False, -81, True, False, True, True, True, False, False, -81]], [[False, -81, True, False, True, -81]], [[2, 5, 1, 9, 4, 3, 6, False, 2, 8, 9, 10, 7, 3]], [[True, -81, True, True, False, True, True, True, True]], [[True, False, -81, False, True, True]], [[2, 5, 1, 4, 3, 6, 7, 8, 9, 10, 3, 9]], [[False, -81, True, False, True, False, True, False]], [[False, False, True, False, True]], [[2, 1, 3, 3, 6, False, 7, 8, 9, 10, 7]], [[False, True, False, True, False, True, False]], [[2, 5, 1, 9, 6, 4, 3, 6, 7, 4, 9, 10, 7]], [[False, -81, True, False, True, False]], [[2, 1, 3, 3, 6, 8, False, 7, 8, 9, 10, 7]], [[5, 9, 6, 4, 3, 6, 7, 4, 9, 10, 7]], [[-80, False, True, False, True]], [[False, False, True, False, True, False]], [[5, 1, 4, 3, 6, 7, 8, 9, 11, 3]], [[False, -81, True, False, True, True, False, False]], [[5, 1, 4, 3, 6, 7, 8, 9, 10, 3, 9, 6]], [[5, 1, 4, 3, 6, 7, 5, 9, 10, 7, 8]], [[-81, True, False, True, True, False, -81, False]], [[-82, True, False, False]], [[5, 9, 6, 4, 3, 6, 7, 4, 9, 8, 7]], [[True, -81, True, True, False, True, True, True, True, True]], [[False, -81, False, True, True, True, True, True, True]], [[-56, 3, 7, 10, 11, 3, 7, 3]], [[True, False, -81, False, False, False, False, False, True, False]], [[2, 1, 3, 3, 6, False, 8, False, 7, 8, 9, 10, 7]], [[-82, 7, True, False, False, False]], [[10, 2, 5, 1, 4, 3, 3, 6, False, 7, 8, 5, 9, 10, 7]], [[False, True, False, True]], [[-81, True, False, False, False, -81]], [[-81, True, False, True, True, False, True, False, False, False]], [[10, 2, 5, 1, False, 3, 3, 6, False, 7, 8, 5, 9, 10, 7]], [[False, True, False, False]]]
results = [False, True, True, False, False, False, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(test_duplicate(*inp), exp, 0)

