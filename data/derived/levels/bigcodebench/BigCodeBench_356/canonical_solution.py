import numpy as np
import matplotlib.pyplot as plt
import cmath

def task_func(x, y):
    """
    Draw the phase of a complex function over a range of x and y and return the matplotlib axes object
    along with the 2D array of calculated phase values.

    Parameters:
    x (numpy.ndarray): The range of x values.
    y (numpy.ndarray): The range of y values.

    Returns:
    tuple: containing
        - matplotlib.axes.Axes: The axes object with the phase plot.
        - numpy.ndarray: The 2D array of calculated phase values.
    
    Raises:
    TypeError: If either `x` or `y` is not a numpy.ndarray.
    ValueError: If `x` and `y` do not have the same length.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - cmath

    Examples:
    >>> ax, Z = task_func(np.array([1, 2, 3]), np.array([1, 2, 3]))
    >>> isinstance(ax, plt.Axes), isinstance(Z, np.ndarray)
    (True, True)
    >>> ax, Z = task_func(np.array([0]), np.array([0]))  # Test with single point
    >>> isinstance(ax, plt.Axes), isinstance(Z, np.ndarray)
    (True, True)
    """
    # Type check for x and y
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("x and y must be numpy.ndarray")

    # Handle empty arrays
    if x.size == 0 or y.size == 0:
        print("Empty x or y array provided.")
        return None, np.array([])  # Adjusted to return a tuple

    # Check for mismatched array sizes
    if len(x) != len(y):
        raise ValueError("Mismatched array sizes: x and y must have the same length")

    Z = np.zeros((len(y), len(x)), dtype=float)
    for i in range(len(y)):
        for j in range(len(x)):
            z = complex(x[j], y[i])
            Z[i, j] = cmath.phase(z**2 - 1)

    fig, ax = plt.subplots()
    c = ax.imshow(Z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)), origin='lower', cmap='hsv')
    fig.colorbar(c, ax=ax, label="Phase (radians)")
    ax.grid()

    return ax, Z
