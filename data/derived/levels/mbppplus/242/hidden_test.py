from solution import count_charac
candidate = count_charac
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


inputs = [['python programming'], ['language'], ['words'], [''], ['a'], ['ɢᴜᴍɪᴇꜱ'], ['cMPNwvV'], ['ccMPNwvV'], ['ccMPcMPNwvVNwvV'], ['accMPNwvV'], ['aaccMPNwvV'], ['ccMPNwV'], ['ccMPNwvVcMPNwvV'], ['aaccMPNwv'], ['ccMPcMPNwvVNvV'], ['ɢᴜaaccMPNwvᴍɪᴇꜱ'], ['aacccMPNwvVMPNwv'], ['aaaccccMPcMPNwvVNwvVNwv'], ['cccMPcMPNwvVNvV'], ['aaccMPNw'], ['cNMPNwvV'], ['cNMPNwvcNMPNwvVV'], ['ccMPV'], ['accaaccMPNwvMPNwvV'], ['aaccccMPNwvVcMPNwvVMPNwvV'], ['aaaccccMPcMPNwvcMPNwvVVNwvVNwv'], ['ccMPccccMPcMPNwvVNvVMPNwvVNwvV'], ['aaccMPaccaaccMPNwvMPNwvVNw'], ['aaaaccMPNcMPNwvVwv'], ['ccMPccccMPcMPNwvVNvVMPNwvVNcwvV'], ['ccMPcMPNwvVNwvvV'], ['accV'], ['cNMPNwvcNMwPNwvVV'], ['accaaccMPNwccMPcMPNwvVNwvvVvMPccMPVNwvV'], ['aaacccccMPcMPNwvVNwvVcNwv'], ['ɢᴜᴍccMPcMPNwvVNvVɪᴇꜱaccMPNwvV'], ['ccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvV'], ['ɢᴜaaccMPNwvᴍaccaaccMPNwccMPcMPNwvVNwvvVvMPccMPVNwvVɪᴇꜱ'], ['ccMPNwaccMPNwvVVvV'], ['aaccMPaNwvMPNwvVNw'], ['accaaccMPNwccMPcMPNwvVNwvvVvMPMccvV'], ['ccMPcMPNwvVNvaaacccaaccMPNwccMPcMPNwvVNwvVcNwvV'], ['aaccMPNww'], ['aaccaaccMPNwvVMPNwcNMPNwvcNMaacccMPNwvVMPNwvwPNwvVVvV'], ['aaaaaccMPNcMPNwvVwv'], ['acacVcccMPcMPNwvVNvV'], ['ccMPccccMPcMPNNwvVNvVMPNwvVNcwvV'], ['cNMPNwv'], ['ɢᴜaaɢccMPNwvᴍɪᴇꜱ'], ['aaacMPNwvVNwvVcNwv'], ['aaccaaccMPNwvVMPNwcNMPNwvcNMaacccMPNwvVMPNwvwPNccMPNwVVV'], ['accaaccMPNPwvMPNwvV'], ['ɢᴜᴍV'], ['accaaccMPccMPNwVNPwaacccMwPNwvVMPNwv'], ['ccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvVccMPcMPNwvVNwvV'], ['cMPNwccMPcMPNwvVNwvvVvMPMccvV'], ['aaccccMPNwvVcV'], ['aaccccMPNwvNwvV'], ['ɢᴜaaccMPNwvᴍaacccMPNwvVMPNwvɪᴇꜱ'], ['ccMPcMPNwvVNvaaacccaacɢᴜaaccMPNwvᴍaacccMPNwvVMPNwvɪᴇꜱcMPNwccMPcMPNwvVNwvVcNwvV'], ['ccMPcMPNwNwvVNwvVcNwvV'], ['aaccMPaccaaccMPwNwvMPNwvVNwV'], ['accaaccMPNwccMPcccMPVvMPNwvVNwvvVvMPccMPVNwvV'], ['ccMPcMPNwvVNvaaccMPNwwV'], ['ccMPcccccMPcMPNNwvVNvVMPNVwvVNcwvV'], ['aaccaaccVaccMPNwvVNMPNwcNMccMPcMPNwvVNvaaacccaacɢᴜaaccMPNwvᴍaacccMPNwvVMPNwvɪᴇꜱcMPNwccMPcMPNwvVNwvVcNwvVPNwvcNMaacccMPNwvVMPNwvwPNccMPNwVVV'], ['ccMPccccMPcMPNccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvVNwvVNvVMPNwvVNcwvaaccaaccMPNwvVMPNwcNMPNwvcNMaacccMPNwvVMPNwvwPNwvVVvVV'], ['ccMccMPNwVPcMPccMPccccMPcMPNccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvVNwvVNvVMPNwvVNcwvaaccaaccMPNwvVMPNwcNMPNwvcNMaacccMPNwvVMPNwvwPNwvVVvVV'], ['aacccMPNwaaacccccMPcMPNwvVNwvVcNwvvVMPNwv'], ['ccMPcMPNwvaaaacMPNwvVNwvVcNwvaaaccMPNcMPNwvVwvVNwvV'], ['ccMPcccPcMPNwvVNvVMPNwvVNwvV'], ['aaccccMPNwvVcMPNwvVccMPcccccMPcMPNNwvVNvVMPNVwvVNcwvVMPNwvV'], ['aaccMPaMNwvMPNwvVNw'], ['ɢᴜaaccMPNwvᴍaccaacccMccMPNwVPcMPccMPccccMPcMPNccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvVNwvVNvVMPNwvVNcwvaaccaaccMPNwvVMPNwcNMPNwvcNMaacccMPNwvVMPNwvwPNwvVVvVVcMPNwccMPcMPNwvVNwvvVvMPccMPVNwvVɪᴇꜱ'], ['accaaccMPccMPNwVNPwaacccMwPNaaccMPNwvVwv'], ['cccMaaccccMPNwvNwvVPcMPNwvVNvV'], ['aaccccMPNwvVwcV'], ['ɢᴜᴍ'], ['accaaccMPaNwccMPcccMPVvMPNwVNwvvVvMPccMPVNwvV'], ['ccMPccccMPcMccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvVccMPcMPNwvVNwvVPNwvVNvVMPNwvVNcwvV'], ['aaacMPNwvVNwvVcNwvv'], ['aaccccMPcccPcMPNwvVNvVMPNwvVNwvVMv'], ['ɢᴜaaɢccMPNwvᴍᴍɪᴇꜱ'], ['accaaccMPNwccMPcccMPVvMPNwvVNwvcMPNwccMPcMPNwvVNwvvVvMPMccvVvVvMPccMPVNwvV'], ['ccMPcMPNPwvVNvaaacccaacɢᴜaaccMPNwvᴍaacccMPNwvVMPNwvɪᴇꜱcMPNwccMPcMPNwvVNwvVcNwvV'], ['aaccMPNwaaccaaccMPNwvVMPNwcNMPNwvcNMaacccMPNwvVMPNwvwPNwvVVvVw'], ['ɢᴜᴍccMPcMPNwvVNɢvVɪᴇꜱaccMPNwvV'], ['ccMPVaaacMPNwvVNwvVcNwvv'], ['acacVcccVNvV'], ['accaaccMPcccMPNwVNPwaacccMwPNaaccMPNwvVwv'], ['cccMPcMPPNwvVNvV'], ['aaccaaccMPNwvVMPNwcNMPNwvcNMaaaacccMPNwvVMPNwvcccMPNwvVMPNwvwPNwvVVvV'], ['aaccMPNwvccMPcMPNwvVNvaaacccaaccMPvNwccMPcMPNwvVNwvVcNwvV'], ['cccMPcɢᴜᴍɪᴇꜱMPPNwvVNvVaaccMPNwvV'], ['accaaccMPNwɢᴜaaɢccMPNwvᴍɪᴇꜱccMPcMPNwvVNwvvVvMPMccvV'], ['aaaccMPNwvV'], ['ccMPNcccccMPcMPNNwvVNvVMPNVwvVNcwvV'], ['aaaccccMPcvcMPNwvVVNwvVNwv'], ['aaccaaccVaccMPNwvVNMPNwcNMvccMPcMPNwvVNvaaacccaacɢᴜaaccMPNwvᴍaacccMPNwvVMPNwvɪᴇꜱcMPNwccMPcMPNwvVNwvVcNwvVPNwvcNMaacccMPNwvVMPNwvwPNccMPNwVVV'], ['ccMPccccMPcMccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvVccMPcMPNwvVNwvVPNwvVMPNwvVNcwvV'], ['aaccMPNaaccMPaMNwvMPNwvVNww'], ['ccMPcccMPccccMPcMPNccMPcMPNwvVNvaaacccccMPcMPNwvVNwvVcNwvVNwvVNvVMPNwvVNcwvaaccaaccMPNwvVMPNwcNMPNwvcNMaacccMPNwvVMPNwvwPNwvVVvVVPcMPNwvVNvVMPNwvVNcwvV'], ['cccMaccccMPNwvNwvVPcMPNwvVNvV'], ['waccMPNwvV'], ['cccMPcMPNaaaccccMPcMPNwvcMPNwvVVNwvVNwv'], ['ccMPNcccccMPcMPNNwvVNvVMPNVVwvVNcwvV']]
results = [18, 8, 5, 0, 1, 6, 7, 8, 15, 9, 10, 7, 15, 9, 14, 15, 16, 23, 15, 8, 8, 16, 5, 18, 25, 30, 30, 26, 18, 31, 16, 4, 17, 39, 25, 29, 39, 54, 18, 18, 35, 47, 9, 53, 19, 20, 32, 7, 16, 18, 56, 19, 4, 36, 54, 29, 14, 15, 31, 78, 22, 28, 45, 23, 34, 139, 124, 138, 41, 51, 28, 59, 19, 192, 40, 30, 15, 3, 45, 85, 19, 34, 17, 74, 79, 62, 30, 24, 12, 41, 16, 69, 57, 32, 51, 11, 35, 26, 140, 82, 27, 151, 29, 10, 39, 36]
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(count_charac(*inp), exp, 0)

