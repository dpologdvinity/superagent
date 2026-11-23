from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


def task_func(data):
    """
    Calculate statistical measurements (mean and standard deviation) of the values associated with
    each key in a list of dictionaries, and visualize mean and standard deviation with bar charts.

    Parameters:
    data (list): The list of dictionaries. Must not be empty. Each dictionary must have numeric values.

    Returns:
    tuple:
        - dict: A dictionary with keys and their corresponding mean and standard deviation.
        - list: A list of matplotlib Axes objects for each key's visualization.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - collections.defaultdict
    
    Raises:
    - ValueError: If the input data is empty.
    - TypeError: If the input is not a list of dictionaries or if any value in the dictionaries is not numeric.
    
    Example:
    >>> stats, axes = task_func([{'cat': 1, 'dog': 3}, {'cat' : 2, 'dog': 5}, {'cat' : 3, 'dog': 7}])
    >>> stats
    {'cat': {'mean': 2.0, 'std': 0.816496580927726}, 'dog': {'mean': 5.0, 'std': 1.632993161855452}}
    >>> axes
    [<Axes: title={'center': 'Statistics of cat'}, ylabel='Value'>, <Axes: title={'center': 'Statistics of dog'}, ylabel='Value'>]
    """
    if not data:
        raise ValueError("Input data is empty.")
    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        raise TypeError("Input must be a list of dictionaries.")
    for d in data:
        if not all(isinstance(value, (int, float)) for value in d.values()):
            raise TypeError("All values in the dictionaries must be numeric.")

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    result = {k: {"mean": np.mean(v), "std": np.std(v)} for k, v in stats.items()}

    # Visualization
    axes = []
    for key in result:
        fig, ax = plt.subplots()
        ax.bar(x=["mean", "std"], height=result[key].values())
        ax.set_title(f"Statistics of {key}")
        ax.set_ylabel("Value")
        axes.append(ax)

    return result, axes
