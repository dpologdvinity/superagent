from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_normal_case(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result = task_func(df)
        self.assertEqual(result.shape, (2, 4))
        plt.close()

    def test_varying_length_lists(self):
        df = pd.DataFrame([['2021-01-01', [8, 10]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result = task_func(df)
        self.assertEqual(result.shape, (2, 4))
        plt.close()

    def test_varying_length_list_2(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        result = task_func(df)
        self.assertEqual(result.empty, False)
        plt.close()
