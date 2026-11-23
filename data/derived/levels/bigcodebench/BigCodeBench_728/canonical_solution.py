import csv
import io

def task_func(filename, from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    """
    Convert the encoding of a CSV file from one encoding to another and return a list of dictionaries along with the converted CSV data as a string.
    
    Parameters:
    - filename (str): The name of the CSV file.
    - from_encoding (str): The original encoding of the CSV file. Default is 'cp1251'.
    - to_encoding (str): The encoding to which the CSV file should be converted. Default is 'utf8'.
    - delimiter (str): The character that separates the fields in the CSV file. Default is ','.
    
    Returns:
    tuple: A tuple containing:
        - list: A list of dictionaries. Each dictionary represents a row in the CSV file.
        - str: The converted CSV data as a string.
    
    Requirements:
    - csv
    - io
    
    Example:
    >>> data, converted_csv = task_func('sample.csv', 'cp1251', 'utf8')
    >>> print(data)
    [{'Name': 'Alice', 'Age': '30'}, {'Name': 'Bob', 'Age': '25'}]
    >>> print(converted_csv)
    "Name,Age\nAlice,30\nBob,25\n"
    
    Note:
    - The default filename to use if not specified is 'sample.csv'.
    - The default delimiter is ','.
    """
    with io.open(filename, 'r', encoding=from_encoding) as file:
        content = file.read()

    content = content.encode(from_encoding).decode(to_encoding)
    file_like = io.StringIO(content)

    reader = csv.DictReader(file_like, delimiter=delimiter)
    data = list(reader)

    output = io.StringIO()
    # Check if fieldnames are present, else set a default
    fieldnames = reader.fieldnames if reader.fieldnames else ['Column']
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    writer.writerows(data)
    converted_csv = output.getvalue().replace('\r\n', '\n')  # Normalize newlines

    return data, converted_csv
