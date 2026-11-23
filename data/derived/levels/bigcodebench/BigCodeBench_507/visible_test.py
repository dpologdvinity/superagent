from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
from datetime import datetime

class TestCases(unittest.TestCase):

    def assertDictAlmostEqual(self, d1, d2, msg=None):
        for k, v in d1.items():
            if isinstance(v, float) and np.isnan(v):
                self.assertTrue(np.isnan(d2[k]), msg or f'{k} not almost equal')
            else:
                self.assertAlmostEqual(v, d2[k], msg=msg or f'{k} not equal')

    def test_case_1(self):
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000], [datetime(2022, 1, 2), 102, 108, 100, 105, 15000], [datetime(2022, 1, 3), 105, 110, 103, 108, 20000]]
        result = task_func('Open', data)
        expected_result = {'sum': 307, 'mean': 102.33333333333333, 'min': 100, 'max': 105}
        self.assertDictAlmostEqual(result, expected_result)

    def test_case_2(self):
        data = []
        result = task_func('Open', data)
        expected_result = {'sum': 0, 'mean': float('nan'), 'min': float('nan'), 'max': float('nan')}
        self.assertDictAlmostEqual(result, expected_result)

    def test_case_3(self):
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]]
        with self.assertRaises(ValueError):
            task_func('InvalidColumn', data)
