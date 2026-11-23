from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        expected_output = [('abc', 3), ('hij', 3), ('efg', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_2(self):
        text = "This is a test without any $ prefixed words."
        expected_output = []
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_3(self):
        text = "$apple $banana $apple $cherry $cherry $cherry"
        expected_output = [('cherry', 3), ('apple', 2), ('banana', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_4(self):
        text = "$$ $$ $$ $$"
        expected_output = [('$$', 4)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
    def test_case_5(self):
        text = "$word1 $word2 $word3 $word4 $word5 $word6"
        expected_output = [('word1', 1), ('word2', 1), ('word3', 1), ('word4', 1), ('word5', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
