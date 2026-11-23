import textwrap
import re

def task_func(input_string, width):
    """
    Divide a multi-line string into separate strings and wrap each line to a certain width.
    
    Parameters:
    - input_string (str): The multi-line string that needs to be wrapped.
    - width (int): The width to wrap each line to.
    
    Returns:
    - str: The wrapped string where each line is wrapped to the specified width.
    
    Requirements:
    - textwrap
    - re
    
    Example:
    >>> task_func('Another line\\nWith wrapping', 8)
    'Another\\nline\\nWith\\nwrapping'
    """
    lines = input_string.split('\\n')
    wrapped_lines = [textwrap.fill(line, width, break_long_words=False) for line in lines]
    # Join wrapped lines into a single string
    wrapped_string = '\\n'.join(wrapped_lines)
    
    # Additional processing using regular expressions (re)
    # For example, let's replace all whole-word instances of 'is' with 'was'
    wrapped_string = re.sub(r'\bis\b', 'was', wrapped_string)
    
    return wrapped_string
