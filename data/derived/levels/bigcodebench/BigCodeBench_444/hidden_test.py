from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test default parameters - values
        points, _ = task_func()
        self.assertEqual(points.shape, (100, 3))
        self.assertTrue(
            (points >= 0).all() and (points < 1).all(),
            "All points should be in the range [0, 1)",
        )
    def test_case_2(self):
        # Test default parameters - plot
        _, plot = task_func()
        self.assertTrue(isinstance(plot, Axes3D))
    def test_case_3(self):
        # Test controlling number of points
        points1, _ = task_func(n_points=1)
        points10, _ = task_func(n_points=10)
        points100, _ = task_func(n_points=100)
        self.assertEqual(points1.shape, (1, 3))
        self.assertEqual(points10.shape, (10, 3))
        self.assertEqual(points100.shape, (100, 3))
    def test_case_4(self):
        # Test random seed
        points1, _ = task_func(random_seed=42)
        points2, _ = task_func(random_seed=42)
        self.assertTrue(
            np.array_equal(points1, points2),
            "The points should be identical for the same seed",
        )
    def test_case_5(self):
        # Test handling invalid inputs
        with self.assertRaises(ValueError):
            task_func(-1)
        for invalid in [0.5, "invalid", None, []]:
            with self.assertRaises(TypeError):
                task_func(invalid)
    def tearDown(self):
        plt.close("all")
