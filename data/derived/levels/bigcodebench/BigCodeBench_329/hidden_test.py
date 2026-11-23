from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        sample_data = {
            "data1.json": {
                "text1": "This is a (sample) text with some (matches) and characters.",
                "text2": "Another (example) with multiple matches."
            },
            "data2.json": {
                "text1": "(Hello) world!",
                "text2": "No matches here."
            },
            "data3.json": {
                "text1": "Testing (with) another (file).",
                "text2": "Just some (random) text."
            },
            "data4.json": {
                "text1": "(A) quick brown (fox) jumps.",
                "text2": "Over the lazy (dog)."
            },
            "data5.json": {
                "text1": "Yet (another) test file.",
                "text2": "With (various) matches."
            }
        }
        # Directory to save the test data
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_data_dir = f"{self.base_tmp_dir}/test/"
        # Create the directory if it doesn't exist
        if not os.path.exists(self.test_data_dir):
            os.makedirs(self.test_data_dir)
        # Saving the test data as JSON files
        for filename, content in sample_data.items():
            with open(os.path.join(self.test_data_dir, filename), "w") as file:
                json.dump(content, file)
    def tearDown(self):
        # Remove the test data directory
        shutil.rmtree(self.test_data_dir)
    def test_case_1(self):
        matches = task_func(os.path.join(self.test_data_dir, "data1.json"))
        expected = {
            "data1.json": [
                'T', 'h', 'i', 's', 'i', 's', 'a', '(sample)', 't', 'e', 'x', 't', 'w', 'i', 't', 
                'h', 's', 'o', 'm', 'e', '(matches)', 'a', 'n', 'd', 'c', 'h', 'a', 'r', 'a', 'c', 
                't', 'e', 'r', 's', 'A', 'n', 'o', 't', 'h', 'e', 'r', '(example)', 'w', 'i', 't',
                'h', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', 'm', 'a', 't', 'c', 'h', 'e', 's'
            ]
        }
        self.assertEqual(matches, expected)
    def test_case_2(self):
        matches = task_func(os.path.join(self.test_data_dir, "data2.json"))
        expected = {
            "data2.json": [
                '(Hello)', 'w', 'o', 'r', 'l', 'd', 'N', 'o', 'm', 'a', 't', 'c', 'h', 
                'e', 's', 'h', 'e', 'r', 'e'
            ]
        }
        self.assertEqual(matches, expected)
    def test_case_3(self):
        matches = task_func(os.path.join(self.test_data_dir, "data3.json"))
        expected = {
            "data3.json": [
                'T', 'e', 's', 't', 'i', 'n', 'g', '(with)', 'a', 'n', 'o', 't', 'h', 'e', 'r', '(file)', 'J',
                'u', 's', 't', 's', 'o', 'm', 'e', '(random)', 't', 'e', 'x', 't'    
            ]
        }
        self.assertEqual(matches, expected)
    def test_case_4(self):
        matches = task_func(os.path.join(self.test_data_dir, "data4.json"))
        expected = {
            "data4.json": [
                '(A)', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', '(fox)', 'j', 'u', 'm', 'p',
                's', 'O', 'v', 'e', 'r', 't', 'h', 'e', 'l', 'a', 'z', 'y', '(dog)'
            ]
        }
        self.assertEqual(matches, expected)
    def test_case_5(self):
        matches = task_func(os.path.join(self.test_data_dir, "data5.json"))
        expected = {
            "data5.json": [
                'Y', 'e', 't', '(another)', 't', 'e', 's', 't', 'f', 'i', 'l', 'e', 'W', 'i', 't', 
                'h', '(various)', 'm', 'a', 't', 'c', 'h', 'e', 's'   
            ]
        }
        self.assertEqual(matches, expected)
