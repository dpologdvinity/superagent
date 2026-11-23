from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create temporary configuration files for testing
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
        # Clean up temporary configuration files after testing
        os.unlink(self.valid_config_file.name)
        os.unlink(self.empty_config_file.name)
        os.unlink(self.invalid_json_file.name)
    
    def test_valid_config(self):
        # Test with a valid configuration file
        config = task_func(self.valid_config_file.name)
        self.assertIsInstance(config, dict)
        self.assertIn("database", config)
        self.assertIn("logging", config)
    
    def test_non_existent_config(self):
        # Test with a non-existent configuration file
        with self.assertRaises(FileNotFoundError):
            task_func("test_data/non_existent_config.json")
    
    def test_invalid_json_format(self):
        # Test with a configuration file containing invalid JSON
        with self.assertRaises(json.JSONDecodeError):
            task_func(self.invalid_json_file.name)
    
    def test_empty_config(self):
        # Test with an empty configuration file
        config = task_func(self.empty_config_file.name)
        self.assertIsInstance(config, dict)
        self.assertEqual(len(config), 0)
    
    def test_additional_config_fields(self):
        # Test with a configuration file containing additional fields
        extra_config_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        extra_config_file.write('{"database": "test_db", "logging": true, "extra_field": "value"}')
        extra_config_file.close()
        
        config = task_func(extra_config_file.name)
        self.assertIsInstance(config, dict)
        self.assertIn("database", config)
        self.assertIn("logging", config)
        self.assertIn("extra_field", config)
        
        os.unlink(extra_config_file.name)
