from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, Mock
import json
class TestCases(unittest.TestCase):
    def setUp(self):
        self.mock_response_with_multiple_repos = json.dumps([
        {"name": "Repo1", "created_at": "2021-01-01T00:00:00Z"},
        {"name": "Repo2", "created_at": "2021-01-02T00:00:00Z"}
    ])
        self.mock_response_with_single_repo = json.dumps([
        {"name": "SingleRepo", "created_at": "2021-01-01T00:00:00Z"}
    ])
        self.mock_response_with_no_repos = json.dumps([])
    @patch('requests.get')
    def test_case_1(self, mock_get):
        # Test if the function returns a list
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_multiple_repos)
        result = task_func('octocat')
        self.assertIsInstance(result, list, "The returned value should be a list.")
    @patch('requests.get')
    def test_case_2(self, mock_get):
        # Test for a user with multiple repositories
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_multiple_repos)
        result = task_func('octocat')
        self.assertTrue(len(result) > 1, "The user 'octocat' should have more than one repository.")
    @patch('requests.get')
    def test_case_3(self, mock_get):
        # Test for a user with no repositories
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_no_repos)
        result = task_func('dummyuserwithnorepos')
        self.assertEqual(len(result), 0, "The user 'dummyuserwithnorepos' should have zero repositories.")
    @patch('requests.get')
    def test_case_4(self, mock_get):
        # Test for a non-existent user
        mock_get.return_value = Mock(status_code=404, text=self.mock_response_with_no_repos)
        result = task_func('nonexistentuserxyz')
        self.assertEqual(len(result), 0, "A non-existent user should have zero repositories.")
    @patch('requests.get')
    def test_case_5(self, mock_get):
        # Test for a user with a single repository
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_single_repo)
        result = task_func('userwithonerepo')
        self.assertEqual(len(result), 1, "The user 'userwithonerepo' should have one repository.")
