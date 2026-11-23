import ast
import os
import glob

# Constants
DIRECTORY = 'data'

def task_func(directory):
    """
    Convert all Unicode string representations of dictionaries in all text files 
    in the specified directory to Python dictionaries.

    Parameters:
    directory (str): The path to the directory containing the text files.

    Returns:
    list: A list of dictionaries extracted from the text files.

    Requirements:
    - ast
    - os
    - glob

    Example:
    >>> task_func("sample_directory/")
    [{'key1': 'value1'}, {'key2': 'value2'}]

    Note:
    Ensure that the text files in the directory contain valid Unicode string representations of dictionaries.

    Raises:
    - The function would raise a ValueError if there are text file(s) that have invalid dictionary representation
    """
    path = os.path.join(directory, '*.txt')
    files = glob.glob(path)

    results = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                results.append(ast.literal_eval(line.strip()))

    return results
