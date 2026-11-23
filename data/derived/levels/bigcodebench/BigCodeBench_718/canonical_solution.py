import re
import numpy as np
from scipy.stats import ttest_rel

def task_func(text1, text2):
    """
    Perform a paired t-test for the number of words in two strings, only if the strings produce the same number of words.
    
    Parameters:
    - text1 (str), text2 (str): The two text strings.
    
    Returns:
    - t_statistic (float): The t-statistic, or NaN if tests cannot be performed due to unequal lengths.
    - p_value (float): The p-value, or NaN if tests cannot be performed due to unequal lengths.
    
    Requirements:
    - re
    - numpy
    - scipy
    
    Example:
    >>> task_func('Words, words, words.', 'And more words!')
    (1.7320508075688774, 0.22540333075851657)
    """
    word_counts1 = np.array([len(word) for word in re.split(r'\W+', text1) if word])
    word_counts2 = np.array([len(word) for word in re.split(r'\W+', text2) if word])

    if len(word_counts1) != len(word_counts2):
        return (np.nan, np.nan)

    t_statistic, p_value = ttest_rel(word_counts1, word_counts2)
    return t_statistic, p_value
