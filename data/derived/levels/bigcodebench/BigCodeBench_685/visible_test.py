from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}))

    def test_case_2(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}))

    def test_case_3(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(task_func(list_of_lists), Counter({1: 3, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}))
