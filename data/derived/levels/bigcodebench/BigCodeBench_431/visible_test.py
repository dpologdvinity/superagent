from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import cv2

class TestCases(unittest.TestCase):

    def setUp(self):
        self.dummy_image_path = 'dummy_image.png'
        np.random.seed(48)
        dummy_image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
        cv2.imwrite(self.dummy_image_path, dummy_image)
        self.dummy_image_path_zero = 'dummy_image_zero.png'
        self.dummy_image_path_max = 'dummy_image_max.png'
        zero_image = np.zeros((10, 10), dtype=np.uint8)
        cv2.imwrite(self.dummy_image_path_zero, zero_image)
        max_image = np.full((10, 10), 255, dtype=np.uint8)
        cv2.imwrite(self.dummy_image_path_max, max_image)

    def tearDown(self):
        os.remove(self.dummy_image_path)
        os.remove(self.dummy_image_path_zero)
        os.remove(self.dummy_image_path_max)

    def test_histogram_output(self):
        histogram = task_func(self.dummy_image_path)
        with open('df_contents.txt', 'w') as file:
            file.write(str(histogram.tolist()))
        self.assertEqual(histogram.shape, (256,))
        self.assertTrue(np.all(histogram >= 0))
        expect = [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 3, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 3, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 2, 1, 1, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(histogram.tolist(), expect, 'DataFrame contents should match the expected output')

    def test_nonexistent_image_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent_image.png')

    def test_invalid_image_file(self):
        with open('invalid_image.txt', 'w') as file:
            file.write('This is not an image file.')
        with self.assertRaises(ValueError):
            task_func('invalid_image.txt')
        os.remove('invalid_image.txt')
