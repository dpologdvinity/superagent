import os
import re
import shutil

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    """
    Move all json files in a source directory to a target directory and rename them by splitting the filename the last time "-" occurs and keeping the prefix part of the filename.
    
    Parameters:
    - None

    Returns:
    - None

    Requirements:
    - os
    - re
    - shutil

    Example:
    >>> task_func()

    """
    SOURCE_DIR = '/source/dir'
    TARGET_DIR = '/target/dir'
    FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')
    for filename in os.listdir(SOURCE_DIR):
        match = FILE_PATTERN.match(filename)
        if match is not None:
            prefix = match.group(1)
            new_filename = f'{prefix}.json'
            shutil.move(os.path.join(SOURCE_DIR, filename), os.path.join(TARGET_DIR, new_filename))
