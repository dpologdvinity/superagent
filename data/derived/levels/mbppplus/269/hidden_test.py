from solution import ascii_value
candidate = ascii_value
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


inputs = [['A'], ['R'], ['S'], ['@'], ['®'], ['!'], [' '], ['ص'], ['&'], ['\n'], ['€'], ['^'], ['ä'], ['π'], ['~'], ['\t'], ['©'], ['๑'], ['$'], ['7'], ['%'], ['['], ['{'], ['é'], ['\x00'], ['\x1d'], ['♥'], ['\uffff'], ['\x7f'], ['\x80'], ['™'], ['文'], ['→'], ['F'], ['q'], ['E'], ['o'], ['W'], ['U'], ['O'], ['K'], ['v'], ['Z'], ['N'], ['P'], ['b'], ['y'], ['l'], ['V'], ['D'], ['u'], ['s'], ['I'], ['h'], ['H'], ['B'], ['k'], ['X'], ['L'], ['p'], ['Y'], ['c'], ['J'], ['T'], ['a'], ['e'], ['r'], ['G'], ['j'], ['m'], ['z'], ['n'], ['g'], ['t'], ['i'], ['d'], ['M'], ['x'], ['f'], ['C'], ['Q'], ['w']]
results = [65, 82, 83, 64, 174, 33, 32, 1589, 38, 10, 8364, 94, 228, 960, 126, 9, 169, 3665, 36, 55, 37, 91, 123, 233, 0, 29, 9829, 65535, 127, 128, 8482, 25991, 8594, 70, 113, 69, 111, 87, 85, 79, 75, 118, 90, 78, 80, 98, 121, 108, 86, 68, 117, 115, 73, 104, 72, 66, 107, 88, 76, 112, 89, 99, 74, 84, 97, 101, 114, 71, 106, 109, 122, 110, 103, 116, 105, 100, 77, 120, 102, 67, 81, 119]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(ascii_value(*inp), exp, 0)

