from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_case_1(self):
        dictionary = [['Apple', 'Banana', 'Orange', 'Apple', 'Banana'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Apple')
        self.assertListEqual(sorted(positions), sorted([(0, 0), (0, 3), (1, 0), (1, 3), (2, 0), (2, 3), (3, 0), (3, 3), (4, 0), (4, 3)]))
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)

    def test_case_2(self):
        dictionary = [['Orange', 'Banana', 'Apple', 'Apple', 'Banana'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Apple')
        self.assertListEqual(sorted(positions), sorted([(0, 2), (0, 3), (1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3), (4, 2), (4, 3)]))
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)

    def test_case_3(self):
        dictionary = [['Apple', 'Banana', 'Apple', 'Orange', 'Banana'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Orange')
        self.assertListEqual(positions, [(i, 3) for i in range(5)])
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
