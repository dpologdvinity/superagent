from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'A')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('A' in df.columns)

    def test_case_2(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'B')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('B' in df.columns)

    def test_case_3(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'C')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('C' in df.columns)
