def last(arr,x):
    return len(arr)-arr[::-1].index(x) - 1
