import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    """
    Generates a histogram and a probability density function (PDF) plot for a specified normal distribution.

    This function draws n_samples from a normal distribution defined by mean (mu) and standard deviation (sigma),
    plots a histogram of the samples, and overlays the PDF of the normal distribution. The histogram's density
    is normalized, and the PDF is plotted with a red line with linewidth=2.

    Parameters:
    - n_samples (int): Number of samples for the histogram. Must be greater than 0. Default is 1000.
    - mu (float): Mean for the normal distribution. Default is 0.
    - sigma (float): Standard deviation for the normal distribution. Must be greater than 0. Default is 1.
    - random_seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    - ax (matplotlib.axes._axes.Axes): Axes object with the histogram and PDF plotted.
    - samples (numpy.ndarray): Generated sample data.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats.norm

    Example:
    >>> ax, samples = task_func()
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(-5.0, 0, '−5'), Text(-4.0, 0, '−4'), Text(-3.0, 0, '−3'), Text(-2.0, 0, '−2'), Text(-1.0, 0, '−1'), Text(0.0, 0, '0'), Text(1.0, 0, '1'), Text(2.0, 0, '2'), Text(3.0, 0, '3'), Text(4.0, 0, '4'), Text(5.0, 0, '5')]
    """
    if n_samples <= 0 or sigma <= 0:
        raise ValueError("Invalid n_samples or sigma")
    np.random.seed(random_seed)
    plt.figure()
    samples = np.random.normal(mu, sigma, n_samples)
    _, _, _ = plt.hist(samples, 30, density=True)
    ax = plt.gca()
    ax.plot(
        np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000),
        norm.pdf(np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000), mu, sigma),
        linewidth=2,
        color="r",
    )
    return ax, samples
