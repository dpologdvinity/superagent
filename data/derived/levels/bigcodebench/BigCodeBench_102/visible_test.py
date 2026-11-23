from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from unittest.mock import patch
from sklearn.datasets import load_diabetes

class TestCases(unittest.TestCase):

    def setUp(self):
        self.diabetes_data = load_diabetes()
        self.diabetes_df = pd.DataFrame(data=self.diabetes_data.data, columns=self.diabetes_data.feature_names)

    def test_return_type(self):
        """Test that the function returns a matplotlib Figure instance."""
        fig, diabetes_df = task_func()
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(diabetes_df, pd.DataFrame)

    def test_dataframe_values_equal(self):
        fig, diabetes_df = task_func()
        for col in self.diabetes_df.columns:
            self.assertTrue(all(self.diabetes_df[col] == diabetes_df[col]))

    def test_font_setting(self):
        """Test if the font setting is correctly applied to the figure."""
        task_func()
        current_font = plt.rcParams['font.family']
        self.assertIn('Arial', current_font)
