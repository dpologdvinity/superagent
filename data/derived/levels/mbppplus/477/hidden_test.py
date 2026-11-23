from solution import is_lower
candidate = is_lower
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


inputs = [['InValid'], ['TruE'], ['SenTenCE'], [''], ['True'], ['FALSE'], ['123'], ['StRiNg'], ['LOWER CASE'], ['nUmBeRs 123'], ['    extra spaces    '], ['camelCase'], ['UPPERCASE'], ['LOWER CASOE'], ['LOWER SE'], ['camelCacamelCasese'], ['1123'], ['LOWTrueER CASOE'], ['11123'], ['spaces'], ['LOWER CASCE'], ['LOWTrucamespaceslCacamelCaseseeER CASOE'], ['SE'], ['extra'], ['X'], ['LOWTrucamespaceslCacam11123 CASOE'], ['exxtra'], ['LOWTrucamespaceslCacam11123'], ['Trrue'], ['LOWRER CASOE'], ['LOWEWR CEASE'], ['LOWER CASROE'], ['TUPPERCASErue'], ['Trrrue'], ['LOWER CAROE'], ['LOWER'], ['LOWER CAS ROLOWRERE'], ['LOWER ROLOWRERECAS ROLOWRERE'], ['LOWER LCASCE'], ['CASCE'], ['camelCaese'], ['LOWRER'], ['CAROE'], ['xLOWER CASOexxtraE'], ['camelCasme'], ['eTrrCASOexxtraEue'], ['xLOWER'], ['11eTrrCASOexxtraEue123'], ['eTrrCASOexxtraaEue'], ['C'], ['camelCsme'], ['spnUmBeRsaces'], ['LOWEWR'], ['LOWER ALCASCE'], ['camelCslme'], ['LCASCE'], ['LR CASOE'], ['oa'], ['LOWTrueER'], ['SLOWER SE'], ['eTrrCASOexxtraaEuCASOexxtraEe'], ['LLOWTrueEROWER CASLOWEWR CEASE ROROLOWREREOLOWRERE'], ['TruenUmBeRs'], ['g'], ['CASE'], ['oaa'], ['LOWER ROLOWRERECAS ROLLOWER SEOWRERE'], ['11eTrrCASOexxte123'], ['SSE'], ['FvqXvHKtQ'], ['xLOWERO CASOexxtra'], ['ROROLOWREREOLOWRERE'], ['RACAROE'], ['LOWR SE'], ['cLLOWTrueEROWER CASLOWEWR CEASE ROROLOWREREOLOWREREamelCacamelCasese'], ['eLCASCExtra'], ['sspnUmBeRsaces'], ['LOWER ROLOWRERECAS ROLLOWER SEOWREREoa'], ['Trueg'], ['LOWER ROLOWRERxLOWERO CASOexxtraECAS ROLLOWER SEOWREREoa'], ['cLLOWTrueEROWER'], ['LOWTrueR'], ['11eTrrCASOexxtraExLOWEaROue123'], ['CCAROE'], ['ceamelCasme'], ['SL OWER SE'], ['eLCASCExtraSSE'], ['TUPPERCASErueSE'], ['caeTrrCASexxtraEuemelCase'], ['LOWOTrueER'], ['111323'], ['WLOWEWOR CEASE'], ['CASOexxtraE'], ['SEOWRERE'], ['123LOWTrueER CASOE'], ['cLLOWTrueEROWER CASLOWEWR CEASE ROROLOWREREOLEOWREREamelCacamelCaLOWRER CASOEsese'], ['camTruegelCaese'], ['oeTrrCASOexxtraEueaa'], ['SL OWER oeTrrCASOexxtraEueaaSE'], ['Tre'], ['ROLLOWER'], ['cLLOWTrueEROWERSLOWER SE'], ['CASOexxtra LCASRCE'], ['LOWER cLLOWTrueEROWERSLOWERASCE'], ['LOWER CCE'], ['LsspnUmBeRsacesOWER LCASCE'], ['cLLOWTrueEROWERSLOWERASCE'], ['CASOexxtra LC ASRCE'], ['LROROLOWREREOLEOWREREamelCacamelCaLOWRERER'], ['LCASRCE'], ['spaceROLOWREREs'], ['LR nUmBeRsxLOWERCASOE'], ['12LOWEROROLOWREREOLEOWREREamelCacamelCaLOWRERR CASE3LOWTrueER CASOE']]
results = ['invalid', 'true', 'sentence', '', 'true', 'false', '123', 'string', 'lower case', 'numbers 123', '    extra spaces    ', 'camelcase', 'uppercase', 'lower casoe', 'lower se', 'camelcacamelcasese', '1123', 'lowtrueer casoe', '11123', 'spaces', 'lower casce', 'lowtrucamespaceslcacamelcaseseeer casoe', 'se', 'extra', 'x', 'lowtrucamespaceslcacam11123 casoe', 'exxtra', 'lowtrucamespaceslcacam11123', 'trrue', 'lowrer casoe', 'lowewr cease', 'lower casroe', 'tuppercaserue', 'trrrue', 'lower caroe', 'lower', 'lower cas rolowrere', 'lower rolowrerecas rolowrere', 'lower lcasce', 'casce', 'camelcaese', 'lowrer', 'caroe', 'xlower casoexxtrae', 'camelcasme', 'etrrcasoexxtraeue', 'xlower', '11etrrcasoexxtraeue123', 'etrrcasoexxtraaeue', 'c', 'camelcsme', 'spnumbersaces', 'lowewr', 'lower alcasce', 'camelcslme', 'lcasce', 'lr casoe', 'oa', 'lowtrueer', 'slower se', 'etrrcasoexxtraaeucasoexxtraee', 'llowtrueerower caslowewr cease rorolowrereolowrere', 'truenumbers', 'g', 'case', 'oaa', 'lower rolowrerecas rollower seowrere', '11etrrcasoexxte123', 'sse', 'fvqxvhktq', 'xlowero casoexxtra', 'rorolowrereolowrere', 'racaroe', 'lowr se', 'cllowtrueerower caslowewr cease rorolowrereolowrereamelcacamelcasese', 'elcascextra', 'sspnumbersaces', 'lower rolowrerecas rollower seowrereoa', 'trueg', 'lower rolowrerxlowero casoexxtraecas rollower seowrereoa', 'cllowtrueerower', 'lowtruer', '11etrrcasoexxtraexlowearoue123', 'ccaroe', 'ceamelcasme', 'sl ower se', 'elcascextrasse', 'tuppercaseruese', 'caetrrcasexxtraeuemelcase', 'lowotrueer', '111323', 'wlowewor cease', 'casoexxtrae', 'seowrere', '123lowtrueer casoe', 'cllowtrueerower caslowewr cease rorolowrereoleowrereamelcacamelcalowrer casoesese', 'camtruegelcaese', 'oetrrcasoexxtraeueaa', 'sl ower oetrrcasoexxtraeueaase', 'tre', 'rollower', 'cllowtrueerowerslower se', 'casoexxtra lcasrce', 'lower cllowtrueerowerslowerasce', 'lower cce', 'lsspnumbersacesower lcasce', 'cllowtrueerowerslowerasce', 'casoexxtra lc asrce', 'lrorolowrereoleowrereamelcacamelcalowrerer', 'lcasrce', 'spacerolowreres', 'lr numbersxlowercasoe', '12lowerorolowrereoleowrereamelcacamelcalowrerr case3lowtrueer casoe']
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(is_lower(*inp), exp, 0)

