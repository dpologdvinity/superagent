from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    """
    Count the number of words in multiple dictionary files (.txt) in a specific directory,
    export the counts to a CSV file, and then return the total number of words.

    Parameters:
    filename (str): The name of the output CSV file.
    test_directory (str): The directory containing the dictionary files (.txt).

    Returns:
    int: total number of words in .txt files

    Note:
    - Header for the csv output file is "Word", "Count"
    - Return 0 if the input invalid or error raised

    Requirements:
    - collections.Counter
    - os
    - csv

    Example:
    >>> task_func('word_counts.csv')
    10
    """
    total_words = 0
    try:
        word_counts = Counter()
        for file_name in os.listdir(test_directory):
            if not file_name.endswith('.txt'):
                continue
            with open(os.path.join(test_directory, file_name), 'r') as file:
                words = file.read().split()
                word_counts.update(words)

        with open(output_file, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Count'])
            writer.writerows(word_counts.items())
        
        for word in word_counts:
            total_words += word_counts[word]
    except Exception as e:
        print(e)
    return total_words
