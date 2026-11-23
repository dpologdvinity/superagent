from solution import remove_Occ
candidate = remove_Occ
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


inputs = [['hello', 'l'], ['abcda', 'a'], ['PHP', 'P'], ['a', 'a'], ['aaa', 'a'], ['hello world', 'x'], ['worlda', 'a'], ['x', 'x'], ['hello world', 'a'], ['world', 'x'], ['xx', 'x'], ['xworlaaada', 'x'], ['axworlaaada', 'x'], ['waaaorlda', 'a'], ['xhello world', 'a'], ['xxx', 'x'], ['worlda', 'x'], ['world', 'a'], ['hwllo world', 'a'], ['axx', 'a'], ['hwllo world', 'x'], ['hwllo', 'a'], ['hwl', 'a'], ['ahwllo world', 'a'], ['xxx', 'a'], ['hwll', 'a'], ['hhwl', 'a'], ['ahwllo', 'x'], ['whwlloorld', 'a'], ['wda', 'x'], ['hwl', 'x'], ['xrworlaaada', 'x'], ['aahwllo', 'a'], ['a', 'x'], ['xxwaaaorlda', 'x'], ['wda', 'a'], ['hxworlaaadawllo', 'a'], ['aaaa', 'a'], ['xrworworldalaaadax', 'x'], ['aaawda', 'x'], ['hello worldx', 'x'], ['xrworworldalaaadax', 'a'], ['xrworlaaadaworldx', 'x'], ['aahwllo', 'x'], ['xworlaaadaaaaa', 'a'], ['xxxx', 'a'], ['xhello worlda', 'a'], ['xrworworaldalaaadax', 'a'], ['xaaaa', 'x'], ['xxwaahello worldxaorlda', 'x'], ['axworlaaada', 'a'], ['worldxaorlda', 'x'], ['hellloa', 'a'], ['xaaa', 'x'], ['aa', 'a'], ['xhello', 'a'], ['xrworlaaaada', 'x'], ['axxxaawda', 'x'], ['hello worldxxhello worlda', 'a'], ['xhello', 'x'], ['hxworlaaadawlolo', 'a'], ['aa', 'x'], ['lo', 'x'], ['xaaaa', 'a'], ['waaaorllda', 'a'], ['ahwllao', 'x'], ['aaa', 'x'], ['xxhello', 'x'], ['wdaa', 'a'], ['xrworworaldalaaadaxa', 'a'], ['waaaorlxxwaaaorlda', 'a'], ['aahwllao', 'x'], ['hello worldx', 'a'], ['lo', 'a'], ['hellloa', 'x'], ['helwdalloa', 'x'], ['worldxxhellox', 'x'], ['hello', 'x'], ['l', 'x'], ['waaaorlldalo', 'x'], ['xrwax', 'x'], ['waaaorllda', 'x'], ['whwlloorld', 'x'], ['aahhwla', 'x'], ['waaaorlda', 'x'], ['llo', 'l'], ['axaahwllaoworlaaada', 'a'], ['hwllor world', 'a'], ['xworlaaadaaaaa', 'x'], ['waaaorlldal', 'a'], ['aahawllao', 'x'], ['lllo', 'l'], ['worlaaaadxaorlda', 'x'], ['hello worldxxhhelloworlda', 'a'], ['hwlll', 'a'], ['xrworwoxxxraldalaaadaxa', 'a'], ['ll', 'x'], ['aaahwllaoo', 'a'], ['worldx', 'a'], ['xrworworaldalaaadaxa', 'x'], ['hxworlaaadawlolo', 'x'], ['whello world', 'x'], ['ahwllo', 'a'], ['ahxworlaaadawlolo', 'a'], ['whello', 'x'], ['ax', 'a']]
results = ['heo', 'bcd', 'H', '', 'a', 'hello world', 'world', '', 'hello world', 'world', '', 'worlaaada', 'aworlaaada', 'waaorld', 'xhello world', 'x', 'worlda', 'world', 'hwllo world', 'xx', 'hwllo world', 'hwllo', 'hwl', 'hwllo world', 'xxx', 'hwll', 'hhwl', 'ahwllo', 'whwlloorld', 'wda', 'hwl', 'rworlaaada', 'hwllo', 'a', 'waaaorlda', 'wd', 'hxworlaadwllo', 'aa', 'rworworldalaaada', 'aaawda', 'hello world', 'xrworworldlaaadx', 'rworlaaadaworld', 'aahwllo', 'xworlaadaaaa', 'xxxx', 'xhello world', 'xrworworldalaaadx', 'aaaa', 'xwaahello worldaorlda', 'xworlaaad', 'worldaorlda', 'helllo', 'aaa', '', 'xhello', 'rworlaaaada', 'axaawda', 'hello worldxxhello world', 'hello', 'hxworlaadwlolo', 'aa', 'lo', 'xaa', 'waaorlld', 'ahwllao', 'aaa', 'hello', 'wd', 'xrworworldalaaadax', 'waaorlxxwaaaorld', 'aahwllao', 'hello worldx', 'lo', 'hellloa', 'helwdalloa', 'worldxhello', 'hello', 'l', 'waaaorlldalo', 'rwa', 'waaaorllda', 'whwlloorld', 'aahhwla', 'waaaorlda', 'o', 'xaahwllaoworlaaad', 'hwllor world', 'worlaaadaaaaa', 'waaorlldl', 'aahawllao', 'lo', 'worlaaaadaorlda', 'hello worldxxhhelloworld', 'hwlll', 'xrworwoxxxrldalaaadax', 'll', 'aahwlloo', 'worldx', 'rworworaldalaaadaa', 'hworlaaadawlolo', 'whello world', 'hwllo', 'hxworlaaadwlolo', 'whello', 'x']
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(remove_Occ(*inp), exp, 0)

