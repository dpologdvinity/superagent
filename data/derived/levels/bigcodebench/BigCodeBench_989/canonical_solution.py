import random
import string


def task_func(length: int, predicates: list, seed: int = None):
    """
    Generates a random string of specified length and evaluates it for specific characteristics.

    Parameters:
    - length (int): Desired length of the generated string.
    - predicates (list of strings): Conditions to evaluate the string.
        Must contain options from 'has_uppercase', 'has_lowercase', 'has_special_chars', 'has_numbers'.
    - seed (int, optional): Seed for the random number generator for reproducibility.

    Returns:
    - tuple:
        - string: the generated random text
        - dict: the text's characteristics

    Raises:
    - ValueError: If the specified length is negative.
    - KeyError: If any predicate is not recognized.

    Notes:
    - Predicates are deduplicated.
    - Characters are randomly sampled from string ascii_letters, digits, and punctuation with replacement.
    - Any invalid predicates provided will result in a KeyError.
    - If no predicates are provided, the result dictionary will be empty.

    Requirements:
    - string
    - random

    Example:
    >>> task_func(10, ['has_uppercase', 'has_numbers'], seed=42)[0]
    '8czu("@iNc'
    >>> task_func(5, ['has_lowercase'], seed=123)
    ('eiMk[', {'has_lowercase': True})
    """
    if seed is not None:
        random.seed(seed)

    if length < 0:
        raise ValueError("Length must be non-negative.")

    predicate_functions = {
        "has_uppercase": lambda x: any(c.isupper() for c in x),
        "has_lowercase": lambda x: any(c.islower() for c in x),
        "has_special_chars": lambda x: any(c in string.punctuation for c in x),
        "has_numbers": lambda x: any(c.isdigit() for c in x),
    }

    predicates = list(set(predicates))
    if any(p not in predicate_functions for p in predicates):
        raise KeyError(f"Invalid predicate provided.")

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_string = "".join(random.choices(characters, k=length))

    results = {
        predicate: predicate_functions[predicate](generated_string)
        for predicate in predicates
    }

    return generated_string, results
