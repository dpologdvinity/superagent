import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    """
    Use a linear regression model to predict the "value" of "feature" in the given dataframe and return the coefficients and intercept.

    Parameters:
    - df (pd.DataFrame): pandas DataFrame that contains columns named 'feature' and 'value'.

    Returns:
    - result (dict): A dictionary with the coefficients and the intercept of the fitted linear regression model.

    Requirements:
    - numpy
    - sklearn

    Example:
    >>> import pandas as pd
    >>> np.random.seed(42)
    >>> df = pd.DataFrame({'feature': np.random.rand(100), 'value': np.random.rand(100)})
    >>> coefficients = task_func(df)
    >>> print(coefficients)
    {'coefficients': [[-0.03353164387961974]], 'intercept': [0.5135976564010359]}
    """
    X = np.array(df['feature']).reshape(-1,1)  # Explicitly converting to numpy array and reshaping
    y = np.array(df['value']).reshape(-1,1)    # Explicitly converting to numpy array and reshaping

    model = LinearRegression().fit(X, y)

    return {'coefficients': model.coef_.tolist(), 'intercept': model.intercept_.tolist()}
