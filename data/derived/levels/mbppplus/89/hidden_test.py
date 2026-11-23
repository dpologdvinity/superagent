from solution import closest_num
candidate = closest_num
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


inputs = [[11], [7], [12], [-5], [0], [True], [False], [-4], [-3], [-1], [-39], [-37], [-36], [-35], [-38], [47], [-20], [46], [-34], [45], [-40], [-33], [-21], [88], [89], [-2], [1], [2], [-59], [-41], [-32], [-58], [-31], [-6], [-42], [-60], [-7], [3], [-53], [4], [72], [-19], [-43], [5], [-52], [44], [52], [-51], [-54], [43], [-55], [55], [42], [-28], [-95], [-22], [-96], [-50], [73], [-97], [90], [-94], [53], [-49], [-23], [-98], [54], [6], [-29], [-30], [41], [91], [56], [63], [-56], [60], [-8], [-68], [48], [87], [86], [-27], [92], [51], [-24], [61], [-44], [-69], [84], [-70], [40], [-61], [-18], [-9], [39], [-93], [62], [64], [-62], [59], [-26], [-99], [-45], [-92], [-10]]
results = [10, 6, 11, -6, -1, 0, -1, -5, -4, -2, -40, -38, -37, -36, -39, 46, -21, 45, -35, 44, -41, -34, -22, 87, 88, -3, 0, 1, -60, -42, -33, -59, -32, -7, -43, -61, -8, 2, -54, 3, 71, -20, -44, 4, -53, 43, 51, -52, -55, 42, -56, 54, 41, -29, -96, -23, -97, -51, 72, -98, 89, -95, 52, -50, -24, -99, 53, 5, -30, -31, 40, 90, 55, 62, -57, 59, -9, -69, 47, 86, 85, -28, 91, 50, -25, 60, -45, -70, 83, -71, 39, -62, -19, -10, 38, -94, 61, 63, -63, 58, -27, -100, -46, -93, -11]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(closest_num(*inp), exp, 0)

