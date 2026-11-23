from solution import text_match_wordz
candidate = text_match_wordz
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


inputs = [['pythonz.'], ['xyz.'], ['  lang  .'], ['*z@'], ['1234z5678'], ['z x z'], ['x'], [''], ['*z@*z@'], ['*z'], ['**z@'], ['**zz@'], ['*z x z*zz@'], ['*x*z@*z@z'], ['***z@'], ['z'], ['x****z@'], ['*z xz x z z*zz@'], ['z*zz@'], ['*@*z@'], ['***@'], ['***zz@@x****z@'], ['*x*z@*z@'], ['*z xzz x z z*zz@'], ['z*z@'], ['**z'], ['*@'], ['*@*z@@'], ['z*zz@z'], ['*@**z@'], ['****@'], ['****z@'], ['*zz'], ['***zz@@x*****z@'], ['z*zz@z*zz@z'], ['z*zz@z*zzz@z'], ['****z*z@z@@x****z@'], ['**zx*z@*z@'], ['*x@*z@'], ['z*****z@zz@z*zz@z'], ['*****@*z'], ['n'], ['**@*z@@'], ['z**z@'], ['*zzz*@z'], ['***@@'], ['z****z@'], ['*z@*z****z@z'], ['****z@*zzz*@z'], ['**z****z*z@z@@x****z@z@'], ['*zzz*z'], ['****z@*zzz*z****z@@z*z@**z@'], [' z  x z'], ['z**@*z@zz@z*zz@z'], ['*z@*z@**zz'], ['*zz xzz x z z*zz@'], ['*z *zz x zz x z z*zz@z*zz@'], ['z**z@*z@zz@z*zz@z'], ['**zx*z@*z*@'], ['z*zzz@'], ['*'], ['z*zz@zz'], ['z**zz@'], ['*z x*x@*z@zz  z*zz@'], ['1234z56n78'], ['z*zzzz@'], ['zzz'], ['**@@x*****z@'], ['**zx*z@*z*@x'], ['***z**z@@@*z@'], ['xz'], ['*zz xzz x z z*z'], ['1234z566n78'], ['z*zz@z*z*zz@z*zzz@zzzz@z'], ['z**@*z@ z  x zzz@z*zz@z'], ['1234z78'], ['zz'], ['*x*z@*zz@'], ['x*x@*z@zz'], ['**zz xzz x z z*z'], ['z**z**zz@'], ['z*zz@***z@'], ['z***zz@z@'], ['12334z78'], ['*z zzz'], ['*@@'], ['yVHKcHlY'], ['z*zz@***z@x*zz xzz x z z*z'], ['*z  x z*zz@'], ['z*zz@z*zz@*@*z@@'], ['*@***z'], ['JlGWYIid'], ['*****@'], ['zyVHKcHlY x z'], ['@*@*z@'], ['****z@*zzz*@zz'], ['*zzz***z x*x@*z@zz  z*zz@*z@z'], ['12314z566n78'], ['z*****z@'], ['12314z566n78*z x*x@*z@zz  z*zz@'], ['l'], ['*z@*z*z x*x@*z@zz  z*zz@****z@z'], ['*x@*zz@'], ['********z@*zzz*@zz'], ['****z@*zzz*z*@@z*z@**z@'], ['1234z566nl78']]
results = [True, True, False, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, False, False, True, True, True, True, True, True, True, False, True, True, True, True, True]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(text_match_wordz(*inp), exp, 0)

