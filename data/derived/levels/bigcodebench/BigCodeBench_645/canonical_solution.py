import os
import pandas as pd


def task_func(filename: str) -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame and then delete the entire contents of the original file.

    Parameters:
    - filename (str): The name of the CSV file to read and erase.

    Returns:
    - DataFrame: The contents of the CSV file as a pandas DataFrame.

    Raises:
    - FileNotFoundError: If the CSV file does not exist.

    Requirements:
    - os
    - pandas

    Example:
    >>> import os
    >>> from unittest.mock import patch
    >>> with patch('os.path.exists', return_value=False):
    ...     task_func('nonexistent.csv')
    Traceback (most recent call last):
        ...
    FileNotFoundError: No such file: 'nonexistent.csv'
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"No such file: '{filename}'")

    if os.stat(filename).st_size == 0:
        # File is empty, return an empty DataFrame with no columns.
        return pd.DataFrame()

    df = pd.read_csv(filename)

    # Erase the original file's content using a context manager to handle the file properly
    with open(filename, 'w') as file:
        file.truncate()

    return df
