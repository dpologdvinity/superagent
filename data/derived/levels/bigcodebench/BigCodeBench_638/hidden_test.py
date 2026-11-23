from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func()
        self.assertEqual(df.shape, (5, 100))
    def test_case_2(self):
        df = task_func(num_teams=3, num_games=10)
        self.assertEqual(df.shape, (3, 10))
        
    def test_case_3(self):
        df = task_func(num_teams=4, num_games=20)
        self.assertListEqual(list(df.index), ['Team1', 'Team2', 'Team3', 'Team4'])
        
    def test_case_4(self):
        df = task_func(num_teams=2, num_games=5)
        self.assertListEqual(list(df.columns), ['Game1', 'Game2', 'Game3', 'Game4', 'Game5'])
        
    def test_case_5(self):
        df = task_func(num_teams=2, num_games=5)
        self.assertTrue((df.dtypes == 'int64').all())
