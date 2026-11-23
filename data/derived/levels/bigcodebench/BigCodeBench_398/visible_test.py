from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
import doctest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_data_folder = f'{self.base_tmp_dir}/test'
        os.makedirs(self.test_data_folder, exist_ok=True)
        valid_json_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        invalid_json_data = ['Alice', 30, 'Bob', 25]
        empty_json_data = []
        non_dict_list_json_data = [{'name': 'Alice', 'age': 30}, ['Bob', 25]]

        def write_json_file(file_name, data):
            with open(os.path.join(self.test_data_folder, file_name), 'w') as file:
                json.dump(data, file)
        write_json_file('valid.json', valid_json_data)
        write_json_file('invalid.json', invalid_json_data)
        write_json_file('empty.json', empty_json_data)
        write_json_file('non_dict_list.json', non_dict_list_json_data)

    def tearDown(self):
        if os.path.exists(self.test_data_folder):
            shutil.rmtree(self.test_data_folder)

    def test_case_1(self):
        file_path = os.path.join(self.test_data_folder, 'valid.json')
        self.assertTrue(task_func(file_path))

    def test_case_2(self):
        file_path = os.path.join(self.test_data_folder, 'invalid.json')
        self.assertFalse(task_func(file_path))

    def test_case_3(self):
        file_path = os.path.join(self.test_data_folder, 'empty.json')
        self.assertTrue(task_func(file_path))
