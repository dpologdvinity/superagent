import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Filters data in a specific date range from a column in an Excel file and returns a Pandas DataFrame of the filtered data.

    Parameters:
    excel_directory (str): The directory of the Excel file.
    file_name (str): The name of the Excel file.
    column_name (str): The name of the date column to filter.
    start_date (str): The start date in 'yyyy-mm-dd' format.
    end_date (str): The end date in 'yyyy-mm-dd' format.

    Returns:
    pd.DataFrame: A pandas DataFrame with the filtered data.

    Raises:
    FileNotFoundError: If the specified Excel file does not exist.
    ValueError: If start_date or end_date are in an incorrect format, or if column_name does not exist in the DataFrame.

    Example:
    >>> data_dir, file_name = './excel_files/', 'excel_file1.xls'
    >>> test_file = create_dummy_file(data_dir, file_name)
    >>> filtered_df = task_func(data_dir, file_name, 'Date', '2020-01-01', '2020-12-31')
    >>> os.remove(test_file)
    >>> os.rmdir(data_dir)
    >>> print(filtered_df.head())
       Unnamed: 0       Date     Value
    0           0 2020-01-01  0.823110
    1           1 2020-01-02  0.026118
    2           2 2020-01-03  0.210771
    3           3 2020-01-04  0.618422
    4           4 2020-01-05  0.098284
    
    Requirements:
    - os
    - pandas
    - datetime
    """
    excel_file = os.path.join(excel_directory, file_name)
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"The file {excel_file} does not exist.")

    df = pd.read_excel(excel_file, engine='openpyxl')

    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame.")

    try:
        df[column_name] = pd.to_datetime(df[column_name])
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Date format is incorrect. Please use 'yyyy-mm-dd' format.") from e

    filtered_df = df[(df[column_name] >= start_date) & (df[column_name] <= end_date)]

    return filtered_df
