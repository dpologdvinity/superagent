from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic properties
        test_cases = [
            (0, 10000, 100, 1, 1000),
            (0, 100000, 1000, 2, 5000),
            (0, 10000, 100, 0.5, 1000),
            (0, 10000, 100, 1, 500),
            (0, 10000, 500, 1, 1000),
        ]
        for start_time, end_time, step, amplitude, period in test_cases:
            with self.subTest(
                start_time=start_time,
                end_time=end_time,
                step=step,
                amplitude=amplitude,
                period=period,
            ):
                ax = task_func(start_time, end_time, step, amplitude, period)
                self.assertIsInstance(ax, plt.Axes)
                self.assertEqual(ax.get_title(), "Time Series with Seasonality")
                self.assertEqual(ax.get_xlabel(), "Timestamp")
                self.assertEqual(ax.get_ylabel(), "Value")
    def test_case_2(self):
        # Test large step
        # Plot should still behave as expected even when step > (end_time - start_time)
        ax = task_func(0, 10000, 200000, 1, 1000)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Time Series with Seasonality")
        self.assertEqual(ax.get_xlabel(), "Timestamp")
        self.assertEqual(ax.get_ylabel(), "Value")
    def test_case_3(self):
        # Test handling invalid input types - period
        with self.assertRaises(ValueError):
            task_func(0, 10000, 100, 1, 0)
        with self.assertRaises(ValueError):
            task_func(0, 10000, 100, 1, -1)
    def test_case_4(self):
        # Test handling invalid input types - step
        with self.assertRaises(ValueError):
            task_func(0, 10000, -100, 1, 1000)
        with self.assertRaises(ValueError):
            task_func(0, 10000, 0, 1, 1000)
    def test_case_5(self):
        # Test plot data integrity
        ax = task_func(0, 10000, 100, 1, 1000)
        xy_data = ax.get_lines()[0].get_xydata()
        expected_length = (10000 - 0) // 100
        self.assertEqual(len(xy_data), expected_length)
    def test_case_6(self):
        # Test random seed
        ax1 = task_func(0, 10000, 100, 1, 1000, seed=42)
        xy_data1 = ax1.get_lines()[0].get_xydata()
        ax2 = task_func(0, 10000, 100, 1, 1000, seed=42)
        xy_data2 = ax2.get_lines()[0].get_xydata()
        ax3 = task_func(0, 10000, 100, 1, 1000, seed=43)
        xy_data3 = ax3.get_lines()[0].get_xydata()
        self.assertTrue(
            np.array_equal(xy_data1, xy_data2),
            "Results should be the same with the same seed",
        )
        self.assertFalse(
            np.array_equal(xy_data1, xy_data3),
            "Results should be different with different seeds",
        )
    def tearDown(self):
        plt.close("all")
