from solution import amicable_numbers_sum
candidate = amicable_numbers_sum
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


inputs = [[999], [9999], [99], [10000], [5000], [4999], [4998], [5001], [90], [92], [89], [91], [10001], [93], [5002], [4997], [True], [94], [4996], [4995], [10002], [88], [10003], [5003], [5004], [21], [87], [22], [4994], [95], [86], [96], [20], [9998], [4993], [23], [47], [97], [5005], [10004], [9], [9997], [10005], [85], [8], [46], [9996], [84], [7], [19], [9995], [98], [10006], [18], [100], [101], [24], [68], [61], [69], [44], [43], [17], [5006], [16], [6], [10], [45], [10007], [66], [15], [83], [48], [9994], [81], [60], [74], [5007], [67], [28], [80], [72], [79], [70], [29], [49], [9993], [65], [4992], [4991], [11], [10008], [73], [12], [62], [71], [4990], [5008], [78], [50], [59], [77], [10009]]
results = [504, 31626, 0, 31626, 8442, 8442, 8442, 8442, 0, 0, 0, 0, 31626, 0, 8442, 8442, 0, 0, 8442, 8442, 31626, 0, 31626, 8442, 8442, 0, 0, 0, 8442, 0, 0, 0, 0, 31626, 8442, 0, 0, 0, 8442, 31626, 0, 31626, 31626, 0, 0, 0, 31626, 0, 0, 0, 31626, 0, 31626, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8442, 0, 0, 0, 0, 31626, 0, 0, 0, 0, 31626, 0, 0, 0, 8442, 0, 0, 0, 0, 0, 0, 0, 0, 31626, 0, 8442, 8442, 0, 31626, 0, 0, 0, 0, 8442, 8442, 0, 0, 0, 0, 31626]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(amicable_numbers_sum(*inp), exp, 0)

