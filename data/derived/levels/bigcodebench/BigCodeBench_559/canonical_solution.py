import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt


def task_func(a, b):
    """
    Calculate the Euclidean distance between two lists, create a Pandas DataFrame from these lists
    with indices 'A' and 'B', and then draw the values with a line displaying the Euclidean distance.

    Parameters:
    a (list): A list of numbers.
    b (list): Another list of numbers.

    Returns:
    float: The computed Euclidean distance between the two lists.
    pd.DataFrame: A DataFrame containing the two lists as columns.
    matplotlib.axes.Axes: The generated plot's Axes object.

    Requirements:
    - pandas
    - scipy.spatial
    - matplotlib.pyplot

    Example:
    >>> euclidean_distance, df, ax = task_func([1, 2, 3], [2, 3, 4])
    >>> print(euclidean_distance)
    1.7320508075688772
    """
    # Calculate the Euclidean distance
    euclidean_distance = distance.euclidean(a, b)

    # Create a DataFrame
    df = pd.DataFrame({'A': a, 'B': b})

    # Plot the values
    fig, ax = plt.subplots()
    ax.plot(df['A'], df['B'])
    ax.plot([df['A'].iloc[0], df['B'].iloc[0]], [df['A'].iloc[-1], df['B'].iloc[-1]], 'ro-')
    
    return euclidean_distance, df, ax
