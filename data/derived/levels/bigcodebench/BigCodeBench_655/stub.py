import re

import nltk

from sklearn.decomposition import NMF

from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

ALPHANUMERIC = re.compile('[\\W_]+')

STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(texts, num_topics):
    # TODO: implement this function.
    pass
