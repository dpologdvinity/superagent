import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def task_func(x, y, labels):
    """ 
    Perform Principal Component Analysis (PCA) on "x" as x-values and "y" as y-values and record the results with labels.

    Parameters:
    x (list): List of numpy arrays representing the x-values of the data points.
    y (list): List of numpy arrays representing the y-values of the data points.
    labels (list): List of strings representing the labels for the chemical compounds.

    Returns:
    fig: Matplotlib figure object.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - sklearn.decomposition

    Example:
    >>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['H₂O', 'O₂', 'CO₂']
    >>> fig = task_func(x, y, labels)
    """
    pca = PCA(n_components=2)

    fig, ax = plt.subplots()

    for i in range(len(x)):
        xy = np.vstack((x[i], y[i])).T
        xy_transformed = pca.fit_transform(xy)
        ax.plot(xy_transformed[:, 0], xy_transformed[:, 1], label=labels[i])
    
    ax.legend()
    
    return fig
