from collections import Counter
import random
from itertools import cycle

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l):
    """
    Create a counter from a list "l" and move the first 3 elements to the end of the list.

    Parameters:
    - l (list): A list of elements that the function will process. 

    Returns:
    - counter (collections.Counter): A frequency counter that maps elements from the input list to their frequencies in the first 30 elements of the cycled, shuffled list. 
    
    Requirements:
    - collections
    - random
    - itertools

    Example:
    >>> random.seed(42)
    >>> task_func(ELEMENTS)
    Counter({'I': 3, 'F': 3, 'G': 3, 'J': 3, 'E': 3, 'A': 3, 'B': 3, 'H': 3, 'D': 3, 'C': 3})
    """
    if not l:  # Check if the list is empty
        return Counter()  # Return an empty counter if the list is empty

    random.shuffle(l)
    l_cycled = cycle(l)
    counter = Counter(next(l_cycled) for _ in range(30))
    keys = list(counter.keys())
    counter = Counter({k: counter[k] for k in keys[3:] + keys[:3]})
    
    return counter
