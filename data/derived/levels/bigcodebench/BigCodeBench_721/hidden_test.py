from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
# Constants
BASE_PATH = 'task_func_data'
FILE_NAME = os.path.join(BASE_PATH, 'Output.txt')
class TestCases(unittest.TestCase):
    def setUp(self):
        """Create the directory for test files."""
        os.makedirs(BASE_PATH, exist_ok=True)
    def tearDown(self):
        """Remove all created test files and the directory after all tests."""
        for filename in os.listdir(BASE_PATH):
            os.remove(os.path.join(BASE_PATH, filename))
        os.rmdir(BASE_PATH)
    def create_and_fill_file(self, filename, contents):
        """Helper method to create and populate a file with given contents."""
        full_path = os.path.join(BASE_PATH, filename)
        with open(full_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for content in contents:
                writer.writerow([content])
        return full_path
    def test_1(self):
        file_path = self.create_and_fill_file('Output.txt', ['banana']*5)
        result = task_func(file_path)
        self.assertEqual(result, ('banana', 5))
    def test_2(self):
        file_path = self.create_and_fill_file('AnotherOutput.txt', ['cat']*5)
        result = task_func(file_path)
        self.assertEqual(result, ('cat', 5))
    def test_3(self):
        file_path = self.create_and_fill_file('YetAnotherOutput.txt', ['moon']*5)
        result = task_func(file_path)
        self.assertEqual(result, ('moon', 5))
    def test_4(self):
        file_path = self.create_and_fill_file('Nonexistent.txt', [])
        result = task_func(file_path)
        self.assertIsNone(result)
    def test_5(self):
        file_path = self.create_and_fill_file('EmptyFile.txt', [])
        result = task_func(file_path)
        self.assertIsNone(result)
