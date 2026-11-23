from solution import dif_Square
candidate = dif_Square
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


inputs = [[5], [10], [15], [991], [567], [13], [24], [568], [992], [569], [990], [566], [True], [989], [25], [14], [565], [23], [988], [12], [11], [16], [17], [993], [564], [563], [22], [994], [9], [21], [995], [996], [20], [18], [997], [8], [987], [45], [562], [570], [26], [561], [998], [19], [77], [7], [76], [560], [986], [27], [44], [571], [28], [75], [46], [78], [74], [985], [29], [572], [984], [73], [983], [79], [573], [47], [50], [982], [981], [71], [49], [80], [51], [999], [30], [81], [6], [1000], [980], [1001], [1002], [82], [1003], [52], [574], [53], [1004], [70], [575], [69], [576], [979], [83], [72], [68], [43], [89], [42], [977], [33], [4], [36], [978], [3]]
results = [True, False, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, False, True, False, True, True, True, True, True, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, False, True, False, True, True, True, False, False, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(dif_Square(*inp), exp, 0)

