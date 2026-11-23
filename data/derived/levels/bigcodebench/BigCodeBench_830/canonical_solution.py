import json
import os

def task_func(filename, data):
    """
    Write a dictionary to a file as a JSON object and return the written content for verification.
    
    This function performs a write operation to store the dictionary data in JSON format
    and then reads it back to verify the content. Additionally, checks if the file exists using the os library.

    Parameters:
    - filename (str): The name of the file to be written to.
    - data (dict): The dictionary containing data to be written as JSON to the file.

    Returns:
    - tuple: A tuple containing a boolean indicating the success of the operation and the content that was written.
        - bool: indicating the success of the operation.
        - written_data (json): the content that was written.
    
    Requirements:
    - json
    - os

    Example:
    >>> result, written_data = task_func('data.json', {'key': 'value'})
    >>> print(result)  # This should print: True
    True
    >>> print(written_data)  # This should print: {'key': 'value'}
    {'key': 'value'}
    """
    try:
        # Write the dictionary to the file as JSON
        with open(filename, 'w') as f:
            json.dump(data, f)
        
        # Verify the file exists after writing, using os.path.exists
        file_exists = os.path.exists(filename)
        if not file_exists:
            return False, None

        # Read the file back to verify content
        with open(filename, 'r') as f:
            written_data = json.load(f)
            if written_data != data:
                return False, None

        return True, written_data
    except Exception as e:
        return False, None
