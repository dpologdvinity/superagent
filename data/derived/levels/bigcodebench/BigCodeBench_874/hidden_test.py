from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        # Testing with no points
        self.assertEqual(task_func([]), [])
    def test_single_point(self):
        # Testing with a single point (no distances can be calculated)
        self.assertEqual(task_func([(0, 0)]), [])
    def test_zero_distance(self):
        # Testing with multiple points at the same location (zero distance)
        self.assertEqual(task_func([(3, 4), (3, 4)]), [0.0])
    def test_various_distances(self):
        # Testing with points at various distances
        points = [(1, 2), (4, 6), (4, 6), (10, 20)]
        # The distances between the points are approximately:
        results = task_func(points)
        self.assertTrue(all(isinstance(x, float) for x in results))
        self.assertAlmostEqual(results[0], 5.0, places=4)
        self.assertAlmostEqual(results[1], 0.0, places=4)
        self.assertAlmostEqual(results[2], 15.2315421, places=4)
    def test_negative_coordinates(self):
        # Testing with points in negative coordinates
        points = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
        results = task_func(points)
        expected = [1.4142135623730951] * 3  # repeating 3 times
        self.assertEqual(results, expected)
