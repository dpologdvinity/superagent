from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        obj_list = [ValueObject(mu=23, std=77), ValueObject(mu=23, std=77, seed=222), ValueObject(mu=23, std=77, seed=333)]
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), 'Fit results: mu = 10.76,  std = 39.42')

    def test_case_2(self):
        obj_list = [ValueObject(mu=23, std=65) for _ in range(1000)]
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), 'Fit results: mu = 40.53,  std = 0.00')

    def test_case_3(self):
        obj_list = [ValueObject(mu=23, std=77, seed=88), ValueObject(mu=11, std=99), ValueObject(mu=41, std=77)]
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), 'Fit results: mu = 27.52,  std = 32.92')
