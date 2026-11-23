from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a typical input list
        input_data = ["lamp, bag, mirror", "table, chair, bag, lamp"]
        result = task_func(input_data, seed=0)
        self.assertTrue(all(item in input_data for item in result["Original String"]))
        self.assertNotEqual(
            result["Original String"].tolist(), result["Modified String"].tolist()
        )
    def test_case_2(self):
        # Test with a single-item list
        input_data = ["lamp, bag, mirror"]
        result = task_func(input_data, seed=0)
        self.assertTrue(all(item in input_data for item in result["Original String"]))
        self.assertNotEqual(
            result["Original String"].tolist(), result["Modified String"].tolist()
        )
    def test_case_3(self):
        # Test with a list of varied length strings
        input_data = ["lamp, chair", "table, mirror, bag", "desk, bed"]
        result = task_func(input_data, seed=0)
        self.assertTrue(all(item in input_data for item in result["Original String"]))
        self.assertNotEqual(
            result["Original String"].tolist(), result["Modified String"].tolist()
        )
    def test_case_4(self):
        # Test with an empty list
        input_data = []
        result = task_func(input_data, seed=0)
        self.assertEqual(len(result), 0)
    def test_case_5(self):
        # Test with a list of empty strings
        input_data = ["", "", ""]
        result = task_func(input_data, seed=0)
        self.assertEqual(result["Original String"].tolist(), ["", "", ""])
        self.assertEqual(result["Modified String"].tolist(), ["", "", ""])
    def test_case_6(self):
        # Test with strings that have no commas
        input_data = ["lamps", "table"]
        result = task_func(input_data, seed=1)
        self.assertTrue(
            all(len(modified) == 5 for modified in result["Modified String"])
        )
    def test_case_7(self):
        # Test with strings that contain multiple identical substrings
        input_data = ["lamp, lamp, lamp"]
        result = task_func(input_data, seed=2)
        self.assertNotEqual(result["Original String"][0], result["Modified String"][0])
        self.assertTrue(
            any(sub != "lamp" for sub in result["Modified String"][0].split(", "))
        )
    def test_case_8(self):
        # Test with mixed case input strings
        input_data = ["Lamp, Bag, Mirror"]
        result = task_func(input_data, seed=4)
        self.assertNotEqual(
            result["Original String"].tolist(), result["Modified String"].tolist()
        )
        self.assertTrue(
            any(char.islower() for char in result["Modified String"][0])
        )  # Ensure replacement is in lowercase
    def test_case_9(self):
        # Test effect of different seeds on output
        input_data = ["lamp, bag, mirror"]
        result_seed_0a = task_func(input_data, seed=0)
        result_seed_0b = task_func(input_data, seed=0)
        result_seed_5 = task_func(input_data, seed=5)
        self.assertEqual(
            result_seed_0a["Modified String"][0], result_seed_0b["Modified String"][0]
        )
        self.assertNotEqual(
            result_seed_0a["Modified String"][0], result_seed_5["Modified String"][0]
        )
    def test_case_10(self):
        # Test case sensitivity
        input_data = ["Lamp, Bag, Mirror"]
        result = task_func(input_data, seed=3)
        original_items = [
            item.lower() for item in result["Original String"][0].split(", ")
        ]
        modified_items = [item for item in result["Modified String"][0].split(", ")]
        self.assertTrue(
            any(mod_item not in original_items for mod_item in modified_items),
            "Modified string should contain a lowercase random replacement not present in the original string",
        )
    def test_case_11(self):
        # Test whitespaces (i.e. make sure leading/trailing whitespaces are removed in processing substrings)
        input_data = ["  lamp, bag   ,mirror  "]
        result = task_func(input_data, seed=3)
        modified = result["Modified String"][0].split(", ")
        self.assertTrue(
            all(item.strip() == item for item in modified),
            "All items in the modified string should have leading and trailing whitespaces removed",
        )
