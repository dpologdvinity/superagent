import hashlib
import os
import base64


def task_func(password: str, salt_length: int = 8) -> str:
    """
    Encrypt a password using Salt and SHA-256, then encode the result in base64.

    Parameters:
    password (str): The password to be encrypted.
    salt_length (int, optional): The length of the generated salt. Default is 8.

    Returns:
    str: The encrypted password in base64 format.

    Requirements:
    - base64
    - hashlib
    - os

    Example:
    >>> isinstance(task_func('my_password'), str)
    True
    """
    # Generate a random salt
    salt = os.urandom(salt_length)
    # Use the salt and the password to create a SHA-256 hash
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Combine the salt and the hash
    salted_hash = salt + hash
    # Encode the salted hash in base64
    encrypted_password = base64.b64encode(salted_hash)

    return encrypted_password.decode('utf-8')
