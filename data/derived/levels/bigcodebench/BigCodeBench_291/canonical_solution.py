import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def task_func(mu, sigma, seed=0):
    """
    Draw a normal distribution using a 1000 samples, indicating the mean and standard deviation 
    with a color bar.
    
    Parameters:
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.
    
    Returns:
    matplotlib.axes._axes.Axes: The Axes object of the plotted distribution.
    
    Requirements:
    - matplotlib.pyplot
    - numpy
    - seaborn
    
    Example:
    >>> plot = task_func(0, 1)
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    """
    # Set the random seed
    np.random.seed(seed)
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, 1000)

    # Generate a KDE plot
    mappable = sns.kdeplot(samples, fill=True)

    # Add a colorbar to the plot
    plt.colorbar(mappable=mappable.collections[0])

    return mappable
