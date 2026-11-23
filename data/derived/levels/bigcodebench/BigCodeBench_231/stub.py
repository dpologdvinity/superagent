import numpy as np

import scipy.stats as stats

import matplotlib.pyplot as plt

import random

from matplotlib.axes import Axes

class ValueObject:
    value = 0

    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)

def task_func(obj_list):
    # TODO: implement this function.
    pass
