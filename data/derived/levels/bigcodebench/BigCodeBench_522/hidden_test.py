from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def _check_plot_structure(self, ax):
        # Assert type of returned object
        self.assertIsInstance(ax, plt.Axes)
        # Check plot title, x-label, y-label
        self.assertEqual(ax.get_title(), "Average Student Scores")
        self.assertEqual(ax.get_xlabel(), "Student")
        self.assertEqual(ax.get_ylabel(), "Average Score")
    def test_case_1(self):
        # Test multiple users multiple data points
        data = [
            {"John": 5, "Jane": 10, "Joe": 7},
            {"John": 6, "Jane": 8, "Joe": 10},
            {"John": 5, "Jane": 9, "Joe": 8},
            {"John": 7, "Jane": 10, "Joe": 9},
        ]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check bar heights (average scores)
        for bar, label in zip(ax.containers[0], ["Jane", "Joe", "John"]):
            if label == "Jane":
                self.assertEqual(bar.get_height(), 9.25)
            elif label == "Joe":
                self.assertEqual(bar.get_height(), 8.5)
            elif label == "John":
                self.assertEqual(bar.get_height(), 5.75)
    def test_case_2(self):
        # Test same user multiple data points
        data = [{"John": 5}, {"John": 6}, {"John": 7}, {"John": 8}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check bar heights (average scores)
        for bar, _ in zip(ax.containers[0], ["John"]):
            self.assertEqual(bar.get_height(), 6.5)
    def test_case_3(self):
        # Test with multiple students and one data point each
        data = [{"John": 10}, {"Jane": 15}, {"Joe": 20}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check bar heights match the single data point for each student
        expected_scores = {"Jane": 15, "Joe": 20, "John": 10}
        for bar, label in zip(ax.containers[0], expected_scores.keys()):
            self.assertEqual(bar.get_height(), expected_scores[label])
    def test_case_4(self):
        # Test multiple users multiple data points different lengths
        data = [{"Jane": 10, "Joe": 7}, {"Joe": 10}, {"Jane": 9, "John": 8}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check bar heights (average scores)
        for bar, label in zip(ax.containers[0], ["Jane", "Joe"]):
            if label == "Jane":
                self.assertAlmostEqual(bar.get_height(), 9.5, places=2)
            elif label == "Joe":
                self.assertAlmostEqual(bar.get_height(), 8.5, places=2)
    def test_case_5(self):
        # Test handling None
        data = [
            {"Jane": 10, "Joe": 7},
            {"Joe": 10, "Jane": None, "John": None},
            {"Jane": 9, "John": 8},
            {"Joe": None},
        ]
        ax = task_func(data)
        self._check_plot_structure(ax)  # Results should be same as test_case_4
        for bar, label in zip(ax.containers[0], ["Jane", "Joe"]):
            if label == "Jane":
                self.assertAlmostEqual(bar.get_height(), 9.5, places=2)
            elif label == "Joe":
                self.assertAlmostEqual(bar.get_height(), 8.5, places=2)
    def test_case_6(self):
        # Test only one data point with multiple students
        data = [{"John": 5, "Jane": 10}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check bar heights (average scores)
        for bar, label in zip(ax.containers[0], ["Jane", "John"]):
            if label == "Jane":
                self.assertEqual(bar.get_height(), 10)
            elif label == "John":
                self.assertEqual(bar.get_height(), 5)
    def test_case_7(self):
        # Test empty input
        data = []
        ax = task_func(data)
        self.assertIsNone(ax)
    def test_case_8(self):
        # Test with data containing negative scores
        data = [{"John": -2, "Jane": 3}, {"John": -4, "Jane": 5}]
        with self.assertRaises(ValueError):
            task_func(data)
    def test_case_9(self):
        # Test with a larger dataset
        data = [{"John": i} for i in range(1000)]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check bar height for the large dataset (average should be close to 499.5)
        self.assertAlmostEqual(
            next(iter(ax.containers[0])).get_height(), 499.5, places=2
        )
    def test_case_10(self):
        # Test with some negative scores mixed with positive ones
        data = [{"John": 5, "Jane": -1}, {"John": -2, "Jane": 2}]
        with self.assertRaises(ValueError):
            task_func(data)
    def test_case_11(self):
        # Test with all scores as 0
        data = [{"John": 0, "Jane": 0}, {"John": 0, "Jane": 0}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check bar heights are 0 for all students
        for bar, label in zip(ax.containers[0], ["Jane", "John"]):
            self.assertEqual(bar.get_height(), 0)
    def test_case_12(self):
        # Test with some dictionaries being empty
        data = [{"John": 5}, {}, {"Jane": 10}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        # Check that the empty dictionary does not affect the output
        expected_scores = {"Jane": 10, "John": 5}
        for bar, label in zip(ax.containers[0], expected_scores.keys()):
            self.assertEqual(bar.get_height(), expected_scores[label])
    def tearDown(self):
        plt.close("all")
