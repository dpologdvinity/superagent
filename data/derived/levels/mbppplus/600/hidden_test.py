from solution import is_Even
candidate = is_Even
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


inputs = [[1], [2], [3], [-10], [-283], [-1000], [1000000000], [-999], [999999999], [-284], [-9], [False], [-282], [True], [999999998], [999999997], [-281], [-73], [-279], [-74], [94], [-280], [-72], [-278], [93], [-276], [999999995], [-285], [-277], [95], [-11], [-75], [-76], [1000000001], [-286], [-71], [92], [91], [-12], [-8], [1000000002], [90], [999999994], [89], [-1001], [1000000003], [-13], [-14], [-94], [999999996], [-95], [-98], [999999993], [-15], [76], [74], [40], [-96], [-70], [-97], [75], [41], [-99], [-19], [96], [88], [73], [39], [-16], [59], [16], [-69], [-77], [-43], [-44], [999999992], [77], [87], [-78], [18], [45], [8], [-100], [14], [-68], [-101], [13], [-79], [-287], [-102], [58], [-17], [38], [98], [-1002], [15], [1000000004], [57], [-288], [-1003], [60], [-20], [-998], [-7], [1000000005], [-18], [-1005]]
results = [False, True, False, True, False, True, True, False, False, True, False, True, True, False, True, False, False, False, False, True, True, True, True, True, False, True, False, False, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, False, False, False, True, True, True, False, True, False, False, True, True, True, True, True, False, False, False, False, False, True, True, False, False, True, False, True, False, False, False, True, True, False, False, True, True, False, True, True, True, True, False, False, False, False, True, True, False, True, True, True, False, True, False, True, False, True, True, True, False, False, True, False]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(is_Even(*inp), exp, 0)

