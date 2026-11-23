def count_list(input_list): 
    return sum(isinstance(e, list) for e in input_list)
