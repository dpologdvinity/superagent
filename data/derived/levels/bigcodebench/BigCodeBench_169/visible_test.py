from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from skimage import data
import numpy as np

class TestCases(unittest.TestCase):

    def test_return_types(self):
        image = data.coins()
        ax, filtered_image = task_func(image)
        self.assertIsInstance(ax, np.ndarray, 'ax is not a numpy array')
        self.assertIsInstance(filtered_image, np.ndarray, 'filtered_image is not a numpy array')

    def test_error_on_non_positive_sigma(self):
        image = data.coins()
        with self.assertRaises(ValueError):
            task_func(image, sigma=0)

    def test_error_on_invalid_image_type(self):
        invalid_image = 'not an image'
        with self.assertRaises(TypeError):
            task_func(invalid_image)
