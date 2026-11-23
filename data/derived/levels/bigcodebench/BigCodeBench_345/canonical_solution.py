import pandas as pd
import seaborn as sns

def task_func(df, col1, col2):
    """
    Draw a scatter plot with a regression line for two columns from a DataFrame.

    Parameters:
    df (DataFrame): Input DataFrame.
    col1 (str): Name of the first column.
    col2 (str): Name of the second column.

    Returns:
    Axes: A seaborn axes object.

    Requirements:
    - pandas
    - seaborn

    Raises:
    - Raise ValueError if the input df is not a DataFrame, empty, or does not contain the specified columns.
    - Raise TypeError if df use non-numeric data

    Example:
    >>> import matplotlib.pyplot as plt
    >>> df = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]})
    >>> plot = task_func(df, 'X', 'Y')
    >>> len(plot.collections[0].get_offsets().data)
    5
    >>> plt.close()
    """
    # Ensure that the df is DataFrame, not empty and the specified column exists
    if not isinstance(df, pd.DataFrame) or df.empty or col1 not in df.columns or col2 not in df.columns:
        raise ValueError("The DataFrame is empty or the specified column does not exist.")
    
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax
