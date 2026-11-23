from solution import replace_char
candidate = replace_char
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


inputs = [['polygon', 'y', 'l'], ['character', 'c', 'a'], ['python', 'l', 'a'], ['', 'a', 'b'], ['python', 'z', 'a'], ['python', 'o', 'o'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'm', 'n'], ['pythoon', 'a', 'b'], ['python', 'z', 'o'], ['z', 'a', 'a'], ['z', 'z', 'z'], ['', 'm', 'm'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'a', 'b'], ['python', 'z', 'z'], ['zzz', 'z', 'z'], ['zzz', 'a', 'a'], ['a', 'a', 'a'], ['a', 'b', 'o'], ['b', 'z', 'o'], ['', 'o', 'm'], ['', 'a', 'a'], ['AbCdEfGhIjKlMnOpQrStUvWYzz', 'a', 'a'], ['n', 'z', 'a'], ['', 'b', 'o'], ['pythona', 'z', 'a'], ['pythoonpythona', 'z', 'a'], ['zz', 'a', 'a'], ['mz', 'z', 'z'], ['', 'o', 'o'], ['a', 'm', 'o'], ['b', 'a', 'b'], ['b', 'o', 'o'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'm', 'n'], ['b', 'a', 'a'], ['mz', 'a', 'a'], ['zzz', 'z', 'a'], ['m', 'a', 'a'], ['zz', 'z', 'a'], ['mz', 'a', 'b'], ['aa', 'b', 'o'], ['m', 'n', 'm'], ['a', 'o', 'b'], ['z', 'a', 'z'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'a', 'a'], ['bb', 'a', 'a'], ['python', 'o', 'b'], ['n', 'n', 'n'], ['zzzzz', 'a', 'a'], ['zz', 'z', 'o'], ['zz', 'o', 'o'], ['a', 'z', 'a'], ['a', 'b', 'a'], ['n', 'z', 'z'], ['opythoon', 'a', 'o'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'm', 'b'], ['zzzzza', 'b', 'b'], ['AbCdEfGhIjKlMnOpQrSthUvWYzz', 'a', 'a'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'b', 'b'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'z', 'z'], ['zz', 'z', 'z'], ['aa', 'b', 'b'], ['pythona', 'a', 'a'], ['AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'o', 'o'], ['mz', 'b', 'o'], ['mAbCdEfGhIjKlMnOpQrSthUvWYzz', 'm', 'm'], ['zz', 'n', 'a'], ['pythoonpynthona', 'z', 'a'], ['aa', 'o', 'o'], ['b', 'b', 'b'], ['a', 'a', 'z'], ['zpythoonpynthona', 'z', 'o'], ['zzzzz', 'm', 'm'], ['a', 'm', 'm'], ['oopythoon', 'a', 'o'], ['m', 'm', 'm'], ['zpythoonpynthona', 'o', 'b'], ['o', 'o', 'o'], ['pytoopythoonhona', 'z', 'a'], ['AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'z', 'a'], ['bb', 'a', 'o'], ['oo', 'o', 'o'], ['pytbboopythoonhona', 'z', 'z'], ['opythoon', 'z', 'z'], ['aa', 'z', 'b'], ['pythnn', 'o', 'b'], ['zzzzza', 'o', 'b'], ['AbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'o', 'o'], ['aaa', 'b', 'b'], ['AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'b', 'b'], ['a', 'o', 'a'], ['pythoAbCdEpythnnfGhIjKlMnOpQaaaxYzn', 'z', 'z'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfKGhIjKlMnOpQrStUvWxYzz', 'm', 'n'], ['opythoon', 'o', 'o'], ['pythooon', 'a', 'b'], ['pythooon', 'm', 'm'], ['', 'b', 'b'], ['zpythoonpynthona', 'b', 'o'], ['o', 'b', 'o'], ['b', 'b', 'o'], ['n', 'z', 'n'], ['zzzzza', 'b', 'a'], ['o', 'b', 'a'], ['ma', 'm', 'm'], ['mz', 'z', 'a'], ['AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'a', 'a'], ['zzzAbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzzzz', 'a', 'a'], ['pytohona', 'z', 'a']]
results = ['pollgon', 'aharaater', 'python', '', 'python', 'python', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'pythoon', 'python', 'z', 'z', '', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'python', 'zzz', 'zzz', 'a', 'a', 'b', '', '', 'AbCdEfGhIjKlMnOpQrStUvWYzz', 'n', '', 'pythona', 'pythoonpythona', 'zz', 'mz', '', 'a', 'b', 'b', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'b', 'mz', 'aaa', 'm', 'aa', 'mz', 'aa', 'm', 'a', 'z', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'bb', 'pythbn', 'n', 'zzzzz', 'oo', 'zz', 'a', 'a', 'n', 'opythoon', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'zzzzza', 'AbCdEfGhIjKlMnOpQrSthUvWYzz', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'zz', 'aa', 'pythona', 'AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'mz', 'mAbCdEfGhIjKlMnOpQrSthUvWYzz', 'zz', 'pythoonpynthona', 'aa', 'b', 'z', 'opythoonpynthona', 'zzzzz', 'a', 'oopythoon', 'm', 'zpythbbnpynthbna', 'o', 'pytoopythoonhona', 'AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYaa', 'bb', 'oo', 'pytbboopythoonhona', 'opythoon', 'aa', 'pythnn', 'zzzzza', 'AbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'aaa', 'AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'a', 'pythoAbCdEpythnnfGhIjKlMnOpQaaaxYzn', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfKGhIjKlMnOpQrStUvWxYzz', 'opythoon', 'pythooon', 'pythooon', '', 'zpythoonpynthona', 'o', 'o', 'n', 'zzzzza', 'o', 'ma', 'ma', 'AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'zzzAbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzzzz', 'pytohona']
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(replace_char(*inp), exp, 0)

