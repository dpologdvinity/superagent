from solution import prime_num
candidate = prime_num
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


inputs = [[13], [7], [-1010], [0], [999999999989], [1572869], [982451653], [9999999967], [False], [9999999966], [1], [True], [999999999988], [999999999990], [9999999968], [982451652], [999999999991], [999999999987], [982451651], [9999999969], [2], [1572868], [982451650], [3], [64], [-1], [1572870], [31], [1572871], [982451654], [9999999970], [32], [33], [74], [982451649], [30], [4], [65], [999999999986], [34], [72], [5], [73], [70], [25], [24], [6], [26], [-71], [999999999992], [1572872], [9999999971], [-70], [71], [27], [66], [999999999993], [9999999972], [999999999994], [17], [1572873], [-55], [63], [-72], [18], [29], [35], [67], [1572874], [982451648], [9999999965], [-56], [999999999995], [68], [61], [75], [23], [19], [8], [999999999985], [-69], [62], [60], [9999999973], [999999999996], [22], [-62], [37], [999999999984], [999999999983], [999999999982], [36], [28], [999999999997], [39], [-45], [69], [-16], [38], [-63], [9999999964], [-68], [-67], [-44], [16], [9], [59], [40]]
results = [True, True, False, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(prime_num(*inp), exp, 0)

