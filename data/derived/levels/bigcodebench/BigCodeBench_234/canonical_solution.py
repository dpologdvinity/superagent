import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def task_func(df):
    """
    Perform a linear regression between "age" and "score" in the DataFrame, excluding rows with duplicate names.
    Plot the regression line and the scatter plot of the data.

    Parameters:
    df (DataFrame): The pandas DataFrame containing the data.

    Returns:
    tuple: A tuple containing the matplotlib.pyplot object and the axes object.

    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.

    Note:
    - The function use "Linear Regression" for the plot title.
    - The function use "Age" and "Score" as the xlabel and ylabel respectively.

    Requirements:
    - pandas
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> data = pd.DataFrame([{'Name': 'Alice', 'Age': 20, 'Score': 70}, {'Name': 'Bob', 'Age': 25, 'Score': 75}, {'Name': 'Eve', 'Age': 30, 'Score': 80}])
    >>> plt, ax = task_func(data)
    >>> ax.lines[0].get_xdata()[0]
    20
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    df = df.drop_duplicates(subset='Name')

    slope, intercept, r_value, _, _ = stats.linregress(df['Age'], df['Score'])

    df['Age_up'] = intercept + slope * df['Age']
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    plt.scatter(df['Age'], df['Score'], label='Data')
    plt.plot(df['Age'].values, df['Age_up'].values, 'r', label='Fitted line')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.title('Linear Regression')
    plt.legend()
    return plt, ax
