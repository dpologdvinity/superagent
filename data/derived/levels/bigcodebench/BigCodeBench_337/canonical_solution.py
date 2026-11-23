import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.

    Parameters:
    - df (DataFrame): The input DataFrame containing the data.
    - group_col (str): The name of the column to group the data by.
    - value_col (str): The name of the column containing the values to plot.

    Returns:
    - Axes: A matplotlib axes object with the bar chart.

    Requirements:
    - matplotlib.pyplot
    - numpy

    Example:
    >>> import matplotlib.pyplot as plt
    >>> import pandas as pd
    >>> df = pd.DataFrame({'Group': ['A', 'B', 'A', 'B', 'A', 'B'], 'Value': [1, 2, 3, 4, 5, 6]})
    >>> ax = task_func(df, 'Group', 'Value')
    >>> len(ax.patches)
    2
    >>> plt.close()

    Note:
    - The function uses a predefined set of colors for the bars. If there are more groups than colors,
      the colors will repeat from the beginning of the COLORS list.
    - This function use "Bar chart of {value_col} by {group_col}" for the plot title.
    - This function use value of variables group_col and value_col as the xlabel and ylabel respectively.

    Raises:
    -This function will raise TypeError if the 'Value' has non-numeric values.
    """

    group_mean = df.groupby(group_col)[value_col].mean()
    group_std = df.groupby(group_col)[value_col].std()

    # Get the number of groups and generate x locations for the bars
    num_groups = len(group_mean)
    index = np.arange(num_groups)

    # Create the bar chart with error bars
    for i, (mean, std) in enumerate(zip(group_mean, group_std)):
        plt.bar(index[i], mean, yerr=std, color=COLORS[i % len(COLORS)], capsize=4, label=f'Group {i+1}')

    # Set labels and title
    plt.xlabel(group_col)
    plt.ylabel(value_col)
    plt.title(f'Bar chart of {value_col} by {group_col}')
    plt.xticks(index, group_mean.index)  # Set x-axis labels to group names
    plt.legend()
    # Return the axes object
    return plt.gca()
