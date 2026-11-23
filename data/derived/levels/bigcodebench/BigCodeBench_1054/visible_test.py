from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, mock_open
import matplotlib

class TestCases(unittest.TestCase):
    """Test cases for task_func."""

    def setUp(self):
        """Set up the test environment."""
        matplotlib.use('Agg')

    def test_valid_csv_file(self):
        """Test with a valid CSV file."""
        mock_data = '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            mean, std_dev, ax = task_func('dummy_path')
            self.assertIsNotNone(mean)
            self.assertIsNotNone(std_dev)

    def test_empty_csv_file(self):
        """Test with an empty CSV file."""
        mock_data = ''
        with patch('builtins.open', mock_open(read_data=mock_data)), self.assertRaises(ValueError):
            task_func('dummy_path')

    def test_non_existent_file(self):
        """Test with a non-existent file path."""
        with self.assertRaises(IOError):
            task_func('non_existent_path.csv')

    def tearDown(self):
        plt.close('all')
