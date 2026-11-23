from texttable import Texttable
import os
import psutil

def task_func():
    """
    Generates a table displaying the system's CPU usage, memory usage, and disk usage.

    Returns:
        A string representation of a table with the columns of 'Item' and 'Value',
        and the following system information:
        - CPU Usage (%)
        - Memory Usage (%)
        - Disk Usage (%)

    Requirements:
    - texttable.Texttable
    - os
    - psutil

    Examples:
    >>> table_str = task_func()
    >>> isinstance(table_str, str)
    True
    >>> 'CPU Usage (%)' in table_str and 'Memory Usage (%)' in table_str
    True
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage(os.sep)

    table = Texttable()
    table.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', cpu_usage],
        ['Memory Usage (%)', memory_info.percent],
        ['Disk Usage (%)', disk_usage.percent]
    ])
    return table.draw()
