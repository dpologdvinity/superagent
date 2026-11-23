import requests
import os
import json
import time

# Redefining the function in the current context

HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}

def task_func(url, directory, metadata):
    """
    Upload all files from a specific directory to the specified server URL, along with the associated metadata. 
    In addition, the speed limit function pauses for one second after each upload.

    Parameters:
    url (str): The server URL.
    directory (str): The directory containing the files to be uploaded.
    metadata (dict): The metadata to be associated with the files.

    Returns:
    list: A list of status codes for the upload responses.

    Requirements:
    - requests
    - os
    - json
    - time

    Raises:
    - The function will raise FileNotFoundError if the directory does not exist.
    - The function will raise TypeError if the url is invalid.

    Example:
    >>> task_func('https://www.example.com', './uploads', {'userId': 'abc'})
    """

    files = os.listdir(directory)
    status_codes = []

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            with open(os.path.join(directory, file), 'rb') as f:
                files = {'file': f}
                response = requests.post(url, files=files, headers=HEADERS, data=json.dumps(metadata))
                status_codes.append(response.status_code)
                time.sleep(1)

    return status_codes
