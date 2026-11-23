def div_sum(num):
    res = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            res += i
            if i * i != num:
                res += num / i
        i += 1
    return res

def amicable_numbers_sum(limit):
    # TODO: implement this function.
    pass
