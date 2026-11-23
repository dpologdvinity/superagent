from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temperatures = pd.DataFrame({'temperature': [random.randint(-10, 30) for _ in range(365)], 'date': pd.date_range(start='01-01-2023', periods=365, tz='America/New_York')}).set_index('date')

    def test_basic_functionality(self):
        ax = task_func(self.temperatures)
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())

    def test_incorrect_dataframe(self):
        incorrect_df = pd.DataFrame({'temp': [20, 21], 'time': [datetime.now(), datetime.now()]})
        with self.assertRaises(ValueError):
            task_func(incorrect_df)
