import pickle

import os

from sklearn.datasets import make_classification

FILE_NAME = 'save.pkl'

DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def task_func(data, target):
    # TODO: implement this function.
    pass
