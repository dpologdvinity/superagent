import json
import os
import glob


# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    """
    Add a new key-value pair to all JSON files in a specific directory and save the updated JSON files.
    
    Specifically, the function searches for all JSON files within the provided directory and 
    updates each JSON file by adding a new key-value pair ('mynewkey': 'mynewvalue') if the key 
    doesn't already exist. The function modifies the JSON files in place.

    Parameters:
    directory (str): The directory containing the JSON files.

    Returns:
    int: The number of JSON files updated.

    Requirements:
    - json
    - os
    - glob

    Example:
    >>> task_func('./json_files') # Random test case with no JSON files
    0
    """
    files = glob.glob(os.path.join(directory, '*.json'))
    updated_files = 0

    for file in files:
        with open(file, 'r+') as f:
            data = json.load(f)
            if KEY not in data:
                data[KEY] = VALUE
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                updated_files += 1

    return updated_files
