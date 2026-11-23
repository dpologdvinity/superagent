from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def _validate_plot(self, ax):
        self.assertEqual(ax.get_title(), 'Grade Distribution')
        self.assertEqual(ax.get_xlabel(), 'Grade')
        self.assertEqual(ax.get_ylabel(), 'Number of Students')

    def _test_helper(self, grades, expected_counts):
        expected_df = pd.DataFrame({'Count': expected_counts}, index=['A', 'B', 'C', 'D', 'F'])
        expected_df.index.name = 'Grade'
        report_df, ax = task_func(grades)
        pd.testing.assert_frame_equal(report_df, expected_df)
        self._validate_plot(ax)

    def test_case_1(self):
        self._test_helper(['A', 'B', 'B', 'C', 'A', 'D', 'F', 'B', 'A', 'C'], [3, 3, 2, 1, 1])

    def test_case_2(self):
        self._test_helper(['A', 'A', 'A', 'A', 'A'], [5, 0, 0, 0, 0])

    def test_case_3(self):
        with self.assertRaises(Exception):
            task_func([], [0, 0, 0, 0, 0])

    def tearDown(self):
        plt.close('all')
