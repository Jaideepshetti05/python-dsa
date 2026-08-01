arr = [1,2,3,4,5,6,7]

k = 3

k %= len(arr)

arr = arr[-k:] + arr[:-k]

print(arr)