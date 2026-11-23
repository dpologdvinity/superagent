from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
import os
import shutil

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def setUp(self):
        if not os.path.exists(TARGET_DIR):
            os.makedirs(TARGET_DIR)
        if os.path.exists(TARGET_DIR):
            shutil.rmtree(TARGET_DIR)

    @patch('urllib.request.urlretrieve')
    @patch('zipfile.ZipFile')
    def test_valid_zip_file(self, mock_zipfile, mock_urlretrieve):
        """Test that the function returns the correct directory path."""
        url = 'https://www.sample-videos.com/zip/Sample-Zip-5mb.zip'
        mock_zipfile.return_value.__enter__.return_value = MagicMock()
        result = task_func(url)
        mock_urlretrieve.assert_called_with(url, TARGET_ZIP_FILE)
        self.assertEqual(result, TARGET_DIR)
        self.assertTrue(os.path.exists(TARGET_DIR))

    @patch('urllib.request.urlretrieve')
    def test_invalid_url(self, mock_urlretrieve):
        """Test that the function raises an exception when the URL is invalid."""
        mock_urlretrieve.side_effect = Exception
        url = 'https://invalid.url/invalid.zip'
        with self.assertRaises(Exception):
            task_func(url)

    @patch('urllib.request.urlretrieve')
    @patch('zipfile.ZipFile')
    def test_non_zip_file(self, mock_zipfile, mock_urlretrieve):
        """Test that the function raises an exception when the URL does not point to a zip file."""
        mock_zipfile.side_effect = zipfile.BadZipFile
        url = 'https://www.sample-videos.com/img/Sample-jpg-image-5mb.jpg'
        with self.assertRaises(zipfile.BadZipFile):
            task_func(url)

    def tearDown(self):
        if os.path.exists(TARGET_DIR):
            shutil.rmtree(TARGET_DIR)
