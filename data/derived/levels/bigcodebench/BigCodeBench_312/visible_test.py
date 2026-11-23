from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
import numpy as np
import random

class TestCases(unittest.TestCase):

    def test_histogram_axes_type(self):
        random.seed(0)
        _, ax = task_func()
        self.assertTrue(ax, plt.Axes)
        plt.close()

    def test_distribution_length(self):
        random.seed(0)
        distribution, _ = task_func()
        self.assertEqual(len(distribution), 1000)
        plt.close()

    def test_distribution_type(self):
        random.seed(0)
        distribution, _ = task_func()
        self.assertIsInstance(distribution, list, 'Distribution should be a list')
        self.assertTrue(all((isinstance(x, float) for x in distribution)))
        plt.close()
