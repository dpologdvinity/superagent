import pandas as pd
import time


def task_func(df, target_value):
    '''
    Convert the input dic of list to DataFrame and searcher in this DataFrame for rows with cells equal to the
    provided target_value. It then plots the count of such rows per column.

    Parameters:
    - df (dic of list): The input dict. It should have a 'Name' key.
    - target_value (str): The target value to be searched in the DataFrame.

    Returns:
    tuple: A tuple containing:
        - A pandas Series with counts of the target value per column.
        - A matplotlib Axes object representing the plot (None if dataframe is empty).

    Requirements:
    - pandas
    - time

    Example:
    >>> df = {'Column1': ['0', 'a', '332', '33']}
    >>> series, ax = task_func(df, '332')
    '''
    start_time = time.time()
    # Convert dataframe to string type for uniform comparison
    dataframe = pd.DataFrame(df)
    dataframe = dataframe.astype(str)
    
    counts = dataframe.apply(lambda x: (x == target_value).sum())

    # Check if DataFrame is empty
    if not dataframe.empty:
        ax = counts.plot(kind='bar')
    else:
        ax = None
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return counts, ax
