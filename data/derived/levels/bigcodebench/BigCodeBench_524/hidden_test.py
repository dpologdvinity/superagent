from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        data = [{"cat": 1, "dog": 3}, {"cat": 2, "dog": 5}, {"cat": 3, "dog": 7}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats["cat"]["mean"], 2.0)
        self.assertAlmostEqual(stats["cat"]["std"], 0.816496580927726)
        self.assertAlmostEqual(stats["dog"]["mean"], 5.0)
        self.assertAlmostEqual(stats["dog"]["std"], 1.632993161855452)
        
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        self.assertEqual(axes[1].get_title(), "Statistics of dog")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_2(self):
        # Test other keys (animals)
        data = [{"bird": 5, "fish": 10}, {"bird": 6, "fish": 8}, {"bird": 7, "fish": 9}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats["bird"]["mean"], 6.0)
        self.assertAlmostEqual(stats["bird"]["std"], 0.816496580927726)
        self.assertAlmostEqual(stats["fish"]["mean"], 9.0)
        self.assertAlmostEqual(stats["fish"]["std"], 0.816496580927726)
        self.assertEqual(axes[0].get_title(), "Statistics of bird")
        self.assertEqual(axes[1].get_title(), "Statistics of fish")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_3(self):
        # Test handling negatives
        data = [{"cat": -1, "dog": -3}, {"cat": -2, "dog": -5}, {"cat": -3, "dog": -7}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats["cat"]["mean"], -2.0)
        self.assertAlmostEqual(stats["cat"]["std"], 0.816496580927726)
        self.assertAlmostEqual(stats["dog"]["mean"], -5.0)
        self.assertAlmostEqual(stats["dog"]["std"], 1.632993161855452)
        
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        self.assertEqual(axes[1].get_title(), "Statistics of dog")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_4(self):
        # Test single input
        data = [{"cat": 1}]
        stats, axes = task_func(data)
        self.assertEqual(stats, {"cat": {"mean": 1.0, "std": 0.0}})
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_5(self):
        # Test handling zero
        data = [{"cat": 0, "dog": 0}, {"cat": 0, "dog": 0}, {"cat": 0, "dog": 0}]
        stats, axes = task_func(data)
        self.assertEqual(
            stats, {"cat": {"mean": 0.0, "std": 0.0}, "dog": {"mean": 0.0, "std": 0.0}}
        )
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        self.assertEqual(axes[1].get_title(), "Statistics of dog")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_6(self):
        # Test correct handling of empty input
        with self.assertRaises(ValueError):
            task_func([])
    def test_case_7(self):
        # Test correct handling of incorrect input types
        with self.assertRaises(TypeError):
            task_func("not a list")
        with self.assertRaises(TypeError):
            task_func([123])
        with self.assertRaises(TypeError):
            task_func([{"cat": "not numeric"}])
    def test_case_8(self):
        # Test with a mix of positive and negative integers
        data = [
            {"apple": -2, "banana": 4},
            {"apple": -4, "banana": 6},
            {"apple": -6, "banana": 8},
        ]
        stats, _ = task_func(data)
        self.assertAlmostEqual(stats["apple"]["mean"], -4.0)
        self.assertAlmostEqual(stats["apple"]["std"], 1.632993161855452)
        self.assertAlmostEqual(stats["banana"]["mean"], 6.0)
        self.assertAlmostEqual(stats["banana"]["std"], 1.632993161855452)
    def test_case_9(self):
        # Test with floating point numbers
        data = [{"x": 0.5, "y": 1.5}, {"x": 2.5, "y": 3.5}, {"x": 4.5, "y": 5.5}]
        stats, _ = task_func(data)
        self.assertAlmostEqual(stats["x"]["mean"], 2.5)
        self.assertAlmostEqual(stats["x"]["std"], 1.632993161855452)
        self.assertAlmostEqual(stats["y"]["mean"], 3.5)
        self.assertAlmostEqual(stats["y"]["std"], 1.632993161855452)
    def tearDown(self):
        plt.close("all")
