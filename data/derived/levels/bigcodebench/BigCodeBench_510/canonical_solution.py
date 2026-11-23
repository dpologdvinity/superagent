import difflib
import gzip

def task_func(file_path1, file_path2):
    """
    Compares the contents of two gzip files and returns a string describing the differences between them.
    It reads the contents of each file, then uses difflib to compute and return the differences. 
    Only differences are returned, with an empty string indicating no differences.

    Parameters:
    file_path1 (str): The file path of the first gzip file.
    file_path2 (str): The file path of the second gzip file.

    Returns:
    str: A string describing the differences between the two files' contents.

    Requirements:
    - difflib
    - gzip

    Examples:
    Assuming 'file1.gz' and 'file2.gz' contain slightly different text,
    >>> result = task_func('file1.gz', 'file2.gz')
    >>> len(result) > 0
    True

    Assuming 'file1.gz' and 'file1.gz' are identical,
    >>> task_func('file1.gz', 'file1.gz')
    ''
    """
    with gzip.open(file_path1, 'rt') as file1, gzip.open(file_path2, 'rt') as file2:
        file1_content = file1.readlines()
        file2_content = file2.readlines()
        diff = difflib.ndiff(file1_content, file2_content)
        diff = [line for line in diff if line.startswith('+ ') or line.startswith('- ')]

    return ''.join(diff)
