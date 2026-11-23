from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_normal_functionality(self):
        """Test the function with typical nested lists."""
        input_list = [['apple', 'banana'], ['apple'], ['banana', 'orange']]
        expected_df = pd.DataFrame({'Count': [2, 2, 1]}, index=['apple', 'banana', 'orange'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func(input_list), expected_df)

    def test_empty_list(self):
        """Test the function with an empty list."""
        expected_df = pd.DataFrame(columns=['Count'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func([]), expected_df)

    def test_single_level_list(self):
        """Test with a non-nested, single-level list."""
        input_list = [['apple', 'banana', 'apple']]
        expected_df = pd.DataFrame({'Count': [2, 1]}, index=['apple', 'banana'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(task_func(input_list), expected_df)
