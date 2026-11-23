from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def test_case_1(self):
        random.seed(0)
        y, _ = task_func(5)
        self.assertEqual(len(y), 5)

    def test_case_2(self):
        random.seed(0)
        y, _ = task_func(5)
        self.assertTrue(all((0 <= num <= 1 for num in y)))
        self.assertAlmostEqual(y, [0.8444218515250481, 0.7579544029403025, 0.420571580830845, 0.25891675029296335, 0.5112747213686085])

    def test_case_3(self):
        random.seed(0)
        with self.assertRaises(TypeError):
            task_func('5')
        with self.assertRaises(TypeError):
            task_func([])
        with self.assertRaises(TypeError):
            task_func(None)

    def tearDown(self):
        plt.close('all')
