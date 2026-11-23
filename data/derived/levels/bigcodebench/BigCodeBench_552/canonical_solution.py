import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']


def task_func(a, b, items=ITEMS):
    """
    Combine two lists and record the frequency of predefined items in the combined list.

    Parameters:
    a (list): A list of items.
    b (list): Another list of items.
    items (list, optional): a list of predefined items

    Returns:
    matplotlib.axes.Axes: A bar chart showing the frequency of predefined items in the combined list.

    Requirements:
    - collections
    - itertools
    - matplotlib.pyplot

    Example:
    >>> ax = task_func(['apple', 'banana', 'cherry'], ['date', 'elderberry', 'apple', 'banana', 'cherry'])
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    # Combine lists
    combined = list(itertools.chain(a, b))
    # Count occurrences of each item
    counter = collections.Counter(combined)
    # Get counts for predefined items
    item_counts = [counter.get(item, 0) for item in items]

    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(items, item_counts, color='skyblue')
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Item Frequency in Combined List')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for item labels

    return ax
