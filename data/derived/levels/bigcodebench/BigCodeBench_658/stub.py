import re

import nltk

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

nltk.download('stopwords')

ALPHANUMERIC = re.compile('[\\W_]+')

STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(texts):
    # TODO: implement this function.
    pass
