from solution import all_Characters_Same
candidate = all_Characters_Same
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


inputs = [['python'], ['aaa'], ['data'], [''], ['ms'], ['mms'], ['msms'], ['mmms'], ['yQNKBeQ'], ['msmyQNKBeQs'], ['mmss'], ['m'], ['msmss'], ['msmyQNyQNKBeQKBeQs'], ['mmsss'], ['mmsmyQNKBeQsmsss'], ['smssms'], ['mmsmss'], ['yKQNKBeQ'], ['mmmmmsmsssmmsss'], ['msmms'], ['msmyQNyQNKBeQKBeQsmmsmss'], ['msmyQNyQNBKBeQKBeQsmmsmss'], ['mmmsms'], ['mmsms'], ['msmmsms'], ['mmmss'], ['smssm'], ['mss'], ['msmmmss'], ['mmmms'], ['mssmsmyQNKBeQs'], ['mmsmyQNKBeQsmmsss'], ['msmyQNKBeQNs'], ['zWgdk'], ['mmsmsmmssss'], ['mQsmyQNKBeQs'], ['smssmsmyQNKBeQsmssms'], ['mmmmsms'], ['RfuIu'], ['mmssms'], ['RufuIu'], ['mmsmyQNyQNKBeQKBeQsmmmsms'], ['mssmsmysQNKBeQs'], ['mssmsNKBeQs'], ['mmmsmsmss'], ['mmmmsmyQNKBeQsmmsssssms'], ['msmmss'], ['smss'], ['smszWgdksm'], ['smssmms'], ['msmyQNyQNKBeQKBseQsmmsmss'], ['mmsmyQNyQNKBmmmsmseQKBeQsmmmsms'], ['msmmmmsmyQNKBeQNsss'], ['mmmsmss'], ['mmmmmmsmsssmmsss'], ['mmmsmyQNKBeQNsssms'], ['smssmsmymmsmsmmssssQNKBeQsmssms'], ['mmsmyQNKBmeQs'], ['mmmsmyQNyQNKBmmmsmseQKBeQsmmmsmsmsms'], ['mmmmsmsmsmmmmmmsmsssmmsss'], ['mmmssyQNKBeQmss'], ['msmyQNyQKNKBeQKBeQsmmsmss'], ['msmyQNyQKNKBmsmyQNKBeQNseQKBeQsmmsmss'], ['msmyQNyQNKBeQKBseQsmmQsmss'], ['msmyQNKBesQNs'], ['yKQNKBemssmsmysQNKBeQsQ'], ['mmsmyQNKBeQssmmsss'], ['msmmsmmsms'], ['mmyKQNKBeQmssyQNKBeQmss'], ['mmmmsmssmsNKBeQsmsmmms'], ['mmmsmmmsmsssmmsss'], ['smssmmmmmsmsssmmsssm'], ['mmmsmyQNKBeQsmssss'], ['msmyQNyQNBKyBeQKBeQsmmsmss'], ['msmmsmmmsms'], ['mmmsmsmyQNyQNKBeQKBseQsmmsmssms'], ['mmmmmsmyQNKBeQNsssmsmms'], ['mmmmsmsmsmmmmmmsmsssmmmmsmyQNKBeQsmmssssss'], ['mmmmsmyQNKBeQNsssmsmsmmsmmssss'], ['mmmmmmmsmyQNKBeQNsssmsmsmmsmmssssmmsmyQNKBeQNsssmsmms'], ['mssmQsmyQNKBeQs'], ['smmsssmsmymmsmsmmssssQNKBeQsmssms'], ['yKQN'], ['smssmmmmmmmmmsmyQNKBeQNsssmsmsmmsmmssssmmsmyQNKBeQNsssmsmmss'], ['smssmsmyQNKBmmsmyQNKBeQssmmssseQsmssms'], ['Rf'], ['mmRufuIus'], ['smssmBmmsmyQNKBeQssmmssseQsmssms'], ['BmmmsmyQNyQNKBmmmsmseQKBeQsmmmsmsmsmsRfuIu'], ['smsmsmssmsmyQNKBmmsmyssseQsmssms'], ['yKQNKmssmQsmyQNKBeQsBeQ'], ['mssmmmmsmyQNKBeQsmmsssssms'], ['zWgdWk'], ['mssmmms'], ['zWgdW'], ['smmsmyQNKBeQssmmsssmssm'], ['mssmsmysQNKBeQss'], ['mszWgWdWkms'], ['msmssmsmysQNKBeQss'], ['mmsmyQNyQNKBmmmsmseQKBmeQsmmmsms'], ['smszkWgdksm'], ['msmyQNyQNKBeQKBesQsmmsmss'], ['smssmBmmsmyQNKBeQsssmmssseQssmssms']]
results = [False, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(all_Characters_Same(*inp), exp, 0)

