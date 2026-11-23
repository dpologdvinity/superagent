from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(task_func([]), [])

    def test_single_point(self):
        self.assertEqual(task_func([(0, 0)]), [])

    def test_zero_distance(self):
        self.assertEqual(task_func([(3, 4), (3, 4)]), [0.0])
