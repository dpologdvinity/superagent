import codecs
import os
import zipfile


def task_func(directory_name="latin_files",
          content='Sopetón',
          file_names=['file1.txt', 'file2.txt', 'file3.txt'],
          encoding="latin-1"):
    '''
    Create a directory with the given name, create specified .txt files. Encode
    the content using the specified encoding and write it into all .txt files, 
    then zip the directory. 

    Args:
    directory_name (str): The name of the directory to be created.
    content (str, optional): The content which should be written to each .txt file.
                             Defaults to 'Sopetón'.
    file_names (list): List of .txt file names to be created.
                       Defaults to ['file1.txt', 'file2.txt', 'file3.txt'].
    encoding (str): The encoding type for the files. Default is 'latin-1'.

    Returns:
    str: The zipped file name.

    Requirements:
    - codecs
    - os
    - zipfile

    Example:
    >>> zipped_file = task_func("latin_files", "test", ["file1.txt", "file2.txt", "file3.txt"])
    >>> print(zipped_file)
    latin_files.zip

    >>> zipped_file = task_func(directory_name="directorio", content='hi', file_names=["custom1.txt", "custom2.txt"], encoding='utf-8')
    >>> print(zipped_file)
    directorio.zip
    '''

    os.makedirs(directory_name, exist_ok=True)

    for file_name in file_names:
        with open(os.path.join(directory_name, file_name), 'wb') as f:
            f.write(codecs.encode(content, encoding))

    zipped_file = directory_name + '.zip'
    with zipfile.ZipFile(zipped_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                zipf.write(os.path.join(root, file))

    return zipped_file 
