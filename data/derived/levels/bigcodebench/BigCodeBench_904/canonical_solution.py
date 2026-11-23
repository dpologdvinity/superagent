import pandas as pd
import matplotlib.pyplot as plt

def task_func(d, keys=['x', 'y', 'z']):
    """
    Plot values from a list of dictionaries based on specified keys and return the plot as a Matplotlib Axes object.
    
    Parameters:
    d (list): A list of dictionaries containing numerical data.
    keys (list, optional): A list of string keys to plot. Defaults to ['x', 'y', 'z'].

    Returns:
    Matplotlib Axes object: The plot showing the values of specified keys from the input list of dictionaries.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> ax = task_func(data)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>

    >>> ax = task_func(data, keys=['x', 'y'])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)

    # Initialize a plot
    fig, ax = plt.subplots()
    
    # Plot the values for the specified keys
    plotted_keys = []
    for key in keys:
        if key in df.columns:
            ax.plot(df[key], label=key)
            plotted_keys.append(key)
    
    # Add a legend if there are any lines plotted
    if plotted_keys:
        ax.legend()
    
    # Return the Axes object
    return ax
