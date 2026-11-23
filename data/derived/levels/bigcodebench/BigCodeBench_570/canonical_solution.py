import inspect
import types
import json

def task_func(f):
    """
    Inspects the given function 'f' and returns its specifications as a JSON string. This includes
    the function's name, arguments, default values, annotations in a string format, and a boolean
    indicating if it's a lambda function.

    Parameters:
    f (function): The function to inspect.

    Returns:
    str: A JSON string containing the function's specifications.

    Requirements:
    - inspect
    - types
    - json

    Examples:
    >>> def sample_function(x, y=2): return x + y
    >>> 'sample_function' in task_func(sample_function)
    True
    >>> def sample_function2(x, y=2): return x * y
    >>> 'sample_function2' in task_func(sample_function2)
    True
    """
    spec = inspect.getfullargspec(f)
    annotations = {k: v.__name__ if isinstance(v, type) else str(v) for k, v in spec.annotations.items()}

    info = {
        'function_name': f.__name__,
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': annotations,
        'is_lambda': isinstance(f, types.LambdaType)
    }

    return json.dumps(info)
