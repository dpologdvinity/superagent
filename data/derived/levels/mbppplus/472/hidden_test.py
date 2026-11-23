from solution import check_Consecutive
candidate = check_Consecutive
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


inputs = [[[1, 2, 3, 4, 5]], [[1, 2, 3, 5, 6]], [[1, 2, 1]], [[4, 1, 9, 5, 2]], [[4, 9, 5, 2]], [[4, 5, 1, 9, 5, 2]], [[4, 5, 1, 9, 5, 2, 2]], [[4, 4, 9, 5, 2]], [[4, 5, 1, 9, 5, 2, 2, 2]], [[5, 1, 9, 5, 2]], [[4, 1, 9, 5, 2, 9]], [[4, 5, 1, 9, 5, 2, 2, 5]], [[5, 1, 9, 1, 2]], [[4, 2, 4, 9, 5, 2]], [[4, 1, 0, 9, 5, 2, 9]], [[4, 9, 5, 3]], [[0, 9, 2, 9]], [[4, 1, 5, 2, 9]], [[4, 5, 1, 9, 5, 5, 2, 2]], [[4, 5, 1, 9, 5, 2, 1]], [[4, 5, 1, 9, 6, 2, 2]], [[1, 4, 5, 2]], [[4, 5, 1, 5, 5, 2, 1, 5]], [[5, 1, 9, 1, 1, 2]], [[4, 9, 5, 2, 9]], [[0, 4, 2, 9]], [[4, 9, 1, 5]], [[1, 5, 1, 9, 4, 5, 2]], [[1, 5, 1, 9, 2, 4, 5, 2]], [[5, 1, 3, 1, 1, 2]], [[9, 2, 9, 9, 0, 0, 9]], [[5, 1, 9, 5, 2, 9]], [[6, 5, 1, 5, 5, 2, 1, 5]], [[4, 2, 3, 4, 9, 5, 2]], [[4, 2, 9, 3, 2]], [[4, 2, 9, 3, 2, 9]], [[2, 9, 2, 9, 9, 0, 0, 9]], [[2, 4, 5, 1, 0, 2, 9, 5, 2, 2, 5]], [[4, 3, 5, 1, 9, 5, 5, 2, 2]], [[4, 9, 5]], [[1, 4, 9, 2]], [[4, 5, 1, 6, 5, 2, 1, 5]], [[6, 5, 1, 9, 2, 4, 2]], [[3, 2, 4, 9, 5, 2]], [[4, 1, 9, 5]], [[4, 9, 1, 4, 9]], [[4, 2, 9, 2, 3, 2, 9]], [[1, 4, 2]], [[4, 5, 1, 9, 5, 5, 9, 2]], [[4, 5, 1, 6, 5, 2, 1, 5, 6]], [[4, 5, 1, 9, 5, 2, 1, 9]], [[4, 3, 1, 0, 9, 5, 2, 9]], [[4, 9, 5, 3, 5, 3]], [[5, 1, 5, 2]], [[4, 5, 3, 9, 5, 2]], [[4, 5, 1, 9, 5, 2, 9]], [[4, 3, 3, 4, 5, 2]], [[5, 5, 1, 9, 5, 2]], [[4, 2, 3, 4, 9, 5, 2, 9, 3]], [[4, 2, 9, 2, 3, 2, 9, 2]], [[4, 6, 6, 3, 9, 5, 2, 5]], [[5, 9, 5, 2, 9]], [[4, 2, 6, 3, 4, 9, 5, 2, 9, 3]], [[4, 2, 9, 2, 9, 9]], [[4, 5, 1, 9, 5, 2, 1, 1]], [[2, 9, 2, 9, 9, 0, 0, 9, 0]], [[2, 9, 9, 0, 0, 9]], [[4, 5, 5, 9, 5, 2, 2, 2]], [[4, 4, 2, 3, 4, 9, 5, 2, 9, 3]], [[1, 5, 2]], [[1, 5, 1, 9, 2, 4, 2]], [[2, 4, 5, 1, 0, 2, 9, 5, 2, 2, 4, 5]], [[4, 5, 1, 9, 5, 2, 8]], [[1, 4, 5]], [[2, 9, 9, 9, 0, 0, 9, 0]], [[1, 4, 9, 8, 2, 2]], [[4]], [[5, 1, 5, 1, 9, 2, 4, 5, 2, 1]], [[4, 3, 5, 1, 10, 9, 5, 2, 1, 1]], [[1, 1, 9, 2, 4, 6, 2]], [[4, 1, 5, 2, 9, 4]], [[4, 1, 9, 0, 9, 2, 9]], [[5, 1, 9, 5, 5, 2]], [[1, 5, 1, 9, 2, 4, 2, 2]], [[4, 5, 1, 9, 1, 8, 2, 2]], [[4, 1, 9, 10]], [[4, 3, 5, 1, 9, 5, 5, 2, 2, 2]], [[6, 6, 1, 9, 4, 2]], [[4, 1, 9, 5, 5, 2, 2]], [[4, 9, 10, 5, 3, 5, 3]], [[5, 1, 9, 2]], [[6, 6, 1, 9, 4, 1]], [[4, 1, 5, 8, 2, 9, 4]], [[4, 5, 1, 6, 5, 2, 1, 5, 5]], [[6, 6, 1, 9, 1, 6, 6]], [[4, 6, 5, 1, 9, 5, 2, 2, 2]], [[1, 5, 1, 9, 2, 4, 2, 8, 2, 1]], [[4, 5, 1, 1]], [[4, 5, 1, 4, 1]], [[4, 1, 5, 8, 2, 9]], [[0, 4, 9]], [[4, 1, 1]], [[4, 5, 1, 5, 5, 5, 9, 2]], [[4, 2, 9, 2, 9, 9, 2, 2, 9]]]
results = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(check_Consecutive(*inp), exp, 0)

