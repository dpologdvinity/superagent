from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
    def tearDown(self):
        self.temp_dir.cleanup()
    def _create_temp_log_file(self, file_name: str, content: str):
        """Helper function to create a temporary log file."""
        path = os.path.join(self.temp_dir.name, file_name)
        with open(path, "w") as f:
            f.write(content)
        return path
    def test_case_1(self):
        # Test log file with mixed levels
        content = (
            "2023-01-01 12:00:00.000000 - INFO - Application started\n"
            "2023-01-01 12:01:00.000000 - ERROR - Failed to connect to database\n"
        )
        log_file_path = self._create_temp_log_file("log1.txt", content)
        df = task_func(log_file_path)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]["Level"], "INFO")
        self.assertEqual(df.iloc[1]["Level"], "ERROR")
    def test_case_2(self):
        # Test case for an empty log file
        log_file_path = self._create_temp_log_file("log2.txt", "")
        df = task_func(log_file_path)
        self.assertTrue(df.empty)
    def test_case_3(self):
        # Log file with lines that do not match the expected format
        content = "This is not a valid log entry\n2023-01-02 13:00:00.000000 - WARNING - Low disk space\n"
        log_file_path = self._create_temp_log_file("log3.txt", content)
        df = task_func(log_file_path)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Level"], "WARNING")
    def test_caes_4(self):
        # Test case to ensure FileNotFoundError is raised when log file does not exist
        with self.assertRaises(FileNotFoundError):
            task_func("/path/to/nonexistent/file.txt")
    def test_case_5(self):
        # Log file with some entries having minor formatting issues
        content = (
            "2023-01-03 14:00:00.000000 - DEBUG - Debugging info included\n"
            "2023-01-03 Not a valid entry\n"
            "WARNING - This log entry is missing its timestamp\n"
            "2023-01-04 15:00:00.000000 - INFO - System update completed\n"
            "Some random text not conforming to the log format\n"
            "2023-01-04 16:00:00.000000 - ERROR - Error in processing\n"
        )
        log_file_path = self._create_temp_log_file("log5.txt", content)
        df = task_func(log_file_path)
        self.assertEqual(len(df), 3)
        self.assertEqual(df.iloc[0]["Level"], "DEBUG")
        self.assertEqual(df.iloc[1]["Level"], "INFO")
        self.assertEqual(df.iloc[2]["Level"], "ERROR")
    def test_case_6(self):
        # Log file with multi-line entries
        content = (
            "2023-02-01 10:00:00.000000 - INFO - Application start successful\n"
            "2023-02-01 10:05:00.000000 - ERROR - Exception occurred:\n"
            "Traceback (most recent call last):\n"
            '  File "<stdin>", line 1, in <module>\n'
            "ZeroDivisionError: division by zero\n"
            "2023-02-01 10:10:00.000000 - INFO - Recovery attempt initiated\n"
        )
        log_file_path = self._create_temp_log_file("log6.txt", content)
        df = task_func(log_file_path)
        self.assertEqual(len(df), 3)
        self.assertEqual(df.iloc[0]["Level"], "INFO")
        self.assertEqual(df.iloc[1]["Level"], "ERROR")
        self.assertEqual(df.iloc[2]["Level"], "INFO")
        self.assertTrue("Exception occurred:" in df.iloc[1]["Message"])
        self.assertFalse(
            "Traceback" in df.iloc[1]["Message"]
            or "ZeroDivisionError" in df.iloc[1]["Message"]
        )
