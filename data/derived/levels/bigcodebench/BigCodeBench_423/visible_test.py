from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
from PIL import Image, ImageDraw

def create_dummy_image(image_path='test_image.jpg', size=(20, 20)):
    """
    Creates a dummy grayscale image for testing.
    The image size is 20x20 pixels.
    """
    img = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([5, 5, 15, 15], fill='black')
    img.save(image_path)

class TestCases(unittest.TestCase):

    def setUp(self):
        create_dummy_image()

    def tearDown(self):
        os.remove('test_image.jpg')

    def test_normal_functionality(self):
        original_img, binary_img = task_func('test_image.jpg', 10)
        self.assertIsInstance(original_img, np.ndarray)
        self.assertIsInstance(binary_img, np.ndarray)
        self.assertEqual(binary_img.max(), 255)
        self.assertEqual(binary_img.min(), 0)

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent.jpg')

    def test_invalid_threshold_non_integer(self):
        with self.assertRaises(ValueError):
            task_func('test_image.jpg', 'invalid')
