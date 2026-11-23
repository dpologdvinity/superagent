from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
import random

class TestCases(unittest.TestCase):

    def test_default_parameters(self):
        random.seed(0)
        ax = task_func()
        self.assertEqual(len(ax.collections[0].get_offsets()), 1000, 'Default parameter points count mismatch')
        self.assertEqual(ax.get_aspect(), 1.0, 'Aspect ratio mismatch in default parameters test')
        plt.close()

    def test_custom_parameters(self):
        random.seed(0)
        ax = task_func(500, 0.5)
        self.assertEqual(len(ax.collections[0].get_offsets()), 500, 'Custom parameter points count mismatch')
        self.assertEqual(ax.get_aspect(), 1.0, 'Aspect ratio mismatch in custom parameters test')
        plt.close()

    def test_radius_accuracy(self):
        random.seed(0)
        radius = 2
        ax = task_func(100, radius)
        points = ax.collections[0].get_offsets()
        for point in points[:1]:
            self.assertTrue(math.sqrt(point[0] ** 2 + point[1] ** 2) <= radius, 'Point outside specified radius')
        plt.close()
