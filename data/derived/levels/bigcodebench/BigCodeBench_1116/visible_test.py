from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        random.seed(0)
        d = {'EMP$$': 10}
        mean_age, median_age, mode_age = task_func(d)
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all((22 <= age <= 60 for age in mode_age)))

    def test_case_2(self):
        random.seed(0)
        d = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
        mean_age, median_age, mode_age = task_func(d)
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all((22 <= age <= 60 for age in mode_age)))

    def test_case_3(self):
        random.seed(0)
        d = {'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
        mean_age, median_age, mode_age = task_func(d)
        self.assertEqual(mean_age, 0)
        self.assertEqual(median_age, 0)
        self.assertEqual(mode_age, [])
