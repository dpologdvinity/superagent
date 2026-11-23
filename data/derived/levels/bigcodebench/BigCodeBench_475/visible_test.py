from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.axes
import numpy as np
from datetime import datetime

class TestCases(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({'dates': ['01/01/2000', '01/02/2000', '02/03/2000', '04/05/2000', '06/07/2000']})

    def test_valid_data(self):
        ax = task_func(self.data, '%d/%m/%Y', 'Russia')
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.get_title(), 'Date Distribution')

    def test_non_existing_country(self):
        with self.assertRaises(ValueError):
            task_func(self.data, '%d/%m/%Y', 'Mars')

    def test_invalid_data_type(self):
        with self.assertRaises(ValueError):
            task_func('Not a DataFrame', '%d/%m/%Y', 'Russia')
