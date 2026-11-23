from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import doctest
import unittest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f'{self.base_tmp_dir}/test'
        if not os.path.exists(self.test_directory):
            os.makedirs(self.test_directory)
        self.test_files = ['file_with_like.txt', 'another_file_with_what.doc', 'file_without_keywords.jpg', 'LIKE_in_caps.pdf', 'hidden_what_in_name.whatever', 'no_keyword.png']
        for file in self.test_files:
            with open(os.path.join(self.test_directory, file), 'w') as f:
                f.write('Dummy content for testing.')
        if os.path.exists(os.path.join(self.test_directory, 'Interesting Files')):
            shutil.rmtree(os.path.join(self.test_directory, 'Interesting Files'))

    def tearDown(self):
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)

    def test_caae_1(self):
        """Test if only files with 'like' or 'what' in their names are moved."""
        expected_files = ['file_with_like.txt', 'another_file_with_what.doc', 'LIKE_in_caps.pdf', 'hidden_what_in_name.whatever']
        moved_files = task_func(self.test_directory)
        self.assertCountEqual(moved_files, expected_files)

    def test_caae_2(self):
        """Test if 'Interesting Files' directory is created."""
        task_func(self.test_directory)
        self.assertTrue(os.path.exists(os.path.join(self.test_directory, 'Interesting Files')))

    def test_caae_3(self):
        """Test that files without 'like' or 'what' in their names are not moved."""
        task_func(self.test_directory)
        remaining_files = os.listdir(self.test_directory)
        expected_remaining = ['file_without_keywords.jpg', 'no_keyword.png']
        self.assertCountEqual(remaining_files, expected_remaining + ['Interesting Files'])
