from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = task_func()
        self.assertEqual(df.shape, (SIZE, 2))

    def test_random_numbers_range(self):
        """Test that the random numbers fall within the specified range."""
        df = task_func()
        self.assertTrue(df['Random Numbers'].between(0, RANGE).all())

    def test_moving_average_calculation(self):
        """Test that the moving average is correctly calculated."""
        df = task_func()
        for i in range(6):
            expected_avg = statistics.mean(df['Random Numbers'].iloc[max(0, i - 5):i + 1])
            self.assertEqual(df['Moving Average'].iloc[i], expected_avg, 'Moving average calculation mismatch.')
