import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    """
    Create SHA256 hashes for all files in the specified directory, including files in subdirectories, 
    and save these hashes in a JSON file named 'hashes.json' in the given directory.

    Parameters:
    - directory (str): The path to the directory containing files to be hashed.
    
    Returns:
    str: The absolute path of the JSON file ('hashes.json') containing the hashes.
    
    Requirements:
    - os
    - hashlib
    - json
    - pathlib.Path

    Example:
    >>> json_file = task_func("/path/to/directory")
    >>> print(f"Hashes saved at: {json_file}")
    """
    hash_dict = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            with open(file_path, 'rb') as f:
                bytes = f.read()  # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest()
                hash_dict[str(file_path)] = readable_hash
                
    # Save to JSON file
    json_file = Path(directory) / 'hashes.json'
    with open(json_file, 'w') as f:
        json.dump(hash_dict, f)
    return str(json_file)
