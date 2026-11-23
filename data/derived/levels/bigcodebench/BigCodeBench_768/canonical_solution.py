import re
import os
import glob


def task_func(dir_path):
    """
    Search for occurrences of the word "error" in all text files within a 
    specified directory and its subdirectories.
    
    Parameters:
    dir_path (str): The path of the directory.
    
    Returns:
    dict: A dictionary with relative file paths as keys and the count of 
            occurrences of the word "error" as values.
    
    Raises:
    - ValueError: If directory in dir_path does not exist.

    Requirements:
    - re: For regex pattern matching.
    - os: For retrieving relative file paths.
    - glob: For fetching all text file paths in the directory.
    
    The function specifically searches for the word "error" in text files
    (with the extension ".txt").
    This function is NOT case sensitive, e.g. also "ERROr" will be counted.
    
    Example:
    >>> task_func("/path/to/directory")
    {'file1.txt': 2, 'subdir/file2.txt': 1}
    """

    if not os.path.isdir(dir_path):
        raise ValueError("Specified directory does not exist.")

    result = {}
    file_paths = glob.glob(f'{dir_path}/**/*.txt', recursive=True)
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
        matches = re.findall(r'\berror\b', content, re.IGNORECASE)
        # Always set the file's count in the result dictionary, even if it's 0
        result[os.path.relpath(file_path, dir_path)] = len(matches)

    return result
