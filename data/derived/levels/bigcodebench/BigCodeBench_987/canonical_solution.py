import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def task_func(json_data: str, data_key: str):
    """
    Processes a JSON string to extract numerical data, Min-Max normalize them,
    and generate a line plot.

    Parameters:
    - json_data (str): JSON formatted string containing the data.
    - data_key (str): Dot-separated full key path to access the numerical data within the JSON structure.

    Returns:
    - Tuple:
      - pd.Series: Original dataset in float64.
      - pd.Series or None: Dataset after Min-Max scaling in float64, or None if data is empty.
      - plt.Axes or None: Line plot of normalized data, or None if data is empty.

    Raises:
    - KeyError: if key path is not found in the given data.

    Requirements:
    - json
    - pandas
    - sklearn
    - matplotlib

    Notes:
    - The line plot includes labeled axes and a legend. It visualizes the original
      data with label "Original Data" and normalized ones as "Normalized Data".
      The function sets the plot title to "Comparison of Original and Normalized Data",
      with "Index" on the x-axis and "Value" on the y-axis.

    Example:
    >>> json_str = '{"data": {"values": [5, 10, 15, 20, 25]}}'
    >>> original_data, normalized_data, ax = task_func(json_str, 'data.values')
    >>> type(original_data), type(normalized_data), type(ax)
    (<class 'pandas.core.series.Series'>, <class 'pandas.core.series.Series'>, <class 'matplotlib.axes._axes.Axes'>)
    """
    data = json.loads(json_data)
    try:
        data = json.loads(json_data)
        for key in data_key.split("."):
            data = data[key]
        values = pd.Series(data, dtype=pd.Float64Dtype)
    except KeyError:
        raise KeyError(f"Key path '{data_key}' not found in the provided JSON data.")

    if values.empty:
        return values, None, None

    scaler = MinMaxScaler()
    normalized_values = pd.Series(
        scaler.fit_transform(values.values.reshape(-1, 1)).flatten(),
        dtype=pd.Float64Dtype,
    )

    fig, ax = plt.subplots()
    ax.plot(values, label="Original Data")
    ax.plot(normalized_values, label="Normalized Data")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()

    return values, normalized_values, ax
