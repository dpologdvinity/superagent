from random import shuffle, randint
import pandas as pd

def task_func(l, n_groups = 5):
    """
    Generate a Series from a list "l". The function shuffles the list, 
    then creates a longer series by cycling through the shuffled list. 
    For each element in the series, it randomly selects n_groups characters
    from the start of the string and moves them to the end. 
    
    Parameters:
    - l (list): A list of strings.
    - n_groups (int): number of groups. Default value is 5.

    Returns:
    - pd.Series: A Series where each element is modified by moving "n" 
                 characters from the start to the end.

    Requirements:
    - pandas
    - random.shuffle
    - random.randint

    Example:
    >>> result = task_func(['ABC', 'DEF', 'GHI'])
    >>> isinstance(result, pd.Series)  # Check if the output is a pandas Series
    True
    >>> len(result) == 15  # Check if the length of the result is as expected for 3 elements cycled 5 times
    True
    """
    if not l:
        return pd.Series()

    # Shuffle list once
    shuffle(l)
    # Precompute random indices for each element to avoid calling randint excessively
    random_shifts = [(randint(1, max(1, len(x) - 1)), randint(1, max(1, len(x) - 1))) for x in l]

    # Create the full list by applying the precomputed shifts
    modified_elements = []
    for _ in range(n_groups):
        for element, (start, end) in zip(l, random_shifts):
            new_element = element[start:] + element[:end] if len(element) > 1 else element
            modified_elements.append(new_element)

    # Convert the list to a Series
    return pd.Series(modified_elements)
