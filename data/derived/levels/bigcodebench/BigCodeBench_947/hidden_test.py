from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
# Unit testing
import unittest
import numpy.testing as npt
class TestCases(unittest.TestCase):
        
    def test_case_1(self):
        # Using default parameters
        matrix = task_func(seed=0)
        self.assertEqual(matrix.shape, (3, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) > 0))  # Dates should be unique
    def test_case_2(self):
        # Using custom rows and columns, and a small date range
        matrix = task_func(2, 2, datetime(2021, 1, 1), datetime(2021, 1, 10), seed=42)
        self.assertEqual(matrix.shape, (2, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
    def test_case_3(self):
        # Using custom rows and columns, and a large date range
        matrix = task_func(4, 4, datetime(2000, 1, 1), datetime(2021, 12, 31), seed=55)
        self.assertEqual(matrix.shape, (4, 4))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
    def test_case_4(self):
        # Using a date range of one day
        matrix = task_func(1, 1, datetime(2021, 1, 1), datetime(2021, 1, 1), seed=0)
        expected_date = np.array(['2021-01-01'], dtype='datetime64[us]').reshape(1, 1)
        npt.assert_array_equal(matrix, expected_date)  # Only one date in the range
    def test_case_5(self):
        # Using custom rows and columns, and a date range with only two days
        matrix = task_func(1, 2, datetime(2021, 1, 1), datetime(2021, 1, 2), seed=41)
        self.assertEqual(matrix.shape, (1, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
        expected_dates = np.array(['2021-01-01', '2021-01-02'], dtype='datetime64[us]').reshape(1, 2)
        for date in expected_dates.ravel():
            self.assertIn(date, matrix.ravel())
