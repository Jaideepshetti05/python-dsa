def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]


numbers = [1, 2, 3, 4, 5, 6]

print(rotate_right(numbers, 2))