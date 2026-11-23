from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import pandas as pd
import numpy as np
import tempfile
from datetime import datetime

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_case_1(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        file_path = os.path.join(self.temp_dir.name, 'test.pkl')
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))

    def test_case_2(self):
        df = pd.DataFrame(np.random.rand(50, 3), columns=list('XYZ'))
        file_path = os.path.join(self.temp_dir.name, 'floats.pkl')
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))

    def test_case_3(self):
        df = pd.DataFrame({'A': ['foo', 'bar', 'baz'], 'B': ['qux', 'quux', 'corge']})
        file_path = os.path.join(self.temp_dir.name, 'strings.pkl')
        loaded_df = task_func(df, file_path)
        self.assertTrue(df.equals(loaded_df))
        self.assertFalse(os.path.exists(file_path))
