import os
import shutil
import string

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
    """
    Scan a directory and organize the files according to their endings. Files with invalid characters in the name will be moved to a new directory called "Invalid."
    
    The invalid characters are defined by the constant INVALID_CHARACTERS, which includes all punctuation and whitespace characters.

    Parameters:
    - directory_path (str): The path to the directory.

    Returns:
    - summary (dict): A summary dictionary containing the count of files moved to each directory.

    Requirements:
    - os
    - shutil
    - string

    Example:
    >>> task_func('path_to_directory')
    {'txt': 2, 'jpg': 1, 'Invalid': 1}
    """
    summary = {}
    for filename in os.listdir(directory_path):
        if any(char in INVALID_CHARACTERS for char in filename):
            if not os.path.exists(os.path.join(directory_path, 'Invalid')):
                os.mkdir(os.path.join(directory_path, 'Invalid'))
            shutil.move(os.path.join(directory_path, filename), os.path.join(directory_path, 'Invalid'))
            summary['Invalid'] = summary.get('Invalid', 0) + 1
        else:
            extension = os.path.splitext(filename)[-1].strip('.')
            if not os.path.exists(os.path.join(directory_path, extension)):
                os.mkdir(os.path.join(directory_path, extension))
            shutil.move(os.path.join(directory_path, filename), os.path.join(directory_path, extension))
            summary[extension] = summary.get(extension, 0) + 1
    return summary
