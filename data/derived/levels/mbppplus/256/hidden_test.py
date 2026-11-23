from solution import count_Primes_nums
candidate = count_Primes_nums
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


inputs = [[5], [10], [100], [1000], [1001], [1002], [1003], [999], [True], [False], [998], [65], [66], [67], [997], [68], [64], [1004], [1005], [99], [996], [63], [995], [1006], [1007], [1008], [62], [994], [86], [1009], [85], [61], [87], [60], [44], [1010], [1011], [45], [59], [80], [69], [70], [71], [98], [97], [79], [1012], [2], [1013], [84], [56], [1], [0], [81], [78], [43], [1014], [72], [1015], [90], [42], [41], [46], [88], [3], [1016], [57], [4], [38], [993], [1017], [77], [101], [1018], [83], [82], [76], [58], [73], [39], [74], [89], [40], [75], [1019], [96], [47], [94], [95], [55], [48], [54], [1020], [102], [53], [91], [992], [1021], [991], [11], [92], [37]]
results = [2, 4, 25, 168, 168, 168, 168, 168, 0, 0, 168, 18, 18, 18, 167, 19, 18, 168, 168, 25, 167, 18, 167, 168, 168, 168, 18, 167, 23, 168, 23, 17, 23, 17, 14, 169, 169, 14, 16, 22, 19, 19, 19, 25, 24, 21, 169, 0, 169, 23, 16, 0, 0, 22, 21, 13, 170, 20, 170, 24, 13, 12, 14, 23, 1, 170, 16, 2, 12, 167, 170, 21, 25, 170, 22, 22, 21, 16, 20, 12, 21, 23, 12, 21, 170, 24, 14, 24, 24, 16, 15, 16, 171, 26, 15, 24, 167, 171, 166, 4, 24, 11]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(count_Primes_nums(*inp), exp, 0)

