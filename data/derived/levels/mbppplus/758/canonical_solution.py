def unique_sublists(list1):
    return {tuple(x): list1.count(x) for x in list1}
