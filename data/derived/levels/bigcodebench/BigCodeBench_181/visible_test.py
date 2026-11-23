from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
import random
if not settings.configured:
    settings.configure(DEBUG=True)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        random.seed(0)
        data = json.dumps({'key': 'value'})
        response = task_func(data, 1, 2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'key': 'value'})

    def test_case_2(self):
        random.seed(0)
        data = json.dumps({'test': 'data', 'sample': 'value'})
        response = task_func(data, 0, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'test': 'data', 'sample': 'value'})

    def test_case_3(self):
        random.seed(0)
        data = json.dumps({'hello': 'world'})
        response = task_func(data, 1, 3)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'hello': 'world'})
