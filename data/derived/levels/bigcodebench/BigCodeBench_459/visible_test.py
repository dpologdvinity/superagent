from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import os
from datetime import datetime

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.script_dir = self.temp_dir.name

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_temp_script(self, script_content):
        fd, path = tempfile.mkstemp(dir=self.script_dir, suffix='.sh')
        with os.fdopen(fd, 'w') as f:
            f.write('#!/bin/bash\n')
            f.write(script_content)
        os.chmod(path, 493)
        return os.path.basename(path)

    def test_case_1(self):
        script_name = self.create_temp_script("echo 'Test'")
        scripts = [script_name]
        delay = 1
        start_times = task_func(self.script_dir, scripts, delay)
        self.assertEqual(len(start_times), 1)
        self.assertTrue(isinstance(datetime.strptime(start_times[0], '%Y-%m-%d %H:%M:%S'), datetime))

    def test_case_2(self):
        script_names = [self.create_temp_script("echo 'Test'"), self.create_temp_script("echo 'Test 2'")]
        delay = 2
        start_times = task_func(self.script_dir, script_names, delay)
        self.assertTrue(2 <= len(start_times))
        time_diff = datetime.strptime(start_times[1], '%Y-%m-%d %H:%M:%S') - datetime.strptime(start_times[0], '%Y-%m-%d %H:%M:%S')
        self.assertTrue(2 <= time_diff.seconds <= 3)

    def test_case_3(self):
        with self.assertRaises(FileNotFoundError):
            task_func(self.script_dir, ["this-doesn't-exist"], 1)
