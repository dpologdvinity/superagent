from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = task_func()
        self.assertEqual(df.shape, (SIZE, 2))

    def test_random_range(self):
        """Test that the random numbers fall within the specified range."""
        df = task_func()
        self.assertTrue(df['X'].between(0, RANGE - 1).all())
        self.assertTrue(df['Y'].between(0, RANGE - 1).all())

    def test_columns_existence(self):
        """Ensure both 'X' and 'Y' columns exist."""
        df = task_func()
        self.assertIn('X', df.columns)
        self.assertIn('Y', df.columns)
