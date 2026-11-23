import pandas as pd
from random import seed, choices

def task_func(L, num_dataframes=5, random_seed=None):
    """
    Generate a specified number of Pandas DataFrames from a list of lists "L".
    Each DataFrame has the same column names randomly chosen from lowercase English
    letters and 3 rows sampled from 'L'. Then, find the common
    rows between all generated DataFrames.

    If L is empty, an empty dataframe is returend.

    Parameters:
    L (list of lists): Input list of lists to be used as rows in the DataFrame.
    num_dataframes (int, optional): Number of DataFrames to generate. Defaults to 5.
    random_seed (int, optional): Seed for the random number generator for reproducibility. Defaults to None

    Returns:
    DataFrame: A pandas DataFrame with the common rows between all generated DataFrames.
    list of DataFrame: A list of all generated DataFrames.
    

    Requirements:
    - pandas
    - random

    Example:
    >>> L = [['14', '65', 76], ['2', '5', 6], ['7', '12', 33], ['14', '22', 46]]
    >>> common_rows, df_list = task_func(L, num_dataframes=3, random_seed=123)
    >>> print(common_rows)
        b   c   k
    0  14  65  76
    1  14  22  46
    4   2   5   6
    >>> print(df_list)
    [    b   c   k
    0  14  65  76
    1  14  22  46
    2  14  65  76,     b   c   k
    0   7  12  33
    1   2   5   6
    2  14  22  46,     b   c   k
    0  14  65  76
    1   2   5   6
    2   2   5   6]

    >>> L = [[1, '65', 76], [2, '5', 6]]
    >>> common_rows, df_list = task_func(L, num_dataframes=1, random_seed=1)
    >>> print(common_rows)
       d   w   t
    0  1  65  76
    >>> print(df_list)
    [   d   w   t
    0  1  65  76
    1  1  65  76
    2  1  65  76]
    """
    if random_seed is not None:
        seed(random_seed)

    if len(L) == 0:
        return pd.DataFrame(), []

    LETTERS = list('abcdefghijklmnopqrstuvwxyz')
    max_cols = min(len(LETTERS), len(L[0]))
    col_names = choices(LETTERS, k=max_cols)
    dataframes = []

    for _ in range(num_dataframes):
        # Randomly sample rows from L for each DataFrame
        sampled_rows = choices(L, k=3)
        dataframe = pd.DataFrame(sampled_rows, columns=col_names)
        dataframes.append(dataframe)

    # Finding common rows across all DataFrames
    # Concatenate all DataFrames and find common rows
    combined_df = pd.concat(dataframes, ignore_index=True)
    common_rows = combined_df[combined_df.duplicated(keep=False)]

    return common_rows.drop_duplicates(), dataframes
