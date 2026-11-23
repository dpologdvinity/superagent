import pandas as pd
import os
import sys

def task_func(file_path: str, column_name: str) -> pd.DataFrame:
    """
    Load a CSV file into a Pandas DataFrame, replace all occurrences of the string '\n' with the string '<br>'
    in the specified column, and return the cleaned DataFrame.
    
    Parameters:
    - file_path (str): The path to the CSV file to be read.
    - column_name (str): The name of the column in which to replace occurrences of '\n' with '<br>'.
    
    Returns:
    - pd.DataFrame: The cleaned Pandas DataFrame.
    
    Requirements:
    - pandas
    - os
    - sys
    
    Examples:
    >>> df = task_func('data.csv', 'Value')
    >>> print(df['Value'].iloc[0])
    "some<br>text"
    >>> df = task_func('another_data.csv', 'Comments')
    >>> print(df['Comments'].iloc[1])
    "hello<br>world"
    """
    if not os.path.exists(file_path):
        print(f'File does not exist: {file_path}')
        sys.exit(1)

    df = pd.read_csv(file_path)
    
    # Check if the column exists
    if column_name in df.columns:
        df[column_name] = df[column_name].replace({'\n': '<br>'}, regex=True)
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame. No changes were made.")

    return df
