from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Testing with a sample date list
        input_dates = ['2022-10-22', '2022-10-23', '2022-10-24', '2022-10-25']
        expected_output = pd.Series([1, 1, 0, 0, 0, 1, 1], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_2(self):
        # Input 2: Testing with a list where all dates fall on a single weekday
        input_dates = ['2022-10-24', '2022-10-31', '2022-11-07']
        expected_output = pd.Series([3, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_3(self):
        # Input 3: Testing with an empty list
        input_dates = []
        expected_output = pd.Series([0, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_4(self):
        # Input 4: Testing with a mixed list of dates
        input_dates = ['2022-01-01', '2022-02-14', '2022-03-17', '2022-12-31']
        expected_output = pd.Series([1, 0, 0, 1, 0, 2, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_5(self):
        # Input 5: Testing with dates spanning multiple weeks
        input_dates = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']
        expected_output = pd.Series([1, 1, 1, 1, 1, 1, 1], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
