from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from PIL import Image, ImageDraw

def create_dummy_image(image_path='test_image.jpg', size=(20, 20)):
    """
    Creates a dummy grayscale image with basic shapes for testing.
    The image size is 20x20 pixels.
    """
    img = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, 6, 6], fill='black')
    draw.ellipse([10, 2, 14, 6], fill='gray')
    draw.line([2, 15, 18, 15], fill='black', width=1)
    img.save(image_path)

class TestCases(unittest.TestCase):

    def setUp(self):
        create_dummy_image()

    def tearDown(self):
        os.remove('test_image.jpg')
        if os.path.exists('binary_image.jpg'):
            os.remove('binary_image.jpg')

    def test_normal_functionality(self):
        original_img, binary_img = task_func('test_image.jpg', 126)
        self.assertTrue(os.path.exists('binary_image.jpg'))
        self.assertIsInstance(original_img, np.ndarray)
        self.assertIsInstance(binary_img, np.ndarray)
        self.assertEqual(original_img.shape, (20, 20))
        self.assertEqual(binary_img.shape, (20, 20))
        unique_values = np.unique(binary_img)
        self.assertTrue(np.array_equal(unique_values, [0, 255]))

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent.jpg')

    def test_invalid_threshold_non_integer(self):
        with self.assertRaises(ValueError):
            task_func('test_image.jpg', 'invalid')
