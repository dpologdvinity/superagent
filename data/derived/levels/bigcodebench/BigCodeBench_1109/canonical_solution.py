import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    """
    Tokenizes a text file using the NLTK library. This function reads each line from the file, 
    breaks it into words or punctuation, and stores the tokens in a list.
    
    Parameters:
    - file_path (str): The path to the text file. Defaults to 'File.txt'.
    
    Returns:
    - list: A list of tokens.
    
    Requirements:
    - os
    - nltk.word_tokenize
    
    Examples:
    >>> task_func('sample.txt')
    ['Hello', ',', 'world', '!']
    >>> task_func('data.txt')
    ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.']
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    tokens = []

    with open(file_path, 'r') as file:
        for line in file:
            tokens.extend(word_tokenize(line))

    return tokens
