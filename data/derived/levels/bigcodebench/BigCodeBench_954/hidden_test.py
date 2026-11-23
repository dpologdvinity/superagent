from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        self.vocabulary = [
            "apple",
            "banana",
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grape",
            "honeydew",
        ]
        random.seed(42)
    def test_case_1(self):
        # Test with multiple target words and sentences
        target_words = ["apple banana", "banana cherry"]
        n_sentences = 1000
        results = task_func(target_words, n_sentences, ["apple", "banana", "cherry"])
        self.assertEqual(len(results), n_sentences)
        for target in target_words:
            underscored_target = target.replace(" ", "_")
            self.assertTrue(
                any(underscored_target in sentence for sentence in results),
                f"{underscored_target} not found in any sentences",
            )
    def test_case_2(self):
        # Test with a single target word in multiple occurrences
        target_words = ["apple"]
        n_sentences = 1
        results = task_func(target_words, n_sentences, ["apple"] * 10)
        self.assertEqual(len(results), n_sentences)
        self.assertTrue(
            results[0].count("apple") > 1,
            "Multiple 'apple' occurrences not replaced correctly",
        )
    def test_case_3(self):
        # Test with no target words
        target_words = []
        n_sentences = 1
        results = task_func(target_words, n_sentences, self.vocabulary)
        self.assertEqual(len(results), n_sentences)
        self.assertTrue(all(" " in sentence for sentence in results), "")
    def test_case_4(self):
        # Test case sensitivity
        target_words = ["Apple Banana"]
        n_sentences = 2
        results = task_func(target_words, n_sentences, self.vocabulary + ["apple banana"])
        self.assertEqual(len(results), n_sentences)
        for result in results:
            self.assertIn(
                "apple_banana", result, "Case sensitivity not handled properly"
            )
    def test_case_5(self):
        # Test generating zero sentences
        target_words = ["apple"]
        n_sentences = 0
        results = task_func(target_words, n_sentences, self.vocabulary)
        self.assertEqual(len(results), n_sentences, "No sentences should be generated")
    def test_case_6(self):
        # Test function handling invalid inputs - vocabulary
        target_words = ["apple"]
        n_sentences = 1
        with self.assertRaises(ValueError):
            task_func(target_words, n_sentences, [])
    def test_case_7(self):
        # Test function handling invalid inputs - n_sentences
        target_words = ["apple"]
        with self.assertRaises(ValueError):
            task_func(target_words, -1, self.vocabulary)
        with self.assertRaises(TypeError):
            task_func(target_words, 1.0, self.vocabulary)
    def test_case_8(self):
        # Test whitespace target word
        target_words = [" "]
        n_sentences = 1
        results = task_func(target_words, n_sentences, ["apple banana", "cherry"])
        assert len(results[0].split("_")) >= 10
    def test_case_9(self):
        # Test target word not in vocabulary
        target_words = ["mango"]
        n_sentences = 2
        results = task_func(target_words, n_sentences, ["apple", "banana", "cherry"])
        for sentence in results:
            self.assertNotIn(
                "mango",
                sentence,
                "Target word not in vocabulary should not appear in sentences.",
            )
