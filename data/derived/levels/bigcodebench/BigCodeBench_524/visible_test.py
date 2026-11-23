from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = [{'cat': 1, 'dog': 3}, {'cat': 2, 'dog': 5}, {'cat': 3, 'dog': 7}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats['cat']['mean'], 2.0)
        self.assertAlmostEqual(stats['cat']['std'], 0.816496580927726)
        self.assertAlmostEqual(stats['dog']['mean'], 5.0)
        self.assertAlmostEqual(stats['dog']['std'], 1.632993161855452)
        self.assertEqual(axes[0].get_title(), 'Statistics of cat')
        self.assertEqual(axes[1].get_title(), 'Statistics of dog')
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))

    def test_case_2(self):
        data = [{'bird': 5, 'fish': 10}, {'bird': 6, 'fish': 8}, {'bird': 7, 'fish': 9}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats['bird']['mean'], 6.0)
        self.assertAlmostEqual(stats['bird']['std'], 0.816496580927726)
        self.assertAlmostEqual(stats['fish']['mean'], 9.0)
        self.assertAlmostEqual(stats['fish']['std'], 0.816496580927726)
        self.assertEqual(axes[0].get_title(), 'Statistics of bird')
        self.assertEqual(axes[1].get_title(), 'Statistics of fish')
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))

    def test_case_3(self):
        data = [{'cat': -1, 'dog': -3}, {'cat': -2, 'dog': -5}, {'cat': -3, 'dog': -7}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats['cat']['mean'], -2.0)
        self.assertAlmostEqual(stats['cat']['std'], 0.816496580927726)
        self.assertAlmostEqual(stats['dog']['mean'], -5.0)
        self.assertAlmostEqual(stats['dog']['std'], 1.632993161855452)
        self.assertEqual(axes[0].get_title(), 'Statistics of cat')
        self.assertEqual(axes[1].get_title(), 'Statistics of dog')
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))

    def tearDown(self):
        plt.close('all')
