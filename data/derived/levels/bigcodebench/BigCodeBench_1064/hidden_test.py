from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""
    def tearDown(self):
        plt.clf()
    def test_scenario_1(self):
        """Scenario 1: Testing with a 2D array created by adding row and column indices."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertEqual(ax.collections[0].colorbar.vmax, expected_vmax)
    def test_scenario_2(self):
        """Scenario 2: Testing with a 2D array where each column has identical values based on the column index."""
        arr = np.array([[i for i in range(3)] for j in range(5)])
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertEqual(ax.collections[0].colorbar.vmax, expected_vmax)
    def test_scenario_3(self):
        """Scenario 3: Testing with a 2D array where each row has identical values based on the row index."""
        arr = np.array([[j for i in range(3)] for j in range(5)])
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertEqual(ax.collections[0].colorbar.vmax, expected_vmax)
    def test_scenario_4(self):
        """Scenario 4: Testing with a 2D array of zeros."""
        arr = np.zeros((5, 3))
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertAlmostEqual(
            ax.collections[0].colorbar.vmax, expected_vmax, delta=0.2
        )
    def test_scenario_5(self):
        """Scenario 5: Testing with a 2D array of ones."""
        arr = np.ones((5, 3))
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertAlmostEqual(
            ax.collections[0].colorbar.vmax, expected_vmax, delta=0.2
        )
