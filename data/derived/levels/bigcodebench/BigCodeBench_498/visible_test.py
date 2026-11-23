from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        self.json_file_path = 'test_output.json'

    def tearDown(self):
        if os.path.exists(self.json_file_path):
            os.remove(self.json_file_path)

    def test_simple_xml_to_dict(self):
        xml_str = '<person><name>John</name><age>30</age></person>'
        result = task_func(xml_str, False, '')
        self.assertEqual(result['person']['name'], 'John')
        self.assertEqual(result['person']['age'], '30')

    def test_nested_xml_to_dict(self):
        xml_str = '<school><class><student>Emma</student></class></school>'
        result = task_func(xml_str, False, '')
        self.assertEqual(result['school']['class']['student'], 'Emma')

    def test_empty_xml_to_dict(self):
        xml_str = '<empty></empty>'
        result = task_func(xml_str, False, '')
        self.assertTrue('empty' in result and result['empty'] is None or result['empty'] == '')
