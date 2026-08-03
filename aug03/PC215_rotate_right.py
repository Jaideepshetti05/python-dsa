arr = [1,2,3,4,5]

k = 2

for _ in range(k):
    arr = [arr[-1]] + arr[:-1]

print(arr)