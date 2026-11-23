import pandas as pd
import re
import random


def task_func(data_list, seed=None):
    """
    Removes a random comma-separated value (treated as a "substring") from each string
    in a list and returns a pandas DataFrame containing the original and modified strings.

    Parameters:
    - data_list (list of str): A list of comma-separated strings. The function will remove
                               leading and trailing whitespaces first before processing.
    - seed (int, optional): Seed for the random number generator for reproducibility.
      Default is None, which uses system time.

    Returns:
    - DataFrame: A pandas DataFrame with columns 'Original String' and 'Modified String'.

    Requirements:
    - pandas
    - re
    - random

    Example:
    >>> task_func(['lamp, bag, mirror', 'table, chair, bag, lamp'], seed=42)
               Original String   Modified String
    0        lamp, bag, mirror         lamp, bag
    1  table, chair, bag, lamp  chair, bag, lamp
    """
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame([s.strip() for s in data_list], columns=["Original String"])

    modified_strings = []
    for s in data_list:
        substrings = re.split(", ", s)
        random_substring = random.choice(substrings)
        modified_s = (
            s.replace(", " + random_substring, "")
            if ", " + random_substring in s
            else s.replace(random_substring + ", ", "")
        )
        modified_strings.append(modified_s)

    df["Modified String"] = modified_strings

    return df
