import re

import string

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

ALPHANUMERIC = re.compile('[\\W_]+')

PUNCTUATIONS = string.punctuation

def task_func(text, sia):
    # TODO: implement this function.
    pass
