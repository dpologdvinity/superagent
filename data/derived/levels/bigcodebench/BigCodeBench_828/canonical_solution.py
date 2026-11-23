import os
import errno
import shutil

def task_func(filename, dest_dir):
    """
    Copy a file to a specified destination directory and clear its contents.
    This function takes in the path to a file and a destination directory path.
    It copies the file to the destination directory. Once the file is copied,
    the function will erase the content of the original file, leaving it empty.

    Parameters:
    - filename (str): The path to the file to be copied and erased. This must be an
                      absolute path or relative to the current working directory.
    - dest_dir (str): The path to the destination directory where the file will be copied.
                      This must be an absolute path or relative to the current working directory.
                      The directory will be created if it does not exist.

    Returns:
    - str: The absolute path to the copied file within the destination directory.

    Requirements:
    - os
    - errno
    - shutil
    
    Raises:
    - OSError: If the destination directory cannot be created and does not exist, or if the file
               cannot be copied for reasons other than a pre-existing directory.

    Examples:
    >>> task_func('/path/to/original/test.txt', '/path/to/destination')
    '/path/to/destination/test.txt'

    Notes:
    - If the destination directory already contains a file with the same name, the function
      will overwrite that file without warning.
    - The original file will not be deleted from the filesystem, only its content will be cleared.
    """
    # Ensure the destination directory exists
    try:
        os.makedirs(dest_dir, exist_ok=True)  # Simplified directory creation
    except OSError as e:
        # Reraise the exception if it's not related to existing directory
        if e.errno != errno.EEXIST:
            raise

    # Copy the file
    dest = shutil.copy(filename, dest_dir)

    # Erase the original file content by opening in write mode and closing it
    with open(filename, 'w') as original_file:
        original_file.truncate(0)

    return os.path.abspath(dest)
