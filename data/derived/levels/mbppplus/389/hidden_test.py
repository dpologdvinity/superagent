from solution import find_lucas
candidate = find_lucas
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


inputs = [[9], [4], [3], [15], [20], [25], [30], [0], [1], [2], [10], [True], [False], [19], [11], [24], [26], [16], [31], [18], [32], [33], [29], [27], [28], [8], [17], [7], [21], [12], [23], [22], [14], [13], [6], [5]]
results = [76, 7, 4, 1364, 15127, 167761, 1860498, 2, 1, 3, 123, 1, 2, 9349, 199, 103682, 271443, 2207, 3010349, 5778, 4870847, 7881196, 1149851, 439204, 710647, 47, 3571, 29, 24476, 322, 64079, 39603, 843, 521, 18, 11]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(find_lucas(*inp), exp, 0)

