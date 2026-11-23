from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import matplotlib.pyplot as plt
import unittest
import random
class TestCases(unittest.TestCase):
    def test_color_returned(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        color = task_func(ax)
        self.assertIn(color, ['b', 'g', 'r', 'c', 'm', 'y', 'k'])
        plt.close()
    def test_random_color(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        colors = set(task_func(ax) for _ in range(10))
        self.assertTrue(len(colors) > 1)
        plt.close()
    def test_plot_exists(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        task_func(ax)
        self.assertTrue(len(ax.lines) > 0)
        plt.close()
    def test_plot_properties(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        color = task_func(ax)
        line = ax.lines[0]
        self.assertEqual(line.get_color(), color)
        plt.close()
    def test_label_position(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        task_func(ax)
        position = ax.get_rlabel_position()
        self.assertTrue(position>1.0)
        plt.close()
