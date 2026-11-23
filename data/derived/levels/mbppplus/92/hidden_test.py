from solution import is_undulating
candidate = is_undulating
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


inputs = [[1212121], [1991], [121], [2121212121212121], [2121212121212122], [2121212121212119], [2121212121212123], [2121212121212124], [2121212121212125], [2121212121212120], [2121212121212118], [2121212121212126], [2121212121212117], [2121212121212127], [82], [40], [83], [39], [81], [2121212121212116], [2121212121212128], [2121212121212115], [41], [80], [19], [20], [42], [84], [18], [2121212121212129], [43], [21], [62], [17], [85], [2121212121212130], [79], [12], [2121212121212131], [86], [44], [52], [16], [11], [53], [63], [10], [78], [51], [61], [87], [50], [77], [54], [92], [55], [49], [22], [96], [38], [97], [56], [23], [91], [2121212121212114], [15], [93], [24], [48], [89], [60], [64], [65], [37], [76], [59], [35], [88], [2121212121212132], [58], [14], [94], [9], [47], [95], [66], [57], [36], [8], [13], [25], [45], [90], [2121212121212113], [67], [46], [7], [68], [75], [34], [2121212121212133], [2121212121212134], [26], [74]]
results = [True, False, True, True, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, False, True, True, False, True, True, True, True, True, True, True, True, False, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, True, False, True, True, False, True, True, True, True, False, True, True, False, True, True, True, False, False, True, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(is_undulating(*inp), exp, 0)

