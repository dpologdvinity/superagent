from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_small_number_of_colors(self):
        color_pattern = task_func(4, rng_seed=123)
        expected_pattern = ['Red', 'Red', 'Green', 'Blue']
        self.assertEqual(color_pattern, expected_pattern)

    def test_large_number_of_colors(self):
        color_pattern = task_func(100, rng_seed=123)
        self.assertEqual(len(color_pattern), 100)
        self.assertTrue(all((color in ['Red', 'Green', 'Blue', 'Yellow', 'Purple'] for color in color_pattern)))

    def test_zero_colors(self):
        color_pattern = task_func(0, rng_seed=123)
        self.assertEqual(color_pattern, [])
