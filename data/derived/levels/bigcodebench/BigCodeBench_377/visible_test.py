from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import re

class TestCases(unittest.TestCase):

    def setUp(self):
        self.result = task_func()

    def test_return_type(self):
        """Test that the function returns a string."""
        self.assertIsInstance(self.result, str)

    def test_table_headers(self):
        """Test the presence of correct headers in the table."""
        for header in ['CPU Usage (%)', 'Memory Usage (%)', 'Disk Usage (%)']:
            with self.subTest(header=header):
                self.assertIn(header, self.result)

    def test_proper_values(self):
        """Test that the table's values are not empty or zero."""
        values = re.findall('\\|\\s*[\\d.]+\\s*\\|', self.result)
        for value_str in values:
            value = float(value_str.strip('| ').strip())
            with self.subTest(value=value):
                self.assertTrue(0 <= value <= 100)
