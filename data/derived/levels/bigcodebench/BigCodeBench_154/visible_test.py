from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, mock_open
import mimetypes

class TestCases(unittest.TestCase):

    def test_return_type(self):
        """Test that the function returns a dictionary."""
        with patch('os.chdir'), patch('glob.glob', return_value=[]), patch('re.search'):
            result = task_func('/path/to/directory', '*', '_suff')
        self.assertIsInstance(result, dict)

    @patch('glob.glob', return_value=['file_suff.txt', 'other_file.txt'])
    @patch('os.chdir')
    def test_dictionary_content(self, mock_chdir, mock_glob):
        """Test the content of the dictionary."""
        result = task_func('/path/to/directory', '*_suff.txt', '_suff')
        self.assertIn('file_suff.txt', result)
        self.assertNotIn('other_file.txt', result)

    @patch('mimetypes.guess_type', return_value=['text/plain'])
    @patch('glob.glob', return_value=['file_suff.txt'])
    @patch('os.chdir')
    def test_file_type_identification(self, mock_chdir, mock_glob, mock_guess_type):
        """Test correct file type identification."""
        result = task_func('/path/to/directory', '*', '_suff')
        self.assertEqual(result['file_suff.txt'], 'text/plain')
