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
        self.df = pd.DataFrame({'A': np.random.normal(0, 1, 1000), 'B': np.random.exponential(1, 1000), 'C': ['text'] * 1000})

    def test_return_type(self):
        axes = task_func(self.df)
        for ax in axes:
            self.assertIsInstance(ax, plt.Axes)

    def test_invalid_input_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            task_func('not a dataframe')
