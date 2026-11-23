from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def test_case_1(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        analyzed_df, ax = task_func(data)
        expected_data = [[1, 1, 2], [1, 2, 1], [2, 1, 3], [2, 2, 1]]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [2, 1, 3, 1])

    def test_case_2(self):
        data = [[1, 1, 2], [1, 1, 3], [1, 2, 4], [1, 1, 5], [1, 3, 7]]
        analyzed_df, ax = task_func(data)
        expected_data = [[1, 1, 3], [1, 2, 1], [1, 3, 1]]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [3, 1, 1])

    def test_case_3(self):
        data = [[1, 1, 1], [1, 2, 3], [2, 1, 4], [2, 2, 5]]
        analyzed_df, ax = task_func(data)
        expected_data = [[1, 1, 1], [1, 2, 1], [2, 1, 1], [2, 2, 1]]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [1, 1, 1, 1])
