from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        np.random.seed(0)
        distribution, ax = task_func(1000)
        self.assertIsInstance(distribution, np.ndarray, "Expected distribution to be a numpy array")
        self.assertIsInstance(ax, plt.Axes, "Expected ax to be a matplotlib Axes object")
        plt.close()
    def test_case_2(self):
        np.random.seed(0)
        length = 500
        distribution, _ = task_func(length)
        self.assertEqual(len(distribution), length, f"Expected distribution length to be {length}")
        plt.close()
    
    def test_case_3(self):
        np.random.seed(0)
        distribution, _ = task_func(1000)
        mean = distribution.mean()
        std_dev = distribution.std()
        self.assertAlmostEqual(mean, 0, delta=0.1, msg=f"Expected mean to be close to 0, got {mean}")
        self.assertAlmostEqual(std_dev, 1, delta=0.1, msg=f"Expected std_dev to be close to 1, got {std_dev}")
        plt.close()
    
    def test_case_4(self):
        np.random.seed(0)
        distribution, ax = task_func(1000)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1, "Expected one line representing PDF in the plot")
        bars = [rect for rect in ax.get_children() if isinstance(rect, plt.Rectangle)]
        self.assertGreater(len(bars), 1, "Expected multiple bars representing histogram in the plot")
        plt.close()
    
    def test_case_5(self):
        np.random.seed(0)
        distribution, _ = task_func(2000)
        self.assertEqual(distribution.shape, (2000,), "Expected shape of distribution to match input length")
        plt.close()
