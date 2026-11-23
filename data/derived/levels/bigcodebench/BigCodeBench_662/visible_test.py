from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.x_data = [np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]), np.array([9, 10, 11, 12]), np.array([13, 14, 15, 16]), np.array([17, 18, 19, 20])]
        self.y_data = [np.array([21, 22, 23, 24]), np.array([25, 26, 27, 28]), np.array([29, 30, 31, 32]), np.array([33, 34, 35, 36]), np.array([37, 38, 39, 40])]
        self.labels = ['H₂O', 'O₂', 'CO₂', 'N₂', 'Ar']

    def test_case_1(self):
        fig = task_func(self.x_data, self.y_data, self.labels)
        self.assertIsInstance(fig, plt.Figure)

    def test_case_2(self):
        x_data = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
        y_data = [np.array([10, 11, 12]), np.array([13, 14, 15]), np.array([16, 17, 18])]
        fig = task_func(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)

    def test_case_3(self):
        x_data = [np.array([1, 2]), np.array([4, 5]), np.array([7, 8])]
        y_data = [np.array([10, 11]), np.array([13, 14]), np.array([16, 17])]
        fig = task_func(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)
