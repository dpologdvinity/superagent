from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
OUTPUT_DIR = './output'

class TestCases(unittest.TestCase):

    def setUp(self):
        self.output_dir = OUTPUT_DIR
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.test_file = os.path.join(self.output_dir, 'test.csv')
        with open(self.test_file, 'w') as f:
            f.write('col1,col2\n1,2\n3,4')
        with open(self.test_file, 'r') as f:
            content = f.read()
        print(f'Debug: Content written to {self.test_file}: {content}')

    def tearDown(self):
        shutil.rmtree(self.output_dir, ignore_errors=True)

    def test_file_not_found(self):
        """Test the function with a filename that does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent.csv')

    def test_file_removal(self):
        """Ensure the function does not remove the file, only erases contents."""
        task_func(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_empty_csv(self):
        """Test reading an empty CSV file."""
        open(self.test_file, 'w').close()
        df = task_func(self.test_file)
        self.assertTrue(df.empty, 'DataFrame should be empty for an empty CSV file.')
        self.assertEqual(os.path.getsize(self.test_file), 0, 'The file should still be erased.')
