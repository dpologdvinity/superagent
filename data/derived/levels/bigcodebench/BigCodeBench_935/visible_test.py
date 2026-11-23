from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_abc(self):
        """Test with the word 'abc'."""
        result = task_func('abc')
        expected = pd.DataFrame({'Letter': ['a', 'b', 'c'], 'Position': [1, 2, 3]})
        pd.testing.assert_frame_equal(result, expected)

    def test_xyz(self):
        """Test with the word 'xyz'."""
        result = task_func('xyz')
        expected = pd.DataFrame({'Letter': ['x', 'y', 'z'], 'Position': [24, 25, 26]})
        pd.testing.assert_frame_equal(result, expected)

    def test_mixed_case_error(self):
        """Test with a mixed case word, expecting a ValueError."""
        with self.assertRaises(ValueError):
            task_func('AbC')
