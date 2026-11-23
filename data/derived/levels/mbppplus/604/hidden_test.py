from solution import reverse_words
candidate = reverse_words
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


inputs = [['python program'], ['java language'], ['indian man'], [''], [' '], ['   '], ['word'], ['a'], ['ab'], ['   word   '], [' a a a a a a  '], ['word1   word2   word3'], ['word1  word2  word3'], ['    a a a a a a'], ['  java language  '], ['word1         word2         word3'], ['abb'], ['java'], ['word1'], ['word1         word2         word3java'], ['language'], ['    a a a a a '], [' a a a a a a a'], ['u  java language  '], ['wordword11'], ['word    a a  a a a '], [' j java language  '], ['word11'], ['  word3java '], ['word1   wo rd2   word3'], ['rwordword11'], ['worword1         word2         word3javad1'], ['    a a a a a  '], ['worword1'], ['u  java langu  java language   '], ['    word   j java language  '], ['u  java languageword1  '], ['    a   a a a a  '], ['javaabb'], ['javvaabb'], ['abword'], ['jaaabb'], ['javaabbwordword11'], ['aorbword'], ['word1           a   a a a a    word2         word3'], [' worword1   a '], ['Ml'], ['languageword1'], ['rwoordword11'], ['wordword11word'], ['  word3langu java '], ['javabwordword11'], ['wword2  word3'], ['word3langu'], ['    '], ['wordwordword11word1'], ['langueage'], ['  java lwordword11anguage  '], ['la     a a a a a anguageword1'], ['aorbwordangueage'], ['    word   j java langjavaabbwordword11uage  '], ['  '], ['rd11'], ['wvord1         word2         word3java'], ['aorbwor  java lwordword11anguag'], ['    a a a'], ['worjavaabbwordword11d    a a  a a a '], ['word1   wo rd2 word1         word2         word3  word3'], ['rdd11'], ['D'], ['wor d1   wo rd2  '], ['wor11wdord'], ['jaavaabb'], ['worworwd1'], ['jaa'], ['    word   j java language  worword1'], ['u  java language  bb'], ['awoor'], ['d1'], ['ja'], ['javbaabb'], ['    word  worworwd1java lwordword11anguage  uage  worword1'], ['worlaenguage1'], ['la     a a a a a anguagejaword1'], ['    a a'], ['abwor  java lwordword11anguag'], ['wordwordword11rword1'], ['javabwoardword11'], ['Db'], ['awoorr'], [' a a a    word  worworwd1java lwordword11anguage  uage   '], ['dabword'], ['javaabbwordword1wonguage1'], ['  wu  java language  ord3langu java '], ['worwword1'], [' j java language  vaabb'], ['la     a a a a a anguagejaaword1'], ['laguageword1'], ['lwordword11anguag'], ['word    a a a3langu'], ['u  java languagewoord1  '], ['lwordword11abwor  java lwordword11anguaganguag'], ['    aa a a a a '], ['lwordword11anguagang a a a a a a  uag'], ['wword3oord1         word2         word3'], ['abwor'], ['uag'], ['anguageword1'], ['iQnak'], ['javbaajbb'], [' a a a a   wu  java language  ord3langu java a a a'], ['wo'], ['word2'], ['u  java languwword2agewoord1  '], ['word     a  a a a '], ['languageweord1']]
results = ['program python', 'language java', 'man indian', '', '', '', 'word', 'a', 'ab', 'word', 'a a a a a a', 'word3 word2 word1', 'word3 word2 word1', 'a a a a a a', 'language java', 'word3 word2 word1', 'abb', 'java', 'word1', 'word3java word2 word1', 'language', 'a a a a a', 'a a a a a a a', 'language java u', 'wordword11', 'a a a a a word', 'language java j', 'word11', 'word3java', 'word3 rd2 wo word1', 'rwordword11', 'word3javad1 word2 worword1', 'a a a a a', 'worword1', 'language java langu java u', 'language java j word', 'languageword1 java u', 'a a a a a', 'javaabb', 'javvaabb', 'abword', 'jaaabb', 'javaabbwordword11', 'aorbword', 'word3 word2 a a a a a word1', 'a worword1', 'Ml', 'languageword1', 'rwoordword11', 'wordword11word', 'java word3langu', 'javabwordword11', 'word3 wword2', 'word3langu', '', 'wordwordword11word1', 'langueage', 'lwordword11anguage java', 'anguageword1 a a a a a la', 'aorbwordangueage', 'langjavaabbwordword11uage java j word', '', 'rd11', 'word3java word2 wvord1', 'lwordword11anguag java aorbwor', 'a a a', 'a a a a a worjavaabbwordword11d', 'word3 word3 word2 word1 rd2 wo word1', 'rdd11', 'D', 'rd2 wo d1 wor', 'wor11wdord', 'jaavaabb', 'worworwd1', 'jaa', 'worword1 language java j word', 'bb language java u', 'awoor', 'd1', 'ja', 'javbaabb', 'worword1 uage lwordword11anguage worworwd1java word', 'worlaenguage1', 'anguagejaword1 a a a a a la', 'a a', 'lwordword11anguag java abwor', 'wordwordword11rword1', 'javabwoardword11', 'Db', 'awoorr', 'uage lwordword11anguage worworwd1java word a a a', 'dabword', 'javaabbwordword1wonguage1', 'java ord3langu language java wu', 'worwword1', 'vaabb language java j', 'anguagejaaword1 a a a a a la', 'laguageword1', 'lwordword11anguag', 'a3langu a a word', 'languagewoord1 java u', 'lwordword11anguaganguag java lwordword11abwor', 'a a a a aa', 'uag a a a a a a lwordword11anguagang', 'word3 word2 wword3oord1', 'abwor', 'uag', 'anguageword1', 'iQnak', 'javbaajbb', 'a a a java ord3langu language java wu a a a a', 'wo', 'word2', 'languwword2agewoord1 java u', 'a a a a word', 'languageweord1']
for i, (inp, exp) in enumerate(zip(inputs, results)):
    assertion(reverse_words(*inp), exp, 0)

