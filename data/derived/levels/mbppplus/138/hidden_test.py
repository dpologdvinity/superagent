from solution import is_Sum_Of_Powers_Of_Two
candidate = is_Sum_Of_Powers_Of_Two
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


inputs = [[10], [7], [14], [123456789], [-14], [-2147483648], [-15], [123456788], [-2147483647], [123456787], [-2147483649], [-2147483650], [True], [-2147483651], [-16], [False], [-2147483646], [123456786], [-17], [-88], [-18], [-19], [-20], [123456785], [-7], [-6], [-2147483652], [-2147483653], [-2147483645], [-2147483654], [123456784], [-86], [-2147483643], [-87], [123456783], [21], [-2147483655], [-85], [-9], [-21], [-10], [19], [-22], [-89], [123456782], [-2147483642], [-23], [-2147483641], [-11], [-8], [-90], [18], [-5], [123456790], [-4], [20], [-2147483640], [9], [123456781], [123456791], [-2147483644], [123456780], [-2147483639], [8], [42], [123456792], [-2147483656], [-13], [-2147483657], [41], [43], [-91], [-2147483638], [-2147483637], [-12], [40], [123456779], [44], [123456793], [28], [29], [45], [123456778], [39], [-55], [82], [-92], [-43], [-3], [27], [11], [-2147483636], [-50], [12], [61], [17], [-75], [81], [-44], [-36], [79], [-45], [-51], [46]]
results = [True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, True, True, False, False, False, False, False, False, False, False, False, True, False, True, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(is_Sum_Of_Powers_Of_Two(*inp), exp, 0)

