import os
import sys
import importlib
from pkgutil import iter_modules


def task_func(package_name):
    """
    Adds all modules of a specified package to the system path. This function is useful for dynamically
    importing modules from a package that might not be on the standard path.

    Parameters:
    package_name (str): The name of the package whose modules are to be added to the system path.

    Returns:
    list: A list of module names that were added to the system path.

    Raises:
    ImportError: If the package is not installed or cannot be found. The exception message should contain
                 the instruction to install the package (i.e., f"pip install {package_name}").

    Requirements:
    - os
    - sys
    - importlib
    - pkgutil.iter_modules

    Examples:
    Assuming 'pandas' is a valid package with modules 'module1' and 'module2',

    >>> len(task_func('pandas')) >= 2
    True

    Verify that 'numpy' (a common package) modules are added to the path,
    >>> 'random' in task_func('numpy')
    True
    """
    added_modules = []
    try:
        package = importlib.import_module(package_name)
    except ImportError:
        raise ImportError(f"The package '{package_name}' is not installed! Please install the package first using 'pip install {package_name}'")

    for _, module_name, _ in iter_modules(package.__path__):
        module_path = os.path.join(package.__path__[0], module_name)
        if module_path not in sys.path:
            sys.path.append(module_path)
            added_modules.append(module_name)

    return added_modules
