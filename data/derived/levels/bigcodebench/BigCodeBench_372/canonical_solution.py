import re
import glob
from docx import Document


def task_func(directory_path: str) -> int:
    """
    Processes all Word (.docx) files in the provided directory, searching for double quotes in the text 
    and adding a backslash before each double quote to "protect" it.
    
    Parameters:
    - directory_path (str): Path to the directory containing .docx files to be processed.
    
    Returns:
    - int: Number of .docx files processed.

    Requirements:
    - re
    - docx
    - glob

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> doc = Document()
    >>> _ = doc.add_paragraph("This is a sample text with double quotes.")
    >>> doc.save(temp_dir + '/sample.docx')
    >>> task_func(temp_dir)
    1
    """
    docx_files = glob.glob(directory_path + '/*.docx')
    processed_files = 0

    for docx_file in docx_files:
        document = Document(docx_file)

        for paragraph in document.paragraphs:
            paragraph.text = re.sub(r'(?<!\\)"', r'\"', paragraph.text)

        document.save(docx_file)
        processed_files += 1

    return processed_files
