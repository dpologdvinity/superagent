from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_dates = ['2022-10-22', '2022-10-23', '2022-10-24', '2022-10-25']
        expected_output = pd.Series([1, 1, 0, 0, 0, 1, 1], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_2(self):
        input_dates = ['2022-10-24', '2022-10-31', '2022-11-07']
        expected_output = pd.Series([3, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_3(self):
        input_dates = []
        expected_output = pd.Series([0, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
