from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_dataframe_shape(self):
        """Test if the DataFrame has the correct shape."""
        df = task_func()
        self.assertEqual(df.shape, (12, 5))

    def test_dataframe_columns(self):
        """Test if the DataFrame has the correct column names."""
        df = task_func()
        expected_columns = PRODUCTS
        self.assertListEqual(list(df.columns), expected_columns)

    def test_dataframe_index(self):
        """Test if the DataFrame has the correct index."""
        df = task_func()
        expected_index = MONTHS
        self.assertListEqual(list(df.index), expected_index)
