from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
from collections import Counter
import tempfile
import shutil
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        plt.close('all')

    def test_case_1(self):
        result, ax = task_func(100, 2, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))

    def test_case_2(self):
        plot_path = os.path.join(self.test_dir, 'test_plot.png')
        result, ax = task_func(1000, 1, plot_path, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(os.path.exists(plot_path))
        self.assertTrue(isinstance(ax, plt.Axes))

    def test_case_3(self):
        result, ax = task_func(500, 5, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))

    def tearDown(self):
        plt.close('all')
