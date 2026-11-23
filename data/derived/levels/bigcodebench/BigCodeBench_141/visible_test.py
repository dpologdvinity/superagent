from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_dataframe_structure(self):
        df, _ = task_func(10)
        self.assertEqual(df.shape, (10, 6))

    def test_invalid_rows_input_negative(self):
        with self.assertRaises(ValueError):
            task_func(-1)

    def test_invalid_rows_input_zero(self):
        with self.assertRaises(ValueError):
            task_func(0)
