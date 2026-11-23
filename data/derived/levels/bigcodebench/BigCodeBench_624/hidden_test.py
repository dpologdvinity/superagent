from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        test_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))
    def test_case_2(self):
        test_input = [[1, 1], [1, 1], [1, 1]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))
    def test_case_3(self):
        test_input = [[1, 2], [3, 4], [5, 6], [7, 8]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (4, 2))
    def test_case_4(self):
        test_input = [[-1, -2], [-3, -4], [-5, -6]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))
    def test_case_5(self):
        test_input = [[-1, 2], [3, -4], [5, -6]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))
