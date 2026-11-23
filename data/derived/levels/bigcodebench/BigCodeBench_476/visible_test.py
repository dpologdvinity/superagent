from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
import itertools

class TestCases(unittest.TestCase):

    def setUp(self):
        self.random_seed = 42
        np.random.seed(self.random_seed)
        self.test_data = [(np.linspace(-10, 10, 100), 3 * np.linspace(-10, 10, 100) ** 2 + 2 * np.linspace(-10, 10, 100) + 1 + np.random.normal(0, 20, 100)), (np.linspace(-5, 5, 100), -2 * np.linspace(-5, 5, 100) ** 2 + 4 * np.linspace(-5, 5, 100) - 3 + np.random.normal(0, 10, 100)), (np.linspace(-100, 100, 100), 0.5 * np.linspace(-100, 100, 100) ** 2 + 1 * np.linspace(-100, 100, 100) + 10 + np.random.normal(0, 50, 100)), (np.linspace(-1, 1, 100), 10 * np.linspace(-1, 1, 100) ** 2 + 5 * np.linspace(-1, 1, 100) + 2 + np.random.normal(0, 1, 100))]

    def assertDataInPlot(self, X, Y, ax):
        xdata, ydata = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(X, xdata))
        self.assertTrue(np.array_equal(Y, ydata))

    def test_case_1(self):
        X, Y = self.test_data[0]
        params, ax = task_func(X, Y)
        self.assertTrue(len(params) == 3)
        self.assertDataInPlot(X, Y, ax)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertAlmostEqual(params[0], 3, places=0)
        self.assertAlmostEqual(params[1], 2, places=0)

    def test_case_2(self):
        X, Y = self.test_data[1]
        params, ax = task_func(X, Y)
        self.assertTrue(len(params) == 3)
        self.assertDataInPlot(X, Y, ax)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertAlmostEqual(params[0], -2, places=0)
        self.assertAlmostEqual(params[1], 4, places=0)

    def test_case_3(self):
        X, Y = self.test_data[2]
        params, ax = task_func(X, Y)
        self.assertTrue(len(params) == 3)
        self.assertDataInPlot(X, Y, ax)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertAlmostEqual(params[0], 0.5, places=0)
        self.assertAlmostEqual(params[1], 1, places=0)

    def tearDown(self):
        plt.close('all')
