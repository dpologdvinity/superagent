from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def base(self, filename, contents, expected):
        with open(filename, 'w') as f:
            f.write(contents)
        task_func(filename)
        with open(filename, 'r') as f:
            self.assertEqual(f.read().strip(), expected.strip())
        os.remove(filename)

    def test_case_1(self):
        self.base('file.csv', 'a,b,c\n1,2,3\n4,5,6\n7,8,9', 'a,b,c\n7,8,9\n4,5,6\n1,2,3')

    def test_case_2(self):
        self.base('file.csv', 'a,b,c\n1,2,3\n4,5,6', 'a,b,c\n4,5,6\n1,2,3')

    def test_case_3(self):
        self.base('file.csv', 'a,b,c\n1,2,3', 'a,b,c\n1,2,3')
