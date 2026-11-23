import numpy as np
import random
from datetime import datetime

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    """
    Generates a matrix of given dimensions (rows x columns) containing unique dates between 
    a specified start date and end date.
    
    Parameters:
    - rows (int): The number of rows for the output matrix. Default is 3.
    - columns (int): The number of columns for the output matrix. Default is 2.
    - start_date (datetime): The start date for the range of unique dates. Default is datetime(2021, 1, 1).
    - end_date (datetime): The end date for the range of unique dates. Default is datetime(2021, 12, 31).
    
    Returns:
    - ndarray: A numpy ndarray with unique dates in the shape (rows, columns).
    
    Requirements:
    - numpy
    - itertools
    - datetime
    - random
    
    Example:
    >>> matrix = task_func(2, 2, datetime(2021, 1, 1), datetime(2021, 1, 10))
    >>> print(matrix)
    [['2021-01-03T00:00:00.000000000', '2021-01-07T00:00:00.000000000'],
     ['2021-01-09T00:00:00.000000000', '2021-01-04T00:00:00.000000000']]
    """
    # Convert start_date and end_date to numpy datetime64 objects
    if seed is not None:
        random.seed(seed)
    
    # Convert start_date and end_date to numpy datetime64 objects
    start_date_np = np.datetime64(start_date)
    end_date_np = np.datetime64(end_date)

    # Calculate the number of days between start_date and end_date
    total_days = int((end_date_np - start_date_np).astype('timedelta64[D]').astype(int) + 1)

    # Randomly select unique dates within the range without replacement using random.sample
    selected_dates = sorted(random.sample(range(total_days), rows * columns))

    # Generate the matrix with selected unique dates
    matrix = (start_date_np + np.array(selected_dates).astype('timedelta64[D]')).reshape(rows, columns)

    return matrix
