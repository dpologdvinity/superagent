from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.valid_config_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.valid_config_file.write('{"database": "test_db", "logging": true}')
        self.valid_config_file.close()
        self.empty_config_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.empty_config_file.write('{}')
        self.empty_config_file.close()
        self.invalid_json_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.invalid_json_file.write('invalid json')
        self.invalid_json_file.close()

    def tearDown(self):
        os.unlink(self.valid_config_file.name)
        os.unlink(self.empty_config_file.name)
        os.unlink(self.invalid_json_file.name)

    def test_valid_config(self):
        config = task_func(self.valid_config_file.name)
        self.assertIsInstance(config, dict)
        self.assertIn('database', config)
        self.assertIn('logging', config)

    def test_non_existent_config(self):
        with self.assertRaises(FileNotFoundError):
            task_func('test_data/non_existent_config.json')

    def test_invalid_json_format(self):
        with self.assertRaises(json.JSONDecodeError):
            task_func(self.invalid_json_file.name)
