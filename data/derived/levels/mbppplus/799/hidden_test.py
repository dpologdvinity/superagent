from solution import left_rotate
candidate = left_rotate
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


inputs = [[16, 2], [10, 2], [99, 3], [1, 3], [5, 3], [29, 3], [0, 4], [0, 0], [1, 1], [4, 4], [1, 4], [1, 0], [0, 1], [4, 1], [5, 4], [4, 0], [3, 3], [5, 5], [4, 3], [1, 5], [2, 1], [2, 5], [3, 2], [3, 0], [6, 5], [5, 0], [2, 3], [4, 6], [6, 2], [3, 1], [6, 1], [3, 4], [2, 6], [6, 6], [0, 6], [5, 6], [5, 1], [6, 4], [2, 4], [3, 5], [1, 6], [4, 2], [7, 1], [7, 7], [2, 2], [1, 2], [6, 3], [4, 5], [8, 8], [7, 6], [7, 3], [8, 7], [9, 1], [7, 0], [9, 4], [9, 8], [7, 2], [8, 6], [7, 8], [8, 0], [5, 2], [5, 10], [8, 3], [2, 0], [9, 10], [2, 8], [3, 9], [4, 10], [10, 6], [6, 9], [5, 8], [True, True], [10, 0], [True, False], [10, 9], [10, 8], [9, 5], [6, 7], [9, 0], [9, 9], [1, 9], [7, 5], [8, 10], [0, 2], [8, 1], [1, 8], [False, False], [2, 9], [9, 3], [10, 10], [0, 3], [6, 0], [3, 10], [11, 11], [9, 11], [11, 10], [8, 9], [12, 6], [False, True], [0, 9], [11, 8], [0, 11], [3, 7], [12, 12], [0, 5]]
results = [64, 40, 792, 8, 40, 232, 0, 0, 2, 64, 16, 1, 0, 8, 80, 4, 24, 160, 32, 32, 4, 64, 12, 3, 192, 5, 16, 256, 24, 6, 12, 48, 128, 384, 0, 320, 10, 96, 32, 96, 64, 16, 14, 896, 8, 4, 48, 128, 2048, 448, 56, 1024, 18, 7, 144, 2304, 28, 512, 1792, 8, 20, 5120, 64, 2, 9216, 512, 1536, 4096, 640, 3072, 1280, 2, 10, 1, 5120, 2560, 288, 768, 9, 4608, 512, 224, 8192, 0, 16, 256, 0, 1024, 72, 10240, 0, 6, 3072, 22528, 18432, 11264, 4096, 768, 0, 0, 2816, 0, 384, 49152, 0]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(left_rotate(*inp), exp, 0)

