from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):
    """Tests case for function `task_func`."""

    def test_dataframe_shape_default(self):
        """Test if the DataFrame has default shape (100 rows, 3 columns) with default parameters."""
        np.random.seed(1)
        df_test = task_func()
        self.assertEqual(df_test.shape, (100, 3))

    def test_dataframe_shape_custom_rows(self):
        """Test if the DataFrame has the correct shape when a custom number of rows is specified."""
        np.random.seed(2)
        df_test = task_func(50)
        self.assertEqual(df_test.shape, (50, 3))

    def test_dataframe_shape_custom_columns(self):
        """Test if the DataFrame has the correct shape with a custom number of columns."""
        np.random.seed(3)
        df_test = task_func(50, 5)
        self.assertEqual(df_test.shape, (50, 5))
