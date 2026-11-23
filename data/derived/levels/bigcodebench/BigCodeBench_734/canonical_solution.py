import nltk

# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from collections import Counter

def task_func(content):
    """
    Count the Part-of-Speech (POS) tags in a sentence without the last word.

    Parameters:
    - content (str): The sentence to count POS tags from.

    Returns:
    - dict: A dictionary with POS tags as keys and their count as values.

    Requirements:
    - nltk
    - collections.Counter

    Example:
    >>> task_func('this is an example content')
    {'DT': 2, 'VBZ': 1, 'NN': 1}
    """
    words = content.split()[:-1]  # Split and remove the last word
    pos_tags = nltk.pos_tag(words)  # Tokenization is built into pos_tag for simple whitespace tokenization
    pos_counts = Counter(tag for _, tag in pos_tags)
    return dict(pos_counts)
