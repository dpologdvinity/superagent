from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        text = '$abc def $efg $hij klm $ $abc $abc $hij $hij'
        expected_output = [('abc', 3), ('hij', 3), ('efg', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        text = 'This is a test without any $ prefixed words.'
        expected_output = []
        result = task_func(text)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        text = '$apple $banana $apple $cherry $cherry $cherry'
        expected_output = [('cherry', 3), ('apple', 2), ('banana', 1)]
        result = task_func(text)
        self.assertEqual(result, expected_output)
