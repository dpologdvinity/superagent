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
        # Test the plot data
        self.assertEqual(len(plot.lines), 2)
    def test_case_3(self):
        data_list = []
        with self.assertRaises(ValueError):  # Expecting a ValueError due to empty data_list
            task_func(data_list)
    def test_case_4(self):
        data_list = [('a', 10, 11), ('b', 11, 12), ('c', 12, 13), ('d', 13, 14)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
        # Test the plot data array
        self.assertEqual(len(plot.lines), 2)
        # Test the plot limits
        self.assertAlmostEqual(plot.get_xlim()[0], -0.15, places=1)
        self.assertAlmostEqual(plot.get_xlim()[1], 3.15, places=1)
    def test_case_5(self):
        data_list = [('a', np.nan, np.nan), ('b', np.nan, np.nan)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
