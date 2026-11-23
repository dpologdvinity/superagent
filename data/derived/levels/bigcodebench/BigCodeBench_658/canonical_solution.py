import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Make sure to download NLTK stopwords
nltk.download('stopwords')

# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')

# Load NLTK's list of English stop words
STOPWORDS = nltk.corpus.stopwords.words('english')


def task_func(texts):
    """
    Creates a document-term matrix (DTM) from a list of text documents using CountVectorizer from Scikit-learn.
    Texts are preprocessed by removing non-alphanumeric characters (excluding spaces),
    converting to lowercase, and excluding English stop words defined in NLTK.

    Parameters:
    - texts (list of str): The list of text documents to convert into a DTM.

    Returns:
    - pd.DataFrame: A DataFrame where rows represent documents and columns represent unique terms;
                    cell values indicate the frequency of a term in a document.

    Requirements:
    - re
    - nltk
    - pandas
    - sklearn.feature_extraction.text

    Example:
    >>> texts = ["Hello, world!", "Machine learning is great.", "Python is my favorite programming language."]
    >>> dtm = task_func(texts)
    """
    cleaned_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    tokenized_texts = [' '.join(word for word in text.split() if word not in STOPWORDS) for text in cleaned_texts]

    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(tokenized_texts)
    dtm_df = pd.DataFrame(dtm.toarray(), columns= vectorizer.get_feature_names_out() if hasattr(vectorizer,
                                                                  'get_feature_names_out') else vectorizer.get_feature_names())

    return dtm_df
