import pandas as pd
import os

def task_func(filename):
    """
    Read a CSV file of pandas, reverse the order of the lines and write the inverted lines back into the file. Then move the cursor back to the beginning of the file. 
    The header should not be inverted and the file may be empty.

    Parameters:
    - filename (str): The name of the CSV file.

    Returns:
    - filename (str): The name of the CSV file.

    Requirements:
    - os
    - pandas

    Example:
    >>> task_func('file.csv')
    'file.csv'
    """
    if not os.path.exists(filename):
        return filename

    # Check if empty
    with open(filename, 'r') as file:
        if not file.read(1):
            return filename

    df = pd.read_csv(filename)
    df = df.iloc[::-1]
    df.to_csv(filename, index=False)

    with open(filename, 'r+') as file:
        file.seek(0)

    return filename
