import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    """
    Analyze and visualize statistical properties of a specified weather data column.

    This function calculates the sum, mean, minimum, and maximum values of a specified column in the given data.
    It also generates a histogram plot of the data in the column. The dataset is expected to be a list of weather
    observations, where each observation includes date, temperature, humidity, wind speed, and precipitation values.
    If the provided data list is empty, resulting in an empty DataFrame, the function handles it by setting:
    - The 'mean' value to np.nan.
    - The 'min' value to np.inf.
    - The 'max' value to -np.inf.

    Parameters:
    column (str): The column to analyze. Valid columns include 'Temperature', 'Humidity', 'Wind Speed', and 'Precipitation'.
    data (list of lists): The weather data where each inner list contains the following format:
                          [Date (datetime object), Temperature (int), Humidity (int), Wind Speed (int), Precipitation (float)]

    Returns:
    - result (dict): A dictionary containing:
        - 'sum': Sum of the values in the specified column.
        - 'mean': Mean of the values in the specified column.
        - 'min': Minimum value in the specified column.
        - 'max': Maximum value in the specified column.
        - 'plot': A matplotlib BarContainer object of the histogram plot for the specified column.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot

    Example:
    >>> data = [[datetime(2022, 1, 1), -5, 80, 10, 0], [datetime(2022, 1, 3), -2, 83, 15, 0]]
    >>> result = task_func('Temperature', data)
    >>> result['sum']
    -7
    >>> type(result['plot'])
    <class 'matplotlib.container.BarContainer'>
    """
    COLUMNS = ["Date", "Temperature", "Humidity", "Wind Speed", "Precipitation"]
    df = pd.DataFrame(data, columns=COLUMNS)
    column_data = df[column]

    result = {
        "sum": np.sum(column_data),
        "mean": np.nan if df.empty else np.mean(column_data),
        "min": np.inf if df.empty else np.min(column_data),
        "max": -np.inf if df.empty else np.max(column_data),
    }

    _, _, ax = plt.hist(column_data)
    plt.title(f"Histogram of {column}")

    result["plot"] = ax

    return result
