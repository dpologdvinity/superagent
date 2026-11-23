from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        np.random.seed(0)

    def test_case_1(self):
        df = pd.DataFrame({'Value': np.random.normal(0, 1, 1000)})
        self.assertTrue(task_func(df, 'Value', 0.05))

    def test_case_2(self):
        df = pd.DataFrame({'Value': np.random.uniform(0, 1, 1000)})
        self.assertFalse(task_func(df, 'Value', 0.05))

    def test_case_3(self):
        df = pd.DataFrame({'Value': np.random.exponential(1, 1000)})
        self.assertFalse(task_func(df, 'Value', 0.05))
