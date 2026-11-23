import os
import shutil

def task_func(src_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.

    Parameters:
    - src_dir (str): The source directory.
    - dest_dir (str): The destination directory.
    - extension (str): The file extension.

    Returns:
    - files_moved (int): The number of files moved.

    Requirements:
    - os
    - shutil

    Example:
    >>> task_func('/path/to/src', '/path/to/dest', '.txt')
    """
    files_moved = 0

    for file_name in os.listdir(src_dir):
        if file_name.endswith(extension):
            shutil.move(os.path.join(src_dir, file_name), os.path.join(dest_dir, file_name))
            files_moved += 1

    return files_moved
