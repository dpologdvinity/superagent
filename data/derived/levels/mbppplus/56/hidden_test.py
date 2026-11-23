from solution import check
candidate = check
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


inputs = [[70], [23], [73], [0], [1], [9], [10], [20], [100], [1000], [11], [22], [33], [44], [55], [66], [77], [88], [99], [12], [21], [34], [43], [56], [65], [78], [87], [90], [8], [999], [45], [102], [42], [103], [79], [64], [41], [54], [72], [71], [13], [76], [98], [2], [86], [40], [57], [39], [7], [89], [63], [46], [53], [67], [38], [101], [80], [74], [15], [91], [37], [35], [24], [32], [75], [19], [14], [104], [3], [82], [6], [25], [1001], [85], [81], [5], [92], [18], [4], [83], [52], [105], [31], [30], [93], [36], [1002], [97], [1003], [95], [26], [1004], [27], [84], [68], [51], [96], [998], [47], [62], [50], [58], [49], [1005], [69], [29], [997], [17], [94], [28], [59], [48], [16], [60], [61], [107], [1006], [106], [996], [108], [1007], [995], [1008], [109], [110]]
results = [False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(check(*inp), exp, 0)

