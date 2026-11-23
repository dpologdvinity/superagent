from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def test_return_type(self):
        """Test if the return type is OrderedDict."""
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, collections.OrderedDict, 'Return type should be OrderedDict.')

    def test_length_of_return(self):
        """Test if the returned OrderedDict has the correct length."""
        random.seed(0)
        result = task_func(5)
        self.assertEqual(len(result), 5, 'Returned OrderedDict should have the same length as TEAMS.')

    def test_inclusion_of_teams(self):
        """Test if all predefined teams are included."""
        random.seed(0)
        result = task_func(5)
        TEAMS = []
        for i in range(1, 5 + 1):
            TEAMS.append('Team ' + str(i))
        self.assertTrue(all((team in result for team in TEAMS)), 'All predefined teams should be included in the result.')
