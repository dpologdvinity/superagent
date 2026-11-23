from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import matplotlib
import unittest
import tempfile
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_data = {
            "test_1.json": [{"a": 2, "b": 4}, {"a": 4, "b": 8}],
            "test_2.json": [{"x": 1}, {"y": 2}, {"z": 6}],
            "invalid.json": {"not": "valid"},
            "empty.json": [],
        }
        # Generate test files
        for filename, content in self.test_data.items():
            with open(os.path.join(self.temp_dir.name, filename), "w") as f:
                json.dump(content, f)
    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close("all")
    def test_case_1(self):
        # Check plot generation
        expected_titles = ["a", "b"]
        _, plots = task_func(os.path.join(self.temp_dir.name, "test_1.json"))
        self.assertEqual(len(plots), len(expected_titles))
        for plot, title in zip(plots, expected_titles):
            assert isinstance(plot, matplotlib.axes._axes.Axes)
            self.assertTrue(plot.get_title(), f"Statistics of {title}")
    def test_case_2(self):
        # Check result correctness
        results, _ = task_func(os.path.join(self.temp_dir.name, "test_1.json"))
        self.assertIn("a", results)
        self.assertIn("b", results)
        self.assertEqual(results["a"]["mean"], 3.0)
        self.assertEqual(results["a"]["median"], 3.0)
        self.assertEqual(results["b"]["mean"], 6.0)
        self.assertEqual(results["b"]["median"], 6.0)
    def test_case_3(self):
        # Test with invalid data structure (not a list of dicts)
        with self.assertRaises(AttributeError):
            task_func(os.path.join(self.temp_dir.name, "invalid.json"))
    def test_case_4(self):
        # Test with empty data
        results, plots = task_func(os.path.join(self.temp_dir.name, "empty.json"))
        self.assertEqual(results, {})
        self.assertEqual(len(plots), 0)
    def test_case_5(self):
        # Test handling nested dicts with one key each
        results, _ = task_func(os.path.join(self.temp_dir.name, "test_2.json"))
        self.assertIn("x", results)
        self.assertIn("y", results)
        self.assertIn("z", results)
        self.assertEqual(results["x"]["mean"], 1.0)
        self.assertEqual(results["x"]["median"], 1.0)
        self.assertEqual(results["y"]["mean"], 2.0)
        self.assertEqual(results["y"]["median"], 2.0)
        self.assertEqual(results["z"]["mean"], 6.0)
        self.assertEqual(results["z"]["median"], 6.0)
    def test_case_6(self):
        # Test with nonexistent filename
        with self.assertRaises(FileNotFoundError):
            task_func(os.path.join(self.temp_dir.name, "NOTEXISTS.json"))
