from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
# Import the function from the provided file
class TestCases(unittest.TestCase):
    
    def test_1(self):
        my_dict = {'apple': 1, 'banana': 2, 'avocado': 3, 'blueberry': 4, 'blackberry': 5}
        result = task_func(my_dict)
        expected = {'a': 4, 'b': 11}
        self.assertEqual(result, expected)
        
    def test_2(self):
        my_dict = {'apple': 10, 'apricot': 10, 'banana': 10, 'blueberry': 10}
        result = task_func(my_dict)
        expected = {'a': 20, 'b': 20}
        self.assertEqual(result, expected)
    def test_3(self):
        my_dict = {}
        result = task_func(my_dict)
        expected = {}
        self.assertEqual(result, expected)
    def test_4(self):
        my_dict = {'apple': 1, 'orange': 2, 'cherry': 3, 'blueberry': 4}
        result = task_func(my_dict)
        expected = {'a': 1, 'o': 2, 'c': 3, 'b': 4}
        self.assertEqual(result, expected)
    def test_5(self):
        my_dict = {'apple': 1, 'apricot': 2, 'banana': 3, 'blueberry': 4, 'cherry': 5, 'date': 6}
        result = task_func(my_dict)
        expected = {'a': 3, 'b': 7, 'c': 5, 'd': 6}
        self.assertEqual(result, expected)
