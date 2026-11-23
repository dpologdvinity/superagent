from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ip_address = json.dumps({'ip': '192.168.1.1'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '192.168.1.1')
    def test_case_2(self):
        ip_address = json.dumps({'ip': '500.500.500.500'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '500.500.500.500')
    def test_case_3(self):
        ip_address = json.dumps({'ip': '192.168.0.3'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '192.168.0.3')
    def test_case_4(self):
        ip_address = json.dumps({'ip': ''}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, 'Invalid IP address received')
    def test_case_5(self):
        ip_address = json.dumps({'ip': 'Non-JSON response'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, 'Invalid IP address received')
