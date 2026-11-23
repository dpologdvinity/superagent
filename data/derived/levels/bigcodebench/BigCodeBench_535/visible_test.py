from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import sqlite3
import tempfile

class TestCases(unittest.TestCase):
    NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, 'test.db')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_case_1(self):
        result = task_func(self.db_path, 'SamplePeople', 50, random_seed=42)
        self.assertEqual(result, 50)

    def test_case_2(self):
        result = task_func(self.db_path, 'NewPeople', 30, random_seed=42)
        self.assertEqual(result, 30)

    def test_case_3(self):
        result = task_func(self.db_path, 'SamplePeople', 20, random_seed=42)
        self.assertEqual(result, 20)
