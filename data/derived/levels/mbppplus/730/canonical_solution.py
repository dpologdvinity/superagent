from itertools import groupby
def consecutive_duplicates(nums):
    return [key for key, _ in groupby(nums)] 
