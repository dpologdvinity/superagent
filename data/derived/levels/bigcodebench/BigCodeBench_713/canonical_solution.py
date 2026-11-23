import os
import re

def task_func(log_file_path: str, keywords: list):
    '''
    Check a log file and format the lines that contain certain keywords. This code reads the log file specified by log_file_path; searches for lines containing any of the keywords provided in the list;
    and formats each line to display the keyword, the timestamp, and the message separated by 20 spaces.
    
    Parameters:
    - log_file_path (str): The path to the log file to be checked.
    - keywords (list): A list of keywords to be searched for in the log file.
    
    Returns:
    - formatted_lines (list): Returns a list of formatted strings containing the relevant information.
    
    Requirements:
    - os
    - re
    
    Example:
    >>> task_func('/path/to/log_file.log', ['ERROR', 'WARNING'])
    ['    ERROR :    11:30:10 : This is an error message', '    WARNING :    11:35:10 : This is a warning message']
    '''
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"Log file {log_file_path} does not exist.")
    
    formatted_lines = []
    with open(log_file_path, 'r') as log:
        for line in log:
            for keyword in keywords:
                if keyword in line:
                    parts = re.split(r'\s+', line.strip(), maxsplit=2)
                    if len(parts) == 3:
                        formatted_line = f"{keyword:>{20}} : {parts[1]:>{20}} : {parts[2]:>{20}}"
                        formatted_lines.append(formatted_line)
                    else:
                        # Handle lines that do not conform to expected structure
                        formatted_lines.append(f"Line format unexpected: {line.strip()}")
    return formatted_lines
