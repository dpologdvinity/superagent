def move_zero(num_list):
    zeros = [0] * num_list.count(0)
    front = [i for i in num_list if i != 0]
    return front + zeros
