import unicodedata
import requests

URL = 'https://api.github.com/users/'

def task_func(username):
    """
    Retrieves user information from the GitHub API for a given username, normalizes all string data to ASCII,
    and returns a dictionary of the normalized data. This function demonstrates data retrieval from a web API
    and handling of Unicode data normalization.

    Parameters:
    username (str): The GitHub username.

    Returns:
    dict: A dictionary with the user's data, where all string values are normalized to ASCII.

    Raises:
    requests.exceptions.HTTPError: For any HTTP response indicating an error.

    Requirements:
    - unicodedata
    - requests

    Examples:
    >>> result = task_func('torvalds')
    >>> isinstance(result, dict)
    True
    >>> 'login' in result
    True
    """
    response = requests.get(URL + username)
    try:
        response.raise_for_status()  # This will raise an HTTPError if the response was an error
        user_data = response.json()
    except requests.exceptions.HTTPError as e:
        # Optionally, log the error or handle it according to your needs
        error_msg = f"Failed to fetch user data for '{username}'. HTTP status: {e.response.status_code} - {e.response.reason}."
        raise Exception(error_msg) from e

    normalized_user_data = {}
    for key, value in user_data.items():
        if isinstance(value, str):
            normalized_value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode()
            normalized_user_data[key] = normalized_value
        else:
            normalized_user_data[key] = value

    return normalized_user_data
