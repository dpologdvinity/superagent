from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange', 'apple', 'banana', 'banana'], 'quantity': [10, 15, 5, 10, 15, 15]})

    def test_valid_input(self):
        ax = task_func(self.df, 'fruit')
        self.assertIsInstance(ax, plt.Axes)
        plt.close()

    def test_nonexistent_column(self):
        with self.assertRaises(Exception):
            task_func(self.df, 'color')
        plt.close()

    def test_empty_dataframe(self):
        with self.assertRaises(Exception):
            task_func(pd.DataFrame(), 'fruit')
        plt.close()
