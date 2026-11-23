from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        x = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
        y = [np.array([4, 5, 6]), np.array([7, 8, 9]), np.array([10, 11, 12])]
        labels = ['H₂O', 'O₂', 'CO₂']
        ax, df = task_func(x, y, labels)
        self.assertEqual(df.shape, (3, 6))
        expected_data = np.array([[1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9], [7, 8, 9, 10, 11, 12]])
        np.testing.assert_array_equal(df.values, expected_data)

    def test_case_2(self):
        x = [np.array([1, 1]), np.array([2, 2])]
        y = [np.array([3, 3]), np.array([4, 4])]
        labels = ['H₂O', 'O₂']
        ax, df = task_func(x, y, labels)
        self.assertEqual(df.shape, (2, 4))
        expected_data = np.array([[1, 1, 3, 3], [2, 2, 4, 4]])
        np.testing.assert_array_equal(df.values, expected_data)

    def test_case_3(self):
        x = [np.array([10])]
        y = [np.array([20])]
        labels = ['H₂O']
        ax, df = task_func(x, y, labels)
        self.assertEqual(df.shape, (1, 2))
        expected_data = np.array([[10, 20]])
        np.testing.assert_array_equal(df.values, expected_data)
