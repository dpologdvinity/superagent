import numpy as np
import itertools
import json


def task_func(data_list, json_file_name="mean_values.json"):
    """
    Calculate the mean of the numeric values for each position in the provided data list 
    and return the results. Optionally, the results can be exported to a specified JSON file.
    
    Parameters:
    - data_list (list of tuples): List of data tuples where each tuple contains a string followed by numeric values.
    - json_file_name (str, optional): Name of the JSON file to export the results. Defaults to 'mean_values.json'.

    Requirements:
    - numpy
    - itertools
    - json

    Returns:
    - dict: A dictionary with keys in the format 'Position {i}' and values being the mean of the numeric values 
            at position i in the provided data list.

    Example:
    >>> import tempfile
    >>> json_file = tempfile.NamedTemporaryFile(delete=False)
    >>> task_func([('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)], json_file.name)
    {'Position 1': 3.0, 'Position 2': 4.0}
    """
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean(column) for column in unzipped_data[1:]]

    results = {'Position {}'.format(i+1): mean_value for i, mean_value in enumerate(mean_values)}
    
    with open(json_file_name, 'w') as f:
        json.dump(results, f)

    return results
