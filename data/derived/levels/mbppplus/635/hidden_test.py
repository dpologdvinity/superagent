from solution import heap_sort
candidate = heap_sort
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


inputs = [[[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]], [[25, 35, 22, 85, 14, 65, 75, 25, 58]], [[7, 1, 9, 5]], [[]]]
results = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [14, 22, 25, 25, 35, 58, 65, 75, 85], [1, 5, 7, 9], []]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(heap_sort(*inp), exp, 0)

