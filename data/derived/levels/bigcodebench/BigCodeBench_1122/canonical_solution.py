import re
import socket
import urllib.parse

def task_func(myString):
    """
    Extracts all URLs from a given string, analyzes each URL to extract the domain, and retrieves the IP address of each domain.
    
    Parameters:
    myString (str): The string from which URLs are extracted. The string should contain valid URLs starting with http or https.
    
    Returns:
    dict: A dictionary with domains as keys and their respective IP addresses (IPv4) as values. If a domain cannot be resolved, the IP address will be None.

    Requirements:
    - re
    - urllib.parse
    - socket

    Raises:
    socket.gaierror if the domain cannot be resolved
    
    Example:
    >>> task_func("Check these links: http://www.google.com, https://www.python.org")
    {'www.google.com': '172.217.12.142', 'www.python.org': '151.101.193.223'}
    """
    urls = re.findall(r'https?://[^\s,]+', myString)
    ip_addresses = {}

    for url in urls:
        domain = urllib.parse.urlparse(url).netloc
        try:
            ip_addresses[domain] = socket.gethostbyname(domain)
        except socket.gaierror:
            ip_addresses[domain] = None  # Handle domains that cannot be resolved

    return ip_addresses
