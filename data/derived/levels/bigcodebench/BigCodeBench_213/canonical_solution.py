import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis


def task_func(intervals=100, seed=0):
    """
    Generates a series of random numbers over a specified number of intervals with a delay of 1 second between 
    each interval. It then plots these numbers as a function of elapsed time and returns the Axes object along
    with the kurtosis value of the generated numbers.
    
    Parameters:
    - intervals (int, optional): Number of intervals for generating random numbers. Default is 100.

    Returns:
    - matplotlib.axes.Axes: The Axes object representing the plot.
    - float: The kurtosis value of the generated numbers.

    Requirements:
    - time
    - random
    - matplotlib.pyplot

    Example:
    >>> ax, kurtosis = task_func(5)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    random.seed(seed)
    times = []
    numbers = []

    try:
        for _ in range(intervals):
            time.sleep(1)
            times.append(time.time())
            numbers.append(random.random())
    except KeyboardInterrupt:
        print('Interrupted by user')

    kurtosis_value = kurtosis(numbers, nan_policy='omit')
    # Initialize a fresh figure
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(times, numbers)
    return ax, kurtosis_value
