from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import random

class TestCases(unittest.TestCase):
    """Test cases for task_func."""

    def test_empty_lists(self):
        """Test with empty color and state lists."""
        self.assertEqual(task_func([], []).empty, True)

    def test_single_color_and_state(self):
        """Test with one color and one state."""
        random.seed(0)
        result = task_func(['Red'], ['Solid'])
        expected = pd.DataFrame({'Color:State 1': ['Red:Solid']})
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_colors_single_state(self):
        """Test with multiple colors and a single state."""
        random.seed(1)
        result = task_func(['Red', 'Blue', 'Green'], ['Solid'])
        expected_combinations = set(['Red:Solid', 'Blue:Solid', 'Green:Solid'])
        result_combinations = set(result['Color:State 1'])
        self.assertEqual(result_combinations, expected_combinations)
