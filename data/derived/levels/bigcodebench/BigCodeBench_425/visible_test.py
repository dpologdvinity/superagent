from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
from PIL import Image, ImageDraw
import matplotlib

def create_dummy_image(image_path='test_image.jpg', size=(20, 20)):
    """
    Creates a dummy grayscale image for testing.
    The image size is 20x20 pixels.
    """
    img = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, 6, 6], fill='black')
    draw.line([2, 15, 18, 15], fill='black', width=1)
    img.save(image_path)

class TestCases(unittest.TestCase):

    def setUp(self):
        create_dummy_image()

    def tearDown(self):
        os.remove('test_image.jpg')
        if os.path.exists('histogram.png'):
            os.remove('histogram.png')

    def test_normal_functionality(self):
        histogram_axes = task_func('test_image.jpg', 'histogram.png')
        self.assertTrue(os.path.exists('histogram.png'))
        self.assertIsInstance(histogram_axes, matplotlib.axes.Axes)
        self.assertEqual(histogram_axes.title.get_text(), 'Grayscale Histogram')

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent.jpg')

    def test_histogram_labels(self):
        histogram_axes = task_func('test_image.jpg')
        self.assertEqual(histogram_axes.get_xlabel(), 'Bins')
        self.assertEqual(histogram_axes.get_ylabel(), '# of Pixels')
