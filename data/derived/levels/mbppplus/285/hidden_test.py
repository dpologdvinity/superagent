from solution import text_match_two_three
candidate = text_match_two_three
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


inputs = [['ac'], ['dc'], ['abbbba'], [''], ['icxh'], ['icicxhxh'], ['icixcxhxh'], ['icicxhxicixcxhxhh'], ['iicixcxhxh'], ['icicxhxicixxhxhh'], ['icixcxhicicxhxicixxhxhhxh'], ['icxiicixcxhxhh'], ['KDZlWIDTdR'], ['icicixcxhicicxhxicxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhh'], ['icicxh'], ['icich'], ['icixcxhicicxhxicicicxhxicixxhxhhixxhxhhxh'], ['icicxhicxchxicixcxhxhh'], ['iicxhxicicicxhxicixxhxhhixxhxhhxh'], ['hicxiicixcxhxhh'], ['hicxiicixcxxhxhh'], ['icixcxhicicxhiicixcxhxhxicixxhxhhxh'], ['icixxhxh'], ['icixcxhxicixcxhxhh'], ['icicixcxhicicxhxicxiicixcxhxhhicixxhxhhxhicxhxicixcxhxh'], ['icixcicixcxhxicixcxhxhhxhxh'], ['icicixcxhicicxhxiicixcxhicicxhxicixxhxhhxhcxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhh'], ['icicxhxicihh'], ['hiicxiicixcxhxhh'], ['icxiichh'], ['icixcxhicicxhxicixxxhxhhxh'], ['hiicxiiciixcxhxhh'], ['icxiicixhh'], ['icixcxhxchicxh'], ['iicxhxicicicxhxhicixxhxhhixxhxhhxh'], ['KDZDlWIDTdR'], ['icixh'], ['icicxhx'], ['icicichxhxh'], ['hiicxiicixcxhchh'], ['icicxhicicixcxhicicxhxiicixcxhicicxhxicixxhxhhxhcxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhhxicihh'], ['iccicxhicixcxhxh'], ['icicxhxichiicxiicixcxhxhhixxhxhh'], ['KDZDlWIDTdicixhR'], ['iicKDZDlWIDTdicixhRxhxicicicxhxhicixxhxhhixxhxhhxh'], ['iicKDZDlWIDTdicixhRhxicicicxhxhicixxhxhhixxhxhhxh'], ['KiDZDlWIDTdicixhR'], ['iciicicxhxhxcxhicicxhxicixxxhxhhxh'], ['icixcxhKDZlWIDTdRicicxhxicicicxhxihiicxiiciixcxhxhhxhhixxhxhhxh'], ['KDZlWicicxhxichiicxiicixcxhxhhixxhxhhdR'], ['KDZlWIDDTdR'], ['hiicxiichiixcxhxhh'], ['hicxxiicixcxhxicixcxhxhhicixcxxhxhh'], ['iicicicxhxicixxhxhhxhxicicixcxhxicixxhxhhixxhxhhxh'], ['KKiDZDlWIDTdicixhRDZlWIDTdR'], ['iccicxhicixcxh'], ['iicixxhxhxhxiciicKDZDlWIDTdicixhRhxicicicxhxhicixxhxhhixxhxhhxhicicxhxcicixxhxhhixxhxhhxh'], ['icxiiciicxiicixcxhxhhxhh'], ['KicicixcxhicicxhxiicixcxhicicxhxicixxhxhhxhcxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhhDZDlWIDTdicixhR'], ['KDZZlWIDDTdR'], ['icxiicixh'], ['icicixcxhicicxhxiicixcxhicicicixcxhKDZlWIDTdRicicxhxicicicxhxihiicxiiciixcxhxhhxhhixxhxhhxhxhxicixxhxhhxhcxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhh'], ['icxiiicixh'], ['vbCTq'], ['icichxhxh'], ['icicxhxichiicxiicixcxhxhhixxhxiicxhxicicicxhxhiciixxhxhhixxihxhhxhhh'], ['hicxiicixcxixhxhh'], ['hhiicxiicixcxhchh'], ['cicicxhx'], ['icicicxiiciicxiicixcxhxhhxhhxhxicihh'], ['icicxhxicicixcxhxchicicixcxhicicxhxicxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhhicxhixxhhxhh'], ['cicicxhxcicxhxicixxxhxhhxh'], ['iicxh'], ['icixcxhicicKDZlWIDTdRxhiicxiicixcxhxhhhiicixcxhxhxicixxhxhhxh'], ['hicxicicixcxhicicxhxiicixcxhicicxhxicixxhxhhxhcxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhhiicihxhh'], ['cch'], ['icixcxxhicicKDZlWIDTdRxhiicxiicixiccicxhicixcxhxhcxhxhhhiicixcxhxhxicixxhxhhxh'], ['iivbCTqcxhxicicicxhxicixxhxhhixxhxiicKDZDlWIDTdicixhRhxicicicxhxhicixxhxhhixxhxhhxhhhxh'], ['iiccxh'], ['icicxhxicihicxicicixcxhicicxhxiicixcxhicicxhxicixxhxhhxhcxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhhiicihxhhxhh'], ['icxicixhh'], ['KKDiDZDlWIDTdicixhRDZlWIDTdR'], ['icicxhxicicixcxhxchicicixcxhicicxhxicxiicixcxhxhhicixxhxhhxhichxhh'], ['icihicxxiicixcxhxicixcxhxhhicixcxxhxhhxicihh'], ['icicxicicxhxicihicxicicixcxhicicxhxiicixcxhicicxhxicixxhxhhxhcxiicixcxhxhhicixxhxhhxhicxhxicixcxhxhhiicihxhhxhhhh'], ['icicxhiicxchxich'], ['xxhxhhixxhxiicKDZDlWIDTdicixhRhxicicicxhxhicixxhxhhixxhxhhxhhhxh'], ['icicxhxichiicxiicixcxhxhhixhxhxiicxhxicicicxhxhiciixxhxhhixxihxhhxhhh'], ['icicicxhxichiicxiicixcxhxhhixxhxiicxhxicicicxhxhiciixxhxhhixxihxhhxhhhicxhxh'], ['icicichxhx'], ['KDZlWIDTdRicixcxxicicKDZlWIDTdRxhiicxiicixiccicxhicixcxhxhcxhxhhhiicixcxhxhxicixxhxhhxh'], ['icxhKDZlWIDTdR'], ['KDZlWIDTdRicixcxxicicKDZlWIDTdRxhiicxiicixxiccicxhicixcxhxhcxhxhhhiicixcxhxhxicixxhxhhxh'], ['icicxhxih'], ['ixh'], ['icxiicKDZDlWIDTdicixhRhxicicicxhxhicixxhxhhxixxhxhhxhiiicixh'], ['icicihchxhxh'], ['icicxhiicicicxhxicixxhxhhxhxicicixcxhxicixxhxhhixxhxhhxhxicicixcxhxchicicixcxhicicxhxicxiicixcxhxhhicixxhxhhxhicxhxicixxcxhxhhicxhixxhhxhh'], ['TIUmFRsecT'], ['ixxh'], ['icicxhxicicixcxhxchicicixcxhicicxhxicxiicixcxhxhhicixixhxhhxhichxhh'], ['KDZlWicicxhxixiicixcxhxhhixxhxhhdR'], ['KKDiDZDlWiciicicxhxhxcxhicicxhxicicixcxhxicixcxhxhhixxxhxhhxhIDTdicixhRDZlWIDTdR'], ['hiicxiiKKDiDZDlWIDTdicixhRDZlWIDTdRcixcxhxhh']]
results = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(text_match_two_three(*inp), exp, 0)

