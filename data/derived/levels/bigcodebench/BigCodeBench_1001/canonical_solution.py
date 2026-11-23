import pandas as pd
import matplotlib.pyplot as plt


def task_func(csv_file_path: str):
    """
    This function reads data from a CSV file, normalizes a specific column named 'column1', and then plots the normalized data.

    - The title is created using Python's string formatting, aligning 'Plot Title' and 'Normalized Column 1' on either side of a 
    colon, each padded to 20 characters.
    - Similarly, the x-label is formatted with 'Index' and 'Normalized Value' on either side of a colon, 
    each padded to 20 characters.
    - The y-label is set in the same manner, with 'Frequency' and 'Normalized Value' on either side of a colon.

    Parameters:
    - csv_file_path (str): Path to the CSV file. The file must contain a column named 'column1'.

    Returns:
    - The matplotlib.axes.Axes object with the plot of the normalized data.

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> ax = task_func('data.csv')
    >>> ax.get_title()
    "          Plot Title :  Normalized Column 1"
    """
    df = pd.read_csv(csv_file_path)
    mean = df["column1"].mean()
    std = df["column1"].std()
    df["column1_normalized"] = (df["column1"] - mean) / std

    # Creating a figure and axes
    _, ax = plt.subplots()
    # Plotting on the created axes
    ax.plot(df["column1_normalized"])
    title = "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    xlabel = "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    ylabel = "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Return the axes object for further manipulation
    return ax
