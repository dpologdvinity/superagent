import re
import os
import shutil


def task_func(directory):
    """
    Find the files with filenames that contain "like" or "what" in a directory, create a new subdirectory called "Interesting Files" 
    and move those files to the new subdirectory.

    Parameters:
    directory (str): The directory path.

    Returns:
    List of files moved

    Requirements:
    - re
    - os
    - shutil

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> files = ['file_with_like.txt', 'another_file_with_what.doc', 'file_without_keywords.jpg', 'hidden_what_in_name.whatever']
    >>> for file in files:
    ...     with open(os.path.join(temp_dir, file), 'w') as f:
    ...         _ = f.write("Dummy content for testing.")
    >>> task_func(temp_dir)
    ['another_file_with_what.doc', 'hidden_what_in_name.whatever', 'file_with_like.txt']
    """
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    if not os.path.exists(os.path.join(directory, 'Interesting Files')):
        os.mkdir(os.path.join(directory, 'Interesting Files'))

    for file in interesting_files:
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'Interesting Files'))

    return interesting_files
