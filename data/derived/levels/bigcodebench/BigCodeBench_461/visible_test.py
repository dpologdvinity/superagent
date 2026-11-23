from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = self.temp_dir.name
        self.script_path_1 = os.path.join(self.temp_path, 'script.sh')
        with open(self.script_path_1, 'w') as script_file:
            os.chmod(self.script_path_1, 493)
            script_file.write('#!/bin/bash\nsleep 5')
        self.script_path_2 = os.path.join(self.temp_path, 'cpu_script.sh')
        with open(self.script_path_2, 'w') as script_file:
            os.chmod(self.script_path_2, 493)
            script_file.write('#!/bin/bash\nfor i in {1..10000}\ndo\n   echo $i > /dev/null\ndone')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_case_1(self):
        resources = task_func(self.script_path_1)
        self.assertIn('CPU Usage', resources)
        self.assertIn('Memory Usage', resources)

    def test_case_2(self):
        resources = task_func(self.script_path_1)
        self.assertIsInstance(resources['CPU Usage'], float)
        self.assertIsInstance(resources['Memory Usage'], int)

    def test_case_3(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_script.sh')
