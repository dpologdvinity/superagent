from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.default_str = '1,2,3,4,5,5,5,4,3,2,1'
        self.default_expected = pd.Series([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1])

    def assertHistogramAttributes(self, series, ax):
        self.assertTrue(ax.yaxis.grid)
        self.assertEqual(matplotlib.colors.to_hex(ax.patches[0].get_fc()), '#607c8e')
        for patch in ax.patches:
            if round(patch.get_x()) in series.values or round(patch.get_x() + patch.get_width()) in series.values:
                self.assertTrue(patch.get_height() >= 0)

    def test_case_1(self):
        series, ax = task_func(self.default_str)
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, self.default_expected)

    def test_case_2(self):
        for bins in [5, 10, 15, 30, 100]:
            with self.subTest(bins=bins):
                series, ax = task_func(self.default_str, bins=bins)
                self.assertIsInstance(series, pd.Series)
                self.assertHistogramAttributes(series, ax)
                pd.testing.assert_series_equal(series, self.default_expected)

    def test_case_3(self):
        data_str = '1|2|3|4|5'
        series, ax = task_func(data_str, separator='|')
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, pd.Series([1, 2, 3, 4, 5]))

    def tearDown(self):
        plt.close('all')
