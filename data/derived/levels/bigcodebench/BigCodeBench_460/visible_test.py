from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import tempfile
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.script_path = os.path.join(self.temp_dir.name, 'script.sh')
        self.output_path = os.path.join(self.temp_dir.name, 'output.csv')
        self.valid_csv_content = [f'echo "Name,Value" > {self.output_path}\n', f'echo "A,1" >> {self.output_path}\n', f'echo "B,2" >> {self.output_path}\n', f'echo "C,3" >> {self.output_path}\n']

    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close('all')

    def _create_script(self, lines):
        with open(self.script_path, 'w') as file:
            file.write('#!/bin/bash\n')
            file.writelines(lines)
        os.chmod(self.script_path, 493)

    def _validate_y_tick_labels(self, ax, df):
        plt.gcf().canvas.draw()
        y_tick_labels = [float(label.get_text()) for label in ax.get_yticklabels() if label.get_text()]
        self.assertTrue(all((y_tick_labels[i] <= y_tick_labels[i + 1] for i in range(len(y_tick_labels) - 1))), 'Y-tick labels are not in increasing order')
        self.assertTrue(min(y_tick_labels) <= df[df.columns[1]].min() <= max(y_tick_labels) and min(y_tick_labels) <= df[df.columns[1]].max() <= max(y_tick_labels), 'Y-tick labels do not cover the range of the data')

    def test_case_1(self):
        self._create_script(self.valid_csv_content)
        df, ax = task_func(self.script_path, self.output_path)
        expected_labels = df.iloc[:, 0].tolist()
        x_tick_labels = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), df.shape[0])
        self.assertListEqual(x_tick_labels, expected_labels)
        self._validate_y_tick_labels(ax, df)

    def test_case_2(self):
        expected_columns = ['Name', 'Value']
        expected_data = {'Name': ['A', 'B', 'C'], 'Value': [1, 2, 3]}
        self._create_script(self.valid_csv_content)
        df, ax = task_func(self.script_path, self.output_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 2))
        self._validate_y_tick_labels(ax, df)
        self.assertListEqual(df.columns.tolist(), expected_columns)
        for column, expected_values in expected_data.items():
            self.assertTrue(all(df[column] == expected_values))

    def test_case_3(self):
        self._create_script(['exit 1\n'])
        with self.assertRaises(ValueError):
            task_func(self.script_path, self.output_path)
