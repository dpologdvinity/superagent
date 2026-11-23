from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib
class TestCases(unittest.TestCase):
    def test_case_1(self):
        x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
        y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
        labels = ['H₂O', 'O₂', 'CO₂']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_2(self):
        x = [np.array([1,3,5]), np.array([2,4,6])]
        y = [np.array([2,4,6]), np.array([1,3,5])]
        labels = ['N₂', 'Ar']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_3(self):
        x = [np.array([10,20,30])]
        y = [np.array([15,25,35])]
        labels = ['H₂O']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_4(self):
        x = [np.array([5,15,25]), np.array([10,20,30]), np.array([15,25,35])]
        y = [np.array([10,20,30]), np.array([15,25,35]), np.array([5,15,25])]
        labels = ['H₂O', 'O₂', 'CO₂']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
    def test_case_5(self):
        x = [np.array([2,4,8]), np.array([1,3,7])]
        y = [np.array([1,3,7]), np.array([2,4,8])]
        labels = ['N₂', 'Ar']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)
