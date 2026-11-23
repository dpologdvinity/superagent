from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame({'Date': pd.date_range(start='1/1/2021', periods=10), 'Sales': np.random.randint(100, 2000, size=10)})

    def test_return_type(self):
        np.random.seed(42)
        large_df = pd.DataFrame({'Date': pd.date_range(start='1/1/2021', periods=30), 'Sales': np.random.randint(100, 2000, size=30)})
        ax = task_func(large_df)
        self.assertIsInstance(ax, plt.Axes)

    def test_value(self):
        ax = task_func(self.df)
        line = ax.get_lines()[0]
        sales = line.get_ydata()
        actual_sales = [str(int(sale)) for sale in sales]
        expect = ['1226', '1559', '960', '1394', '1230', '1195', '1824', '1144', '1738', '221']
        self.assertEqual(actual_sales, expect, 'DataFrame contents should match the expected output')

    def test_plot_title_and_labels(self):
        np.random.seed(42)
        large_df = pd.DataFrame({'Date': pd.date_range(start='1/1/2021', periods=30), 'Sales': np.random.randint(100, 2000, size=30)})
        ax = task_func(large_df)
        self.assertEqual(ax.get_title(), 'Daily Turnover')
        self.assertEqual(ax.get_ylabel(), 'Sales')
