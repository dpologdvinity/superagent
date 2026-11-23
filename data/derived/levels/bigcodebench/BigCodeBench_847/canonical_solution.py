import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    """
    Split a multi-line string into separate strings, remove special characters, and save each string as a separate text file.
    
    Parameters:
    - input_string (str): The multi-line string to be split and saved.
    - directory (str): The directory where the text files will be saved. Default is './text_files'.
    
    Returns:
    - file_paths (list): A list of file paths where the text is saved.
    
    Requirements:
    - re
    - os
    - string
    - random 
    
    Example:
    >>> task_func('line a\nfollows by line b\n...bye\n')
    ['./text_files/12345.txt', './text_files/67890.txt', './text_files/11223.txt']
    """
    lines = input_string.split('\n')
    file_paths = []
    for line in lines:
        line = re.sub('['+string.punctuation+']', '', line)
        filename = str(random.randint(10000, 99999)) + '.txt'
        filepath = os.path.join(directory, filename)
        file_paths.append(filepath)
        with open(filepath, 'w') as file:
            file.write(line)
    return file_paths
