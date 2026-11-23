import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    '''
    Move all files with certain extensions from one directory to another.

    Parameters:
    - source_dir (str): The directory containing the source files.
    - target_dir (str): The directory to which the files should be moved.
    - extensions (List[str]): The list of file extensions to be moved.

    Returns:
    int: The number of moved files.

    Raises:
    - ValueError: If source_dir or target_dir does not exist.

    Requirements:
    - shutil
    - pathlib.Path

    Example:
    >>> task_func('path/to/source/', 'path/to/target/', ['.jpg', '.png', '.gif'])
    15
    >>> task_func('path/to/source/', 'path/to/target/', ['.txt'])
    1
    '''

    if Path(source_dir).is_dir() == False:
        raise ValueError("source_dir does not exist.")

    if Path(target_dir).is_dir() == False:
        raise ValueError("target_dir does not exist.")

    count = 0

    for extension in extensions:
        for file_name in Path(source_dir).glob(f'*{extension}'):
            shutil.move(str(file_name), target_dir)
            count += 1

    return count
