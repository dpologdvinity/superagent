import os
import glob
import shutil
import time

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    """
    Archive files that were changed older than a specified number of days in a given directory. This function searches for files with specific extensions (.txt, .csv, .xlsx, .docx, .pdf) in the given directory.
    Files older than 'days_old' are moved to an 'archive' subdirectory within the specified directory.

    Parameters:
    my_path (str): The path of the directory to search.
    days_old (int): The age of files to archive, in days.

    Returns:
    str: The path of the archive subdirectory where files are moved.

    Requirements:
    - os
    - glob
    - shutil
    - time

    Example:
    >>> task_func('/usr/my_directory', 30)
    '/usr/my_directory/archive'
    """

    archive_dir = os.path.join(my_path, 'archive')
    os.makedirs(archive_dir, exist_ok=True)

    for ext in FILE_EXTENSIONS:
        files = glob.glob(os.path.join(my_path, '*' + ext))
        for file in files:
            if os.path.isfile(file) and os.path.getmtime(file) < time.time() - days_old * 86400:
                shutil.move(file, archive_dir)

    return archive_dir
