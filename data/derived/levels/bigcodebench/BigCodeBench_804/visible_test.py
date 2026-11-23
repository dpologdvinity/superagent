from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, mock_open, MagicMock

class TestCases(unittest.TestCase):

    def setUp(self):
        self.metrics = {'accuracy': 0.98, 'loss': 0.05}
        self.filename = 'metrics.log'
        self.log_dir = './temp_logs'

    def test_non_string_filename(self):
        with self.assertRaises(ValueError):
            task_func(self.metrics, 12345, log_dir=self.log_dir)

    def test_non_dictionary_metrics(self):
        with self.assertRaises(ValueError):
            task_func('accuracy: 0.95', self.filename, log_dir=self.log_dir)

    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_normal_metrics_logging(self, mock_exists, mock_file, mock_makedirs):
        result = task_func(self.metrics, self.filename, log_dir=self.log_dir)
        self.assertTrue(result)
        mock_file.assert_called_once_with(os.path.join(self.log_dir, self.filename), 'a')
