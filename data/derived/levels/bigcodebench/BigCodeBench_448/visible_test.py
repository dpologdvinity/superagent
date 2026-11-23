from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax = task_func()
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        self.assertAlmostEqual(x[np.argmax(y)], 0, delta=0.1)
        self.assertTrue(min(x) >= -3 and max(x) <= 3)

    def test_case_2(self):
        ax = task_func(mu=5, sigma=2)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        expected_min, expected_max = (5 - 3 * 2, 5 + 3 * 2)
        self.assertAlmostEqual(min(x), expected_min, delta=0.1)
        self.assertAlmostEqual(max(x), expected_max, delta=0.1)

    def test_case_3(self):
        ax = task_func(mu=-3, sigma=0.5)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        self.assertAlmostEqual(x[np.argmax(y)], -3, delta=0.1)
        self.assertTrue(min(x) >= -3 - 1.5 and max(x) <= -3 + 1.5)

    def tearDown(self):
        plt.close('all')
