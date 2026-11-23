from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import shutil
import doctest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_case_1(self):
        file_1 = os.path.join(self.test_dir, 'file_1.json')
        file_2 = os.path.join(self.test_dir, 'file_2.json')
        with open(file_1, 'w') as f:
            json.dump({'name': 'Alice'}, f)
        with open(file_2, 'w') as f:
            json.dump({'name': 'Bob', 'mynewkey': 'existingvalue'}, f)
        updated_files = task_func(self.test_dir)
        self.assertEqual(updated_files, 1)
        with open(file_1, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {'name': 'Alice', 'mynewkey': 'mynewvalue'})
        with open(file_2, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {'name': 'Bob', 'mynewkey': 'existingvalue'})

    def test_case_2(self):
        file_1 = os.path.join(self.test_dir, 'file_3.json')
        file_2 = os.path.join(self.test_dir, 'file_4.json')
        with open(file_1, 'w') as f:
            json.dump({'id': 1}, f)
        with open(file_2, 'w') as f:
            json.dump({'id': 2}, f)
        updated_files = task_func(self.test_dir)
        self.assertEqual(updated_files, 2)
        with open(file_1, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {'id': 1, 'mynewkey': 'mynewvalue'})
        with open(file_2, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {'id': 2, 'mynewkey': 'mynewvalue'})

    def test_case_3(self):
        updated_files = task_func(self.test_dir)
        self.assertEqual(updated_files, 0)
