from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax = task_func(5, 100, seed=42)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_2(self):
        for n_walk in [0, 1, 2, 10, 50]:
            ax = task_func(n_walk, 10, seed=42)
            lines = ax.get_lines()
            self.assertEqual(len(lines), n_walk)

    def test_case_3(self):
        for n_steps in [0, 1, 10, 100, 500]:
            ax = task_func(2, n_steps, seed=42)
            lines = ax.get_lines()
            self.assertEqual(len(lines[0].get_ydata()), n_steps)

    def tearDown(self):
        plt.close('all')
