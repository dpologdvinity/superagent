from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from faker import Faker
import matplotlib
class TestCases(unittest.TestCase):
    def setUp(self):
        # Using Faker to create test data
        fake = Faker()
        self.test_data = pd.DataFrame([{'Name': fake.name(), 'Age': fake.random_int(min=18, max=100), 'Score': fake.random_int(min=0, max=100)} for _ in range(10)])
    def test_duplicate_removal(self):
        df, _ = task_func(self.test_data)
        self.assertEqual(df['Name'].nunique(), df.shape[0])
    def test_standardization(self):
        df, _ = task_func(self.test_data)
        self.assertAlmostEqual(df['Age'].mean(), 0, places=1)
        self.assertAlmostEqual(int(df['Age'].std()), 1, places=1)
        self.assertAlmostEqual(df['Score'].mean(), 0, places=1)
        self.assertAlmostEqual(int(df['Score'].std()), 1, places=1)
    def test_return_types(self):
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Score': 85},
            {'Name': 'James', 'Age': 35, 'Score': 90},
            {'Name': 'Lily', 'Age': 28, 'Score': 92},
            {'Name': 'Sam', 'Age': 40, 'Score': 88},
            {'Name': 'Nick', 'Age': 50, 'Score': 80}
        ])
        df, ax = task_func(data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_plot_contents(self):
        _, ax = task_func(self.test_data)
        self.assertEqual(ax.get_title(), 'Scatter Plot of Standardized Age and Score')
        self.assertEqual(ax.get_xlabel(), 'Age (standardized)')
        self.assertEqual(ax.get_ylabel(), 'Score (standardized)')
    def test_plot_data_points(self):
        df, ax = task_func(self.test_data)
        scatter = [child for child in ax.get_children() if isinstance(child, matplotlib.collections.PathCollection)]
        self.assertGreater(len(scatter), 0)
        self.assertEqual(len(scatter[0].get_offsets()), len(df))
