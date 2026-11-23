def interleave_lists(list1, list2, list3):
    return [el for pair in zip(list1, list2, list3) for el in pair]
