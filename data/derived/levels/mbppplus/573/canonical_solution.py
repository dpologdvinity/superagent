def unique_product(list_data):
    from functools import reduce
    return reduce(lambda x, y: x*y, set(list_data))
