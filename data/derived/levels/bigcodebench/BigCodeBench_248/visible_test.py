from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))

    def test_case_2(self):
        data_list = [('a', 6, 7), ('b', 7, 8), ('c', 8, 9)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
        self.assertEqual(len(plot.lines), 2)

    def test_case_3(self):
        data_list = []
        with self.assertRaises(ValueError):
            task_func(data_list)
