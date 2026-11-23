from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_positive_outcomes(self):
        """Test the function with positive goals and penalties."""
        df, _ = task_func(5, 3, rng_seed=42)
        self.assertFalse(df.empty)
        self.assertListEqual(list(df.columns), ['Team', 'Goals', 'Penalty Cost'])

    def test_zero_goals_penalties(self):
        """Test the function with zero goals and penalties."""
        df, _ = task_func(0, 0, teams=['Team A'], rng_seed=42)
        self.assertTrue((df['Goals'] == 0).all())
        self.assertTrue((df['Penalty Cost'] == 0).all())

    def test_negative_input(self):
        """Ensure negative inputs are treated as positive."""
        df, _ = task_func(-5, -3, rng_seed=42)
        self.assertFalse((df['Goals'] < 0).any())
        self.assertFalse((df['Penalty Cost'] < 0).any())
