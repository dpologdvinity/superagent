from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic point type and structure
        _, points = task_func(5)
        self.assertTrue(
            all(
                isinstance(point, tuple)
                and len(point) == 2
                and all(isinstance(coord, float) for coord in point)
                for point in points
            ),
            "Points should be a list of tuples with float coordinates",
        )
    def test_case_2(self):
        # Test parameter 'n'
        for n in [0, 1, 5, 100]:
            plot, points = task_func(n)
            self.assertEqual(len(points), n)
            self.assertTrue(isinstance(plot, type(plt.figure())))
    def test_case_3(self):
        # Test random seed - reproduction
        _, points1 = task_func(5, seed=1)
        _, points2 = task_func(5, seed=1)
        self.assertEqual(
            points1, points2, "Points generated with the same seed should match exactly"
        )
    def test_case_4(self):
        # Test random seed - differences
        _, points1 = task_func(5, seed=1)
        _, points2 = task_func(5, seed=10)
        self.assertNotEqual(
            points1, points2, "Points generated with the same seed should match exactly"
        )
    def test_case_5(self):
        # Test invalid inputs
        with self.assertRaises(ValueError):
            task_func(-5)
        with self.assertRaises(TypeError):
            task_func(5.5)
        with self.assertRaises(TypeError):
            task_func("5")
    def test_case_6(self):
        # Test visualization
        fig, _ = task_func(1)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), "Scatter plot of random points")
        self.assertEqual(ax.get_xlabel(), "X")
        self.assertEqual(ax.get_ylabel(), "Y")
    def tearDown(self):
        plt.close("all")
