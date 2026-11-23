from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_return_type(self):
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame)

    def test_data_points_count(self):
        random.seed(0)
        result = task_func()
        self.assertEqual(len(result), 10000)

    def test_value_range(self):
        random.seed(0)
        result = task_func()
        within_range = result['Value'].apply(lambda x: 0.0 <= x <= 10.0)
        self.assertTrue(within_range.all())
