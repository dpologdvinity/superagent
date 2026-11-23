from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from faker import Faker

class TestCases(unittest.TestCase):
    faker = Faker()
    faker.seed_instance(42)

    def generate_objects(self, count):

        class TestObject:

            def __init__(self, value):
                self.value = value
        return [TestObject(self.faker.random_int(min=1, max=100)) for _ in range(count)]

    def test_case_1(self):
        obj_list = self.generate_objects(10)
        result, rand = task_func(obj_list, 'value', 5, seed=12)
        self.assertEqual(result, [95, 95, 82, 36, 32])
        self.assertEqual(rand, 18)

    def test_case_2(self):
        obj_list = self.generate_objects(50)
        result, rand = task_func(obj_list, 'value', 7, seed=1)
        self.assertEqual(result, [98, 98, 95, 94, 92, 90, 90])
        self.assertEqual(rand, 12)

    def test_case_3(self):
        obj_list = []
        result, rand = task_func(obj_list, 'value', 5, seed=2)
        self.assertEqual(result, [])
        self.assertEqual(rand, None)
