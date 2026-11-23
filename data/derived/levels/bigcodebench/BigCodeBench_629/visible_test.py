from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        """Ensure the data directory exists before any tests are run."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def tearDown(self):
        """Clean up by removing the data directory and its contents after all tests."""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)

    def test_single_dataframe(self):
        """Test with a single DataFrame."""
        df = pd.DataFrame({'Column1': [1, 2], 'Column2': [3, 4]})
        task_func([df], 'single_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'single_dataframe.csv')))

    def test_multiple_dataframes(self):
        """Test with multiple DataFrames."""
        df1 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
        df2 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})
        task_func([df1, df2], 'multiple_dataframes.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'multiple_dataframes.csv')))

    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df = pd.DataFrame()
        task_func([df], 'empty_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'empty_dataframe.csv')))
