def even_ele(test_tuple):
    res = tuple()
    for ele in test_tuple:
        if isinstance(ele, tuple):
            res += (even_ele(ele),)
        elif ele % 2 == 0:
            res += (ele,)
    return res

def extract_even(test_tuple):
    # TODO: implement this function.
    pass
