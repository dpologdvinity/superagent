from solution import count_Set_Bits
candidate = count_Set_Bits
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


inputs = [[2], [4], [6], [999999999], [1000000000], [True], [False], [1000000001], [999999998], [67], [999999997], [999999996], [1000000002], [1000000003], [66], [999999995], [65], [999999994], [68], [69], [71], [72], [999999993], [1000000004], [1], [73], [70], [64], [1000000005], [74], [98], [63], [0], [999999992], [1000000006], [3], [61], [62], [97], [999999991], [75], [11], [95], [1000000007], [94], [93], [96], [92], [76], [12], [77], [9], [44], [13], [10], [1000000008], [14], [91], [78], [79], [59], [99], [80], [90], [999999990], [85], [60], [57], [1000000009], [58], [84], [100], [43], [101], [48], [23], [1000000010], [56], [86], [55], [102], [5], [53], [46], [81], [47], [52], [49], [54], [83], [45], [16], [50], [30], [28], [82], [42], [33], [17], [31], [41], [51]]
results = [1, 1, 2, 21, 13, 1, 0, 14, 20, 3, 20, 19, 14, 15, 2, 20, 2, 19, 2, 3, 4, 2, 19, 14, 1, 3, 3, 1, 15, 3, 3, 6, 0, 18, 15, 2, 5, 5, 3, 20, 4, 3, 6, 16, 5, 5, 2, 4, 3, 2, 4, 2, 3, 3, 2, 14, 3, 5, 4, 5, 5, 4, 2, 4, 19, 4, 4, 4, 15, 4, 3, 3, 4, 4, 2, 4, 15, 3, 4, 5, 4, 2, 4, 4, 3, 5, 3, 3, 4, 4, 4, 1, 3, 4, 3, 3, 3, 2, 2, 5, 3, 4]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(count_Set_Bits(*inp), exp, 0)

