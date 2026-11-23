from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        self.letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        random.seed(42)
        self.df = pd.DataFrame({'Letters': random.choices(self.letters, k=100)})

    def test_return_type(self):
        ax = task_func(self.df)
        self.assertIsInstance(ax, plt.Axes)

    def test_invalid_input_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            task_func('not a dataframe')
