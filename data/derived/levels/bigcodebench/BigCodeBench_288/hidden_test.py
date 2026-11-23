from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
import tempfile
import doctest
# Create a temporary directory for testing
TEST_DIR_PATH = tempfile.mkdtemp()
def setup_test_directory():
    """
    Set up a directory with multiple JSON files for testing purposes.
    """
    if os.path.exists(TEST_DIR_PATH):
        shutil.rmtree(TEST_DIR_PATH)
    os.makedirs(TEST_DIR_PATH)
    json_files_data = [
        {'name': 'John', 'age': 25, 'address': '123 Main St'},
        {'name': 'Doe', 'age': 30},
        {'name': 'Jane', 'email': 'jane@example.com'},
        {'title': 'Mr', 'name': 'Smith'},
        {'name': 'Eva', 'email': 'eva@example.com', 'address': '456 Elm St'}
    ]
    
    for idx, data in enumerate(json_files_data):
        with open(os.path.join(TEST_DIR_PATH, f"sample_{idx}.json"), 'w') as f:
            json.dump(data, f)
class TestCases(unittest.TestCase):
    def setUp(self):
        setup_test_directory()
    def tearDown(self):
        if os.path.exists(TEST_DIR_PATH):
            shutil.rmtree(TEST_DIR_PATH)
    def test_case_1(self):
        # Test with 5 JSON files containing various keys
        expected_result = {'name': 5, 'age': 2, 'address': 2, 'email': 2, 'title': 1}
        result = task_func(TEST_DIR_PATH)
        self.assertDictEqual(result, expected_result)
    def test_case_2(self):
        # Test with a non-existent directory path
        with self.assertRaises(FileNotFoundError):
            task_func("/non/existent/path/")
    
    def test_case_3(self):
        # Test with a directory that doesn't have any JSON files
        os.makedirs(f"{TEST_DIR_PATH}/empty_directory/")
        result = task_func(f"{TEST_DIR_PATH}/empty_directory/")
        self.assertDictEqual(result, {})
    def test_case_4(self):
        # Test with JSON files having nested keys (nested keys should not be counted)
        with open(os.path.join(TEST_DIR_PATH, "sample_nested.json"), 'w') as f:
            json.dump({'person': {'name': 'John', 'age': 30}}, f)
        expected_result = {'name': 5, 'age': 2, 'address': 2, 'email': 2, 'title': 1, 'person': 1}
        result = task_func(TEST_DIR_PATH)
        result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
        self.assertDictEqual(result, expected_result)
    def test_case_5(self):
        # Test with an empty JSON file (should not change the count of keys)
        with open(os.path.join(TEST_DIR_PATH, "sample_empty.json"), 'w') as f:
            json.dump({}, f)
        expected_result = {'name': 5, 'age': 2, 'address': 2, 'email': 2, 'title': 1}
        result = task_func(TEST_DIR_PATH)
        result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
        self.assertDictEqual(result, expected_result)
