from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from faker import Faker
fake = Faker()

def generate_mock_articles(num_articles=10):
    categories = ['Sports', 'Technology', 'Health', 'Science', 'Business']
    mock_articles = []
    for _ in range(num_articles):
        article = {'title': fake.sentence(), 'title_url': fake.slug(), 'id': fake.unique.random_int(min=1, max=1000), 'category': fake.random_element(elements=categories)}
        mock_articles.append(article)
    return mock_articles

class TestCases(unittest.TestCase):

    def test_wrong_keys(self):
        """wrong input"""
        input1 = [{}]
        input2 = {'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'Technology'}
        input3 = [{'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'Technology', 'test': 2}]
        input4 = [{'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'test': 'Technology'}]
        self.assertRaises(Exception, task_func, input1)
        self.assertRaises(Exception, task_func, input2)
        self.assertRaises(Exception, task_func, input3)
        self.assertRaises(Exception, task_func, input4)

    def test_case_1(self):
        """two categories"""
        articles = [{'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'science'}, {'title': 'Tech Crunch', 'title_url': 'Tech_Crunch', 'id': 3, 'category': 'science'}, {'title': 'Wired', 'title_url': 'Wired', 'id': 4, 'category': 'Technology'}]
        expected = {'Technology': [{'title': 'Wired', 'title_url': 'Wired', 'id': 4, 'category': 'Technology'}], 'science': [{'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'science'}, {'title': 'Tech Crunch', 'title_url': 'Tech_Crunch', 'id': 3, 'category': 'science'}]}
        sorted_articles = task_func(articles)
        self.assertIn('Technology', sorted_articles)
        self.assertIn('science', sorted_articles)
        self.assertCountEqual(sorted_articles['science'], expected['science'])
        self.assertCountEqual(sorted_articles['Technology'], expected['Technology'])

    def test_case_2(self):
        """test for correct count with one category"""
        articles = [{'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'Technology'}, {'title': 'Tech Crunch', 'title_url': 'Tech_Crunch', 'id': 3, 'category': 'Technology'}, {'title': 'Wired', 'title_url': 'Wired', 'id': 4, 'category': 'Technology'}]
        expected = {'Technology': [{'title': 'Wired', 'title_url': 'Wired', 'id': 4, 'category': 'Technology'}, {'title': 'Apple News', 'title_url': 'Apple_News', 'id': 2, 'category': 'Technology'}, {'title': 'Tech Crunch', 'title_url': 'Tech_Crunch', 'id': 3, 'category': 'Technology'}]}
        sorted_articles = task_func(articles)
        self.assertCountEqual(sorted_articles['Technology'], expected['Technology'])
