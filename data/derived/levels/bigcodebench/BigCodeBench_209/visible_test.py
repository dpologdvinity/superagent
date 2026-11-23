from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = [(10, 20), (30, 50), (60, 25), (80, 65)]
        ax = task_func(data)
        self.assertEqual(ax.get_title(), 'Max Tuple Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [10, 30, 60, 80]))
        self.assertTrue(np.array_equal(y_data, [20, 50, 25, 65]))
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 80)
        self.assertEqual(y_max, 65)

    def test_case_2(self):
        data = [(5, 10), (15, 35), (40, 55), (70, 30)]
        ax = task_func(data)
        self.assertEqual(ax.get_title(), 'Max Tuple Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [5, 15, 40, 70]))
        self.assertTrue(np.array_equal(y_data, [10, 35, 55, 30]))
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 40)
        self.assertEqual(y_max, 55)

    def test_case_3(self):
        data = [(3, 7), (9, 11), (13, 17), (19, 23)]
        ax = task_func(data)
        self.assertEqual(ax.get_title(), 'Max Tuple Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [3, 9, 13, 19]))
        self.assertTrue(np.array_equal(y_data, [7, 11, 17, 23]))
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 19)
        self.assertEqual(y_max, 23)
