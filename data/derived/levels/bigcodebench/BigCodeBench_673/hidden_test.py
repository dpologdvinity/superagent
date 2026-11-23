from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
class TestCases(unittest.TestCase):
    def base(self, dir, n_files, contents):
        random.seed(42)
        # Create directory
        if not os.path.exists(dir):
            os.makedirs(dir)
        # Run function
        n = task_func(dir, n_files)
        # Check files
        self.assertEqual(n, n_files)
        read_data = []
        for f in sorted(os.listdir(dir)):
            self.assertTrue(f.endswith('.txt'))
            with open(os.path.join(dir, f), 'r') as file:
                read_data.append(file.read())
                file.seek(0)
        self.assertEqual(read_data, contents)
    def tearDown(self):
        shutil.rmtree('./directory', ignore_errors=True)
        shutil.rmtree('./dir', ignore_errors=True)
        shutil.rmtree('./d', ignore_errors=True)
    def test_case_1(self):
        self.base('./directory', 5, ['1', '0', '4', '3', '3'])
    def test_case_2(self):
        self.base('./dir', 10, ['1', '9', '0', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_3(self):
        self.base('./d', 15, ['1', '9', '6', '0', '0', '1', '3', '0', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_4(self):
        self.base('./d', 20, ['1', '9', '6', '0', '0', '1', '3', '3', '8', '9', '0', '0', '8', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_5(self):
        self.base('./directory', 25, ['1', '9', '6', '0', '0', '1', '3', '3', '8', '9', '0', '0', '8', '3', '8', '6', '3', '7', '4', '3', '3', '2', '1', '8', '1'])
