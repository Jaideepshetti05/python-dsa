def search(arr, l, h, key):
    if l > h:
        return -1

    m = (l+h)//2

    if arr[m] == key:
        return m

    if key < arr[m]:
        return search(arr, l, m-1, key)

    return search(arr, m+1, h, key)

arr = [2,5,7,9,13,20]

print(search(arr,0,len(arr)-1,13))