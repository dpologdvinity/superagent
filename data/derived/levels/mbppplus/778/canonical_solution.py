from itertools import groupby
def pack_consecutive_duplicates(list1):
    return [list(group) for _, group in groupby(list1)]
