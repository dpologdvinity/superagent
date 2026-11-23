from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        _, points = task_func(5)
        self.assertTrue(all((isinstance(point, tuple) and len(point) == 2 and all((isinstance(coord, float) for coord in point)) for point in points)), 'Points should be a list of tuples with float coordinates')

    def test_case_2(self):
        for n in [0, 1, 5, 100]:
            plot, points = task_func(n)
            self.assertEqual(len(points), n)
            self.assertTrue(isinstance(plot, type(plt.figure())))

    def test_case_3(self):
        _, points1 = task_func(5, seed=1)
        _, points2 = task_func(5, seed=1)
        self.assertEqual(points1, points2, 'Points generated with the same seed should match exactly')

    def tearDown(self):
        plt.close('all')
