from solution import dog_age
candidate = dog_age
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


inputs = [[12], [15], [24], [100], [0], [30], [29], [99], [101], [28], [98], [27], [26], [True], [False], [97], [25], [31], [32], [33], [23], [21], [34], [1], [35], [2], [22], [36], [3], [96], [95], [4], [102], [56], [5], [55], [54], [6], [20], [37], [39], [19], [38], [7], [53], [57], [8], [93], [43], [103], [104], [9], [18], [17], [52], [64], [16], [65], [94], [40], [66], [92], [41], [67], [58], [63], [68], [105], [60], [69], [59], [106], [51], [70], [42], [88], [89], [107], [50], [71], [91], [62], [49], [10], [48], [108], [44], [61], [87], [109], [90], [110], [111], [45], [11], [46], [47], [72], [112], [76], [86], [113], [114]]
results = [61, 73, 109, 413, 0.0, 133, 129, 409, 417, 125, 405, 121, 117, 10.5, 0.0, 401, 113, 137, 141, 145, 105, 97, 149, 10.5, 153, 21.0, 101, 157, 25, 397, 393, 29, 421, 237, 33, 233, 229, 37, 93, 161, 169, 89, 165, 41, 225, 241, 45, 385, 185, 425, 429, 49, 85, 81, 221, 269, 77, 273, 389, 173, 277, 381, 177, 281, 245, 265, 285, 433, 253, 289, 249, 437, 217, 293, 181, 365, 369, 441, 213, 297, 377, 261, 209, 53, 205, 445, 189, 257, 361, 449, 373, 453, 457, 193, 57, 197, 201, 301, 461, 317, 357, 465, 469]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(dog_age(*inp), exp, 0)

