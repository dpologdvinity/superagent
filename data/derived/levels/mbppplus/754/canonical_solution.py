def extract_index_list(l1, l2, l3):
    return [a for a, b, c in zip(l1, l2, l3) if a == b == c]
