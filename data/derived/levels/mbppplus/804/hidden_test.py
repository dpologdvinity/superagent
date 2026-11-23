from solution import is_product_even
candidate = is_product_even
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


inputs = [[[1, 2, 3]], [[1, 2, 1, 4]], [[1, 1]], [[2, 2, 2, 2, 2]], [[1, 2, 3, 4, 5]], [[0, 0, 0, 0, 0]], [[1, 3, 5, 7, 9]], [[2, 4, 6, 8, 10]], [[2, -2, -2, -2, -2]], [[1, -2, 3, -4, 5]], [[-1, 2, 3, 5]], [[1, -2, 3, 5]], [[0, 2, 3, 5]], [[1, 3, 5, 7, 9, 1]], [[0, 9, 4, 5]], [[0, 2, 9, 3, 5]], [[-1, 2, 3, 4]], [[1, 3, 5]], [[1, -2, 1, 3, -4, 5]], [[1, 2, 3, 4, 3]], [[3, 3, 1, 2, 2, 2]], [[1, -2, 1, 3, -4, 5, -4]], [[-1, 2, 3, 4, 4]], [[1, 3, 5, 7]], [[-1, 2, 3, 5, 4, 4, 3]], [[-1, 2, 3, 2, 5, 3]], [[9, 5]], [[10, 0, 9, 4, 5, 9]], [[0, 2, 0, 2, 3, 5]], [[1, 3, 5, 3]], [[1, 1, 4, 3, 1]], [[-1, 7, 2, 3, 5]], [[1, 3, 5, 7, 7]], [[1, 1, 3, 10, 5, 3]], [[2, -2, -2, -2, -2, -2, -2]], [[3, 3, 1, 2, 4, 2, 2]], [[9, 1]], [[1, 10, 5, 3]], [[0, 9, 4, 5, 5]], [[0, 0, 0, 0, 0, 0, 0]], [[1, 1, 3, 10, 9, 5, 3, 9]], [[1, 1, 2, 5, 7]], [[1, 3, 7, 3, 3]], [[-1, 2, 3, 2, 5, 3, 3]], [[3, 1, 3, 7, 3, 3]], [[0, 0, 0, 1, 0, 0]], [[1, -2, 1, 3, -4, 5, -4, 1]], [[1, 10, 5, 2, 3]], [[0, 2, 9]], [[1, 2, 4, 3, 1]], [[2, 4, 6, 8, 10, 2]], [[-1, 7, 2, 3, 5, 3]], [[0, -1, 2, 9]], [[-1, 2, 3, 5, 4, 5, 3]], [[1, 1, 2, 1, 7, 1]], [[1, 1, 3, 10, 9, 5, 3, 3, 9]], [[1, 3, 8, 3]], [[1, 3, 5, 7, 9, 3]], [[1, 2, 3, 3]], [[2, -2, -2, -2, -2, -2]], [[1, 3, 7, 7]], [[3, 3, 1, 2, 1, 2, 2]], [[-1, 2, 3]], [[1, 10, 5]], [[0, 0, 0, 0, 0, 0, 0, 0]], [[8, 1, 3, 5, 4]], [[0, 0, 0, 0, 0, 0]], [[-1, 7, 2, 3, 5, 7]], [[3, 3, 1, 2, 10, 2, 2]], [[2, 9, -2, -2, -2, -2, -2]], [[1, 4, 3, 6]], [[1, 1, 3, -4, 5, -4, 1, 3]], [[7, 1, 5, 7, 9]], [[9, -1, -2, 5]], [[-1, 2, 3, 2]], [[1, 1, 2, 1, 5, 7]], [[0, 0, 0, 1, 0, 0, 0]], [[1, 1, 2, 1, 5, 7, 6, 2]], [[3, 3, 1, 2, -2, 2]], [[1, 5, 5, 3]], [[3, 6, 1, 2, 1, 2, 2]], [[-1, 1, 5, -2, 2, 3]], [[3, 5]], [[-2, 1, 3, -4, 5, -4, 1]], [[1, 4, 3, 1]], [[-1, 2, 3, 6, 4]], [[2, 4, 6, 9, 8, 10, 2]], [[3, 3, 1, 2, 2]], [[2, 3, 10, 5, 3]], [[4, -2, 4, 3, -4, 5, -2]], [[2, 10, 2, 3]], [[2, 1, 3, 8, 3, 3]], [[1, 0, 0, 0, 0]], [[2, 1, 3, 5, 7, 9, 1]], [[3, 1, 3, 7, 4, 3, 3]], [[0, 2, 9, 0, -1, 5]], [[3, 6, 1, 2, 1, -2, 2]], [[1, -2, 1, 3, -4, 5, -4, 1, -4]], [[1, 4, 5, 7]], [[0, -1, 0, 0, 0, 0]], [[-2, 0, 9, 4, 5]], [[-1, 2, 2, 3, 2, 2]], [[3, 3, 5]], [[2, 3, 6, 4, 3]], [[1, 3, 2, 3, 5, 5, 3]], [[-2, 0, 9, 4, 5, 0]], [[2, 4, 6, 8, 10, 2, 4]], [[1, 1, 2, 2, 5, 7]], [[3, 3, 1, 2, 10, 2, 2, 2]], [[-1, 2, 3, 2, 5, 3, 9, 3]], [[5, 2, 2, 2, 2, 2, 2]], [[3, 3, 1, 2, -4, 10, 2, 2, 2]]]
results = [True, True, False, True, True, True, False, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True, True, False, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(is_product_even(*inp), exp, 0)

