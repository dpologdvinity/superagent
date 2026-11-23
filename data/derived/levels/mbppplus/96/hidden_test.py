from solution import divisor
candidate = divisor
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


inputs = [[15], [12], [9], [79337], [79336], [86], [87], [88], [85], [79335], [79334], [79333], [79332], [True], [89], [79331], [95], [90], [79338], [91], [92], [93], [84], [94], [83], [79330], [82], [46], [47], [44], [48], [49], [81], [43], [42], [96], [41], [45], [97], [79], [78], [79329], [80], [50], [40], [79328], [51], [17], [98], [39], [16], [18], [99], [38], [79327], [19], [20], [79325], [77], [79339], [37], [36], [79324], [79340], [79341], [35], [34], [79323], [73], [79322], [21], [22], [79320], [52], [23], [74], [65], [79326], [79321], [33], [79319], [76], [32], [14], [75], [57], [100], [62], [67], [72], [58], [59], [60], [66], [56], [53], [101], [54], [68], [63], [55], [61], [64]]
results = [4, 6, 3, 2, 16, 4, 4, 8, 4, 24, 4, 2, 24, 1, 2, 6, 4, 12, 16, 4, 6, 4, 12, 4, 2, 8, 4, 4, 2, 6, 10, 3, 5, 2, 8, 12, 2, 6, 2, 2, 8, 8, 10, 6, 8, 24, 4, 2, 6, 4, 5, 6, 6, 4, 4, 2, 6, 12, 4, 8, 2, 9, 12, 12, 8, 4, 4, 8, 2, 8, 4, 4, 32, 6, 2, 4, 4, 32, 4, 4, 2, 6, 6, 4, 6, 4, 9, 4, 2, 12, 4, 2, 12, 8, 8, 2, 2, 8, 6, 6, 4, 2, 7]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(divisor(*inp), exp, 0)

