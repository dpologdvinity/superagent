import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt


def task_func(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    
    Parameters:
    data (list of tuple): A list of tuples where each tuple contains two integers.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot for further manipulation and testing, with the title 'Max Tuple Highlighted', x-axis labeled 'x', y-axis labeled 'y', and a legend.
    
    Requirements:
    - numpy
    - operator
    - matplotlib.pyplot
    
    Example:
    >>> ax = task_func([(10, 20), (30, 40), (25, 50)])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    max_tuple = max(data, key=itemgetter(1))
    tuples = np.array(data)
    x = tuples[:,0]
    y = tuples[:,1]
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data')
    ax.scatter(*max_tuple, color='red', label='Max Tuple')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Max Tuple Highlighted')
    ax.legend()
    return ax
