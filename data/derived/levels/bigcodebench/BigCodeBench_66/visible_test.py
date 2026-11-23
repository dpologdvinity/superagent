from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def test_case_1(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        analyzed_df, plot = task_func(data)
        expected_df = pd.DataFrame({'col1': [1, 1, 2, 2], 'col2': [1, 2, 1, 2], 'col3': [2, 1, 3, 1]})
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(plot.get_xlabel(), 'col3')

    def test_case_2(self):
        data = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
        analyzed_df, plot = task_func(data)
        expected_df = pd.DataFrame({'col1': [1, 1], 'col2': [1, 2], 'col3': [3, 1]})
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(plot.get_xlabel(), 'col3')

    def test_case_3(self):
        data = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [6, 7, 8]]
        analyzed_df, plot = task_func(data)
        expected_df = pd.DataFrame({'col1': [1, 6], 'col2': [2, 7], 'col3': [3, 1]})
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(plot.get_xlabel(), 'col3')
