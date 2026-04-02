def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]