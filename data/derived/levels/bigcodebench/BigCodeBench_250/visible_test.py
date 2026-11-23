from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.json_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        self.json_file.close()

    def test_case_1(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        expected_output = {'Position 1': 3.0, 'Position 2': 4.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)

    def test_case_2(self):
        data_list = [('a', 10, 20), ('b', 20, 30), ('c', 30, 40)]
        expected_output = {'Position 1': 20.0, 'Position 2': 30.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)

    def test_case_3(self):
        data_list = [('a', 5), ('b', 10), ('c', 15)]
        expected_output = {'Position 1': 10.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
