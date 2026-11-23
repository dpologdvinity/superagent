from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import os
import glob
import codecs
# Helper function to create a text file with specific encoding
def create_text_file(filename, content, encoding):
    with codecs.open(filename, 'w', encoding) as file:
        file.write(content)
import codecs
import os
import glob
# Constants
DIRECTORY_PATH = './files/'
class TestCases(unittest.TestCase):
    def setUp(self):
        os.makedirs('./test_files/', exist_ok=True)
        os.makedirs('./empty/', exist_ok=True)
        
    def tearDown(self):
        for filename in glob.glob('./test_files/*.txt'):
            os.remove(filename)
        os.rmdir('./test_files/')
        os.rmdir('./empty/')
    @patch('glob.glob')
    def test_encoding_conversion(self, mock_glob):
        mock_glob.return_value = ['./test_files/file1.txt', './test_files/file2.txt']
        create_text_file('./test_files/file1.txt', 'Hello', 'utf8')
        create_text_file('./test_files/file2.txt', 'World', 'utf8')
        task_func(directory='./test_files/', from_encoding='utf8', to_encoding='ascii')
        with codecs.open('./test_files/file1.txt', 'r', 'ascii') as file:
            self.assertEqual(file.read(), 'Hello')
        with codecs.open('./test_files/file2.txt', 'r', 'ascii') as file:
            self.assertEqual(file.read(), 'World')
            
    @patch('glob.glob')
    def test_empty_directory(self, mock_glob):
        mock_glob.return_value = []
        task_func(directory='./empty/', from_encoding='utf8', to_encoding='ascii')
        
    @patch('glob.glob')
    def test_same_encoding(self, mock_glob):
        mock_glob.return_value = ['./test_files/file3.txt']
        create_text_file('./test_files/file3.txt', 'Same Encoding', 'utf8')
        task_func(directory='./test_files/', from_encoding='utf8', to_encoding='utf8')
        with codecs.open('./test_files/file3.txt', 'r', 'utf8') as file:
            self.assertEqual(file.read(), 'Same Encoding')
            
    @patch('glob.glob')
    def test_invalid_encoding(self, mock_glob):
        mock_glob.return_value = ['./test_files/file4.txt']
        create_text_file('./test_files/file4.txt', 'Invalid', 'utf8')
        with self.assertRaises(LookupError):
            task_func(directory='./test_files/', from_encoding='utf8', to_encoding='invalid_encoding')
            
    @patch('glob.glob')
    def test_nonexistent_directory(self, mock_glob):
        mock_glob.return_value = []
        task_func(directory='./nonexistent/', from_encoding='utf8', to_encoding='ascii')
