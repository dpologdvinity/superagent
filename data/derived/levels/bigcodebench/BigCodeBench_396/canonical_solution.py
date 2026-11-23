import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def task_func(mu, sigma, sample_size, seed=0):
    """
    Create a Gaussian kernel density estimate diagram of a normal distribution with a given mean and a 
    standard deviation using a random sample of a size determined by the sample_size parameter. The density 
    diagram is plotted using default settings in a deterministic matplotlib plot. Return the axes object.
    
    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    sample_size (int): The size of the sample to generate. Must be a positive integer.
    seed (int, Optional): The seed to be used for the random number generator. Default is 0.
    
    Returns:
    matplotlib.axes._axes.Axes: Axes object containing the plot of the normal distribution.
    
    Requirements:
    - numpy
    - matplotlib
    - scipy.stats
    
    Example:
    >>> ax = task_func(0, 1, 1000)
    >>> type(ax) # The result should be a matplotlib.axes._axes.Axes object
    <class 'matplotlib.axes._axes.Axes'>
    """
    if sample_size <= 0:
        raise ValueError('sample_size must be a positive integer.')

    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    density = stats.gaussian_kde(sample)

    x = np.linspace(min(sample), max(sample), sample_size)
    fig, ax = plt.subplots()
    ax.plot(x, density(x))
    
    return ax
