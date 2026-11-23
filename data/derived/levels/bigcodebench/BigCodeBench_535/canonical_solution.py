import sqlite3
import numpy as np
from random import choice, seed


def task_func(db_path, table_name, num_entries, random_seed=None):
    """
    Insert random data into an SQLite3 table that contains random names, ages, and heights.
    If the table does not exist, it will be created.
    This function uses the following constants:
    - NAMES: List of possible names ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia'].
    - AGES: Range of possible ages from 18 to 64.
    - HEIGHTS: Range of possible heights from 150cm to 199cm.

    Parameters:
    db_path (str): The path to the SQLite3 database file.
    table_name (str): The name of the table to insert data into.
    num_entries (int): The number of entries to insert. Must not be negative.
    random_seed (int, optional): Seed for random number generation. Defaults to None (no fixed seed).

    Returns:
    int: The number of rows inserted.

    Raises:
    ValueError: If num_entries is negative.
    
    Requirements:
    - sqlite3
    - numpy
    - random.choice
    - random.seed

    Example:
    >>> task_func('path_to_test.db', 'People', 100, random_seed=42)
    100
    """
    # Setting the random seed if provided
    if random_seed is not None:
        seed(random_seed)
        np.random.seed(random_seed)

    if num_entries < 0:
        raise ValueError("num_entries cannot be negative.")

    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = list(range(18, 65))
    HEIGHTS = list(range(150, 200))

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    table_creation_sql = (
        "CREATE TABLE IF NOT EXISTS {} (name TEXT, age INTEGER, height INTEGER)".format(
            table_name
        )
    )
    cur.execute(table_creation_sql)

    inserted_rows = 0
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        insertion_sql = "INSERT INTO {} VALUES (?, ?, ?)".format(table_name)
        cur.execute(insertion_sql, (name, age, height))
        inserted_rows += cur.rowcount

    conn.commit()

    return inserted_rows
