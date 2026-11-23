from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd

class TestCases(unittest.TestCase):

    def test_case_1(self):
        """Test the correctness of the scaling applied by the function."""
        data = {'a': [10.5, 23.4, 15.6, 78.9], 'b': [45.6, 67.8, 89.0, 12.3], 'c': [12.3, 45.6, 78.9, 0.1]}
        df = pd.DataFrame(data)
        result = task_func(data)
        self.assertTrue(np.isclose(result['a'].mean(), 0, atol=1e-07))
        self.assertTrue(np.isclose(result['b'].mean(), 0, atol=1e-07))
        self.assertTrue(np.isclose(np.std(result['a']), 1, atol=0.01))
        self.assertTrue(np.isclose(np.std(result['b']), 1, atol=0.01))

    def test_case_2(self):
        """Test with an empty DataFrame."""
        data = {}
        df = pd.DataFrame(data)
        result = task_func(data)
        self.assertTrue(result.empty)

    def test_case_3(self):
        """Test with a DataFrame that doesn't have any columns to scale."""
        data = {'c': ['foo', 'bar']}
        df = pd.DataFrame(data)
        result = task_func(data)
        pd.testing.assert_frame_equal(result, df, check_dtype=False)
