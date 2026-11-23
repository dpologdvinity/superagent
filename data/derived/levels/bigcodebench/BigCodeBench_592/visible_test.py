from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
FILE_PATH = os.path.join(OUTPUT_DIR, 'sensor_data.csv')

class TestCases(unittest.TestCase):

    def tearDown(self):
        """Clean up any files created during the tests."""
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)

    def test_csv_file_creation(self):
        """Test if the CSV file is successfully created."""
        task_func(1)
        self.assertTrue(os.path.exists(FILE_PATH))

    def test_csv_file_rows(self):
        """Test if the CSV file contains the correct number of rows for 24 hours."""
        task_func(24)
        with open(FILE_PATH, 'r') as f:
            self.assertEqual(len(f.readlines()), 25)

    def test_csv_file_header(self):
        """Test if the CSV file header matches the expected sensors."""
        task_func(0)
        with open(FILE_PATH, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Time', 'Temperature', 'Humidity', 'Pressure'])
