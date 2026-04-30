arr = [5, 3, 7, 1, 9]
key = 7
for i in range(len(arr)):
    if arr[i] == key:
        print("Found at index", i)
        break
else:
    print("Not Found")