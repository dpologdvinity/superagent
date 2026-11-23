from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import doctest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = tempfile.mkdtemp()
        self.log_text_1 = 'Request from 102.168.0.1\nRequest from 118.128.1.11\nRequest from 175.193.115.67'
        self.log_text_2 = 'Request from 189.56.7.1\nRequest from 128.45.234.88\nRequest from 985.123.1.1'
        self.log_text_3 = 'Request from localhost\nRequest from remote'
        self.log_text_4 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec odio. Sed non posuere.'
        self.log_text_5 = 'Request from 181.94.113.34\nMemory usage: 50'

    def test_case_1(self):
        """Tests with 5 log files containing various IP addresses."""
        with open(os.path.join(self.test_data_dir, 'file1.log'), 'w') as file:
            file.write(self.log_text_1)
        with open(os.path.join(self.test_data_dir, 'file2.log'), 'w') as file:
            file.write(self.log_text_2)
        with open(os.path.join(self.test_data_dir, 'file3.log'), 'w') as file:
            file.write(self.log_text_3)
        with open(os.path.join(self.test_data_dir, 'file4.log'), 'w') as file:
            file.write(self.log_text_4)
        with open(os.path.join(self.test_data_dir, 'file5.log'), 'w') as file:
            file.write(self.log_text_5)
        result = task_func(self.test_data_dir)
        expected = {'189.56.7.1': 1, '128.45.234.88': 1, '985.123.1.1': 1, '102.168.0.1': 1, '118.128.1.11': 1, '175.193.115.67': 1, '181.94.113.34': 1}
        self.assertDictEqual(result, expected)

    def test_case_2(self):
        """Tests with an empty directory."""
        empty_dir = os.path.join(self.test_data_dir, 'empty_dir')
        os.makedirs(empty_dir, exist_ok=True)
        result = task_func(empty_dir)
        self.assertDictEqual(result, {})

    def test_case_3(self):
        """Tests with a directory containing only non-log files."""
        non_log_dir = os.path.join(self.test_data_dir, 'non_log_dir')
        os.makedirs(non_log_dir, exist_ok=True)
        with open(os.path.join(non_log_dir, 'file.txt'), 'w') as file:
            file.write('192.168.0.1\n192.168.0.2')
        result = task_func(non_log_dir)
        self.assertDictEqual(result, {})
