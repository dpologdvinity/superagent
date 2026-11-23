from solution import count_divisors
candidate = count_divisors
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


inputs = [[10], [100], [125], [1], [2], [3], [7], [11], [17], [23], [31], [57], [79], [13], [1000000], [987654321], [12], [32], [22], [24], [4], [True], [25], [33], [78], [80], [18], [77], [21], [8], [6], [76], [9], [49], [34], [987654320], [50], [56], [30], [35], [51], [58], [5], [36], [81], [987654322], [37], [82], [54], [19], [1000001], [53], [52], [26], [55], [999999], [29], [16], [75], [47], [14], [48], [20], [45], [15], [61], [83], [89], [90], [62], [84], [28], [46], [63], [27], [999998], [987654323], [38], [74], [73], [91], [64], [987654324], [85], [39], [999997], [999996], [88], [93], [40], [1000002], [87], [59], [999995], [70], [60], [44], [987654325], [68], [1000003], [69], [999994], [94], [987654326], [1000004], [41], [987654327], [987654328], [67], [42], [95], [97], [92], [72], [65]]
results = [True, False, True, False, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(count_divisors(*inp), exp, 0)

