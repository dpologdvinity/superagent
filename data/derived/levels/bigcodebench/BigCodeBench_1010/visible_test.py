from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
from PIL import Image
from pathlib import Path
import shutil
import os

class TestCases(unittest.TestCase):
    """Test cases for task_func function."""
    directory = 'mnt/data/f_852_data'

    def setUp(self):
        """Setup method to create a sample image inr test files."""
        self.test_dir = Path(self.directory)
        self.test_dir.mkdir(parents=True, exist_ok=True)
        self.sample_image_path = Path(self.test_dir) / 'sample_image.png'
        sample_image = Image.new('RGBA', (100, 100), color='blue')
        sample_image.save(self.sample_image_path)

    @patch('requests.get')
    def test_valid_image_url(self, mock_get):
        """Test task_func function with a valid image URL."""
        with open(self.sample_image_path, 'rb') as image_file:
            mock_get.return_value.content = image_file.read()
        img = task_func('https://www.google.com/images/srpr/logo11w.png')
        self.assertIsInstance(img, Image.Image, 'Returned object is not a PIL Image')

    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        """Test task_func function with an invalid URL (not an image)."""
        mock_get.side_effect = ValueError('Invalid URL')
        with self.assertRaises(ValueError):
            task_func('https://www.google.com')

    @patch('requests.get')
    def test_nonexistent_url(self, mock_get):
        """Test task_func function with a nonexistent URL."""
        mock_get.side_effect = ValueError('Nonexistent URL')
        with self.assertRaises(ValueError):
            task_func('https://example.com/nonexistent_image.jpg')

    def tearDown(self):
        dirs_to_remove = ['mnt/data', 'mnt']
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
