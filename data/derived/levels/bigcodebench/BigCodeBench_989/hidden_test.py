from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import string
class TestCases(unittest.TestCase):
    def test_valid_length_and_predicates(self):
        result_str, result_dict = task_func(
            10,
            ["has_uppercase", "has_lowercase", "has_numbers", "has_special_chars"],
            seed=1,
        )
        self.assertEqual(len(result_str), 10)
        self.assertTrue(result_dict["has_uppercase"])
        self.assertTrue(result_dict["has_lowercase"])
        self.assertTrue(result_dict["has_numbers"])
        self.assertTrue(result_dict["has_special_chars"])
    def test_result_correctness(self):
        n_repetitions = 1000
        for _ in range(n_repetitions):
            result_str, result_dict = task_func(
                10,
                ["has_uppercase", "has_lowercase", "has_numbers", "has_special_chars"],
                seed=1,
            )
            if any(c.isupper() for c in result_str):
                self.assertTrue(result_dict["has_uppercase"])
            if any(c.islower() for c in result_str):
                self.assertTrue(result_dict["has_lowercase"])
            if any(c in string.punctuation for c in result_str):
                self.assertTrue(result_dict["has_special_chars"])
            if any(c.isdigit() for c in result_str):
                self.assertTrue(result_dict["has_numbers"])
    def test_empty_string(self):
        result_str, result_dict = task_func(0, ["has_uppercase", "has_numbers"], seed=3)
        self.assertEqual(result_str, "")
        self.assertFalse(result_dict["has_uppercase"])
        self.assertFalse(result_dict["has_numbers"])
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            task_func(-1, ["has_uppercase"])
    def test_no_predicates(self):
        result_str, result_dict = task_func(10, [], seed=5)
        self.assertEqual(len(result_str), 10)
        self.assertEqual(result_dict, {})
    def test_key_error(self):
        with self.assertRaises(KeyError):
            task_func(10, ["has_uppercase", "invalid"])
    def test_deduplicate_predicates(self):
        _, result_dict = task_func(15, ["has_uppercase", "has_uppercase"], seed=7)
        self.assertEqual(len(result_dict), 1)
    def test_random_seed_reproducibility(self):
        result_str1, result_dict1 = task_func(10, ["has_uppercase", "has_numbers"], seed=8)
        result_str2, result_dict2 = task_func(10, ["has_uppercase", "has_numbers"], seed=8)
        self.assertEqual(result_str1, result_str2)
        self.assertEqual(result_dict1, result_dict2)
