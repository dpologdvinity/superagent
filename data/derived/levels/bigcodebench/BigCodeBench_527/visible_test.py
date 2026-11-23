from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import tempfile
import matplotlib.pyplot as plt
import json

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.sample_data_file = os.path.join(self.temp_dir.name, 'sample_data.json')
        self.sample_data = [{'A': 10, 'B': 20, 'C': 30}, {'A': 15, 'B': 25, 'C': 35}, {'A': 20, 'B': 30, 'C': 40}]
        with open(self.sample_data_file, 'w') as f:
            json.dump(self.sample_data, f)
        self.invalid_json_file = os.path.join(self.temp_dir.name, 'invalid.json')
        with open(self.invalid_json_file, 'w') as f:
            f.write('invalid content')

    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close('all')

    def test_case_1(self):
        _, ax = task_func(self.sample_data_file)
        self.assertIsInstance(ax, plt.Axes, 'The function should return a plot (Axes).')
        self.assertTrue(len(ax.get_xticks()) > 0, 'The plot should have x-axis ticks.')
        self.assertTrue(len(ax.get_yticks()) > 0, 'The plot should have y-axis ticks.')
        self.assertTrue(ax.get_title(), 'Boxplot of Values for Each Key')

    def test_case_2(self):
        results, _ = task_func(self.sample_data_file)
        self.assertIn('A', results)
        self.assertIn('B', results)
        self.assertIn('C', results)
        self.assertEqual(results['A']['mean'], 15.0)
        self.assertEqual(results['A']['median'], 15.0)
        self.assertEqual(results['B']['mean'], 25.0)
        self.assertEqual(results['B']['median'], 25.0)
        self.assertEqual(results['C']['mean'], 35.0)
        self.assertEqual(results['C']['median'], 35.0)

    def test_case_3(self):
        _, ax = task_func(self.sample_data_file)
        x_labels = [label.get_text() for label in ax.get_xticklabels()]
        expected_x_labels = ['A', 'B', 'C']
        self.assertListEqual(x_labels, expected_x_labels, 'The x-axis labels are not as expected.')
