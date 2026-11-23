from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'item1': ['a', 'b', 'a'], 'item2': ['b', 'c', 'b'], 'item3': ['c', 'd', 'c'], 'item4': ['d', 'e', 'd'], 'item5': ['e', 'f', 'e']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 2)
        self.assertEqual(freq[('b', 'c', 'd', 'e', 'f')], 1)
    def test_case_2(self):
        df = pd.DataFrame({'item1': ['c', 'b', 'a'], 'item2': ['b', 'c', 'b'], 'item3': ['c', 'd', 'c'], 'item4': ['d', 'e', 'd'], 'item5': ['e', 'f', 'e']})
        freq = task_func(df)
        print(freq)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 1)
        self.assertEqual(freq[('b', 'c', 'd', 'e', 'f')], 1)
        if ('b', 'c', 'c', 'd', 'e') in freq:
            self.assertEqual(freq[('b', 'c', 'c', 'd', 'e')], 1)
        elif ('c', 'b', 'c', 'd', 'e') in freq:
            self.assertEqual(freq[('c', 'b', 'c', 'd', 'e')], 1)
    def test_case_3(self):
        df = pd.DataFrame({'item1': ['a'], 'item2': ['a'], 'item3': ['a'], 'item4': ['a'], 'item5': ['a']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'a', 'a', 'a', 'a')], 1)
    def test_case_4(self):
        df = pd.DataFrame({'item1': ['a', 'b', 'c'], 'item2': ['b', 'c', 'd'], 'item3': ['c', 'd', 'e'], 'item4': ['d', 'e', 'f'], 'item5': ['e', 'f', 'g']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 1)
        self.assertEqual(freq[('b', 'c', 'd', 'e', 'f')], 1)
        self.assertEqual(freq[('c', 'd', 'e', 'f', 'g')], 1)
    def test_case_5(self):
        df = pd.DataFrame({'item1': ['a', 'a', 'a'], 'item2': ['b', 'b', 'b'], 'item3': ['c', 'c', 'c'], 'item4': ['d', 'd', 'd'], 'item5': ['e', 'e', 'e']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 3)
