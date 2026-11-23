from itertools import groupby
from operator import itemgetter

# Constants
KEY_FUNC = itemgetter(0)

def task_func(my_dict):
    """
    Group the dictionary entries after the first character of the key and add the values for each group.

    Parameters:
    - my_dict (dict): The dictionary to process.

    Returns:
    - aggregated_dict (dict): The aggregated dictionary.

    Requirements:
    - itertools
    - operator
    
    Example:
    >>> my_dict = {'apple': 1, 'banana': 2, 'avocado': 3, 'blueberry': 4, 'blackberry': 5}
    >>> aggregated_dict = task_func(my_dict)
    >>> print(aggregated_dict)
    {'a': 4, 'b': 11}
    """
    sorted_items = sorted(my_dict.items(), key=lambda item: item[0][0])
    # Group items by the first character of the key and sum their values
    aggregated_dict = {k: sum(item[1] for item in g) for k, g in groupby(sorted_items, key=lambda item: item[0][0])}

    return aggregated_dict
