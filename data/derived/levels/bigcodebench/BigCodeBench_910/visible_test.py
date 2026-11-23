from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_basic_input(self):
        ax = task_func(['A', 'B', 'C'], [3, 5, 2], ['red', 'green', 'blue'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Frequency of Letters')
        self.assertEqual(ax.get_xlabel(), 'Letters')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
        expected_colors = ['red', 'green', 'blue']
        for patch, expected_color in zip(ax.patches, expected_colors):
            self.assertEqual(patch.get_facecolor(), plt.cm.colors.to_rgba(expected_color))
        expected_counts = [3, 5, 2]
        for patch, expected_count in zip(ax.patches, expected_counts):
            self.assertEqual(patch.get_height(), expected_count)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            task_func(['A', 'B'], [3], ['red', 'green'])

    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            task_func([], [], [])
