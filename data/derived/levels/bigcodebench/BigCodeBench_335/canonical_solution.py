import collections
from queue import PriorityQueue
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    """
    Create a random string of a given length from a predefined list of letters and count the frequency 
    of each letter, returning an ordered dictionary sorted by frequency in descending order.

    Parameters:
    - string_length (int, optional): The length of the random string to be generated. Default is 100.

    Returns:
    - collections.OrderedDict: An ordered dictionary where keys are letters and values are 
      their frequencies in the generated string, sorted in descending order of frequency.

    Requirements:
    - collections
    - queue.PriorityQueue
    - random

    Example:
    >>> random.seed(0)
    >>> freq = task_func(50)
    >>> freq  # Example output: OrderedDict([('e', 15), ('a', 12), ('b', 10), ('d', 8), ('c', 5)])
    OrderedDict(...)
    """

    string = ''.join([LETTERS[random.randint(0, len(LETTERS)-1)] for _ in range(string_length)])

    freq = collections.Counter(string)

    pq = PriorityQueue()
    for letter, count in freq.items():
        pq.put((-count, letter))

    sorted_freq = collections.OrderedDict()
    while not pq.empty():
        count, letter = pq.get()
        sorted_freq[letter] = -count

    return sorted_freq
