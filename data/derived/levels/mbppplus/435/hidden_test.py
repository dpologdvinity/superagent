from solution import last_Digit
candidate = last_Digit
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


inputs = [[123], [25], [30], [-987], [0], [999999999999999999999999], [-988], [-989], [-2], [-3], [97], [True], [False], [-990], [1], [-1], [42], [-986], [999999999999999999999998], [96], [95], [94], [93], [61], [-14], [-992], [-991], [43], [-18], [98], [62], [92], [5], [60], [91], [-48], [28], [-994], [-19], [44], [2], [29], [1000000000000000000000000], [53], [-4], [63], [-985], [-5], [4], [-79], [-15], [999999999999999999999997], [3], [-78], [-91], [-993], [-90], [59], [-92], [49], [-76], [-17], [45], [58], [64], [-16], [-995], [-77], [-6], [27], [-12], [6], [22], [46], [1000000000000000000000001], [-20], [54], [65], [41], [57], [56], [-7], [23], [-67], [55], [66], [50], [51], [99], [-65], [-93], [-66], [-21], [-23], [-47], [-996], [47], [-13], [-8], [-71], [89], [52], [48], [-24], [-50]]
results = [3, 5, 0, 7, 0, 9, 8, 9, 2, 3, 7, 1, 0, 0, 1, 1, 2, 6, 8, 6, 5, 4, 3, 1, 4, 2, 1, 3, 8, 8, 2, 2, 5, 0, 1, 8, 8, 4, 9, 4, 2, 9, 0, 3, 4, 3, 5, 5, 4, 9, 5, 7, 3, 8, 1, 3, 0, 9, 2, 9, 6, 7, 5, 8, 4, 6, 5, 7, 6, 7, 2, 6, 2, 6, 1, 0, 4, 5, 1, 7, 6, 7, 3, 7, 5, 6, 0, 1, 9, 5, 3, 6, 1, 3, 7, 6, 7, 3, 8, 1, 9, 2, 8, 4, 0]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(last_Digit(*inp), exp, 0)

