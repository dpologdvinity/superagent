import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


def task_func(input_file):
    """
    Reads a JSON file containing a list of dictionaries. For each key across all dictionaries,
    calculates the mean and median of its values using numpy. Visualizes the mean and median
    using bar charts. Returns the results and plots.

    Parameters:
        - input_file (str): Path to the input JSON file containing a list of dictionaries.

    Returns:
        - result (dict): each key corresponds to those in the input dictionaries, and the corresponding
          value is another dict with keys 'mean' and 'median', representing the calculated statistics.
        - plots  (list[matplotlib.axes._axes.Axes]): A list of bar charts, one for
          each key in the dictionaries, visualizing the mean and median values.

    Requirements:
        - json
        - numpy
        - collections.defaultdict
        - matplotlib.pyplot

    Example:
    >>> results, plots = task_func("sample_data.json")
    >>> type(plots[0])
    <class 'matplotlib.axes._axes.Axes'>
    >>> results
    {'a': {'mean': 3.0, 'median': 3.0}, 'b': {'mean': 6.0, 'median': 6.0}}
    """
    with open(input_file, "r") as f:
        data = json.load(f)

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    result = {k: {"mean": np.mean(v), "median": np.median(v)} for k, v in stats.items()}

    plots = []
    for key, values in result.items():
        _, ax = plt.subplots()
        ax.bar(["mean", "median"], [values["mean"], values["median"]])
        ax.set_title(f"Statistics of {key}")
        plots.append(ax)
    return result, plots
