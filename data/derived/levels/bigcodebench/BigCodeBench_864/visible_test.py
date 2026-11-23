from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):
    test_data_sets = [[('vote', 19), ('those', 15), ('recent', 4), ('manage', 12), ('again', 13), ('box', 16), ('box', 16), ('box', 16)], [('experience', 14), ('interesting', 8), ('firm', 13), ('enjoy', 19), ('area', 3), ('what', 12), ('along', 1)], [('our', 11), ('then', 2), ('imagine', 6), ('heavy', 17), ('low', 6), ('site', 12), ('nearly', 3), ('organization', 6), ('me', 14), ('eat', 17)], [('involve', 2), ('money', 11), ('use', 15), ('fish', 19), ('boy', 3), ('both', 10)], [('take', 16), ('activity', 12), ('tend', 10), ('take', 2)]]

    def test_empty(self):
        report = task_func([])
        self.assertTrue(report.empty)

    def test_case_1(self):
        report = task_func(self.test_data_sets[0])
        expected = pd.DataFrame({'Total Count': {'vote': 19, 'those': 15, 'recent': 4, 'manage': 12, 'again': 13, 'box': 48}, 'Average Count': {'vote': 19.0, 'those': 15.0, 'recent': 4.0, 'manage': 12.0, 'again': 13.0, 'box': 16.0}})
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)

    def test_case_2(self):
        report = task_func(self.test_data_sets[1])
        expected = pd.DataFrame({'Total Count': {'experience': 14.0, 'interesting': 8.0, 'firm': 13.0, 'enjoy': 19.0, 'area': 3.0, 'what': 12.0, 'along': 1.0}, 'Average Count': {'experience': 14.0, 'interesting': 8.0, 'firm': 13.0, 'enjoy': 19.0, 'area': 3.0, 'what': 12.0, 'along': 1.0}})
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
