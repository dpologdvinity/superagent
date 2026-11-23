from solution import max_run_uppercase
candidate = max_run_uppercase
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


inputs = [['GeMKSForGERksISBESt'], ['PrECIOusMOVemENTSYT'], ['GooGLEFluTTER'], ['A'], ['a'], ['aa'], ['aA'], ['Aaa'], ['aaaAaA'], ['aaaAaAA'], ['aaaA'], ['aaA'], ['aAaa'], ['aaaaA'], ['AaaA'], ['aaaAaaaAaAA'], ['aAaaa'], ['aaaAAaA'], ['AaaaAA'], ['aaaaAaAA'], ['AaaaAAA'], ['aaaaAaA'], ['AaaaaAA'], ['Aa'], ['aaaAaaaaaAAA'], ['aaaAAaaaaaAAaaaAAaAA'], ['aaaaAAaA'], ['aAaaaaAAaaaaAAA'], ['aaaaaAAaA'], ['aaaaaAaAAaaAAaA'], ['aaaaAAaAA'], ['xTzcVWVVy'], ['aaaaAAaAAAaaA'], ['aaAaaaAAaA'], ['aaaaaAaAAaaAaAaA'], ['aaaaAaaaAaAA'], ['AaaaAAaA'], ['AAa'], ['aaaaaAaAAaaAAaAA'], ['AaAa'], ['AaaaaAAA'], ['aaaaaAAaAAAaa'], ['aaAaaaAAAaaAAaAA'], ['xTzcVWVaaaAAaaaaaAAaaaAAaAAy'], ['aaaaAaAaAaa'], ['aaaaAaaaaaAaAaAaaA'], ['AaaaaAAaaaaaAAaaaAAaAAaaAAA'], ['aaaaaAaAAaaaAAaA'], ['aaaaAaaAAaA'], ['aaAaaaAaaAAaAA'], ['aaaAA'], ['aAaAaaA'], ['aaaAAaaaaaAAaaAaAAaAA'], ['AaaaaA'], ['AAAa'], ['aaaAAAaaaAaaAAaA'], ['aaAaaaaAAAaaAAaAA'], ['aaaaAaAAaa'], ['aaa'], ['aaaAAaaaaaAAaAaAaAAaaAaaaAAAaaAAaAAaAA'], ['aaaaAaaaaAAAaaAAaA'], ['aaAaaaAAAaaAAaAAaaAaaaAaA'], ['AaaaaAAaaaaaAAaAaAaAAaaAaaaAAAaaAAaAAaAAaA'], ['aaaAaaaAaaaaaAAAaAA'], ['aaaaaAaaaaaAAAAaaaaAAAaaAAaAA'], ['aaaaaaaaAaAAaaAaAaAaaAaAAaaAAaA'], ['aaaaAaaaaaAaAAaaAAaA'], ['aaaaaAaAAaa'], ['aaaaaAaaaaAaAAaaaAAaaaAAaA'], ['aaaAAaaaaaAAAaAaAaAAaaAaaaAAAaaAAaAAaAA'], ['aaAaaaAAAaaAAAaAA'], ['aaaaaaaaAaAAaaAaAaAaaAaaaaAAaAAaAAaaAAaaaaAAaAaaaaA'], ['aaaaaAaaaAaAA'], ['aaaaAaaaaaAaaaaaAAAAaaaaAAAAaAA'], ['aaaaAAaaaaaAAaaAaAAaAA'], ['AAaaaAAaA'], ['AAaaaaAAaA'], ['AAaaaA'], ['aAaaaaAAaAaaA'], ['aaaaAaAAaaaAAa'], ['aaaaaaaaaaAaaaAAAaaAAaAAAaAAaaAaAaaaaAAaaaaA'], ['aaaaaAaaaaAAAaaAAaA'], ['aaaAAaaaaAAA'], ['aAaaaAAaAAAaaA'], ['AaAaaaaAA'], ['aaaaaaaAaaaaAaAAaaaAAaaaAAaAaAA'], ['AaAaaaaAAAaA'], ['xzcVWVVy'], ['AaAaAaaaAAAaA'], ['aaaaAaaa'], ['aaaaaA'], ['aaaaaaaaAaAAaaAaAaAaaAaaaaAAaAAaAAaaAAaaaaAAaAAAaaAaaaaAAaAaaaaA'], ['aaaaAaaaaaAaAaAaaAaaaAAaaaaaAAaAaAaAAaaAaaaAAAaaAAaAAaAA'], ['aaaAaaaaAAAaaAAaAA'], ['aaaaaaaAaAaAaaAAaaaaAAA'], ['aAaaaaAAaaaaAA'], ['aaaAAaaaaaAAaaaAAaAAaaaaaAaaaAaAA'], ['AaaaA'], ['AaAaA'], ['AaaaaAAAa'], ['aAaAaaaAA'], ['AaA'], ['aaaAaaaAaaaaaAAAaAAA'], ['aAAaaaAA'], ['aaaAAaaaaaaaaAAaaaaaAAAaAaAaAAaaAaaaAAAaaAAaAAaAAAAaaaAAaAAaaaaaAaaaAaAA']]
results = [5, 6, 4, 1, 0, 0, 1, 0, 1, 2, 1, 1, 0, 1, 1, 2, 0, 1, 2, 2, 3, 1, 2, 1, 3, 2, 1, 3, 1, 1, 2, 4, 1, 1, 1, 2, 1, 2, 2, 1, 3, 0, 2, 2, 0, 1, 3, 1, 1, 2, 2, 1, 2, 1, 3, 1, 2, 0, 0, 2, 1, 1, 1, 2, 2, 1, 1, 0, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 3, 1, 2, 2, 1, 4, 1, 0, 1, 1, 2, 2, 3, 2, 2, 1, 1, 3, 2, 1, 3, 2, 2]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(max_run_uppercase(*inp), exp, 0)

