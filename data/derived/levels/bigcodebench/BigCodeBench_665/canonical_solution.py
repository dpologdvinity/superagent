import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    """
    Copy all files from 'src_dir' to 'dst_dir' that match any pattern in ['*.txt', '*.docx'].

    Parameters:
    - src_dir (str): The source directory.
    - dst_dir (str): The destination directory.

    Returns:
    - str: The destination directory.
    
    Requirements:
    - shutil
    - os
    - fnmatch
    - itertools

    Example:
    >>> task_func('./source', './destination')
    >>> './destination'
    """
    FILE_PATTERNS = ['*.txt', '*.docx']
    # Find all matching files
    matching_files = list(itertools.chain.from_iterable(
        fnmatch.filter(os.listdir(src_dir), pattern) for pattern in FILE_PATTERNS))

    for filename in matching_files:
        shutil.copy2(os.path.join(src_dir, filename), dst_dir)

    return dst_dir
