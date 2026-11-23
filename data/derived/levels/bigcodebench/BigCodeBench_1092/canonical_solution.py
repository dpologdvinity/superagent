import ast
import requests
from bs4 import BeautifulSoup


def task_func(url):
    """
    Fetches the content of a webpage specified by its URL, parses it to find <script> tags,
    and attempts to evaluate any string within these tags as a Python dictionary.

    Parameters:
    - url (str): The URL of the webpage to scrape.

    Returns:
    - list of dict: A list containing dictionaries that were successfully evaluated from string representations
      found within <script> tags on the webpage. 
    
    Note:
    - If an error occurs during the request or if no dictionaries are found/evaluable, an empty list is returned.

    Requirements:
    - ast
    - requests
    - bs4.BeautifulSoup

    Example:
    >>> task_func('https://example.com')
    [{'key': 'value'}, ...]
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for script in soup.find_all('script'):
        try:
            results.append(ast.literal_eval(script.string))
        except (ValueError, SyntaxError):
            continue

    return results
