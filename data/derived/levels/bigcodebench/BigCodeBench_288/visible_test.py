from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
import tempfile
import doctest
TEST_DIR_PATH = tempfile.mkdtemp()

def setup_test_directory():
    """
    Set up a directory with multiple JSON files for testing purposes.
    """
    if os.path.exists(TEST_DIR_PATH):
        shutil.rmtree(TEST_DIR_PATH)
    os.makedirs(TEST_DIR_PATH)
    json_files_data = [{'name': 'John', 'age': 25, 'address': '123 Main St'}, {'name': 'Doe', 'age': 30}, {'name': 'Jane', 'email': 'jane@example.com'}, {'title': 'Mr', 'name': 'Smith'}, {'name': 'Eva', 'email': 'eva@example.com', 'address': '456 Elm St'}]
    for idx, data in enumerate(json_files_data):
        with open(os.path.join(TEST_DIR_PATH, f'sample_{idx}.json'), 'w') as f:
            json.dump(data, f)

class TestCases(unittest.TestCase):

    def setUp(self):
        setup_test_directory()

    def tearDown(self):
        if os.path.exists(TEST_DIR_PATH):
            shutil.rmtree(TEST_DIR_PATH)

    def test_case_1(self):
        expected_result = {'name': 5, 'age': 2, 'address': 2, 'email': 2, 'title': 1}
        result = task_func(TEST_DIR_PATH)
        self.assertDictEqual(result, expected_result)

    def test_case_2(self):
        with self.assertRaises(FileNotFoundError):
            task_func('/non/existent/path/')

    def test_case_3(self):
        os.makedirs(f'{TEST_DIR_PATH}/empty_directory/')
        result = task_func(f'{TEST_DIR_PATH}/empty_directory/')
        self.assertDictEqual(result, {})
