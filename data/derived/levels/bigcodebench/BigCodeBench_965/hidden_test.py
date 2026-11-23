from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import os
class TestCases(unittest.TestCase):
    def create_test_files(self, directory, file_names):
        # Helper to create files for testing
        for file_name in file_names:
            with open(os.path.join(directory, file_name), "a") as file:
                file.write("test content")
    def test_files_moved(self):
        # Test basic case with default pattern
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dst:
            self.create_test_files(
                src,
                [
                    "1234.txt",
                    "test5678.txt",
                    "nope.txt",
                    "another1234.txt",
                    "4321done.txt",
                ],
            )
            result = task_func(src, dst)
            self.assertEqual(
                result, 4, "Should move 4 files matching the default pattern."
            )
            for file_name in [
                "1234.txt",
                "another1234.txt",
                "4321done.txt",
                "test5678.txt",
            ]:
                self.assertTrue(
                    os.path.exists(os.path.join(dst, file_name)),
                    f"{file_name} should be in the target directory",
                )
    def test_files_moved_with_custom_pattern(self):
        # Test case with custom pattern
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dst:
            self.create_test_files(
                src,
                [
                    "1234.txt",
                    "test5678.txt",
                    "nope.txt",
                    "another1234.txt",
                    "4321done.txt",
                ],
            )
            result = task_func(src, dst, r"test\w+")
            self.assertEqual(
                result, 1, "Should move 1 file matching the custom pattern 'test\\w+.'"
            )
    def test_no_files_moved_if_no_match(self):
        # Test no match
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dst:
            self.create_test_files(src, ["nope.txt"])
            result = task_func(src, dst)
            self.assertEqual(result, 0, "Should move 0 files if no match.")
    def test_return_zero_if_source_does_not_exist(self):
        # Test source_directory if not exists
        with tempfile.TemporaryDirectory() as dst:
            result = task_func(os.path.join(dst, "non_existing_dir"), dst)
            self.assertEqual(
                result, 0, "Should return 0 if source directory does not exist."
            )
    def test_target_directory_created_if_not_exist(self):
        # Test that destination directory will be created if it did not exist
        with tempfile.TemporaryDirectory() as src:
            self.create_test_files(src, ["1234.txt"])
            new_target = os.path.join(src, "new_target_dir")
            task_func(src, new_target)
            self.assertTrue(
                os.path.exists(new_target),
                "Target directory should be created if it does not exist.",
            )
    def test_no_files_in_source(self):
        # Test empty source direcotry
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dst:
            result = task_func(src, dst)
            self.assertEqual(
                result, 0, "Should move 0 files if source directory is empty."
            )
