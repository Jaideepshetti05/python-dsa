arr = [2,4,6,8,10]

print(all(arr[i] <= arr[i+1] for i in range(len(arr)-1)))