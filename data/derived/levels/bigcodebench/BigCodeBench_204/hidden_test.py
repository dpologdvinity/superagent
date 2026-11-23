from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        stats = task_func(L)
        self.assertAlmostEqual(stats['mean'], np.mean(L))
        self.assertAlmostEqual(stats['median'], np.median(L))
        self.assertEqual(stats['mode'], 1)
        self.assertAlmostEqual(stats['std_dev'], np.std(L))
        self.assertIsInstance(stats['plot'], plt.Axes)
    def test_case_2(self):
        L = [5, 5, 5, 5, 5]
        stats = task_func(L)
        self.assertAlmostEqual(stats['mean'], 5.0)
        self.assertAlmostEqual(stats['median'], 5.0)
        self.assertEqual(stats['mode'], 5)
        self.assertAlmostEqual(stats['std_dev'], 0.0)
        self.assertIsInstance(stats['plot'], plt.Axes)
    def test_case_3(self):
        L = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9]
        stats = task_func(L)
        self.assertAlmostEqual(stats['mean'], np.mean(L))
        self.assertAlmostEqual(stats['median'], np.median(L))
        self.assertEqual(stats['mode'], 8)
        self.assertAlmostEqual(stats['std_dev'], np.std(L))
        self.assertIsInstance(stats['plot'], plt.Axes)
    def test_case_4(self):
        L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        stats = task_func(L)
        self.assertAlmostEqual(stats['mean'], np.mean(L))
        self.assertAlmostEqual(stats['median'], np.median(L))
        self.assertEqual(stats['mode'], 10)
        self.assertAlmostEqual(stats['std_dev'], np.std(L))
        self.assertIsInstance(stats['plot'], plt.Axes)
    def test_case_5(self):
        L = [5]
        stats = task_func(L)
        self.assertAlmostEqual(stats['mean'], 5.0)
        self.assertAlmostEqual(stats['median'], 5.0)
        self.assertEqual(stats['mode'], 5)
        self.assertAlmostEqual(stats['std_dev'], 0.0)
        self.assertIsInstance(stats['plot'], plt.Axes)
