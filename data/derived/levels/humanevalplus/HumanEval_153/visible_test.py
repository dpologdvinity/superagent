from solution import Strongest_Extension
import numpy as np

def is_floats(x) -> bool:
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all((isinstance(i, float) for i in x))
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False

def assertion(out, exp, atol):
    exact_match = out == exp
    if atol == 0 and is_floats(exp):
        atol = 1e-06
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match

def check(candidate):
    inputs = [['Watashi', ['tEN', 'niNE', 'eIGHt8OKe']], ['Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']], ['__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']]]
    for inp in inputs:
        print(candidate(*inp))
check(Strongest_Extension)
