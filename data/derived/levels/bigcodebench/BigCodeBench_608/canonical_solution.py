import seaborn as sns
from random import sample


# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random pairs of two columns 
    against each other to generate pairplots.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    tuples (list of tuple): A list of tuples, where each tuple represents a row to be removed based on its values.
    n_plots (int): The number of pairplots to be generated using randomly selected column pairs.

    Returns:
    tuple: A tuple containing:
        - DataFrame: The modified DataFrame after removing specified rows.
        - list of Axes: A list containing the generated pairplots.

    Requirements:
    - seaborn
    - random

    Example:
    >>> import numpy as np, pandas as pd
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = task_func(df, tuples, 3)
    """
    if not df.empty:
        df = df[~df.apply(tuple, axis=1).isin(tuples)]

    plots = []
    if n_plots > 0 and not df.empty:
        available_columns = df.columns.tolist()
        for _ in range(min(n_plots, len(available_columns) // 2)):  # Ensure we have enough columns
            # Randomly select two columns for pairplot
            selected_columns = sample(available_columns, 2)
            plot = sns.pairplot(df, vars=selected_columns)
            plots.append(plot)

    return df, plots
