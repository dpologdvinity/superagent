from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
import doctest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        sample_data = {'data1.json': {'text1': 'This is a (sample) text with some (matches) and characters.', 'text2': 'Another (example) with multiple matches.'}, 'data2.json': {'text1': '(Hello) world!', 'text2': 'No matches here.'}, 'data3.json': {'text1': 'Testing (with) another (file).', 'text2': 'Just some (random) text.'}, 'data4.json': {'text1': '(A) quick brown (fox) jumps.', 'text2': 'Over the lazy (dog).'}, 'data5.json': {'text1': 'Yet (another) test file.', 'text2': 'With (various) matches.'}}
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_data_dir = f'{self.base_tmp_dir}/test/'
        if not os.path.exists(self.test_data_dir):
            os.makedirs(self.test_data_dir)
        for filename, content in sample_data.items():
            with open(os.path.join(self.test_data_dir, filename), 'w') as file:
                json.dump(content, file)

    def tearDown(self):
        shutil.rmtree(self.test_data_dir)

    def test_case_1(self):
        matches = task_func(os.path.join(self.test_data_dir, 'data1.json'))
        expected = {'data1.json': ['T', 'h', 'i', 's', 'i', 's', 'a', '(sample)', 't', 'e', 'x', 't', 'w', 'i', 't', 'h', 's', 'o', 'm', 'e', '(matches)', 'a', 'n', 'd', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's', 'A', 'n', 'o', 't', 'h', 'e', 'r', '(example)', 'w', 'i', 't', 'h', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', 'm', 'a', 't', 'c', 'h', 'e', 's']}
        self.assertEqual(matches, expected)

    def test_case_2(self):
        matches = task_func(os.path.join(self.test_data_dir, 'data2.json'))
        expected = {'data2.json': ['(Hello)', 'w', 'o', 'r', 'l', 'd', 'N', 'o', 'm', 'a', 't', 'c', 'h', 'e', 's', 'h', 'e', 'r', 'e']}
        self.assertEqual(matches, expected)

    def test_case_3(self):
        matches = task_func(os.path.join(self.test_data_dir, 'data3.json'))
        expected = {'data3.json': ['T', 'e', 's', 't', 'i', 'n', 'g', '(with)', 'a', 'n', 'o', 't', 'h', 'e', 'r', '(file)', 'J', 'u', 's', 't', 's', 'o', 'm', 'e', '(random)', 't', 'e', 'x', 't']}
        self.assertEqual(matches, expected)
